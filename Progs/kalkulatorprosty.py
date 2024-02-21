
def dodaj(x:float, y:float) -> float:
    return x+y

def odejmij(x:float, y:float) -> float:
    return x-y

def pomnoz(x:float, y:float) -> float:
    return x*y

def podziel(x:float, y:float) -> float:
    return x/y

def calc() -> None:

    x:float = float(input("Podaj 1 liczbe:"))
    y:float = float(input("Podaj 2 liczbe:"))

    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Pomnóż")
    print("4. Podziel")
    print("5. Zakończ")

    opr:int = int(input("Podaj operacje logiczna :"))

    if opr == 5:
        print("Stopping program...")
    elif opr == 1:
        print(dodaj(x, y))
    elif opr == 2:
        print(odejmij(x, y))
    elif opr == 3:
        print(pomnoz(x, y))
    elif opr == 4:
        print(podziel(x, y))
    calc()


if __name__ == '__main__':     
    calc()