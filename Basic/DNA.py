def dna_t(dna):
    DnaStr = []
    for x in dna:
        if x == 'A':
            DnaStr.append('T')
        if x == 'T':
            DnaStr.append('A')
        if x == 'G':
            DnaStr.append('C')
        if x == 'C':
            DnaStr.append('G')
    
    str1 = ""
    for x in DnaStr:
        str1 += x

    return str1
    
x =  input("Input DNA string (A,G,T,C) : ")

print("String ",x," is ", dna_t(x))