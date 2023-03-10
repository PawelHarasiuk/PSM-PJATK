public class Main {
    public static double sin(double x) {
        // Przybliżenie działa poprawnie tylko w pierwszej ćwiartce
        x = x % (2*Math.PI);

        // Przybliżenie działa poprawnie tylko w radianach, zamiana stopni na radiany
        x = Math.toRadians(x);

        // Licznik i mianownik szeregu
        double numerator = x;
        double denominator = 1;
        double result = 0;

        // Obliczanie kolejnych wyrazów szeregu
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0) {
                result += numerator / denominator;
            } else {
                result -= numerator / denominator;
            }

            numerator *= -x * x;
            denominator *= (2*i + 2) * (2*i + 3);
        }

        return result;
    }

    public static void main(String[] args) {
        // Testowanie funkcji
        for (int i = 1; i <= 10; i++) {
            double x = i * Math.PI / 6;
            double approx = sin(x);
            double actual = Math.sin(x);
            double diff = Math.abs(approx - actual);
            System.out.printf("x = %.3f, sin(x) = %.15f, Math.sin(x) = %.15f, diff = %.15f%n",
                    x, approx, actual, diff);
        }
    }
}

