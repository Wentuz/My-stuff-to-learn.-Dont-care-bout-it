

def main():

    amount = [0, 0]

    def USD(value: int) -> int:
        return value * 91.0517
    def EUR(value: int) -> int:
        return value * 97.8278
    def PLN(value: int) -> int:
        return value * 22.5177
    
    def get_currency():

        amount = input("Insert currency, example: 13 EUR\n")
        value_tab = amount.split()

        if len(value_tab) != 2:
            print("Invalid input. Please enter a value followed by a currency")
            return
        try:
            value = int(value_tab[0])
        except:
            print("Invalid input, please enter a valid value")
        currency = value_tab[1].upper()

        if currency == 'USD':
            converted = USD(value)
        elif currency == 'EUR':
            converted = EUR(value)
        elif currency == 'PLN':
            converted = PLN(value)
        else:
            print("Unsupported currency. Please try USD, EUR or PLN")

        print(f"{value}{currency} = {converted} RUB")

    get_currency()
main()