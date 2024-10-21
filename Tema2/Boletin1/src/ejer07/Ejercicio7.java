package ejer07;

public class Ejercicio7 {
	
	public static boolean comprobarFecha(int dia, int mes, int año) {
		boolean res = false;
		int maxDias = 0;
		
		switch (mes) {
		
		case 1, 3, 5, 7, 8, 10, 12 -> {
			maxDias = 31;
		}
		
		case 4, 6, 9, 11 -> {
			maxDias = 30;
		}
		
		case 2 -> {
			if (año % 4 == 0) {
				maxDias = 29;
			} else {
				maxDias = 28;
			}
		}
		
		}
		
		if (dia <= maxDias && dia >= 0 && mes <= 12 && mes >= 1) {
			res = true;
		}
		
		return res;
	}
	
}