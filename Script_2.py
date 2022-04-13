# A python script to transfer files from the directories to the path.
print("A python script to transfer files from the directories to the path.")
import os
# Path that includes directories containing files.
path = r"C:\Users\alric\Downloads\New folder (2)\archive (3)\State-wise_OLX\\"
filenames=[] # List which will store all of the filenames.
def move(file_paths):
    i=0
    # Looping filepath one by one. And looping though filenames one by one.
    for file_path in file_paths:
        os.rename(file_path , path + filenames[i])
        i+=1

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            filenames.append(filename)
            file_paths.append(os.path.join(root, filename)) # Add it to the list.
    return file_paths  # Self-explanatory.

file_paths=get_filepaths(path)
move(file_paths)
print("Done")