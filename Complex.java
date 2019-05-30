
public class Complex {
	float real;
    float imag;
	public Complex() {
		real = 0;
		imag = 0;
	}
	public Complex(float r, float i) {
		real = r;
		imag = i;
	}
	public Complex add(Complex complex) {
		Complex result = new Complex();
		result.real = this.real + complex.real;
		result.imag = this.imag + complex.imag;
		return result;
	}
	public Complex subtract(Complex complex) {
		Complex result = new Complex();
		result.real = this.real - complex.real;
		result.imag = this.imag - complex.imag;
		return result;

	}
	public Complex multiply(Complex complex) {
		Complex result = new Complex();
		result.real = this.real * complex.real - this.imag * complex.imag;
		result.imag = this.real * complex.imag + this.imag * complex.real;
		return result;
	}
	public Complex divide(Complex complex) {
		return this.multiply(complex.reciprocal());

	}
	
	public Complex reciprocal() {
		float scale = this.real * this.real + this.imag * this.imag;
		Complex result = new Complex(this.real/scale, (0 - this.imag)/scale);
		return result;
	}
	
	public String toString() {
		if(this.imag == 0)
			return "c = "+ this.real;
		if(this.real == 0)
			return "c = "+ this.imag + "i";
		if(this.imag <0)
			return "c = "+ this.real + " - " + (0 - this.imag) + "i";
		else
			return "c = " + this.real + " + "+ this.imag + "i";
	}
}
