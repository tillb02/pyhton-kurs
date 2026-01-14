#a)

#Erstellen der Liste
Liste = [1,2,3,4,5,6,7,8,9,10]
#Summieren der Listeneinträge
Summe = float(sum(Liste))
#Berechnen des Durchschnitts der Einträge
Durchschnitt = float(Summe / len(Liste))
#Ausgeben der Zahlenwerte
print(Summe)
print(Durchschnitt)

#b)

String = str(input('Gebe einen Zahlenwert ein:'))

if '.' in String:
    Datentyp = 'Float'
else:
    Datentyp = 'Integer'

print(Datentyp)

#c)
#Eingabe der beiden Zahlen
Zahl1 = float(input('Gebe eine Zahl ein: '))
Zahl2 = float(input('Gebe eine weitere Zahl ein: '))
#Multiplizieren der beiden Zahlen
Summe = Zahl1 * Zahl2
#Ausgeben des Ergebnisses
print('Das Ergebnis der Multiplikation ist: ' + Summe)

#d)
print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = float(input("Bitte gib eine Zahl ein: "))
zahl2 = float(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)

#Der Code war falsch da der Input die Zahlen in einen String schreibt und dann beide Zahlen hintereinander ausgibt, anstatt diese zu Addieren.
#Durch das angeben des Floats mit dem Input werden die Zahlen direkt in einen Float umgewandelt und so korrekt addiert
