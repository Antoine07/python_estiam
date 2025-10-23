
# permet d'ouvrir un fichier en mode lecture
# deux paramètres le premier c'est le nom du fichier avec son chemin et extension
# le second c'est le mode d'ouverture du fichier ici 
f = open('notes.txt', 'r') # read = lecture seule 

print(f) # affiche l'objet fichier qui est ouvert 

# permet de lire le contenu du fichier ligne par ligne
for line in f:
    print(line.strip()) # strip() permet de supprimer les espaces avant et après la ligne

# une fois le fichier parcouru on n'a plus rien a lire, donc rien ne s'affiche
for line in f:
    print(line.strip()) # strip() permet de supprimer les espaces avant et après la ligne

f.close() # ferme le fichier

# lire un fichier se trouvant dans un dossier DATA

f = open('DATA/notes.txt', 'r') # read = lecture seule


# permet de lire le contenu du fichier ligne par ligne
for line in f:
    print(line.strip()) # strip() permet de supprimer les espaces avant et après la ligne

f.close() # ferme le fichier

# log enregistre des informations dans un fichier log.txt

file_log = open('DATA/log.txt', 'a') # a = append mode (ajout à la fin du fichier)

file_log.write('Ouverture du fichier log.txt\n')
file_log.write('Aujourdhui on a eu un cours Python\n')
file_log.write('Ce soir a une un cours de soutien \n')

file_log.close() # ferme le fichier log.txt