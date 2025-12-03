#
#   Projet de développement Python 
#   Gestionnaire d'utilisateurs d'une piscine 
#

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
        for nageur, nage, longueur, date in liste:            
            print(f"Prénom {nageur}, nage {nage}, longueur {longueur}, le {date}")

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
                
# Fin du programme