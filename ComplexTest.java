import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

/*
 *  Test multiply with max numbers and min numbers
 *  Test divide
 *  
 */

class ComplexTest {
	
	public static Complex max = new Complex(Float.MAX_VALUE, Float.MAX_VALUE);
	public static Complex negMax = new Complex(0-Float.MAX_VALUE, 0-Float.MAX_VALUE);
	public static Complex min = new Complex(Float.MIN_VALUE, Float.MIN_VALUE);
	public static Complex zero = new Complex(0.00f, 0.00f);

	@Test
	void Complextest() {
		Complex c = new Complex(4,5);
		assertEquals(4, c.real);
		assertEquals(5, c.imag);
	}
	
	@Test
	void addTest() {
		Complex c = new Complex(4,5);
		Complex d = new Complex(6,3);
		Complex result = c.add(d);
		assertEquals(10, result.real);
		assertEquals(8, result.imag);
		
		// Testing Max
		result = max.add(max);
		assertEquals(Float.POSITIVE_INFINITY, result.real);
		assertEquals(Float.POSITIVE_INFINITY, result.imag);
		
		result = min.add(min);
		assertEquals(Float.MIN_VALUE + Float.MIN_VALUE, result.real);
		assertEquals(Float.MIN_VALUE + Float.MIN_VALUE, result.imag);
	}
	
	@Test
	void subtractTest() {
		Complex c = new Complex(4,5);
		Complex d = new Complex(6,3);
		Complex result = c.subtract(d);
		assertEquals(-2, result.real);
		assertEquals(2, result.imag);
		
		// Testing min
		result = negMax.subtract(max);
		assertEquals(Float.NEGATIVE_INFINITY, result.real);
		assertEquals(Float.NEGATIVE_INFINITY, result.imag);
				
		
	}
	
	@Test
	void multiplyTest() {
		Complex c = new Complex(5,6);
		Complex d = new Complex(-3,4);
		Complex result = c.multiply(d);
		assertEquals(-39, result.real);
		assertEquals(2, result.imag);
		
		result = max.multiply(max);
		assertEquals(Float.POSITIVE_INFINITY, result.real);
		assertEquals(Float.POSITIVE_INFINITY, result.imag);
	}
	
	@Test
	void divideTest() {
		Complex c = new Complex(5,6);
		Complex d = new Complex(-3,4);
		Complex result = c.divide(d);
		assertEquals(0.36f, result.real);
		assertEquals(-1.52f, result.imag);
		
		result = max.divide(min);
	}
	
	@Test
	void toStringTest() {
		Complex a = new Complex(1.59f, 0);
		Complex b = new Complex(0, 1.59f);
		Complex c = new Complex(1.59f, -1.59f);
		Complex d = new Complex(-1.59f, -1.59f);
		String resultA = a.toString();
		String resultB = b.toString();
		String resultC = c.toString();
		String resultD = d.toString();
		assertEquals("c = 1.59", resultA);
		assertEquals("c = 1.59i", resultB);
		assertEquals("c = 1.59 - 1.59i", resultC);
		assertEquals("c = -1.59 - 1.59i", resultD);
		
	}

}
