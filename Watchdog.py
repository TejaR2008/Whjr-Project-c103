from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

dir = "C:/Users/starf/OneDrive/Desktop/WhJr Python Projects"

class FileMomentHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(event)
        print("This file: {event.src_path} has been created!")

    def on_modified(self, event):
        print(event)
        print("This file: {event.src_path} has been modified!")

    def on_moved(self, event):
        print(event)
        print("This file: {event.src_path} has been moved somewhere else!")

    def on_deleted(self, event):
        print(event)
        print("This file: {event.src_path} has been deleted!")                


RandomObject = FileMomentHandler()   
observer = Observer()
observer.schedule(RandomObject, dir)
observer.start()  

try:
    while True:
        time.sleep(5)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()        
