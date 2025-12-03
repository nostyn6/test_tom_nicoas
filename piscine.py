#
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

# Le nom du fichier
nom_fichier = 'utilisateur.txt'

print("--- Gestionnaire d'utilisateurs d'une piscine ---")

liste = [(0, 0, 15, "25-11-24"),
         (1, 0, 9, "25-11-24"),
         (2, 1, 8, "25-11-26"),
         (0, 1, 10, "25-11-25"),
         (1, 2, 9, "25-11-26"),
         (2, 0, 8, "25-11-26")]

liste_nageur = ["Léa", "Pierre", "Michel"]
liste_nage = ["Brasse", "Crawl", "Dos"]
liste_info = ["1", "2", "3", "4", "5"]
commande = ''

while commande != 'exit':
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        a = int(input("Qui nage ? "))
        b = int(input("Quelle nage ? "))
        c = int(input("Combien de longueur ? "))
        d = input("Quel jour ? YY_MM_DD")
        liste.append((a,b,c,d))

    if commande == 'nouveau_nageur':
        nouveau_nageur = input("Qui est le nouveau nageur ? ")
        liste_nageur.append(nouveau_nageur)

    if commande == 'nouvelle_nage':
        nouvelle_nage = input("Qu'elle est la nouvelle nage ? ")
        liste_nage.append(nouvelle_nage)
    
    if commande == 'nouvelle_info':
        nouvelle_info = input("Qu'elle est la nouvelle info ? ")
        liste_info.append(nouvelle_info)
    
   
    if commande == 'liste':

        elt1 = "|Nageur    |"
        elt2 = "|Nage      |"
        elt3 = "|Longueur  |"
        elt4 = "|Date      |"

        # Affichage des éléments avec une largeur de champ de 10
        largeur_champ = 10

        for nageur, nage, longueur, date in liste:            
            elt1 += f"{liste_nageur[int(nageur)]:<{largeur_champ}}|"
            elt2 += f"{liste_nage[nage]:<{largeur_champ}}|"
            elt3 += f"{longueur:<{largeur_champ}}|"
            elt4 += f"{date:<{largeur_champ}}|"

        print("--- Alignement par Défaut (Gauche) ---")
        print(elt1)  # 'Nageur' suivi des nageurs
        print(elt2)  # 'Nage' suivi des nages
        print(elt3)  # 'Longueur' suivi des longueurs
        print(elt4)  # 'Date' suivi des dates
        print("-" * 24)

    if commande == 'nageur':
        id_nageur = int(input("Qui nage ? "))
        for nageur, nage, longueur, date in liste:            
            if id_nageur == nageur:
                print(f"{liste_nageur[nageur]} nage du {liste_nage[nage]}, le {date}")

    if commande == 'nage':
        id_nage = int(input("Quelle nage ? "))
        for nageur, nage, longueur, date in liste:            
            if id_nage == nage:
                print(f"{liste_nageur[nageur]} nage du {liste_nage[nage]}, le {date}")

    if commande == 'date':
        date_input = input("Quel jour ? YY_MM_DD")
        for nageur, nage, longueur, date in liste:            
            if date_input == date:
                print(f"{liste_nageur[nageur]} nage du {liste_nage[nage]}, le {date}")

    if commande == 'save':
        # Ouvrir le fichier en mode écriture ('w') et s'assurer qu'il se ferme après
        with open(nom_fichier, 'w') as f:
            # Convertir le tuple en une chaîne de caractères
                for nageur, nage, longueur, date in liste:
    
                    # Écrire la chaîne
                    f.write(f"{nageur},{nage},{longueur},{date}\n")

                print(f"✅ Tuple sauvegardé dans le fichier '{nom_fichier}'.")

    if commande == 'load':
        liste = []  # on écrase l'ancienne liste
        with open(nom_fichier, 'r') as fichier:

            for ligne in fichier:
                # Supprime les sauts de ligne et autres espaces inutiles au début/fin
                ligne = ligne.strip()

                if ligne:
                    # Sépare la ligne en une liste de chaînes de caractères
                    valeurs = [v.strip() for v in ligne.split(',')]

                    # Affectation aux variables
                    nageur_str, nage_str, longueur_str, date = valeurs

                    # Conversion obligatoire pour retrouver EXACTEMENT ton format d'origine
                    nageur = int(nageur_str)
                    nage = int(nage_str)
                    longueur = int(longueur_str)

                    liste.append((nageur, nage, longueur, date))

                
# Fin du programme