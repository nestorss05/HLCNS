package ejer02;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class Ejercicio2Test {

	@Test
	void numeroPar() {
		boolean resul = Ejercicio2.esPar(2);
		assertTrue(resul);
	}

	@Test
	void numeroImpar() {
		boolean resul = Ejercicio2.esPar(1);
		assertFalse(resul);
	}

}
