# 1  Conditions avec les instructions if/else
# ensoleille = True
ensoleille = False
if ensoleille:
    print("on va à la plage !")
else:
    print("on reste à la maison !")

# 2  Conditions alternatives en ajoutant une clause 'elif'
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

# 3  Conditions multiples avec les opérateurs logiques : and - or - not
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")

# 4 Conditions complexes avec des expressions comparatives
nombre_de_sieges = 30
nombre_dinvites = 25
if nombre_dinvites < nombre_de_sieges:
    print("autoriser plus d'inviter !")
else:
    print("na pas autoriser plus d'inviter !")

# 5 Simplifiez votre code avec les match cases
fruit = "orange"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

# Exercice :
def main():
    nombre_a_gauche = input("Entrez le nombre entier à gauche : ")
    nombre_a_droite = input("Entrez le nombre entier à doite : ")
    operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")

    resultat = 0

    # Vérifie si les deux nombres sont valides avec la fonction
    # isinstance (soit un integer, soit un float)
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
        print("Erreur: les deux nombres doivent être des nombres entiers")
    else:
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
        
        match operation:
            case "+":
                resultat = nombre_a_gauche + nombre_a_droite
            case "-":
                resultat = nombre_a_gauche - nombre_a_droite
            case "*":
                resultat = nombre_a_gauche * nombre_a_droite
            case "/":
                # Vérifie si la variable `nombre_a_droite` n'est pas nulle pour la division
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")
                else:
                    resultat = nombre_a_gauche / nombre_a_droite
            # Si on est dans le cas par défaut, c'est que le symbole est incorrect.
            case _:
                print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

        # Affiche le résultat
        print(f"Le résultat de l'opération est: {resultat}")

if __name__ == "__main__":
    main()


    