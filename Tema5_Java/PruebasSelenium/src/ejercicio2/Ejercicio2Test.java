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
		driver1.get("http://localhost:3000/");
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
	void selectSexo() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement sexo = driver1.findElement(By.id("sexo"));
		assertNotNull(sexo);
	}
	
	@Test
	void selectSexoM() {
		WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(5));

        WebElement masculinoOption = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//div[contains(text(),'Masculino')]")
        ));
        masculinoOption.click();

        WebElement sexoEscogido = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("sexoEscogido")));
        wait.until(ExpectedConditions.not(ExpectedConditions.attributeToBe(sexoEscogido, "value", "")));  
	    
	    String selectedSexo = sexoEscogido.getAttribute("value"); 
	    assertEquals("Masculino", selectedSexo);
	}
	
	@Test
	void selectSexoF() {
		WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(5));

        WebElement masculinoOption = wait.until(ExpectedConditions.elementToBeClickable(
            By.xpath("//div[contains(text(),'Femenino')]")
        ));
        masculinoOption.click();

        WebElement sexoEscogido = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("sexoEscogido")));
        wait.until(ExpectedConditions.not(ExpectedConditions.attributeToBe(sexoEscogido, "value", "")));  
	    
	    String selectedSexo = sexoEscogido.getAttribute("value"); 
	    assertEquals("Femenino", selectedSexo);
	}
	
	@Test
	void selectCorreo() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement correo = driver1.findElement(By.id("correo"));
		assertNotNull(correo);
	}	
	
	@Test
	void selectCheckbox1() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement checkbox1 = driver1.findElement(By.id("checkbox1"));
		assertNotNull(checkbox1);
	}
	
	@Test
	void checkCheckbox1() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement checkbox1 = driver1.findElement(By.id("checkbox1"));
		String ariaChecked = checkbox1.getAttribute("aria-checked");
		assertEquals("true", ariaChecked);
	}
	
	@Test
	void selectCheckbox2() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement checkbox2 = driver1.findElement(By.id("checkbox2"));
		assertNotNull(checkbox2);
	}
	
	@Test
	void selectSubmit() {
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
		WebElement enviar = driver1.findElement(By.id("enviar"));
		assertNotNull(enviar);
	}

}
