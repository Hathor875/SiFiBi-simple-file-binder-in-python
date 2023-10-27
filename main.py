import json
from pathlib import Path

def load_config(filename: str) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)

def move_file(source: Path, destination: Path):
    if destination.exists() and destination.is_dir():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    source.rename(destination)

def handle_file(extension: str, source: Path):
    folder_name = config["file_types"].get(extension)
    if not folder_name:
        return

    if source.stat().st_size / 1048576 > config["settings"]["size_threshold"]:
        return

    destination = source.parent / folder_name / source.name
    move_file(source, destination)

if __name__ == '__main__':
    config = load_config('config.json')
    currentFolder = Path('.')
    for item in currentFolder.iterdir():
        if item.is_file():
            handle_file(item.suffix, item)
