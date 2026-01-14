Counter = int(1)
Fehlercounter = int(0)
while Counter == 1:
    print('Wann wurde Till Emanuel Buchwald geboren ? ')
    Antwort = str(input('a.2005 b.1999 c.2002 Wähle eine der Antworten '))

    if Antwort == 'a':
        print('Diese Antwort ist leider Falsch. Versuche es erneut')
        Fehlercounter = Fehlercounter + 1
    elif Antwort == 'b':
        print('Diese Antwort ist leider Falsch. Versuche es erneut')
        Fehlercounter = Fehlercounter + 1
    elif Antwort == 'c':
        print('Diese Antwort ist richtig. Gut gemacht!')
        Counter = 2
while Counter == 2:
     print('Wo wohnt Till ? ')
     Antwort2 = str(input('a.Göppingen b.Rechberghausen c.Uhingen  Wähle eine der Antworten '))
     if Antwort2 == 'a':
        print('Diese Antwort ist leider Falsch. Versuche es erneut')
        Fehlercounter = Fehlercounter + 1
     elif Antwort2 == 'b':
        print('Diese Antwort ist richtig. Gut gemacht!')
        Counter = 3
     elif Antwort2 == 'c':
        print('Diese Antwort ist leider Falsch. Versuche es erneut')
        Fehlercounter = Fehlercounter + 1

while Counter == 3:
      print('Was für ein Auto fährt Till ? ')
      Antwort3 = str(input('a.Audi b.Mercedes c.BMW Wähle eine der Antworten '))

      if Antwort3 == 'a':
        print('Diese Antwort ist leider Falsch. Versuche es erneut')
        Fehlercounter = Fehlercounter + 1
      elif Antwort3 == 'b':
         print('Diese Antwort ist leider Falsch. Versuche es erneut')
         Fehlercounter = Fehlercounter + 1
      elif Antwort3 == 'c':
         print('Diese Antwort ist richtig. Gut gemacht!')
         Counter = 4
if Counter == 4:
    print('Super gemacht du hast alle Fragen richtig beantwortet und hattest ',Fehlercounter , 'Fehler')
