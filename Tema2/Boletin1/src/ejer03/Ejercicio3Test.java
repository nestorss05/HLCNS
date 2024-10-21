package ejer03;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class Ejercicio3Test {

	@Test
	void testFizz() {
		String resul = Ejercicio3.cadenator(6);
		assertEquals("fizz", resul);
	}
	
	@Test
	void testBuzz() {
		String resul = Ejercicio3.cadenator(10);
		assertEquals("buzz", resul);
	}
	
	@Test
	void testFizzBuzz() {
		String resul = Ejercicio3.cadenator(15);
		assertEquals("fizzbuzz", resul);
	}
	
	@Test
	void testNull() {
		String resul = Ejercicio3.cadenator(4);
		assertEquals("", resul);
	}

}
