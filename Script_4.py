# A python script to compression images and folders.
import os
import tarfile # Tarfile module for compression.

paths = {
    'TENSORFLOW_PATH': 'Tensorflow',

    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'TEST_PATH': os.path.join('Tensorflow', 'workspace','images', 'test'),
    'TRAIN_PATH': os.path.join('Tensorflow', 'workspace','images', 'train')
} # File paths.

def tarCompression(filename, paths): # Function to compress folder.
    with tarfile.open(filename, 'w:gz') as tar_handle:
        tar_handle.add(paths['TEST_PATH']) # Adds test to the archive.
        tar_handle.add(paths['TRAIN_PATH']) # Adds train to the archive.
        tar_handle.close()

def dir_existensce(paths):
    flag=0
    for path in paths.values():# Checking if the folders exists, if not creates them.
            if not os.path.exists(path):
                os.mkdir(path)
                flag=1
    if flag==1:
        print("Please upload images: ")
        exit()
    image_existensce(paths)

def image_existensce(paths): # Checking if the folders are having images or not.
    if not (os.listdir(paths['TEST_PATH']) and os.listdir(paths['TRAIN_PATH'])):
        print("Please upload images: ")
        exit()

dir_existensce(paths)

tarCompression('archive.tar.gz', paths)

print("Succuss in compression.")