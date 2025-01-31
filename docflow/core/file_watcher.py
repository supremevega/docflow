import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DebouncedHandler(FileSystemEventHandler):
    def __init__(self, delay=5):
        self.debounce_time = delay
        self._timer = None

    def on_created(self, event):
        if not event.is_directory:
            self._debounce(event.src_path)

    def _debounce(self, path):
        if self._timer:
            self._timer.cancel()
        self._timer = threading.Timer(self.debounce_time, self.process, args=(path,))
        self._timer.start()

    def process(self, path):
        # Main processing logic will be added here
        print(f"Processing file: {path}")
