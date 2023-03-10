import math
import openpyxl


def sin(x):
    # Przybliżenie działa poprawnie tylko w pierwszej ćwiartce
    x = x % (2 * math.pi)

    # Przybliżenie działa poprawnie tylko w radianach, zamiana stopni na radiany
    x = math.radians(x)

    # Licznik i mianownik szeregu
    numerator = x
    denominator = 1
    result = 0

    # Obliczanie kolejnych wyrazów szeregu
    for i in range(10):
        if i % 2 == 0:
            result += numerator / denominator
        else:
            result -= numerator / denominator

        numerator *= -x * x
        denominator *= (2 * i + 2) * (2 * i + 3)

    return result


# Tworzenie nowego pliku Excela
workbook = openpyxl.Workbook()

# Dodawanie nowego arkusza
sheet = workbook.active
sheet.title = "Sin Approximation"

# Dodawanie nagłówków kolumn
header_row = ["x", "sin(x) approximation", "math.sin(x)", "Difference"]
sheet.append(header_row)

# Testowanie funkcji i dodawanie wyników do arkusza
for i in range(1, 11):
    x = i * math.pi / 6
    approx = sin(x)
    actual = math.sin(x)
    diff = abs(approx - actual)
    data_row = [x, approx, actual, diff]
    sheet.append(data_row)

# Zapisywanie pliku Excela
workbook.save("sin_approximation.xlsx")
print("File saved successfully.")
