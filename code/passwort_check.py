#Passwort Check

Passwort = '12345'
Input = str(input('Bitte geben Sie ihr Passwort ein !'))

if Passwort == Input:
    print('Passwort wurde erkannt.')
    print('Willkommen')
else:
    print('Falsches Passwort !')
    print('Bitte erneut versuchen.')


#Kinokarte
Alter = int(input('Willkommen im Kino! Bitte geben SIe Ihr Alter an!'))
print('(Alter Jahre): ' ,Alter)

if Alter > 17:
    Kosten = 8.50
else:
    Kosten = 5.00

print('Ihr Ticket kostet ' ,Kosten,'€')
print('Viel Spaß!')

#Auskunft
Fall = str(input('Willkommen! Bitte stellen Sie Ihre Frage.'))
print('Frage: ',Fall)

if 'Wann' in Fall:
    print('Vielen Dank für Ihre Frage zum Liefertermin.')
    print('Carla hilft Ihnen gerne weiter.')
elif 'Rechnung' in Fall:
    print('Vielen Dank für Ihre Frage zu einer Rechnung.')
    print('Tom hilft Ihnen gerne weiter.')
else:
    print('Ihr Anliegen konnte nicht ermittelt werden.')
    print('Ihr Anliegen wird anschließend von Kim geprüft')

    #Grundumsatz Kalorien
    G = str(input('Bitte Geschlecht angeben (M/W)'))
    a = float(input('Bitte dein Alter angeben'))
    h = float(input('Bitte deine Körpergröße in cm angeben'))
    m = float(input('Bitte dein Gewicht in kg angeben'))

if 'M'or 'm' in G:
    Umsatz = float(66.5 + 13 * m + 5 * h - 6.8 * a)
    print('Dein Grundumsatz in Kalorien pro Tag beträgt: ' , Umsatz)
elif 'W' or 'w' in G:
    Umsatz = float(655 + 9,6 * m + 1,8 * h - 4,7 * a)
    print('Dein Grundumsatz in Kalorien pro Tag beträgt: ' , Umsatz)
