import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        print(f'O arquivo {event.src_path} acaba de ser criado')
        if event.src_path[event.src_path.rindex('.') + 1:] == 'txt':
            print('Um arquivo de texto foi criado')
        else:
            pass

    @staticmethod
    def on_modified(event):
        print(f'O arquivo {event.src_path} acaba de ser modificado')

    @staticmethod
    def on_moved(event):
        print(f'O arquivo {event.src_path} acaba de ser movido')

    @staticmethod
    def on_deleted(event):
        print(f'O arquivo {event.src_path} acaba de ser deletado')


file_change_handler = Handler()
observer = Observer()
observer.schedule(file_change_handler, os.getcwd(), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
except ValueError:
    observer.stop()
observer.join()