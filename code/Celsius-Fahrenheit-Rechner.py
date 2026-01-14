def temperatur_umwandler(t , e='C'):
        if e == 'F':
            return (t-32)*5/9

        elif e == 'C':
            return t*9/5+32
        else:
            return None
try:
    while True:
        t = float(input('Gebe die Temperatur (als Zahl) ein welche Umgewandelt werden soll: '))
        e = str(input('Gebe die Einheit der Temperatur ein (C/F): '))
        umgerechnet = temperatur_umwandler(t,e)
        if umgerechnet is not None:
            if e == 'C':
                print(f"{t} °C entspricht {umgerechnet} °F")
            else:
                print(f"{t} °F entspricht {umgerechnet} °C")
except ValueError:
        print("Bitte gib eine gültige Zahl für die Temperatur ein.")
except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

print('Die Temperatur beträgt umgerechnet ',t ,e)
f = str(input('Möchtest du eine weitere Temperatur umrechnen ? (j/n) '))
exit
