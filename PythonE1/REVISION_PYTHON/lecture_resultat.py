
# ouverture et fermeture automatique d'un fichier avec "with"
with open('DATA/ESTIAM/resultats.txt', 'r') as f: 
    
    for line in f:
        print(line.strip())