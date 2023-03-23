#Write a python or bash script that counts the number of script files in a directory subdividing it by the shebang interpreter.

# An example output in macOS is:
# countexec /usr/bin
# 81 #!/usr/bin/perl
# 52 #!/usr/bin/perl5.18
# 47 #!/bin/sh
# 44 #!/usr/bin/perl5.28
# 22 #!/usr/sbin/dtrace -s
# ...

import os #fornisce funzioni per interagire con il sistema operativo

directory = "/usr/bin" #directory da cercare

counts = {} #dictionary per memorizzare il conteggio per ogni shebang 

#scorrere tutti i file della directory
for filename in os.listdir(directory):  #listdir() restituisce la lista di file e directories presenti nella directory

    #per verificare se il file è eseguibile e non una directory
    filepath = os.path.join(directory, filename) 
    if os.access(filepath, os.X_OK) and not os.path.isdir(filepath):
        
        #legge la prima riga del file
        with open(filepath, "r") as f:
            first_line = f.readline().strip()

        #incremento del contatore
        if first_line in counts:
            counts[first_line] += 1
        else:
            counts[first_line] = 1

#stampa il conteggio per ogni interprete
for interpreter in sorted(counts):
    count_str = str(counts[interpreter])
    print(count_str + " " + interpreter)

