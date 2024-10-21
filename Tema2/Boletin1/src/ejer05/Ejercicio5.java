package ejer05;

public class Ejercicio5 {

	public static boolean esCapicua(int num) {
		
		boolean res = false;
		int numInverso = 0;
		int numAux = num;
		int cifra;
		
		while (numAux!=0) {
			cifra = numAux % 10;
			numInverso = numInverso * 10 + cifra;
			numAux = numAux / 10;
		}
		
		if (num == numInverso) {
			res = true;
		}
		
		return res;
	
	}
	
}