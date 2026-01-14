#Dateiname: Interaktive Programme.py
#Das Programm fragt nach einem Namen und gibt einen Gruß aus, welcher diesen Namen enthält
#Autor: Till Buchwald
#Letze Änderung: 04.12.2024

name =  input('Name:')
gruß = 'Hallo ' + name + '!'
print(gruß)

#Berechnung von Volumen eines Zylinders
print('Berechnung des Volumen eines Zylinders')
durchm = input('Durchmesser in Meter:')
hoehe = input('Höhe in Meter:')

#Verarbeitung
h = float(hoehe)
d = float(durchm)
volumen = (d/2)**2*h 

#Ausgabe
text = 'Das Volumen beträgt '+ str(volumen) + 'Kubikmeter.'
print(text)
#input('Programm beenden mit ENTER')

#Berechnung Urlaubskosten pro Tag
print('Berechnung der Urlaubskosten pro Tag')
hotel = float(input('Hotelkosten: '))
essen = float(input('Gesamtkosten für Restaurants: '))
tage = float(input('Anzahl der Urlaubstage: '))

#Verarbeitung
kosten = (hotel + essen) / tage
#Ausgabe
print('Mittlere Kosten pro Urlaubstag: ', kosten)
