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
        b = input("Quelle nage ? ")
        c = input("Combien de longueur ? ")
        d = input("Quel jour ? YY_MM_DD")
        liste.append((a,b,c,d))
   
    if commande == 'liste':
        for elt in liste:
            print(f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}, le {elt[3]}")

    if commande == 'nageur':
        nageur = input("Qui nage ? ")
        for elt in liste:
            if nageur == elt[0]:
                print(f"{elt[0]} nage du {elt[1]}, le {elt[3]}")

    if commande == 'nage':
        nage = input("Quelle nage ? ")
        for elt in liste:
            if nage == elt[1]:
                print(f"{nage}, utiliser par, {elt[0]}, le {elt[3]}")
                
# Fin du programme