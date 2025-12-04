import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

PYTHON = sys.executable
TARGET = "main.py"

class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.proc = None
        self.restart_app()

    def restart_app(self):
        # Kill old app if running
        if self.proc:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()

        # Start a new instance
        print(f"🔄 Restarting {TARGET}...")
        self.proc = subprocess.Popen([PYTHON, TARGET])

    def on_modified(self, event):
        # Only restart on Python file changes
        if event.src_path.endswith(".py"):
            self.restart_app()

if __name__ == "__main__":
    # Start initial app
    handler = ReloadHandler()
    observer = Observer()
    observer.schedule(handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if handler.proc:
            handler.proc.terminate()
    observer.join()
