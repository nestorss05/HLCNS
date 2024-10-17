def ascensor(pisos):
    pisosArray = pisos.split(" ")
    pisoFinal = 0
    pisoAnterior = 0

    for piso in range(len(pisosArray)):
        if pisosArray.index(pisosArray[piso]) != 0:
            if pisoAnterior < int(pisosArray[piso]):
                pisoFinal += int(pisosArray[piso]) - int(pisoAnterior)
            else:
                pisoFinal += int(pisoAnterior) - int(pisosArray[piso])
        pisoAnterior = int(pisosArray[piso])

    return pisoFinal