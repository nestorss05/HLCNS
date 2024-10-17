letrasFrase = "abcdefghijklmnñopqrstuvwxyz"

def cifradoCesar(frase, desp):

    fraseNueva = ""
    for caracter in frase:
        if caracter not in letrasFrase:
            fraseNueva += caracter
        else:
            pos = letrasFrase.index(caracter)
            fraseNueva += letrasFrase[(pos + desp)%len(letrasFrase)]

    return fraseNueva