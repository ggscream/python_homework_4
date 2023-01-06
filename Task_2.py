# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


if (number := int(input())) == 1:
    print("1")
else:
    print(Factor(number))