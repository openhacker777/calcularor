import math as mt

print("Чтобы посчитать квадратное уравнение, введите 1 \n Чтобы раскрыть квадрат суммы/разности, введите 2")
user = input("")

if user == "1":
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число с: "))
    D = b**2-4*a*c
    if D<0:
        print("Нет решения дискриминант меньше нуля")
    else:
        dd = mt.sqrt(D)
        x1 = (-b+dd)/(2*a)
        x2 = (-b-dd)/(2*a)
        print("Первый корень равен ",x1)
        print("Второй корень равен ",x2)
elif user == "2":
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    sumvol = input("Минус или плюс?: (-/+)")
    if sumvol == "+":
        ab = a**2+2*a*b+b**2
        print(ab)
    else:
        ab = a**2-2*a*b+b**2
        print(ab)