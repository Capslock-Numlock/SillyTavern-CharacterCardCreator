import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import json
import os
import base64
import png  # pypng library


class CharacterCardCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("SillyTavern Character Card Creator")
        self.root.geometry("400x300")

        # Variables to store file paths and JSON content
        self.json_path = tk.StringVar()
        self.png_path = tk.StringVar()
        self.output_name = tk.StringVar()
        self.json_content = None  # To store pasted JSON

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # JSON section
        tk.Label(self.root, text="Select JSON File or Paste JSON:").pack(pady=5)
        json_frame = tk.Frame(self.root)
        json_frame.pack()
        tk.Button(json_frame, text="Browse", command=self.select_json).pack(side=tk.LEFT, padx=5)
        tk.Button(json_frame, text="Paste JSON", command=self.paste_json).pack(side=tk.LEFT, padx=5)
        tk.Label(self.root, textvariable=self.json_path).pack()

        # PNG file selection
        tk.Label(self.root, text="Select PNG File (400x600):").pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.select_png).pack()
        tk.Label(self.root, textvariable=self.png_path).pack()

        # Output file name
        tk.Label(self.root, text="Output File Name (optional):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.output_name).pack()
        tk.Label(self.root, text="You'll choose save location next").pack()

        # Create button
        tk.Button(self.root, text="Create Character Card",
                  command=self.create_card).pack(pady=20)

    def select_json(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Select JSON file"
        )
        if file_path:
            self.json_path.set(file_path)
            self.json_content = None  # Clear pasted JSON if a file is selected

    def paste_json(self):
        # Open a new window for pasting JSON
        paste_window = tk.Toplevel(self.root)
        paste_window.title("Paste JSON")
        paste_window.geometry("400x300")

        # Save button at the top
        def save_pasted_json():
            try:
                # Try to parse the pasted text as JSON to validate it
                pasted_content = json_text.get("1.0", tk.END).strip()
                json.loads(pasted_content)  # Validate JSON
                self.json_content = pasted_content
                self.json_path.set("Pasted JSON")  # Indicate JSON is from paste
                paste_window.destroy()
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON format. Please check your input.")

        tk.Button(paste_window, text="Save JSON", command=save_pasted_json).pack(pady=5)

        # Label and text area below the button
        tk.Label(paste_window, text="Paste your JSON code below:").pack(pady=5)
        json_text = scrolledtext.ScrolledText(paste_window, width=50, height=15)
        json_text.pack(padx=10, pady=5)

    def select_png(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png")],
            title="Select PNG file"
        )
        if file_path:
            self.png_path.set(file_path)

    def create_card(self):
        if not (self.json_path.get() or self.json_content):
            messagebox.showerror("Error", "Please select a JSON file or paste JSON content")
            return
        if not self.png_path.get():
            messagebox.showerror("Error", "Please select a PNG file")
            return

        try:
            # Get JSON data (from file or pasted content)
            if self.json_content:
                json_data = json.loads(self.json_content)
            else:
                with open(self.json_path.get(), 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

            # Convert JSON to string, then to base64 for SillyTavern
            json_str = json.dumps(json_data, separators=(',', ':'))  # Compact JSON
            json_bytes = json_str.encode('utf-8')
            base64_json = base64.b64encode(json_bytes).decode('utf-8')

            # Read the input PNG as chunks
            with open(self.png_path.get(), 'rb') as f:
                reader = png.Reader(file=f)
                chunk_list = list(reader.chunks())  # Get all chunks as a list

            # Prepare metadata chunk (tEXt)
            text_chunk = (b'tEXt', b'chara\0' + base64_json.encode('utf-8'))

            # Insert tEXt chunk before IEND
            for i, chunk in enumerate(chunk_list):
                if chunk[0] == b'IEND':
                    chunk_list.insert(i, text_chunk)
                    break

            # Prompt user to choose save location
            initial_file = self.output_name.get() if self.output_name.get() else "character_card"
            output_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")],
                initialfile=initial_file,
                title="Save Character Card As"
            )

            if not output_path:
                messagebox.showinfo("Canceled", "Save operation canceled.")
                return

            # Write the new PNG with modified chunks
            with open(output_path, 'wb') as f:
                png.write_chunks(f, chunk_list)  # Write all chunks including tEXt

            messagebox.showinfo("Success",
                                f"Character card created successfully!\nSaved as: {output_path}")

            # Clear inputs
            self.json_path.set("")
            self.png_path.set("")
            self.output_name.set("")
            self.json_content = None  # Reset pasted JSON

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    app = CharacterCardCreator(root)
    root.mainloop()


if __name__ == "__main__":
    main()