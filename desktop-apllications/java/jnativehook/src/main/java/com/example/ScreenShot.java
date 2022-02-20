package com.example;

import java.awt.AWTException;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class ScreenShot {
	public static void main(String[] args) {
		try {
			Thread.sleep(12000);
			printScreen();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
				
		
	          
	   

	}
	
	public static void printScreen() {
		String path= "C:\\Users\\hp\\Documents\\work\\local\\jnativehook\\src\\main\\java\\com\\example\\ScreenShot.jpg";
		try {
			Robot robotObj = new Robot();
	          Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
	          Rectangle rectObj= new Rectangle(dim);
	          BufferedImage img = robotObj.createScreenCapture(rectObj);
	          ImageIO.write(img, "jpg", new File(path));
	          System.out.println("Screenshot Saved.");
		} catch (AWTException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
