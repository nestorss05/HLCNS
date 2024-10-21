package ejer09;

public class Ejercicio9 {
	
	public static int parseBinary(int num) {
		String resString = Integer.toBinaryString(num);
		int res = Integer.parseInt(resString);
		return res;
	}
	
}