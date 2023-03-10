import math


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


# Testowanie funkcji
for i in range(1, 11):
    x = i * math.pi / 6
    approx = sin(x)
    actual = math.sin(x)
    diff = abs(approx - actual)
    print(f"x = {x}, sin(x) = {approx}, math.sin(x) = {actual}, diff = {diff}")
