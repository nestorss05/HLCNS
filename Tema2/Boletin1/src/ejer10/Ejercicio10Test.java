package ejer10;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Ejercicio10Test {

	@Test
	void testYoga() {
		boolean esPalindromo = Ejercicio10.esPalindromo("Yo hago yoga hoy");
		assertTrue(esPalindromo);
	}
	
	@Test
	void testBobo() {
		boolean esPalindromo = Ejercicio10.esPalindromo("Bobo tu");
		assertFalse(esPalindromo);
	}

}
