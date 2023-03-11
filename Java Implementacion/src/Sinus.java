public class Sinus {
    public static double sin(double kat){
        //upewnic sie ze kat jest w radianach
        double sin = 0;
        kat %= (2*Math.PI);

        if (kat >= 0 && kat <= (Math.PI)/2){
            sin = ciagTylora(kat,5);
        }else if (kat > (Math.PI)/2 && kat <= Math.PI){
            kat = Math.PI - kat;
            sin = ciagTylora(kat,5);
        }else if (kat > Math.PI && kat <= Math.PI + (Math.PI)/2){
            kat = -(kat - Math.PI);
            sin = ciagTylora(kat,5);
            //sin = - sin;
        }else if (kat > Math.PI + (Math.PI)/2 && kat <= 2*Math.PI){
            kat = -(2*Math.PI - kat);
            sin = ciagTylora(kat,5);
            //sin = - sin;
        }

        return sin;
    }

    public static double ciagTylora(double kat, int dokladnosc){
        double przyblizenie = 0;
        int znak = 0;

        for (int i = 1; i < dokladnosc * 2; i+=2) {
            if (znak%2==0){
                przyblizenie += potega(kat, i)/silnia(i);
            }else {
                przyblizenie -= potega(kat, i)/silnia(i);
            }

            znak++;
        }

        return przyblizenie;
    }

    public static int silnia(int x){
        if (x <= 0){
            return 1;
        }
        return silnia(x-1) * x;
    }

    public static double potega(double x, int stopien){
        double potega = 1;
        for (int i = 0; i < stopien; i++) {
            potega *= x;
        }
        return potega;
    }

    public static void ktoraCwiarka(double kat){
        if (!(kat%Math.PI==0)){
            return;
        }
        kat %= Math.PI*2;
        System.out.println("------------------------------------");
        if (kat <= Math.PI/2){
            System.out.println("Cwiartka I");
        } else if (kat <= Math.PI){
            System.out.println("Cwiartka II");
        }else if (kat <= (3*Math.PI)/2){
            System.out.println("Cwiartka III");
        }else if (kat <= 2*Math.PI){
            System.out.println("Cwiartka IV");
        }
        System.out.println(kat);
        System.out.println();
    }

    public static void main(String[] args) {
        for (double kat = 0; kat <= 2*Math.PI; kat +=Math.PI/20) {
            ktoraCwiarka(kat);
            double sinObliczony = sin(kat);
            double sinDokladny = Math.sin(kat);
            double err = sinDokladny - sinObliczony;
            System.out.println("Kat: " + kat);
            System.out.println("Sinus obliczony: " + sinObliczony);
            System.out.println("Sinus dokladny: " + sinDokladny);
            System.out.println("Blad: " + Math.abs(err));
            System.out.println();
        }
    }
}
