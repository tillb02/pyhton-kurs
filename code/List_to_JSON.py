#Dateiname: Teilprüfung 3 Till-Emanuel Buchwald.py
#Autor: Till Buchwald
#Letze Änderung: 20.12.2024

import json

def read_names_from_file(filename):
    """Liest eine Liste von Namen aus einer Textdatei, wobei jeder Name in einer neuen Zeile steht."""
    try:
        with open(filename, 'r') as file:
            names = file.read().splitlines()
        print(f"Erfolgreich {len(names)} Namen aus {filename} gelesen.")
        return names
    except FileNotFoundError:
        print(f"Fehler: Datei '{filename}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    return []

def write_names_to_json(names, output_filename):
    """Schreibt eine Liste von Namen in eine JSON-Datei."""
    try:
        with open(output_filename, 'w') as file:
            json.dump(names, file, indent=4)
        print(f"Namen erfolgreich in {output_filename} gespeichert.")
    except Exception as e:
        print(f"Ein Fehler ist beim Schreiben der Datei aufgetreten: {e}")

def main():
    """Bietet eine benutzerbasierte Konsolenoberfläche."""
    while True:
        print("\nWähle eine Option:")
        print("1: Namen aus einer Datei lesen")
        print("2: Namen in eine JSON-Datei speichern")
        print("3: Beenden")
        
        choice = input("Deine Auswahl: ")
        
        if choice == '1':
            filename = input("Gib den Namen der Datei ein, aus der die Namen gelesen werden sollen: ")
            names = read_names_from_file(filename)
        elif choice == '2':
            if 'names' in locals() and names:
                output_filename = input("Gib den Namen der JSON-Datei ein, in der die Namen gespeichert werden sollen: ")
                write_names_to_json(names, output_filename)
            else:
                print("Keine Namen vorhanden. Bitte zuerst Namen aus einer Datei lesen.")
        elif choice == '3':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
