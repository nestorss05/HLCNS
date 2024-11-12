from parchis.Parchis import Parchis

def test_pintaTableroP1_3__P2_5():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 3
    objeto.fichaJ2 = 5
    tablero = Parchis.pintaTablero(objeto)
    tableroF1 = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF"
    tableroF2 = objeto.nomJ1 + "\tI\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroF3 = objeto.nomJ2 + "\tI\t\t\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroRes = tableroF1 + "\n" + tableroF2 + "\n" + tableroF3 + "\n"
    assert tablero == tableroRes

def test_pintaTableroP1_3__P2_0():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 3
    objeto.fichaJ2 = 0
    tablero = Parchis.pintaTablero(objeto)
    tableroF1 = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF"
    tableroF2 = objeto.nomJ1 + "\tI\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroF3 = objeto.nomJ2 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroRes = tableroF1 + "\n" + tableroF2 + "\n" + tableroF3 + "\n"
    assert tablero == tableroRes

def test_pintaTableroP1_20__P2_17():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 20
    objeto.fichaJ2 = 17
    tablero = Parchis.pintaTablero(objeto)
    tableroF1 = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF"
    tableroF2 = objeto.nomJ1 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroF3 = objeto.nomJ2 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO\t\t\tF"
    tableroRes = tableroF1 + "\n" + tableroF2 + "\n" + tableroF3 + "\n"
    assert tablero == tableroRes

def test_pintaTableroP1_minus1__P2_17():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = -1
    objeto.fichaJ2 = 17
    tablero = Parchis.pintaTablero(objeto)
    tableroF1 = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF"
    tableroF2 = objeto.nomJ1 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroF3 = objeto.nomJ2 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO\t\t\tF"
    tableroRes = tableroF1 + "\n" + tableroF2 + "\n" + tableroF3 + "\n"
    assert tablero == tableroRes

def test_pintaTableroP1_21__P2_17():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 21
    objeto.fichaJ2 = 17
    tablero = Parchis.pintaTablero(objeto)
    tableroF1 = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF"
    tableroF2 = objeto.nomJ1 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    tableroF3 = objeto.nomJ2 + "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO\t\t\tF"
    tableroRes = tableroF1 + "\n" + tableroF2 + "\n" + tableroF3 + "\n"
    assert tablero == tableroRes
