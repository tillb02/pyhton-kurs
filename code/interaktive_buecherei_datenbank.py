#Dateiname: interaktive_buecherei_datenbank.py
#Das Programm lässt den Nutzer interaktiv nach verschiedenen Büchern suchen, Bücher hinzufügen und Filtern
#Autor: Till Buchwald
#Letze Änderung: 24.01.2025

class Buch:
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):
        return f"{self.titel} von {self.autor} ({self.kategorie}) - {self.preis:.2f} €"

class Buchladen:
    def __init__(self):
        self.inventar = []

    def buch_hinzufuegen(self, buch):
        """Fügt ein Buch zum Inventar hinzu."""
        self.inventar.append(buch)

    def suche_nach_kategorie(self, kategorie):
        """Durchsucht das Inventar nach einer bestimmten Kategorie und gibt passende Bücher zurück."""
        return [buch for buch in self.inventar if buch.kategorie.lower() == kategorie.lower()]

    def berechne_gesamtpreis(self, buchauswahl):
        """Berechnet den Gesamtpreis für eine Auswahl von Büchern."""
        return sum(buch.preis for buch in buchauswahl)

# Beispielverwendung
def main():
    # Erstelle einige Buchobjekte
    buch1 = Buch("Buch1", "Name1", "Roman", 19.99)
    buch2 = Buch("Buch2", "Name2", "Sachbuch", 24.95)
    buch3 = Buch("Buch3", "Name3", "Wissenschaft", 29.50)
    buch4 = Buch("Buch4", "Name4", "Roman", 14.99)

    # Erstelle den Buchladen
    buchladen = Buchladen()

    # Füge Bücher zum Inventar hinzu
    buchladen.buch_hinzufuegen(buch1)
    buchladen.buch_hinzufuegen(buch2)
    buchladen.buch_hinzufuegen(buch3)
    buchladen.buch_hinzufuegen(buch4)

    while True:
        print("\nWas möchten Sie tun?")
        print("1. Bücher nach Kategorie filtern")
        print("2. Gesamtpreis für eine Auswahl berechnen")
        print("3. Beenden")

        wahl = input("Wählen Sie eine Option (1/2/3): ")

        if wahl == "1":
            kategorie = input("Geben Sie die Kategorie ein: ")
            gefundene_buecher = buchladen.suche_nach_kategorie(kategorie)
            if gefundene_buecher:
                print(f"\nBücher in der Kategorie '{kategorie}':")
                for buch in gefundene_buecher:
                    print(buch)
            else:
                print(f"\nKeine Bücher in der Kategorie '{kategorie}' gefunden.")

        elif wahl == "2":
            print("\nVerfügbare Bücher:")
            for i, buch in enumerate(buchladen.inventar, start=1):
                print(f"{i}. {buch}")
            auswahl = input("Geben Sie die Nummern der Bücher ein, getrennt durch Kommas: ")
            try:
                indices = [int(x) - 1 for x in auswahl.split(",")]
                buchauswahl = [buchladen.inventar[i] for i in indices if 0 <= i < len(buchladen.inventar)]
                gesamtpreis = buchladen.berechne_gesamtpreis(buchauswahl)
                print(f"\nDer Gesamtpreis für die ausgewählten Bücher beträgt: {gesamtpreis:.2f} €")
            except (ValueError, IndexError):
                print("\nUngültige Eingabe. Bitte versuchen Sie es erneut.")

        elif wahl == "3":
            print("\nProgramm beendet.")
            break

        else:
            print("\nUngültige Option. Bitte wählen Sie erneut.")

if __name__ == "__main__":
    main()
