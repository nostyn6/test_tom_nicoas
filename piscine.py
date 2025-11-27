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
        for nageur, nage, longueur, date in liste:
            print(f"Prénom {nageur}, nage {nage}, longueur {longueur}, le {date}")

    if commande == 'nageur':
        input_nageur = input("Qui nage ? ")
        for nageur, nage, longueur, date in liste:
            if input_nageur == nageur:
                print(f"{nageur} nage du {nage}, le {date}")

    if commande == 'nage':
        input_nage = input("Quelle nage ? ")
        for nageur, nage, longueur, date in liste:
            if input_nage == nage:
                print(f"{nage}, utiliser par, {nageur}, le {date}")
                
# Fin du programme