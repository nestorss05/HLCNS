package ejer03;

public class Ejercicio3 {

	public static String cadenator(int num) {
		String res = "";
		if (num % 3 == 0) {
			res += "fizz";
		}
		if (num % 5 == 0) {
			res += "buzz";
		}
		return res;
	}
	
}