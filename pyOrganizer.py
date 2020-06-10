import watchdog, os, getpass, shutil, json, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    monitor_folder = "/Users/" + getpass.getuser() + "/Downloads"
    destination_folder = "/Users/" + getpass.getuser() + "/General Files"
    def folder_modified(self, event):
        for filename in os.listdir(monitor_folder):
            src = monitor_folder + "/" + filename
            destination = destination_folder + "/" + filename
            os.rename(src, )


