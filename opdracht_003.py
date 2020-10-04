# schrijf een programma dat de volgende berekening maakt
# n+ n*n + n*n*n

def bereken(n:float) -> float:
    # TODO
    return 0

if __name__ == "__main__":

    # vraag de gebruiker om input
    s = input("Geef een getal in >")

    # probeer tekst om te zetten naar een kommagetal
    try:
        s = float(s)
    except:
        print("Dat is geen getal.")
        pass

    # bereken
    o = bereken(s)

    # toon het aan de gebruiker
    print("Het resultaat van de berekening is %f" % o)
