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
	static String url = "http://localhost:3002/";

	@BeforeAll
	static void setURL() {
		driver1 = new ChromeDriver();
		driver1.get(url);
	}

	@Test
	void testEnlaces() {
		driver1.get(url);
		driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
		
		WebElement enlaces = driver1.findElement(By.id("enlaces"));
        String texto = enlaces.getText();
        assertEquals("Enlaces favoritos", texto);
	}
	
	@Test
	void testBuscadores() {
		WebElement buscadores = driver1.findElement(By.id("buscadores"));
        buscadores.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(3));
        WebElement paginaBuscadores = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("page-buscadores")));
        
        String textoBuscadores = paginaBuscadores.getText();
        assertEquals("Buscadores", textoBuscadores);       
	}
	
	@Test
	void testBuscadoresGoogle() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("buscadores"));
        buscadores.click();
		
		WebElement google = driver1.findElement(By.id("google"));
        google.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.google.es/", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testBuscadoresBing() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("buscadores"));
        buscadores.click();
		
		WebElement bing = driver1.findElement(By.id("bing"));
		bing.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.bing.com/?brdr=1", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testBuscadoresBaidu() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("buscadores"));
        buscadores.click();
		
		WebElement baidu = driver1.findElement(By.id("baidu"));
		baidu.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.baidu.com/", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testRedes() {
		
		WebDriverWait wait = new WebDriverWait(driver1, Duration.ofSeconds(3));
		WebElement paginaRedes = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("redes")));
		
		WebElement redes = driver1.findElement(By.id("redes"));
		redes.click();
		
        paginaRedes = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("page-redes")));
		
        String textoRedes = paginaRedes.getText();
        assertEquals("Redes Sociales", textoRedes);

        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testRedesInstagram() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("redes"));
        buscadores.click();
		
		WebElement instagram = driver1.findElement(By.id("instagram"));
        instagram.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.instagram.com/", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testRedesTikTok() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("redes"));
        buscadores.click();
		
		WebElement tiktok = driver1.findElement(By.id("tiktok"));
        tiktok.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.tiktok.com/es/", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}
	
	@Test
	void testRedesFacebook() {
		String originalWindowHandle = (String) driver1.getWindowHandles().toArray()[0];
		driver1.switchTo().window(originalWindowHandle);
		
		driver1.get(url);
		
		WebElement buscadores = driver1.findElement(By.id("redes"));
        buscadores.click();
		
		WebElement facebook = driver1.findElement(By.id("facebook"));
        facebook.click();
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
        String handles = (String) driver1.getWindowHandles().toArray()[driver1.getWindowHandles().toArray().length - 1];
        driver1.switchTo().window(handles);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        
        String url = driver1.getCurrentUrl();

        assertEquals("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F", url);
        
        driver1.switchTo().window(originalWindowHandle);
        driver1.manage().timeouts().implicitlyWait(Duration.ofSeconds(3));
        WebElement volver = driver1.findElement(By.id("volver"));
        volver.click();
	}

}
