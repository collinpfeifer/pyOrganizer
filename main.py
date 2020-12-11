import os, pathlib, shutil, time, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileWatcher(FileSystemEventHandler):
    
    if not os.path.isdir("./GeneralFiles"):
        os.mkdir("./GeneralFiles")


    if not os.path.isdir("./ImportantStuff"):
        os.mkdir("./ImportantStuff")

    monitor_folder = "./ImportantStuff"
    destination_folder = "./GeneralFiles"


    def __init__(self):
        self.observer = Observer()
        print("start")
        
            
    def run(self):
        event_handler = FileWatcher()
        self.observer.schedule(event_handler, self.monitor_folder, recursive=True)
        
        day_folder = " ".join(time.asctime().split()[:3])
        month_folder = " ".join(time.asctime().split()[1:2])
        year_folder = " ".join(time.asctime().split()[4:])

        if not os.path.isdir("./" + self.destination_folder + "/" 
        + year_folder):
            os.mkdir("./" + self.destination_folder + "/" + year_folder)

        if not os.path.isdir("./" + self.destination_folder + "/" + year_folder + "/" + month_folder):
            os.mkdir("./" + self.destination_folder + "/" + year_folder + "/" + month_folder)

        if not os.path.isdir("./" + self.destination_folder + "/" + year_folder + "/" + month_folder + "/" + day_folder):
            os.mkdir("./" + self.destination_folder + "/" + year_folder + "/" + month_folder + "/" + day_folder)

        self.observer.start()
        try:
            while True:
                for filename in os.listdir(self.monitor_folder):
                    time.sleep(5)
                    src = self.monitor_folder + "/" + filename

                    destination = self.destination_folder + "/" + year_folder + "/" + month_folder + "/" + day_folder + "/" + str(time.asctime()) + str(pathlib.Path(filename).suffix)
                    os.rename(src, destination)
                
        except KeyboardInterrupt:
            self.observer.stop()
            print("observer stopped")

        self.observer.join()
        

if __name__ == '__main__':
    watch = FileWatcher()
    watch.run()
