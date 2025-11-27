#
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = []
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))
   
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}")

    if commande == 'nageur':
        nageur = input("Qui nage ? ")
        for elt in liste:
            if nageur == elt[0]:
                print(nageur, "nage du", elt[1])

    if commande == 'nage':
        nage = input("quelle nage? ")
        for elt in liste:
            if nage == elt[1]:
                print(nage, "utiliser par", elt[0])
                
# Fin du programme