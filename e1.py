'''
David Muñoz
Pol Danés
Yeray Lopez
24 gener 2024

SeaTemp
'''

temperature_data = {
    2022: [13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14.0, 14.3, 16.0, 15.1, 14.0],
    2021: [13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7, 14.1],
    2020: [14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14.0, 14.3, 14.7, 15.6, 14.6, 14.2],
    2019: [13.9, 12.5, 13.3, 13.4, 14.0, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4, 14.1],
    2018: [13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14.0, 14.1, 14.3, 17.9, 17.7, 15.9, 14.4],
    2017: [13.7, 12.8, 13.4, 13.9, 14.0, 14.0, 13.9, 14.0, 14.0, 14.6, 14.8, 13.3, 13.9],
    2016: [14.1, 13.6, 12.9, 13.5, 14.0, 13.9, 14.0, 14.0, 14.2, 16.3, 16.5, 15.6, 14.4],
    2015: [14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1, 14.1],
    2014: [13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14.0, 14.5, 15.7, 16.5, 16.0, 14.5],
    2013: [13.2, 12.2, 12.0, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6, 13.7],
    2012: [13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9, 13.8],
    2011: [13.0, 12.5, 12.5, 13.6, 13.5, 14.0, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9, 14.1],
    2010: [12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14.0, 13.6],
    2009: [13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14.0, 16.2, 15.9, 14.5, 13.9],
    2008: [13.2, 13.0, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8, 13.7],
    2007: [14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14.0, 15.5, 15.5, 13.9, 14.1],
    2006: [12.5, 12.3, 12.1, 12.9, 13.1, 13.4, 13.2, 13.2, 14.0, 15.5, 17.3, 15.8, 13.8],
    2005: [13.3, 12.3, 12.3, 12.9, 13.4, 13.3, 13.3, 13.4, 13.9, 15.2, 17.1, 14.4, 13.7],
    2004: [13.5, 12.7, 12.3, 12.6, 13.2, 13.1, 13.3, 13.6, 14.9, 15.3, 15.4, 14.6, 13.7],
    2003: [13.6, 12.2, 12.5, 12.8, 14.7, 13.5, 13.6, 13.7, 14.2, 15.9, 15.3, 15.0, 13.9],
    2002: [13.2, 12.4, 12.9, 13.4, 13.7, 13.6, 14.4, 13.8, 14.3, 14.8, 15.3, 14.2, 13.8],
    2001: [13.8, 13.0, 12.6, 13.6, 13.5, 13.4, 14.0, 14.0, 14.2, 15.3, 16.8, 14.0, 14.0],
    2000: [12.7, 12.4, 12.6, 12.4, 13.0, 13.6, 13.3, 13.6, 13.5, 15.9, 15.3, 14.9, 13.6]
}

#Temperaturas de 2022
max_temperatura_2022 = float('-inf')
min_temperatura_2022 = float('inf')
sum_temperatura_2022 = 0
temp2022 = temperature_data[2022]

for temperatura in temp2022:
    if temperatura > max_temperatura_2022:
        max_temperatura_2022 = temperatura
    if temperatura < min_temperatura_2022:
        min_temperatura_2022 = temperatura
    sum_temperatura_2022 += temperatura

med_temperatura_2022 = sum_temperatura_2022 / len(temp2022)
print("Any 2022")
print("Maximum temperature:", f"{max_temperatura_2022:.2f}")
print("Minimum temperature:", f"{min_temperatura_2022:.2f}")
print("Average temperature:", f"{med_temperatura_2022:.2f}")


#Temperaturas de todos los años
max_temperatura = float('-inf')
min_temperatura = float('inf')
sum_temperatura = 0
for year, temperatures in temperature_data.items():
    for temperatura in temperatures:
        if temperatura > max_temperatura:
            max_temperatura = temperatura
        if temperatura < min_temperatura:
            min_temperatura = temperatura
        sum_temperatura += temperatura
#13.96
med_temperatura = sum_temperatura / 299

print("periode 2000-2022")
print("Maximum temperature:", f"{max_temperatura:.2f}")
print("Minimum temperature:", f"{min_temperatura:.2f}")
print("Average temperature:", f"{med_temperatura:.2f}")

