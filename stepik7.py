figure = input()

if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print(s)
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif figure == 'круг':
    pi = float(3.14)
    r = float(input())
    print(pi * (r**2))