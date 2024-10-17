package ejer08;

public class Ejercicio8 {
	
	public static int fibonacci(int num) throws Exception {
		int res = 0;
		int numFibo1 = 0;
		int numFibo2 = 1;
		if (num < 1) {
			throw new Exception("ERROR: el numero no puede ser menor que 1");
		} else {
			for (int i = 0; i < num; i++) {
				res = numFibo1 + numFibo2;
				numFibo2 = res - numFibo2;
				numFibo1 = res;
			}
		}
		return res;
	}
	
}