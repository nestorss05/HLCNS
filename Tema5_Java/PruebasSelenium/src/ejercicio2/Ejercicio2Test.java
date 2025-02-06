package ejercicio2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

class Ejercicio2Test {

	static WebDriver driver1;

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver1.get("http://localhost:3001/");
	}
	
	@Test
	void testHeader() {
		WebElement heading = driver1.findElement(By.id("heading"));
        String texto = heading.getText();
        assertEquals("Formulario de registro", texto);
	}
	
	@Test
	void testTituloPagina() {
		String title = driver1.getTitle();
        assertEquals("Formulario de registro - Mi web", title);
	}
	
	@Test
	void testNombreForm() {
		WebElement nombre = driver1.findElement(By.id("nombre"));
		assertNotNull(nombre);
	}

}
