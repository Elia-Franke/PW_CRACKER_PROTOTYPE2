from time import sleep
print("Taschenrechner von Elia am 12-07-2021")
print("Benutze +, -, *, / , Potenz , <, > , =")
fragen = input("Willst du +, -, *, /, eine Potenz rechnen oder Nummern vergleichen?")

if fragen == "+":
    summand_1 = input("1. Summand:")
    summand_2 = input("2. Summand:")
    Summe = float(summand_1) + float(summand_2)
    print(Summe)
elif fragen == "-":
    minus_1 = input("Minuend:")
    minus_2 = input("Subtrahend:")
    Differenz = float(minus_1) - float(minus_2)
    print(Differenz)
elif fragen == "*":
    Faktor_1 = input("1. Faktor:")
    Faktor_2 = input("2. Faktor:")
    Produkt = float(Faktor_1) * float(Faktor_2)
    print(Produkt)
elif fragen == "/":
    quotient_1 = input("Dividend:")
    quotient_2 = input("Divisor:")
    Quotient = float(quotient_1) / float(quotient_2)
    print(Quotient)
elif fragen == "Potenz":
    eins_Zahl = input("1. Zahl")
    zwei_Zahl = input("Exponent")
    Ergebnis_Potenz = float(eins_Zahl) ** float(zwei_Zahl)
    print(Ergebnis_Potenz)
elif fragen == "<":
    eins_Zahl_eins = input("1. Zahl")
    zwei_Zahl_zwei = input("2. Zahl")
    Ergebnis_lt = float(eins_Zahl_eins) < float(zwei_Zahl_zwei)
    print(Ergebnis_lt)
elif fragen == ">":
    eins_Zahl_eins_eins = input("1. Zahl")
    zwei_Zahl_zwei_zwei = input("2. Zahl")
    Ergebnis_gt = float(eins_Zahl_eins_eins) > float(zwei_Zahl_zwei_zwei)
    print(Ergebnis_gt)
elif fragen == "=":
    eins_Zahl_eins_eins_eins = input("1. Zahl")
    zwei_Zahl_zwei_zwei_zwei = input("2. Zahl")
    Ergebnis_st = float(eins_Zahl_eins_eins_eins) == float(zwei_Zahl_zwei_zwei_zwei)
    print(Ergebnis_st)

sleep(1111111)
