# P1C6 
# Enregistrez des groupes de données avec les listes avec crochets
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print(plateformes_sociales)

# Pour accéder aux éléments d’une liste, on utilise un indice. 
# Une liste commence à indice 0
plateformes_sociales[0]
# réponse -> "Facebook"

print(f"Le réseau en position 0 est : {plateformes_sociales[0]}")
print(f"Le réseau en position 0 est : {plateformes_sociales[2]}")

# Pour accéder au dernier élément de la liste, utilisez l’indice -1.
print(f"Le réseau en position -1 est : {plateformes_sociales[-1]}")

# Accédez aux éléments d’une chaîne de caractères 
langage  = "PYTHON"
langage[2]
# réponse : T

# Modifier un élément d'une liste
# LinkedIn prend la place de Snapchat
plateformes_sociales[2] = "LinkedIn"
print(plateformes_sociales)

# Ajoutez, retirez et triez les listes
# Ajoutez (en dernier) -> append()
plateformes_sociales.append("TikTok")
print(plateformes_sociales)

# Retirez -> remove()
plateformes_sociales.remove("TikTok")
print(plateformes_sociales)

# Trier une liste : sort()
print(plateformes_sociales.sort())

# Longueur d'une liste avec la méthode : len()
print(len(plateformes_sociales))

# Trouver un élément avec l'opérateur in , reetourne True ou False
nombres = [1,2,3,4,5]
# >>> 5 in nombres
# True
# >>> 8 in nombres
# False
print(5 in nombres)
print(8 in nombres)

# Exercice
fruits = ["pomme", "banane", "orange"]
print(fruits)
# Ajout de kiwi
fruits.append("kiwi")
print(fruits)
# Supprimer
fruits.remove("orange")
print(fruits)
# Modifier le 2eme élement en ananas
fruits[1] = "ananas"
print(fruits)
# Trier la liste
fruits.sort()
print(fruits)

