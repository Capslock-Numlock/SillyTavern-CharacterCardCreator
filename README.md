# 🏰 SillyTavern Character Card Creator v0.1

A lightweight Python app that creates [SillyTavern](https://github.com/SillyTavern/SillyTavern) character cards by embedding JSON data into a PNG file. It has a simple Tkinter GUI: load a JSON file or paste JSON, pick a PNG, and save the finished card.

It uses `pypng` instead of heavier libraries like Pillow, so the executables you build stay small (~10-20 MB).

## Features

- ✔️ Load JSON from a file, or paste it into a text window
- ✔️ Embeds the JSON as a base64-encoded `chara` metadata chunk, compatible with SillyTavern
- ✔️ Choose where to save the card with a file dialog
- ✔️ Pure Python, with `pypng` as the only dependency
- ✔️ Buildable into a standalone `.exe` with PyInstaller for Windows users

## Requirements

- [Python 3.10](https://www.python.org/downloads/release/python-31011/)
- `pypng`

```
pip install -r requirements.txt
```

## Usage

```
python CharacterCardCreator.py
```

1. Click **Browse** to load a `.json` file, or **Paste JSON** to paste the contents (invalid JSON is rejected).
2. Select the PNG image to use as the card art (the app suggests 400x600).
3. Save. The new PNG contains your JSON and can be imported into SillyTavern.

## Building an executable

```
pyinstaller -w CharacterCardCreator.py
```
Produces a folder (~5-15 MB zipped).

```
pyinstaller -F -w CharacterCardCreator.py
```
Produces a single-file executable (~10-20 MB).

## License

[MIT](LICENSE)
