import time
import hashlib
import os
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Compute SHA-256 hash of a file
def compute_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

# Database connection
def log_event(filename, action):
    conn = sqlite3.connect('file_logs.db')
    cursor = conn.cursor()
    file_hash = compute_hash(filename) if action != "Deleted" else None
    cursor.execute("INSERT INTO logs (filename, hash, action) VALUES (?, ?, ?)", 
                   (filename, file_hash, action))
    conn.commit()
    conn.close()

# File System Event Handler
class FileMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")
            log_event(event.src_path, "Created")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")
            log_event(event.src_path, "Modified")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")
            log_event(event.src_path, "Deleted")

# Start monitoring
observer = Observer()
path = "monitored_folder"
os.makedirs(path, exist_ok=True)
event_handler = FileMonitorHandler()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
