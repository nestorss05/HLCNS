def comprobarCodigo(numero: int):

    res = False
    numeroStr = str(numero)

    if len(numeroStr) <= 13:

        if len(numeroStr) != 13 and len(numeroStr) != 8:

            numExtra = ""
            numDiv = 13

            if len(numeroStr) < 8:
                numDiv = 8

            for i in range(len(numeroStr), numDiv):
                numExtra += "0"

            numeroStr = numExtra + numeroStr

        numeroArray = list(map(int, numeroStr))
        primerNumero = True
        triple = True
        numeroCheck = 0
        numeroPosFinal = numeroArray[len(numeroArray)-1]

        for num in reversed(numeroArray):

            if not primerNumero:
                print(num)
                if triple:
                    numeroCheck += (num * 3)
                else:
                    numeroCheck += num
                triple = not triple
            else:
                primerNumero = False

        if (numeroCheck + numeroPosFinal) % 10 == 0:
            res = True

    return res