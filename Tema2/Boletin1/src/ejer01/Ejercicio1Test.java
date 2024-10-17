package ejer01;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Ejercicio1Test {

	@ParameterizedTest
	@MethodSource("vocalista")
	void testEsVocal(char caracter, boolean resEsperado) {
		boolean resObtenido = Ejercicio1.esVocal(caracter);
		assertEquals(resEsperado, resObtenido);
	}
	
	private static Stream<Arguments> vocalista() {
		return Stream.of(
				Arguments.of('a', true),
				Arguments.of('e', true),
				Arguments.of('I', true),
				Arguments.of('O', true),
				Arguments.of('u', true),
				Arguments.of('C', false));
	}
	
//	@Test
//	void testEsVocalAMinuscula() {
//		boolean resul = Ejercicio1.esVocal('a');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalAMayuscula() {
//		boolean resul = Ejercicio1.esVocal('A');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalEMinuscula() {
//		boolean resul = Ejercicio1.esVocal('e');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalEMayuscula() {
//		boolean resul = Ejercicio1.esVocal('E');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalIMinuscula() {
//		boolean resul = Ejercicio1.esVocal('i');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalIMayuscula() {
//		boolean resul = Ejercicio1.esVocal('I');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalOMayuscula() {
//		boolean resul = Ejercicio1.esVocal('O');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalUMayuscula() {
//		boolean resul = Ejercicio1.esVocal('U');
//		assertTrue(resul);
//	}
//	
//	@Test
//	void testEsVocalConsonante() {
//		boolean resul = Ejercicio1.esVocal('C');
//		assertFalse(resul);
//	}

}