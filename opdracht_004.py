# schrijf een programma dat berekent of een jaar een schrikkeljaar is
# een jaar is een schrikkeljaar als:
# - het jaartal deelbaar is door 4
# - niet deelbaar is door 100
#
# 1999 is GEEN schrikkeljaar
# 2004 is een schrikkeljaar
# 2000 is GEEN schrikkeljaar

def is_schrikkeljaar(n:int) -> bool:
    # TODO
    return False

if __name__ == "__main__":

    # vraag de gebruiker om input
    y = input("Geef een jaar in >")

    # probeer tekst om te zetten naar een getal
    try:
        y = int(y)
    except:
        print("Dat is geen getal.")
        pass

    # bereken of dit jaar een schrikkeljaar is
    s = is_schrikkeljaar(y)

    # toon het aan de gebruiker
    if s:
        print("%d is een schrikkeljaar." % y)
    else:
        print("%d is GEEN schrikkeljaar." % y)
