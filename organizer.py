import os, pathlib, time, logging, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig()

# File Watcher class
class FileWatcher(FileSystemEventHandler):
    while True:
        monitor_folder = input("Please give the full path for the folder in which you wish to monitor:\n")

        if not os.path.isdir(monitor_folder):
            print("The folder is not accessible, please try again\n")
        
        else: 
            parent_directory = os.path.dirname(monitor_folder)
            break
   
    # Checking if the moved folder exists, if it doesn't, it is created
    destination_folder = os.path.dirname(monitor_folder) + "/GeneralFiles"
    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder)
        logging.debug("Moved folder created")


    # Checking if the inital folder exists, if it doesn't, it is created
    if not os.path.isdir(monitor_folder):
        os.mkdir(monitor_folder)
        logging.debug(monitor_folder)


    # Names for folders per year, month, and day, determined off current time
    day_folder = " ".join(time.asctime().split()[:3])
    month_folder = " ".join(time.asctime().split()[1:2])
    year_folder = " ".join(time.asctime().split()[4:])
    time_name = " ".join(time.asctime().split()[3:4])

    base_destitation = destination_folder + "/" + year_folder + "/" + month_folder + "/" + day_folder + "/"
    # initialization of watchdog observer
    def __init__(self):
        self.observer = Observer()
        logging.debug("Observer started")
        
    # main function, will check day, month, year folders, move and rename files 
    # found in initial folder
    def run(self):
        event_handler = FileWatcher()
        self.observer.schedule(event_handler, self.monitor_folder, recursive=True)

        # Checking if the current year folder exists, if not it is created
        if not os.path.isdir(self.destination_folder + "/" + self.year_folder):
            os.mkdir(self.destination_folder + "/" + self.year_folder)
            logging.debug("New year folder created")

        # Checking if the current month folder exists, if not it is created
        if not os.path.isdir(self.destination_folder + "/" + self.year_folder + "/" + self.month_folder):
            os.mkdir( + self.destination_folder + "/" + self.year_folder + "/" + self.month_folder)
            logging.debug("New month folder created")

        # Checking if the current day folder exists, if not it is created
        if not os.path.isdir(self.destination_folder + "/" + self.year_folder + "/" + self.month_folder + "/" + self.day_folder):
            os.mkdir(self.destination_folder + "/" + self.year_folder + "/" + self.month_folder + "/" + self.day_folder)
            logging.debug("New day folder created")

        # Observer is started with a try statement
        self.observer.start()
        try:
            while True:
                time.sleep(5)

                # For loop for checking for files in the monitor folder
                for file in os.listdir(self.monitor_folder):
                    if not file == ".DS_Store":
                        logging.debug("Within file searcher for loop")
                        # Destination and monitor folder variable is created 
                            
                        source = self.monitor_folder + "/" + file
                        destination = self.base_destitation + self.time_name + str(pathlib.Path(file).suffix)
                        try:
                            if os.path.isfile(source):
                                # Files are renamed
                                os.rename(source, self.destination)
                                logging.debug("File renamed")

                            if os.path.isdir(source):
                                # Folders are renamed
                                shutil.copytree(source, self.base_destitation + file)
                                shutil.rmtree(source)
                                logging.debug("Folder renamed")  
                        except FileExistsError:  
                            logging.debug("This file/folder already exists")
                
        except KeyboardInterrupt:
            self.observer.stop()
            logging.debug("Observer stopped")

        self.observer.join()
        
if __name__ == '__main__':
    Handeler = FileWatcher()
    Handeler.run()
