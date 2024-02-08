'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

Traduccio d'insultss
'''
insults ={
    "cap de suru": {
        "CAT": "suru",
        "ESP": "cabeza de corcho",
        "ENG": "hat nap",
        "KLI": "vishmila"
    },
    "bufa gaitas": {
        "CAT": "bufa gaitas",
        "ESP": "sopla gaitas",
        "ENG": "blow bagpipes",
        "KLI": "habibi "
    },
    "ruc": {
        "CAT": "ruc",
        "ESP": "asno",
        "ENG": "donkey",
        "KLI": "hasbulla"
    },
    "menja merda": {
        "CAT": "menja merda",
        "ESP": "come mierda",
        "ENG": "eat shiter",
        "KLI": "atapundimak"
    },
    "tita petita": {
        "CAT": "tita petita",
        "ESP": "pene pequeño",
        "ENG": "small dick",
        "KLI": "sahbi"
    },
    "fill de puta": {
        "CAT": "fill de puta",
        "ESP": "hijo de puta",
        "ENG": "son of a bitch",
        "KLI": "habsibi"
    },
    "puter": {
        "CAT": "puter",
        "ESP": "putero",
        "ENG": "whore",
        "KLI": "hotfordowam"
    },
    "disminuit": {
        "CAT": "disminuit",
        "ESP": "disminuido",
        "ENG": "retard",
        "KLI": "slasnfme"
    }}
try:
    insult = input("Possa un dels seguents insults en catala: (cap de suru, bufa gaitas, ruc, tita petita, fill de puta, puter, disminuit)  ")
    if insult in insults:
        print(f"Traducció a Castella: {insults[insult]['ESP']}")
        print(f"Traduccio a English: {insults[insult]['ENG']}")
        print(f"Traduccio a Klingon: {insults[insult]['KLI']}")

except:
    print("El insult que has introduit no es troba en el nostre diccionari o ha estat introduit incorrectament.")