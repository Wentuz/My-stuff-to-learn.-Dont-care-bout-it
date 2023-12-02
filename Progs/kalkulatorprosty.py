from multiprocessing.resource_sharer import stop

window = [1024,640]

def calc():

    x = int(input("Podaj 1 liczbe:"))
    y = int(input("Podaj 2 liczbe:"))

    def dodaj():
        print(x+y)
        calc()
    def odejmij():
        print(x-y)
        calc()
    def pomnoz():
        print(x*y)
        calc()
    def podziel():
        print(x/y)
        calc()

    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Pomnóż")
    print("4. Podziel")
    print("5. Zakończ")

    opr = int(input("Podaj operacje logiczna :"))

    if opr == 5:
        stop
    elif opr == 1:
        dodaj()
    elif opr == 2:
        odejmij()
    elif opr == 3:
        pomnoz()
    elif opr == 4:
        podziel()
        
calc()