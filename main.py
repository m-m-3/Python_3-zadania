def main():
    while True:
        print("\n=== MENU ===")
        print("1. Prosty kalkulator")
        print("2. Konwerter temperatur (C <-> F)")
        print("3. Średnia ocen ucznia")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            Kalkulator()
        elif choice == "2":
            KonwerterTemperatury()
        elif choice == "3":
            ObliczSredniaOcen()
        elif choice == "0":
            return
        else:
            print("Niepoprawny wybór.")
            input()


def WczytajLiczbe(tekst=""):
    while True:
        try:
            return float(input(tekst))
        except ValueError:
            print("Błąd, wpisz prawidłową liczbę: ", end="")


def WczytajInt(tekst=""):
    while True:
        try:
            return int(input(tekst))
        except ValueError:
            print("Błąd, wpisz prawidłową liczbę całkowitą: ", end="")


def Pauza():
    input("Wciśnij Enter, aby wrócić do menu...")


def Kalkulator():
    print("=== KALKULATOR ===")
    Pauza()


def KonwerterTemperatury():
    print("=== KONWERTER (C <-> F) ===")
    Pauza()


def ObliczSredniaOcen():
    print("=== OBLICZ ŚREDNIĄ OCEN ===")
    Pauza()


if __name__ == "__main__":
    main()