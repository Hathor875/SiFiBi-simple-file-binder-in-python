import json
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def auto_run():
    current_folder = Path('..')
    for item in current_folder.iterdir():
        if item.is_file():
            handle_file(item.suffix, item)


class MyHandler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if event.is_directory:
            return
        auto_run()


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
    auto_run()
    path = ".."
    sleepTime = config["settings"]["size_threshold"]
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(sleepTime)
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
