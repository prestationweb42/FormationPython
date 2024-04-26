# Enregistrez des données complexes avec des dictionnaires
nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
print(nouvelle_campagne)

# Accéder à une valeur avec sa clé
print(nouvelle_campagne["date_de_début"])

# Définir une nouvelle valeur avec sa clé
nouvelle_campagne["date_de_début"] = "02/02/2022"
print(nouvelle_campagne)

# Ajouter une nouvelle clé / valeur
nouvelle_campagne["date_de_fin"] = "03/03/2023"
print(nouvelle_campagne)

# Supprimer une paire clé / valeur avec del
del nouvelle_campagne["date_de_fin"] 
print(nouvelle_campagne)

# Vérifier la présence d'une clé spécifique
"date_de_début" in nouvelle_campagne
print("date_de_début" in nouvelle_campagne)

# Exercice -> créer un dictionnaire fruits
fruits = {
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange",
    }
print(fruits)

# ajout de kiwi vert
fruits["kiwi"] = "vert"
print(fruits)

# Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane
couleur_banane = fruits["banane"]
print(couleur_banane)

# Modifiez la valeur associée à la clé  pomme  pour  vert
fruits["pomme"] = "verte"
print(fruits)

# Supprimez la clé  orange  du dictionnaire  fruits
del fruits['orange']
print(fruits)