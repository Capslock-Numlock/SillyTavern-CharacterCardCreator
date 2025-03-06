🏰<b>SillyTavern Character Card Creator v0.1</b><br><br>
A lightweight Python application for creating SillyTavern character cards by embedding JSON data into PNG files. This tool features a simple GUI built with Tkinter, allowing users to either load a JSON file or paste JSON content directly, select a PNG image, and save the resulting character card with embedded metadata. Optimized for minimal size using pypng instead of heavier libraries like Pillow, it generates compact executables (~10-20 MB) for easy sharing.<br>

Features:<br>
✔️ Load JSON from files or paste directly via a text editor window.<br>
✔️ Embed JSON as base64-encoded chara metadata in PNG files, compatible with SillyTavern.<br>
✔️ User-defined save locations with a file dialog.<br>
✔️ Pure-Python implementation with pypng for lightweight operation.<br>
✔️ Buildable into a standalone .exe with PyInstaller for Windows users.<br>

Requirements:<br>
<a href="https://www.python.org/downloads/release/python-31011/">Python 3.10</a><br>
pypng (<i>pip install pypng</i>)<br>

Build Instructions:<br>
Run <i>pyinstaller -w CharacterCardCreator.py</i> for a folder (~5-15 MB zipped).<br>
Or <i>pyinstaller -F -w CharacterCardCreator.py</i> for a single-file executable (~10-20 MB).<br><br>

Made for SillyTavern users who want a portable, easy-to-use tool for character card creation without complex dependencies.
