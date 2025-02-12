package ejercicio2;

import static org.junit.jupiter.api.Assertions.*;

import java.time.Duration;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

class Ejercicio2Test {

	static WebDriver driver1;

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver1.get("http://localhost:3001/");
	}
	
	@Test
	void testHeader() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement heading = driver1.findElement(By.id("heading"));
        String texto = heading.getText();
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        assertEquals("Formulario de registro", texto);
	}
	
	@Test
	void testTituloPagina() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		String title = driver1.getTitle();
        assertEquals("Formulario de registro - Mi web", title);
	}
	
	@Test
	void testNombreForm() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement nombre = driver1.findElement(By.id("nombre"));
		assertNotNull(nombre);
	}
	
	@Test
	void testApellidosForm() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement apellidos = driver1.findElement(By.id("apellidos"));
		assertNotNull(apellidos);
	}
	
	@Test
	void testNombre49() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement nombre = driver1.findElement(By.id("nombre"));
		nombre.clear();
		String nombreOG = "Gustavo Aurelio Jocantaro Paulino de las Nieves P";
		nombre.sendKeys(nombreOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertEquals(nombre.getAttribute("value"), nombreOG);
	}
	
	@Test
	void testNombre50() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement nombre = driver1.findElement(By.id("nombre"));
		nombre.clear();
		String nombreOG = "Gustavo Aurelio Jocantaro Paulino de las Nieves Pe";
		nombre.sendKeys(nombreOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertEquals(nombre.getAttribute("value"), nombreOG);
	}
	
	@Test
	void testNombre51() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement nombre = driver1.findElement(By.id("nombre"));
		nombre.clear();
		String nombreOG = "Gustavo Aurelio Jocantaro Paulino de las Nieves Pez";
		nombre.sendKeys(nombreOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertNotEquals(nombre.getAttribute("value"), nombreOG);		
	}
	
	@Test
	void testApellidos49() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement apellidos = driver1.findElement(By.id("apellidos"));
		apellidos.clear();
		String apellidoOG = "Cuevas Sanchez Gonzalez Ordoñez Cruz Rivas Hernan";
		apellidos.sendKeys(apellidoOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertEquals(apellidos.getAttribute("value"), apellidoOG);
	}
	
	@Test
	void testApellidos50() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement apellidos = driver1.findElement(By.id("apellidos"));
		apellidos.clear();
		String apellidoOG = "Cuevas Sanchez Gonzalez Ordoñez Cruz Rivas Hernand";
		apellidos.sendKeys(apellidoOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertEquals(apellidos.getAttribute("value"), apellidoOG);
	}
	
	@Test
	void testApellidos51() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement apellidos = driver1.findElement(By.id("apellidos"));
		apellidos.clear();
		String apellidoOG = "Cuevas Sanchez Gonzalez Ordoñez Cruz Rivas Hernando";
		apellidos.sendKeys(apellidoOG);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		assertNotEquals(apellidos.getAttribute("value"), apellidoOG);
	}
	
	@Test
	void selectCorreo() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement correo = driver1.findElement(By.id("correo"));
		assertNotNull(correo);
	}
	
	@Test
	void selectSubmit() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement enviar = driver1.findElement(By.id("enviar"));
		assertNotNull(enviar);
	}
	
	@Test
	void selectCheckbox1() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement novs = driver1.findElement(By.id("novs"));
		assertNotNull(novs);
	}
	
	@Test
	void checkCheckbox1() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement novs = driver1.findElement(By.id("novs"));
		System.out.println(novs.isSelected());
		assertTrue(novs.isSelected());
	}

}
