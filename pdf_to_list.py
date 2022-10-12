import pdfplumber
import re

""" with pdfplumber.open(r"commandes/20-09.pdf") as pdf:
    for j in range(len(pdf.pages)):
        f_page = pdf.pages[j]
        texte = ""
        for i in range(len(f_page.chars)):
            texte= texte + f_page.chars[i]['text']
        texte.split(" ")
        print(texte) """


pdf = pdfplumber.open("commandes/13-09.pdf")
page = pdf.pages[0]

texte = ""
for i in range(len(page.chars)):
    texte = texte + page.chars[i]['text']

# print(texte)
texte = re.split('Total TTC', texte)
aliments = texte[1]

# ----- DEBUT DES FILTRES SUR LES IMPORTS ----- 

# separateur de [TEXTE 123G]
test = re.split('[a-zA-Z ]* [0-9]*G', aliments)

# separateur sur les €texte d'un aliment

opti = []

for i in range(len(test)):
    opti = opti + re.split('€(?=[a-zA-Z])', test[i])

print(opti)

for i in range(0, len(opti)-1, 2):
    prix_complet = re.split('€', opti[i+1])
    prix_unit = float(prix_complet[0])


    ####  test de qt avec 1 digit ####

    qt = int(prix_complet[1][0])
    prix_total = float(prix_complet[1][1:])


    if abs(prix_unit*qt-prix_total) <= 0.001:
        opti[i+1] = [qt]
    else : 
        opti[i] = [int(prix_complet[1][0:2])]


for i in range(len(opti)):
    print(opti[i])
    if i % 2 == 1:
        print("")
