#Dateiname: Buecherei_Database.py
#Das Programm lässt den Nutzer interaktiv nach verschiedenen Büchern suchen, Bücher hinzufügen und Filtern
#Autor: Till Buchwald
#Letze Änderung: 13.12.2024


# Erstellen der Bücherei Datenbank
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
]

# Defiinieren der Funktion zum Suchen von Büchern + definieren des Rückgabewertes
def suche_buch(titel, autor=None):
    result = [buch for buch in buecherei_datenbank if buch["Titel"].lower() == titel.lower() and (autor is None or buch["Autor"].lower() == autor.lower())]
    return result

# Definieren der Funktion zum Hinzufügen neuer Bücher
def fuege_buch_hinzu(titel, autor, jahr):
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    buecherei_datenbank.append(neues_buch)
    print(f"Das Buch '{titel}' von {autor} (Erscheinungsjahr: {jahr}) wurde hinzugefügt.")

# Definieren der Funktion zum Filtern nach Jahren + Rückgabe Liste
def buecher_nach_jahr(jahr):
    return list(filter(lambda buch: buch["Jahr"] == jahr, buecherei_datenbank))

# Definieren der Funktion zum Anzeigen der Bücher, welche aktuell in der Datenbank vorhanden sind
def zeige_datenbank():
        print("\nAktuelle Bücherei-Datenbank:")
        for buch in buecherei_datenbank:
            print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Erscheinungsjahr: {buch['Jahr']}")

# Definieren des interaktiven Menüs mit Möglichkeiten zum Aufrufen der oben definierten Funktionen
def interaktives_menue():
    while True:
        print("\nBücherei-Verwaltung:")
        print("1. Buch suchen")
        print("2. Buch hinzufügen")
        print("3. Bücher nach Jahr filtern")
        print("4. Bücherei-Datenbank anzeigen")
        print("5. Programm beenden")

        try:
            auswahl = int(input("Bitte wähle eine Option (1-5): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gebe eine Zahl zwischen 1 und 5 ein.")
            continue

        if auswahl == 1:
            titel = input("Gebe den Titel des Buches ein: ")
            autor = input("Gebe den Autor ein (optional): ").strip() or None
            ergebnisse = suche_buch(titel, autor)
            if ergebnisse:
                print("\nGefundene Bücher:")
                for buch in ergebnisse:
                    print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Erscheinungsjahr: {buch['Jahr']}")
            else:
                print("Keine Bücher gefunden.")

        elif auswahl == 2:
            titel = input("Gebe den Titel des Buches ein: ")
            autor = input("Gebe den Autor ein: ")
            try:
                jahr = int(input("Gebe das Erscheinungsjahr ein: "))
                fuege_buch_hinzu(titel, autor, jahr)
            except ValueError:
                print("Ungültiges Erscheinungsjahr. Bitte gebe eine Zahl ein.")

        elif auswahl == 3:
            try:
                jahr = int(input("Gebe das Jahr ein: "))
                gefilterte_buecher = buecher_nach_jahr(jahr)
                if gefilterte_buecher:
                    print("\nBücher aus dem Jahr", jahr, ":")
                    for buch in gefilterte_buecher:
                        print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Erscheinungsjahr: {buch['Jahr']}")
                else:
                    print("Keine Bücher aus diesem Jahr vorhanden.")
            except ValueError:
                print("Ungültige Eingabe. Bitte gebe eine Zahl ein.")

        elif auswahl == 4:
            zeige_datenbank()

        elif auswahl == 5:
            print("Programm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Ungültige Option. Bitte wählen Sie eine Zahl zwischen 1 und 5.")

# Programm starten
if __name__ == "__main__":
    interaktives_menue()
