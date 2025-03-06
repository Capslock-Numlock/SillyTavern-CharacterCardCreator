SillyTavern Character Card Creator
A lightweight Python application for creating SillyTavern character cards by embedding JSON data into PNG files. This tool features a simple GUI built with Tkinter, allowing users to either load a JSON file or paste JSON content directly, select a PNG image, and save the resulting character card with embedded metadata. Optimized for minimal size using pypng instead of heavier libraries like Pillow, it generates compact executables (~10-20 MB) for easy sharing.

Features:
✔️ Load JSON from files or paste directly via a text editor window.
✔️ Embed JSON as base64-encoded chara metadata in PNG files, compatible with SillyTavern.
✔️ User-defined save locations with a file dialog.
✔️ Pure-Python implementation with pypng for lightweight operation.
✔️ Buildable into a standalone .exe with PyInstaller for Windows users.

Requirements:
Python 3.10
pypng (pip install pypng)

Build Instructions:
Run pyinstaller -w character_card_creator.py for a folder (~5-15 MB zipped).
Or pyinstaller -F -w character_card_creator.py for a single-file executable (~10-20 MB).

Made for SillyTavern users who want a portable, easy-to-use tool for character card creation without complex dependencies.
