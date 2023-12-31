"""
Répétez le mot-clé jusqu'à ce qu'il atteigne la longueur du message.
Message : CODINGAME
Mot-clé : APPLEAPPL

Additionnez le message et le mot-clé lettre par lettre en attribuant des valeurs entières aux lettres de 0 à 25 dans l'ordre alphabétique 
(c'est-à-dire A=0, B=1, C=2, etc.)."""
*l,k=open(0).read().split()
a,b,*l=map(int,l)
k*=a
for i,j in zip(l,k):print(end=chr(65+(i-ord(j)+65)%26))

"""renvoyer la moyenne des valeurs ascii des entrées"""
s=[ord(a) for a in input()]
print(sum(s)//len(s))

"""
Mettre en majuscule la première lettre de chaque mot et en minuscule les lettres suivantes."""

import sys
s = input()
# Diviser la chaîne en mots
mots = s.split()
# Appliquer les modifications à chaque mot
resultat = ' '.join([mot.capitalize() for mot in mots])
print(resultat)

""" Calculer l'air d'un trapeze"""

a = int(input())
b = int(input())
h = int(input())

# Calculer l'aire du trapèze
aire_trapeze = 0.5 * (a + b) * h

# Afficher l'aire avec une décimale
print(format(aire_trapeze, ".1f"))

"""
prend a et b et une plage s et e retourner le nombre de chiffres dans les categorie suivante:

Multiples de a, mais pas de b
Multiples de b, mais pas de a
Multiples à la fois de a et b
Aucun des cas ci-dessus
"""

a, b = [int(i) for i in input().split()]
s, e = [int(i) for i in input().split()]

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
for i in range(s, e+1):
    if i%a ==0 and i%b!=0:
        cat1+=1
    elif i%b ==0 and i%a!=0:
        cat2+=1
    if i%a ==0 and i%b==0:
        cat3+=1
    if i%a !=0 and i%b!=0:
        cat4+=1

print(cat1,cat2,cat3,cat4)

"""
votre adversaire peut attaquer de trois côtés (gauche, droite ou en haut), et il peut utiliser deux types d'attaques : 
une attaque normale (usual) ou une attaque puissante (hard). 
Vous devez déterminer la meilleure réponse en fonction de l'attaque et du côté de l'adversaire.

Voici un résumé des règles :

Si l'adversaire utilise une attaque normale (usual), vous devez vous défendre du même côté que lui.
Si l'adversaire utilise une attaque puissante (hard), vous devez esquiver dans la direction opposée à son attaque
"""

power = input()
side = input()
if power == "usual":
    print('defence')
    print(side)
else:
    print('dodging')
    if side=="above":
        print('any')
    elif side =="right":
        print('left')
    else:
        print('right')

"""
calculer le troisième angle d'un triangle connaissant les deux premiers angles
"""
a, b = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(180 - a - b)

"""
produire un entier en concaténant les chiffres du milieu des entiers fournis
"""

n = int(input())
numbers=[]
for i in input().split():
    numbers.append(i)

middle_digits = []

# Parcourir chaque entier
for integer in numbers:
    stripped_integer = str(int(integer))

    middle_digits.append(stripped_integer[1:-1])
try:
    result = int("".join(middle_digits))
except:
    result =0

print(result)


"""
vous recevez une chaîne de chiffres. 
Pour chaque chiffre (en commençant par le plus à gauche), 
vous devez calculer ce chiffre élevé à la puissance de son indice, 
puis afficher la somme cumulative jusqu'à présent. 
"""
_str = input()

cumulative_sum = 0

for i, digit_char in enumerate(_str):
    digit = int(digit_char)
    cumulative_sum += digit ** i
    print(cumulative_sum)


"""
 calculer le nombre de rangées dans une mosquée,
 en fonction de la longueur de la mosquée (l) et de la distance entre les rangées (d)
 """
print((int(input())*100)//int(input()))


"""
 calculer le pourcentage (arrondi à l'entier supérieur)
 qu'un ensemble de caractères spécifiés représente dans une chaîne donnée (en ignorant la casse).
"""
import math
# Lire la chaîne et le nombre de caractères spécifiés
s = input()
n = int(input())
# Initialiser un dictionnaire pour stocker le nombre d'occurrences de chaque caractère
occurrences = {}
# Compter le nombre d'occurrences de chaque caractère (en ignorant la casse)
for char in s.lower():
    occurrences[char] = occurrences.get(char, 0) + 1
# Parcourir les caractères spécifiés
for _ in range(n):
    # Lire le caractère spécifié
    specified_char = input().lower()
    # Obtenir le nombre d'occurrences de ce caractère dans la chaîne
    char_count = occurrences.get(specified_char, 0)
    # Calculer le pourcentage (arrondi à l'entier supérieur)
    try:
        percentage = math.ceil((char_count / len(s)) * 100)
    # Afficher le résultat
        print(f"{percentage}%")
    except:
        print("0%")