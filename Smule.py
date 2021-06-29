



kjente_brukere = ["Kari","Eva", "Emir", "Muffin", "Smule", "Jens", "Åge", "Olav", "Renate", "Q"]

print(len(kjente_brukere))

while True:
    print("Hei! Mitt navn er Smule")
    name = input("Hva er ditt navn?: ").strip().capitalize()

    if name in kjente_brukere:
        print("Navn gjennkjent, velkommen " + (name) + "!")
        remove = input("Ønsker du å bli slettet fra våre systemem (ja/nei) ?").strip().lower()
        if remove == "ja":
            kjente_brukere.remove(name)
            print("Så dumt! Håper vi en gang treffes igjen!")
        elif remove == "nei":
            print("Så bra!! Jeg ville ikke at du skulle forlate meg!")



    else:
        print("Jeg tror ikke jeg har møtt deg enda {}".format(name))
        add_me = input("Vil du bli lagt til i våre systemer (ja/nei): ").strip().lower()
        if add_me == "ja":
            kjente_brukere.append(name)
            print("Da er du blitt registrert i våre systemer! Ha en fin dag videre.")
        elif add_me == "nei":
            print("Ingen problem! Vi snakkes.")


print(len(kjente_brukere))

