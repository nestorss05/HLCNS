package ejer01;

public class Ejercicio1 {

	public static boolean esVocal(char caracter) {
		boolean res = false;
		char caracterMinus = Character.toLowerCase(caracter);
		
		switch (caracterMinus) {
		case 'a', 'e', 'i', 'o', 'u' -> {
			res = true;
		}
		}
		
		return res;
	}
	
}