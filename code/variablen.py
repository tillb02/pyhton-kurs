#a)
String = str('Hallo Welt') #Ein String stellt Zeichenketten aus Zahlen und Buchstaben dar
Integer = int(5) #Ein Integer stellt eine Ganzzahl dar
Float = float(5.5555) #Ein Float kann eine Gleitkommazahl darstellen
Boole = bool(1) #Ein Boole kann zwichen dem Wert 1 für richtig und dem Wert 0 für falsch unterscheiden

#b)
Liste = list['Hallo', 2 , 5.35]
for element in Liste:
    print(type(element))


#c)
#Um einen Int in einen Float zu casten nutzt man = float()) und sagt dann Float = Integer
Integer = 2
Float = float(Integer)
print(Float)

#d)
# Ein Tupel ist eine Sammlung, die geordnet, aber unveränderlich ist. Im Gegensatz dazu ist eine Liste geordnet und veränderlich.
# Das bedeutet, dass man die Elemente einer Liste ändern kann, die eines Tupels jedoch nicht. Beispiel für ein Tupel: (42, 3.14, "Hallo Welt")



#e)
String = str(input('Gebe einen Satz ein: '))
#Eingabe des Strings
Integer = int(input('Gebe eine Ganzzahl ein: '))
#Eingabe des Integers
Integer = str(Integer)
#Umwandlung des Integers in einen String
String = String + Integer
#Zusammenfügen der beiden Strings
print(String)
#Ausgeben des Zusammengefügten Strings
