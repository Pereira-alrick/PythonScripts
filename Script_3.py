# A python script to replace label name with "License" in the name tag.
import glob, os # The glob module is used to retrieve files/path names matching a specified pattern. 
path = r'C:\Users\alric\Desktop\Scripts\PythonScripts\archive\Tensorflow\workspace\images\test\\'

success=0

failure = []

print("A python script to replace label name with \"License\" in the name tag.")

# Function to replace label name with "License".
def replace_word(filename):
    global success 
    global failure
    try:
        with open(filename, 'r+') as file:
            lines = file.readlines() # Returns the lines of the file in form of a list. 
            line=lines[14] # Picks line 14 where the name tag is located.
            line=line.replace(line[8:-8], 'License')
            lines[14]=line # Places the modified back in the list.
            file.writelines(lines) # Rewrites the file.
            success=success+1
            file.close()
            
    except:
        try:
            file.close()
            failure.append(filename)
        except:
            failure.append(filename)

# You can also use this code snippet instead of glob module, that would help to replace label names in large portions of files from a defined path comtaining various directories.
"""for root, directories, files in os.walk(path):
        for filename in files:
            filename.append(filename)
            file_paths.append(os.path.join(root, filename)) # Add it to the list.
file_paths"""

for files in glob.glob(path + '*.xml'): # With glob method, i used wild card * to make path retrieval more simple and convenient.
    replace_word(files)

if len(failure)!=0:
    print("Failure in replacing:")
    [print(i) if len(failure) != 1 else print(failure) for i in failure]

print("Success in replacing: {}, Failure in replacing: {}.".format(success, len(failure)))