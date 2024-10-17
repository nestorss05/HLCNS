package ejer06;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class Ejercicio6Test {

	@Test
	void testSuma() {
		double resul = Ejercicio6.calculadora(3, 3, 1);
		assertEquals(6, resul);
	}
	
	@Test
	void testResta() {
		double resul = Ejercicio6.calculadora(5, 3, 2);
		assertEquals(2, resul);
	}
	
	@Test
	void testMultiplicacion() {
		double resul = Ejercicio6.calculadora(5, 3, 3);
		assertEquals(15, resul);
	}
	
	@Test
	void testDivision() {
		double resul = Ejercicio6.calculadora(6, 3, 4);
		assertEquals(2, resul);
	}
	
	@Test
	void testDivision0() {
		Exception exception = Assert.assertThrows(ArithmeticException.class, () -> {
			Ejercicio6.calculadora(3, 0, 4);
			throw new ArithmeticException("ERROR: no es posible la division entre 0");
		});
		assertEquals("ERROR: no es posible la division entre 0", exception.getMessage());
	}

}
