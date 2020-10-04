# schrijf een programma dat je BMI berekent
# BMI (body mass index) kan je berekenen als volgt:
# gewicht (in kg) / lengte (in cm) * lengte

def vraag_lengte() -> int:
    l = input("Geef je lengte in (cm)>")
    try:
        l = int(l)
    except:
        pass
    if l < 0 or l > 250:
        print("Je lengte moet tussen 0 en 250 cm liggen.")
    return l

def vraag_gewicht() -> int:
    # TODO
    return 0

def bereken_bmi(lengte: int, gewicht: int) -> float:
    # TODO
    return 0

if __name__ == "__main__":

    # vraag de gebruiker om input
    l = vraag_lengte()
    g = vraag_gewicht()

    # bereken
    b = bereken_bmi(l, g)

    # toon het resultaat aan de gebruiker
    print("Je BMI is %f" % b)