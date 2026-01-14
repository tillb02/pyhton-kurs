elemente = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]

#b)
# Die Funktion 'pruefe_element' überprüft, ob ein spezifisches Tupel in der Liste 'elemente' vorhanden ist.
def pruefe_element(buchstabe, zahl):
    if (buchstabe, zahl) in elemente:
        print(f"Element gefunden: ({buchstabe}, {zahl})")
    else:
        print("Element nicht gefunden.")

#c)
# Die Funktion 'zeichenkette_in_zahl' versucht, eine Eingabe von einer Zeichenkette in eine ganze Zahl umzuwandeln.
def zeichenkette_in_zahl(zeichenkette):
    zahl = int(zeichenkette)
    print(f"Umwandlung erfolgreich: {zahl}")
    return zahl

#e)
while True:
    aktion = input("Wähle eine Aktion: 'suchen', 'umwandeln' oder 'beenden': ")
    if aktion == 'suchen':
        buchstabe = input("Gib den Buchstaben des Elements ein: ")
        zahl = int(input("Gib die Zahl des Elements ein: "))
        pruefe_element(buchstabe, zahl)
    elif aktion == 'umwandeln':
        zeichenkette = input("Gib eine Zeichenkette ein, die in eine Zahl umgewandelt werden soll: ")
        umgewandelte_zahl = zeichenkette_in_zahl(zeichenkette)
        # f) Kontrollstruktur für umgewandelte Zahl
        if umgewandelte_zahl is not None:
            if umgewandelte_zahl > 0:
                print("Die Zahl ist positiv.")
            elif umgewandelte_zahl < 0:
                print("Die Zahl ist negativ.")
            else:
                print("Die Zahl ist Null.")
    elif aktion == 'beenden':
        break
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut.")
