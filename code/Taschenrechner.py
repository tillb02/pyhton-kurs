#Dateiname: Taschenrechner.py
#Das Programm erfragt, welche Operation und mit welchen Zahlen diese durchgeführt werden soll + gibt Ergebnis aus
#Autor: Till Buchwald
#Letze Änderung: 06.12.2024

# Dem Benutzer werden die Auswahlmöglichkeiten angezeigt
print('Welche Operation soll ausgeführt werden ?')
print('a. Addition')
print('s. Subtraktion')
print('m. Multiplikation')
print('d. Division')

# Input Input Felder zum Aufnehmen der Nutzerdaten
Op = str(input('Gebe den Buchstaben für die gewünschte Operation ein: '))
z1 = float(input('Gebe die erste Zahl an: '))
z2 = float(input('Gebe die zweite Zahl an:'))

#Verarbeiten der Daten

#Eingabe a, addieren der Werte + Ausgabe Ergebnis
if Op == 'a':
    ergebnis = z1 + z2
    print('Das Ergebnis der Addition ist: ',ergebnis)
#Eingabe s, subtrahieren der Werte + Ausgabe Ergebnis
elif Op == 's':
    ergebnis = z1 - z2
    print('Das Ergebnis der Subtraktion ist: ',ergebnis)
#Eingabe m, multiplizieren der Werte + Ausgabe Ergebnis
elif Op == 'm':
    ergebnis = z1 * z2
    print('Das Ergebnis der Multiplikation ist: ',ergebnis)
#Eingabe d, dividieren der Werte + Ausgabe Ergebnis
elif Op == 'd':
   #Prüfung ob versucht wird durch 0 zu dividieren + Ausgabe Fehlertext
    if z2 == 0:
        print('Eine Division durch 0 ist leider nicht möglich, bitte wähle eine andere Zahl')
    else:
        ergebnis = z1 / z2
        print('Das Ergebnis der Division ist: ',ergebnis)
