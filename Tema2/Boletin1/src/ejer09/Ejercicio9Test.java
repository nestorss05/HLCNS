package ejer09;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class Ejercicio9Test {

	@Test
	void test11() {
		int resul = Ejercicio9.parseBinary(11);
		assertEquals(1011, resul);
	}
	
	@Test
	void test101() {
		int resul = Ejercicio9.parseBinary(101);
		assertEquals(1100101, resul);
	}

}
