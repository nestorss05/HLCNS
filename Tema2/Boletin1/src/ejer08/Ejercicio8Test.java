package ejer08;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class Ejercicio8Test {

	@Test
	void testNumeroCorrecto1() throws Exception {
		int resul = Ejercicio8.fibonacci(1);
		assertEquals(1, resul);
	}
	
	@Test
	void testNumeroCorrecto2() throws Exception {
		int resul = Ejercicio8.fibonacci(2);
		assertEquals(1, resul);
	}
	
	@Test
	void testNumeroCorrecto6() throws Exception {
		int resul = Ejercicio8.fibonacci(6);
		assertEquals(8, resul);
	}
	
	@Test
	void testNumeroCorrecto8() throws Exception {
		int resul = Ejercicio8.fibonacci(8);
		assertEquals(21, resul);
	}
	
	@Test
	void testNumeroMenorQue1() throws Exception {
		assertThrows(Exception.class, () -> Ejercicio8.fibonacci(-3), "ERROR: el numero no puede ser menor que 1");
	}

}
