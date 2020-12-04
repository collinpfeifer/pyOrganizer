import os, getpass, shutil, time, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher:
    
    if not os.path.isdir("./GeneralFiles"):
        os.mkdir("./GeneralFiles")

    destination_folder = "./GeneralFiles"

    if not os.path.isdir("./ImportantStuff"):
        os.mkdir("./ImportantStuff")

    monitor_folder = "./ImportantStuff"

    def __init__(self):
        self.observer = Observer()

    def folder_modified(self):

        event_handler = Handler()
        self.observer.schedule(event_handler, self.monitor_folder, recursive=True)
        self.observer.start()
        try:
          while True:
              time.sleep(5)
              for filename in os.listdir(self.monitor_folder):
                src = monitor_folder + "/" + filename
                destination = destination_folder + "/" + str(time.ctime(time.time()))
                os.rename(src, destination)
        except KeyboardInterrupt:
                self.observer.stop()
        
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(self, event):
        if event.is_directory:
            return None
        
    def on_modified(self, event):
        print("Watchdog recieved a modified event")


if __name__ == '__main__':
    watch = FileWatcher()
    watch.folder_modified()
