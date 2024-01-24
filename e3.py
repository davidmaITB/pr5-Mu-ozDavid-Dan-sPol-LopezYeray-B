'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

blsshsfgh
'''
insultos ={
    "cap de suru": {
        "CAT": "Insulto1",
        "ESP": "Insult1_ES",
        "ENG": "Insult1_EN",
        "KLI": "Insult1_KLI"
    },
    "bufa gaitas": {
        "CAT": "Insulto2",
        "ESP": "Insult2_ES",
        "ENG": "Insult2_EN",
        "KLI": "Insult2_KLI"
    },
    "ruc": {
        "CAT": "Insulto3",
        "ESP": "Insult3_ES",
        "ENG": "Insult3_EN",
        "KLI": "Insult3_KLI"
    },
    "menja merda": {
        "CAT": "Insulto4",
        "ESP": "Insult4_ES",
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
}
insulto = input("Escribe un insulto en catalán: ")
if insulto in insultos:
    print(f"Traducción a castellano: {insultos[insulto]['ESP']}")
    print(f"Translation to English: {insultos[insulto]['ENG']}")
    print(f"Translation to Klingon: {insultos[insulto]['KLI']}")
else:
    print("Insulto no encontrado en la base de datos.")
