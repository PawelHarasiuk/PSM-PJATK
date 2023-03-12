public class Main {
    public static double sin(double rad) {
        double sin = 0;
        rad %= (2 * Math.PI);
        if (rad >= 0 && rad <= (Math.PI) / 2) {
            sin = obliczSinusSzeregiemTaylora(rad);
        } else if (rad > (Math.PI) / 2 && rad <= Math.PI) {
            rad = Math.PI - rad;
            sin = obliczSinusSzeregiemTaylora(rad);
        } else if (rad > Math.PI && rad <= Math.PI + (Math.PI) / 2) {
            rad = -(rad - Math.PI);
            sin = obliczSinusSzeregiemTaylora(rad);
        } else if (rad > Math.PI + (Math.PI) / 2 && rad <= 2 * Math.PI) {
            rad = -(2 * Math.PI - rad);
            sin = obliczSinusSzeregiemTaylora(rad);
        }
        return sin;
    }

    public static double obliczSinusSzeregiemTaylora(double rad) {
        double przyblizenie = 0;
        boolean znak = true;
        for (int i = 1; i < 10 * 2; i += 2) {
            if (znak) {
                przyblizenie += potega(rad, i) / silnia(i);
            } else {
                przyblizenie -= potega(rad, i) / silnia(i);
            }
            znak = !znak;
        }
        return przyblizenie;
    }

    public static int silnia(int x) {
        if (x <= 0) {
            return 1;
        }
        return silnia(x - 1) * x;
    }

    public static double potega(double x, int stopien) {
        double potega = 1;
        for (int i = 0; i < stopien; i++) {
            potega *= x;
        }
        return potega;
    }

    public static void main(String[] args) {
        for (double rad = 0; rad <= 2 * Math.PI; rad += Math.PI / 20) {
            double sinObliczony = sin(rad);
            double sinDokladny = Math.sin(rad);
            double err = Math.abs(sinDokladny - sinObliczony);

            System.out.println("Kat: " + Math.toDegrees(rad) + " stopni");
            System.out.println("Sinus obliczony: " + sinObliczony);
            System.out.println("Sinus dokladny: " + sinDokladny);
            System.out.println("Blad: " + err);
            System.out.println();
        }
    }
}
