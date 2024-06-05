import random
import time

ascii_symbols = [(chr(i)) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
length = 10

psswd = ""

while length > 0:
    x = random.choice(ascii_symbols)
    psswd += str(x)

    length = length - 1
print(psswd)