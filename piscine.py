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

liste_nageur = [(0, "Léa"), (1, "Pierre"), (2, "Michel")]
liste_nage = [(0, "Brasse"), (1, "Crawl"), (2, "Dos")]
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
   
    if commande == 'liste':

        elt1 = "|Nageur    |"
        elt2 = "|Nage      |"
        elt3 = "|Longueur  |"
        elt4 = "|Date      |"

        # Affichage des éléments avec une largeur de champ de 10
        largeur_champ = 10

        for nageur, nage, longueur, date in liste:            
            elt1 += f"{liste_nageur[nageur][1]:<{largeur_champ}}|"
            elt2 += f"{liste_nage[nage][1]:<{largeur_champ}}|"
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
                print(f"{liste_nageur[nageur][1]} nage du {liste_nage[nage][1]}, le {date}")

    if commande == 'nage':
        id_nage = int(input("Quelle nage ? "))
        for nageur, nage, longueur, date in liste:            
            if id_nage == nage:
                print(f"{liste_nageur[nageur][1]} nage du {liste_nage[nage][1]}, le {date}")

    if commande == 'date':
        date_input = input("Quel jour ? YY_MM_DD")
        for nageur, nage, longueur, date in liste:            
            if date_input == date:
                print(f"{liste_nageur[nageur][1]} nage du {liste_nage[nage][1]}, le {date}")

    if commande == 'save':
        # Ouvrir le fichier en mode écriture ('w') et s'assurer qu'il se ferme après
        with open(nom_fichier, 'w') as f:
            # Convertir le tuple en une chaîne de caractères
                f.write(f"@Liste des nageurs\n")
                for id_nageur, nageur in liste_nageur:
    
                    # Écrire la chaîne
                    f.write(f"{id_nageur},{nageur}\n")
                                
                f.write(f"@Liste des nages\n")
                for id_nage, nage in liste_nage:
    
                    # Écrire la chaîne
                    f.write(f"{id_nage},{nage}\n")

                f.write(f"@Liste de la table des nageurs\n")
                for nageur, nage, longueur, date in liste:
    
                    # Écrire la chaîne
                    f.write(f"{nageur},{nage},{longueur},{date}\n")
                print(f"✅ Tuple sauvegardé dans le fichier '{nom_fichier}'.")

    if commande == 'load':
        liste = []  # on écrase l'ancienne liste
        liste_nageur = []  # on écrase l'ancienne liste
        liste_nage = []  # on écrase l'ancienne liste
        step = 0
        with open(nom_fichier, 'r') as fichier:

            for ligne in fichier:
                # Supprime les sauts de ligne et autres espaces inutiles au début/fin
                ligne = ligne.strip()

                if ligne:

                    if ligne[0] == '@':
                        step+=1

                    elif step == 1:
                        # Sépare la ligne en une liste de chaînes de caractères
                        valeurs = [v.strip() for v in ligne.split(',')]

                        """# Affectation aux variables
                        id_nageur_str, nageur = valeurs

                        # Conversion obligatoire pour retrouver EXACTEMENT ton format d'origine
                        id_nageur = int(id_nageur_str)

                        liste_nageur.append((id_nageur, nageur))"""
                        id_nageur = int(valeurs[0])  # Conversion en entier
                        nageur = valeurs[1]
                        liste_nageur.append((id_nageur, nageur))

                    elif step == 2:
                        # Sépare la ligne en une liste de chaînes de caractères
                        valeurs = [v.strip() for v in ligne.split(',')]
                        
                        # Affectation aux variables
                        id_nage_str, nage = valeurs

                        # Conversion obligatoire pour retrouver EXACTEMENT ton format d'origine
                        id_nage = int(id_nage_str)
                        print((id_nage, nage))
                        liste_nage.append((id_nage, nage))

                    elif step == 3:
                        # Sépare la ligne en une liste de chaînes de caractères
                        valeurs = [v.strip() for v in ligne.split(',')]

                        # Affectation aux variables
                        id_nageur_str, id_nage_str, longueur_str, date = valeurs

                        # Conversion obligatoire pour retrouver EXACTEMENT ton format d'origine
                        id_nageur = int(id_nageur_str)
                        id_nage = int(id_nage_str)
                        longueur = int(longueur_str)

                        liste.append((id_nageur, nage, longueur, date))

            print(f"✅ Le fichier a bien était chargé '{nom_fichier}'.")
            print(liste_nageur)
            print(liste_nage)
                
# Fin du programme