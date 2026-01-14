#Dateiname: JSON_Suche.py
#Das Programm durchsucht eine JSON Datei nach Sätzen mit einem bestimmten Schlagwort und hebt diese hervor
#Autor: Till Buchwald
#Letze Änderung: 10.01.2025

import re
import json

# Funktionen

def lese_datei(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("\u274C Datei nicht gefunden: Bitte stellen Sie sicher, dass die Datei existiert.")
        return None
    except IOError:
        print("\u274C Fehler beim Lesen der Datei.")
        return None

def extrahiere_daten(text):
    return re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

def zaehle_daten(daten_liste):
    daten_dict = {}
    for datum in daten_liste:
        daten_dict[datum] = daten_dict.get(datum, 0) + 1
    return daten_dict

def finde_exzellente_kommentare(text):
    return [kommentar for kommentar in text.splitlines() if re.search(r'\bexzellent\b', kommentar, re.IGNORECASE)]

def speichere_json(dateiname, daten):
    try:
        with open(dateiname, 'w', encoding='utf-8') as file:
            json.dump(daten, file, ensure_ascii=False, indent=4)
        print(f"\u2705 Datei erfolgreich gespeichert: {dateiname}")
    except IOError:
        print(f"\u274C Fehler beim Schreiben der Datei: {dateiname}")

# Hauptlogik

def main():
    dateiname = 'feedback.txt'
    text = lese_datei(dateiname)

    if text is None:
        return

    # a) Extrahiere Daten
    daten_liste = extrahiere_daten(text)
    daten_dict = zaehle_daten(daten_liste)

    # b) Finde "exzellente" Kommentare
    exzellente_kommentare = finde_exzellente_kommentare(text)

    # c) Speichere Ergebnisse
    speichere_json('datums_vorkommen.json', daten_dict)
    speichere_json('exzellente_feedbacks.json', exzellente_kommentare)

if __name__ == '__main__':
    main()
