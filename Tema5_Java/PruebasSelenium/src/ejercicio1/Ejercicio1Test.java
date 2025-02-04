package ejercicio1;
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

class Ejercicio1Test {

	static WebDriver driver1;

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver1.get("http://localhost:3001/");
	}

	@Test
	void test1() {
		WebElement enlaces = driver1.findElement(By.id("enlaces"));
        String texto = enlaces.getText();
        assertEquals("Enlaces favoritos", texto);
	}
	
	@Test
	void test2() {
		WebElement buscadores = driver1.findElement(By.id("buscadores"));
        buscadores.click();
        
        WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(3));
        WebElement paginaBuscadores = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("page-buscadores")));
        
        String textoBuscadores = paginaBuscadores.getText();
        assertEquals("Buscadores", textoBuscadores);
	
        WebElement google = driver1.findElement(By.id("google"));
        google.click();
        
        WebElement bing = driver1.findElement(By.id("bing"));
        bing.click();
        
        WebElement baidu = driver1.findElement(By.id("baidu"));
        baidu.click();
        
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void test3() {
		
		WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(3));
		WebElement paginaRedes = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("redes")));
		
		WebElement redes = driver1.findElement(By.id("redes"));
		redes.click();
		
        paginaRedes = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("page-redes")));
		
        String textoRedes = paginaRedes.getText();
        assertEquals("Redes Sociales", textoRedes);
                
        WebElement instagram = driver1.findElement(By.id("instagram"));
        instagram.click();
        
        WebElement tiktok = driver1.findElement(By.id("tiktok"));
        tiktok.click();
        
        WebElement facebook = driver1.findElement(By.id("facebook"));
        facebook.click();
        
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}

}
