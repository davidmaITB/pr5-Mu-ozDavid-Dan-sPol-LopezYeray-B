'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

blsshsfgh
'''
insultos ={
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
        "CAT": "Insulto4",
        "ESP": "come mierda",
        "ENG": "Insult4_EN",
        "KLI": "Insult4_KLI"
    },
    "tita petita": {
        "CAT": "Insulto5",
        "ESP": "Insult5_ES",
        "ENG": "Insult5_EN",
        "KLI": "Insult5_KLI"
    },
    "fill de puta": {
        "CAT": "Insulto6",
        "ESP": "Insult6_ES",
        "ENG": "Insult6_EN",
        "KLI": "Insult6_KLI"
    },
    "puter": {
        "CAT": "Insulto7",
        "ESP": "Insult7_ES",
        "ENG": "Insult7_EN",
        "KLI": "Insult7_KLI"
    },
    "disminuit": {
        "CAT": "Insulto8",
        "ESP": "Insult8_ES",
        "ENG": "Insult8_EN",
        "KLI": "Insult8_KLI"
    }

insulto = input("Escribe un insulto en catalán: ")
if insulto in insultos:
    print(f"Traducción a castellano: {insultos[insulto]['ESP']}")
    print(f"Translation to English: {insultos[insulto]['ENG']}")
    print(f"Translation to Klingon: {insultos[insulto]['KLI']}")
else:
    print("Insulto no encontrado en la base de datos.")
