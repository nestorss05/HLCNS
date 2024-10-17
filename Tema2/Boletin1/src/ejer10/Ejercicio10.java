package ejer10;

public class Ejercicio10 {
	
	public static boolean esPalindromo(String texto) {
		boolean res = true;
		String analizTexto = texto.toLowerCase().replace(" ", "");
		char textoChar[] = analizTexto.toCharArray();
		int i = 0;
		int j = textoChar.length - 1;
		while (i < textoChar.length) {
			if (textoChar[i] != textoChar[j]) {
				res = false;
				break;
			}
			i++;
			j--;
		}
		return res;
	}
	
}