def int_to_str(number):
    stringConv = str(number) + " "
    return stringConv

num = int(input("Input number to convert: "))

print("Type before: ",type(num))
print("Type after: ",type(int_to_str(num)))