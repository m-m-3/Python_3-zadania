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
            print("Błąd, wpisz prawidłową liczbę: ")


def WczytajInt(tekst=""):
    while True:
        try:
            return int(input(tekst))
        except ValueError:
            print("Błąd, wpisz prawidłową liczbę całkowitą: ")


def Pauza():
    input("Wciśnij Enter, aby wrócić do menu...")


def Kalkulator():
    print("=== KALKULATOR ===")
    a = WczytajLiczbe("Podaj pierwszą liczbę: ")
    b = WczytajLiczbe("Podaj drugą liczbę: ")
    operacja = input("Wybierz operację (+, -, * lub /): ").strip()

    if operacja == "+":
        print(f"Wynik:  {a + b}")
    elif operacja == "-":
        print(f"Wynik:  {a - b}")
    elif operacja == "*":
        print(f"Wynik:  {a * b}")
    elif operacja == "/":
        if b == 0:
            print("Nie można dzielić przez 0!")
            Pauza()
            return
        print(f"Wynik:  {a / b}")
    else:
        print("Nie obsługuję takiej operacji!")
        Pauza()
        return
    Pauza()


def KonwerterTemperatury():
    print("=== KONWERTER (C <-> F) ===")
    konwersjaZ = input("Jaką temperaturę chcesz skonwertować (C/F)?\n").strip().upper()
    if konwersjaZ != "C" and konwersjaZ != "F":
        print("Nie obsługuję takiej operacji!")
        Pauza()
        return
    
    temperatura = WczytajLiczbe("Podaj temperaturę: ")

    if konwersjaZ == "C":
        print(f"{temperatura}°C = {(temperatura * 1.8) + 32.0}°F")
    else:
        print(f"{temperatura}°F = {(temperatura - 32.0) / 1.8}°C")
    
    Pauza()


def ObliczSredniaOcen():
    print("=== OBLICZ ŚREDNIĄ OCEN ===")
    liczbaOcen = WczytajInt("Ile ocen ma uczeń? ")

    if liczbaOcen <= 0:
        print("Uczeń nie ma ocen!")
        Pauza()
        return

    suma = 0.0

    for i in range(1, liczbaOcen + 1):
        ocena = WczytajLiczbe(f"Podaj ocenę nr {i} (1-6): ")

        while ocena < 1 or ocena > 6:
            ocena = WczytajLiczbe("Nieprawidłowa ocena, podaj ponownie: ")

        suma += ocena

    srednia = suma / liczbaOcen
    print(f"Średnia ucznia to: {srednia:.2f}")

    if srednia >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")
    
    Pauza()
    


if __name__ == "__main__":
    main()