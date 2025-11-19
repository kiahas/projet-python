liste_nom = ["Alice", "Bob", "Charlie"]
print(liste_nom)

ajout= input("Ecrire nom 1: ")
ajout2= input("Ecrire nom 2: ")
liste_nom.append(ajout)
liste_nom.append(ajout2)

if "Bob" in liste_nom:
    liste_nom.remove("Bob")
print(liste_nom)

if "Alice" in liste_nom:
    print("Alice est dans la liste")
