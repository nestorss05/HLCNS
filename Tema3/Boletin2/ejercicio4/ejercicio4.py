def kaprekar(num):
    res = 0
    numCad = add0(num)
    resta = num

    if num > 9999:
        raise Exception("No puede tener mas de cinco caracteres")

    if num % 1111 == 0:
        res = 8
    else:
        while resta != 6174:
            res+=1
            numCad = add0(resta)
            numAsc = ordenaAsc(numCad)
            numDesc = ordenaDesc(numCad)
            resta = int(numDesc) - int(numAsc)

    return res

def add0(num):
    numCad = str(num)

    while len(numCad) < 4:
        numCad = "0" + numCad

    return numCad

def ordenaAsc(numCad):
    cadOrd = sorted(numCad)
    cadOrd = "".join(cadOrd)
    return cadOrd

def ordenaDesc(numCad):
    cadOrd = sorted(numCad, reverse=True)
    cadOrd = "".join(cadOrd)
    return cadOrd