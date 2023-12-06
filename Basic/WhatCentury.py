def what_century(year):
    century = int((int(year)-1) / 100 + 1)
    tip = century % 10
    if tip == 2 and century > 20:
        out = str(century) + "nd"
    elif tip == 3 and century > 20:
        out = str(century) + "rd"
    elif tip == 1 and century > 20:
        out = str(century) + "st"
    else:
        out = str(century) + "th"
    return out


print(what_century(2016))
print(what_century(2000))
print(what_century(2150))
print(what_century(2236))
print(what_century(1136))
