public class MainButExcel {
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
/*
    public static void main(String[] args) {
        // Tworzenie nowego pliku Excela
        XSSFWorkbook workbook = new XSSFWorkbook();

        // Dodawanie nowego arkusza
        XSSFSheet sheet = workbook.createSheet("Sin Approximation");

        // Dodawanie nagłówków kolumn
        Row headerRow = sheet.createRow(0);
        Cell headerCell = headerRow.createCell(0);
        headerCell.setCellValue("x");
        headerCell = headerRow.createCell(1);
        headerCell.setCellValue("sin(x) approximation");
        headerCell = headerRow.createCell(2);
        headerCell.setCellValue("Math.sin(x)");
        headerCell = headerRow.createCell(3);
        headerCell.setCellValue("Difference");

        // Testowanie funkcji i dodawanie wyników do arkusza
        for (int i = 1; i <= 10; i++) {
            double x = i * Math.PI / 6;
            double approx = sin(x);
            double actual = Math.sin(x);
            double diff = Math.abs(approx - actual);

            Row dataRow = sheet.createRow(i);
            Cell dataCell = dataRow.createCell(0);
            dataCell.setCellValue(x);
            dataCell = dataRow.createCell(1);
            dataCell.setCellValue(approx);
            dataCell = dataRow.createCell(2);
            dataCell.setCellValue(actual);
            dataCell = dataRow.createCell(3);
            dataCell.setCellValue(diff);
        }

        // Zapisywanie pliku Excela
        try (FileOutputStream outputStream = new FileOutputStream("sin_approximation.xlsx")) {
            workbook.write(outputStream);
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("File saved successfully.");
    }
 */

}

