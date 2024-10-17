package ejer06;

public class Ejercicio6 {

	public static double calculadora(double num1, double num2, int opc) {
		double res = 0;
		switch (opc) {
		case 1 -> {
			res = num1 + num2;
		}
		case 2 -> {
			res = num1 - num2;
		}
		case 3 -> {
			res = num1 * num2;
		}
		case 4 -> {
			res = num1 / num2;			
		}
		}
		return res;
	}

}