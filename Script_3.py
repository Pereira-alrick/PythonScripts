#A python script to replace label name with "License" in the name tag.
import glob, os # The glob module is used to retrieve files/path names matching a specified pattern. 
path = r'C:\Users\alric\Downloads\New folder (2)\archive (3)\State-wise_OLX\\'

print("A python script to replace label name with \"License\" in the name tag.")

# Function to replace label name with "License".
def replace_word(filename):

    try:
        with open(filename, 'r') as file:
            lines = file.readlines() # Returns the lines of the file in form of a list. 
            line=lines[14] # Picks line 14 where the name tag is located.
            line=line.replace(line[8:-8], 'License')
            lines[14]=line # Places the modified back in the list.
    except:
        print(filename + ' Failed to open.')
    finally:
        file.close()

    try:
        with open(filename, 'w') as file:
            file.writelines(lines) # Rewrites the file.
        print(filename + ' Sucuss in replacing.')
    except:
        print(filename + ' Failed')
    finally:
        file.close()

# You can also use this code snippet instead of glob module, that would help to replace label names in large portions of files from a defined path comtaining various directories.
"""for root, directories, files in os.walk(path):
        for filename in files:
            filename.append(filename)
            file_paths.append(os.path.join(root, filename)) # Add it to the list.
file_paths"""

for files in glob.glob(path + '*.xml'): # With glob method, i used wild card * to make path retrieval more simple and convenient.
    replace_word(files)