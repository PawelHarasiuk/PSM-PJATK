import java.lang.Math;

public class Sin {
    public static double sin(double x) {
        // Convert x to the range [0, 2pi]
        x %= 2*Math.PI;
        if (x < 0) {
            x += 2*Math.PI;
        }

        double result = 0;
        double term = x;
        int sign = 1;
        for (int i = 1; i <= 10; i++) {
            result += sign * term;
            term *= x * x / ((2*i) * (2*i+1));
            sign *= -1;
        }

        return result;
    }

    public static void main(String[] args) {
        double[] angles = {0, Math.PI/6, Math.PI/4, Math.PI/3, Math.PI/2, Math.PI, 3*Math.PI/2, 2*Math.PI};
        for (double x : angles) {
            System.out.printf("kat: %.2f rad\n", x);
            for (int i = 1; i <= 10; i++) {
                double approx = sin(x);
                double exact = Math.sin(x);
                double diff = Math.abs(approx - exact);
                System.out.printf("%d wyraz(y) szeregu: przyblizenie=%.10f, dokladne=%.10f, roznica=%.10f\n", i, approx, exact, diff);
            }
            System.out.println();
        }
    }
}
