def velocidad(datos):
    datosString = datos.split(" ")
    d = datosString[0].split("D=")
    t = datosString[1].split("T=")
    resN = int(d[1]) / int(t[1])
    res = f"V={int(resN)}"
    return res