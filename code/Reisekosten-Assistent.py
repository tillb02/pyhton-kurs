Rb = float(input('Kosten für den Reisebus in EUR: '))
H = float(input('Kosten für das Hotel pro Person in EUR: '))
Rf = float(input('Kosten für den Reiseführer in EUR: '))
At = int(input('Anzahl der Reisegäste: '))

H = H * At

Gk = Rb + H + Rf
print('Gesamtkosten der Reise: ', Gk , ' Euro')

KpG = Gk / At
print('Jeder Gast muss ' , KpG , ' Euro bezahlen')
