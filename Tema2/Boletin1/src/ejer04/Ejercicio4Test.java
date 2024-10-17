package ejer04;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class Ejercicio4Test {

	@Test
	void testPrimo1() {
		boolean res = Ejercicio4.esPrimo(1);
		assertTrue(res);
	}
	
	@Test
	void testPrimo2() {
		boolean res = Ejercicio4.esPrimo(2);
		assertTrue(res);
	}
	
	@Test
	void testPrimo3() {
		boolean res = Ejercicio4.esPrimo(3);
		assertTrue(res);
	}
	
	@Test
	void testPrimo4() {
		boolean res = Ejercicio4.esPrimo(4);
		assertFalse(res);
	}
	
	@Test
	void testPrimo5() {
		boolean res = Ejercicio4.esPrimo(5);
		assertTrue(res);
	}

}
