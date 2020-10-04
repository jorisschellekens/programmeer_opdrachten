#  Schrijf een programma dat de straal van een cirkel als input krijgt, en de oppervlakte berekent

def oppervlakte(straal: float) -> float:
    # TODO
    return 0

if __name__ == "__main__":

    # vraag de gebruiker om input
    s = input("Geef de straal in >")

    # probeer tekst om te zetten naar een kommagetal
    try:
        s = float(s)
    except:
        print("Dat is geen getal.")
        pass

    # bereken de oppervlakte
    o = oppervlakte(s)

    # toon het aan de gebruiker
    print("De oppervlakte van de cirkel is %f" % o)
