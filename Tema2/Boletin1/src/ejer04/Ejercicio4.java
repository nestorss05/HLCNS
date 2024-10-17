package ejer04;

public class Ejercicio4 {

	public static boolean esPrimo(int num) {
		boolean res = true;
		int cont = 2;
		
		while(cont <= Math.sqrt(num) && res) {
			if (num % cont == 0) {
				res = false;
			}
			
			cont++;
		}
		
		return res;
	}
	
}