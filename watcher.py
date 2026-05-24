import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from extractor import process, INBOX

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() == ".pdf":
            time.sleep(1)  # wait for file to finish copying
            process(path)

if __name__ == "__main__":
    print(f"[Watcher] Watching {INBOX} — drop PDFs to process automatically. Ctrl+C to stop.")
    observer = Observer()
    observer.schedule(PDFHandler(), str(INBOX), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
