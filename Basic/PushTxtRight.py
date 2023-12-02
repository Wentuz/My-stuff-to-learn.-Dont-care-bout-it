'''
9. Wyrównaj dowolny napis do prawej w polu o podanej długości. 
'''

def right(txt, num):
    
    x = 0
    y = 0
    ntxt = ''

    index = num + len(txt) - 1
    while x <= index:
        if x < num: 
            ntxt += " "
        else: 
            ntxt += txt[y]
            y += 1
        x+=1
    return ntxt

def main():

    txt = input("Input txt: ")
    num = int(input("Input field: "))

    print(right(txt,num))

main()