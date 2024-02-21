
def factorial(y:int) -> int:
    x:int = 0
    sil:int = 1
    while x < y:
        x+=1
        sil *= x
    return sil


def main() -> None:
    rangeError:int = 0
    try:
        num:int = int(input("Podaj liczbe naturalna nie wieksza niz 21: "))
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


if __name__ == '__main__':
    main()