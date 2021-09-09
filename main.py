import glob
import os
import shutil
os.chdir("/users/rhyshooks/downloads")
for file in glob.glob("*.png"):
    print(file)

# Paths

source_folder = r"/users/rhyshooks/downloads"
destination_folder = r"/Users/rhyshooks/Desktop/Images/"

# Search files with .png extension in source directory

ext = "/*.png"
files = glob.glob(source_folder + ext)

# move files with png ext
for file in files:
    file_name = os.path.basename(file)
    shutil.move(file, destination_folder)
    print("Moved: ", file)
