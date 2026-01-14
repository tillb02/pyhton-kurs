print('Berechnung des Bremswegs')
v = float(input('Geschwindigkeit in kmh:'))
Wetter = str(input('Wetterverhältnisse (trocken/nass): '))

v = (v / 3.6)
if Wetter == 'trocken': 
    a = 8
elif Wetter == 'nass':
    a = 7
else:
    print('Das Wetter muss mit "trocken" oder "nass" angeben werden')
    
s = float(v**2 / (2*a))

print('Der Bremsweg beträgt: ',s, ' Meter')
