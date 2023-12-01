def even_odd(number):
    if ( number % 2 == 0 ):
        return 'even'
    else:
        return 'odd'
    
x = int(input("Input number: "))

print("The number is ",even_odd(x))