import os
import shutil


#Paths

src = "/users/rhyshooks/"
target_dir = "/Users/rhyshooks/Desktop/Images/"

def locate_files_by_file_suffix(directory, file_suffix):
    located_files = []
    for dirpath, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_suffix):
                located_files.append(os.path.join(dirpath, file))
    return located_files


def move_file(src, target_dir):
    shutil.move(src, target_dir)
    print("Files have been successfully moved")


files = locate_files_by_file_suffix("/users/rhyshooks/", ("*.png", "*.jpg"))
print(f"List of all files: {files}")

move_file(r"/Users/rhyshooks/Desktop/Images/")
