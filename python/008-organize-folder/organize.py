from pathlib import Path
import shutil

TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "PDF": [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
}

folder = Path(input("Folder path: ").strip('" '))

for file in folder.iterdir():
    if not file.is_file():
        continue
    target = "Other"
    for name, extensions in TYPES.items():
        if file.suffix.lower() in extensions:
            target = name
    destination = folder / target
    destination.mkdir(exist_ok=True)
    if (destination / file.name).exists():
        print("Skipped (already there):", file.name)
        continue
    shutil.move(str(file), str(destination / file.name))
    print(file.name, "->", target)
