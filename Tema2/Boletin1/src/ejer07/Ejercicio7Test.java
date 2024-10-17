package ejer07;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class Ejercicio7Test {

	@Test
	void testFechaCorrecta() {
		boolean esCorrecta = Ejercicio7.comprobarFecha(26, 9, 2024);
		assertTrue(esCorrecta);
	}
	
	@Test
	void testDiaIncorrecto() {
		boolean esCorrecta = Ejercicio7.comprobarFecha(31, 9, 2024);
		assertFalse(esCorrecta);
	}
	
	@Test
	void testMesIncorrecto() {
		boolean esCorrecta = Ejercicio7.comprobarFecha(31, 13, 2024);
		assertFalse(esCorrecta);
	}

}
