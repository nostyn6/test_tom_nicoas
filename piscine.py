#
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

# Le nom du fichier
nom_fichier = 'utilisateur.txt'

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = [("Léa", "Brasse", "15", "25-11-24"),
         ("Pierre", "Brasse", "9", "25-11-24"),
         ("Michel", "Crawl", "8", "25-11-26"),
         ("Léa", "Crawl", "10", "25-11-25"),
         ("Pierre", "Dos", "9", "25-11-26"),
         ("Michel", "Brasse", "8", "25-11-26")]
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = input("Qui nage ? ").capitalize()
        b = input("Quelle nage ? ").capitalize()
        c = input("Combien de longueur ? ")
        d = input("Quel jour ? YY_MM_DD")
        liste.append((a,b,c,d))
   
    if commande == 'liste':

        elt1 = "|Prénom    |"
        elt2 = "|Nage      |"
        elt3 = "|Longueur  |"
        elt4 = "|Date      |"

        # Affichage des éléments avec une largeur de champ de 10
        largeur_champ = 10

        for nageur, nage, longueur, date in liste:            
            elt1 += f"{nageur:<{largeur_champ}}|"
            elt2 += f"{nage:<{largeur_champ}}|"
            elt3 += f"{longueur:<{largeur_champ}}|"
            elt4 += f"{date:<{largeur_champ}}|"

        print("--- Alignement par Défaut (Gauche) ---")
        print(elt1)  # 'Prénom' suivi d'espaces
        print(elt2)  # 'Nage' suivi d'espaces
        print(elt3)  # 'Longueur' suivi d'espaces
        print(elt4)  # 'Date' suivi d'espaces
        print("-" * 24)

    if commande == 'nageur':
        nageur_input = input("Qui nage ? ").capitalize()
        for nageur, nage, longueur, date in liste:            
           if nageur_input == nageur:
               print(f"{nageur} nage du {nage}, le {date}")

    if commande == 'nage':
        nage_input = input("Quelle nage ? ").capitalize()
        for nageur, nage, longueur, date in liste:            
            if nage_input == nage:
                print(f"{nage}, utiliser par, {nageur}, le {date}")

    if commande == 'date':
        date_input = input("Quel jour ? YY_MM_DD")
        for nageur, nage, longueur, date in liste:            
            if date_input == date:
               print(f"{nageur} nage du {nage}, le {date}")

    if commande == 'save':
        # Ouvrir le fichier en mode écriture ('w') et s'assurer qu'il se ferme après
        with open(nom_fichier, 'w') as f:
            # Convertir le tuple en une chaîne de caractères
            donnees_a_ecrire = str(liste)
    
            # Écrire la chaîne
            f.write(donnees_a_ecrire)

            print(f"✅ Tuple sauvegardé dans le fichier '{nom_fichier}'.")
                
# Fin du programme