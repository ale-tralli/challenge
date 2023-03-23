#Write a python or bash script that takes three parameters, two strings and a directory name, 
#and substitutes any occurrence of the first string with the second string for any file in the directory, 
#recursively

import os #fornisce funzioni per interagire con il sistema operativo
import sys

#per ottenere gli argomenti della linea di comando
if len(sys.argv) != 4:
    print("Usage: python script.py old_string new_string directory_path")
    sys.exit(1) #termina il programma a causa di un errore

old_string = sys.argv[1]
new_string = sys.argv[2]
directory_path = sys.argv[3]

#scorre la directory e sostituisce, per ogni file, la vecchia stringa con la nuova 
for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f:
            content = f.read()
        content = content.replace(old_string, new_string)
        with open(file_path, "w") as f:
            f.write(content)


