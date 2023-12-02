
def factorial(y):
    x = 0
    sil = 1
    while x < y:
        x+=1
        sil *= x
    return sil


def main():
    rangeError = 0
    try:
        num = int(input("Podaj liczbe naturalna: "))
        if num >= 21:
            raise rangeError("Range error")
    except ValueError:
        print("Niepoprawne dane")
        main()
    except Exception:
        print("Prosze podac liczbe z wlasciwego zakresu")
        main()
    else:
        print("Silnia",num,"! = ", factorial(num))

main()