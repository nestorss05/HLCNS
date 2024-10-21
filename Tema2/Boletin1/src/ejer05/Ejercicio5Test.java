package ejer05;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Ejercicio5Test {

	@Test
	void testEsCapicua3() {
		boolean res = Ejercicio5.esCapicua(3);
		assertTrue(res);
	}
	
	@Test
	void testEsCapicua33() {
		boolean res = Ejercicio5.esCapicua(33);
		assertTrue(res);
	}
	
	@Test
	void testNoEsCapicua34() {
		boolean res = Ejercicio5.esCapicua(34);
		assertFalse(res);
	}
	
	@Test
	void testEsCapicua303() {
		boolean res = Ejercicio5.esCapicua(303);
		assertTrue(res);
	}
	
	
	@Test
	void testNoEsCapicua400() {
		boolean res = Ejercicio5.esCapicua(400);
		assertFalse(res);
	}

}
