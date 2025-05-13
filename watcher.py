from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

filename = "test.py"

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = subprocess.Popen(["python", filename])

    def restart(self):
        print("🔁 Reloading...")
        self.process.kill()
        self.process = subprocess.Popen(["python", filename])

    def on_modified(self, event):
        if event.src_path.endswith(filename):
            self.restart()

if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print("👀 Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()