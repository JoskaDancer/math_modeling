#числа близнецы
lower = int(input("Введите минимальную границу: "))
upper = int(input("Введите максимальную границу, которая будет умножена на 2: "))
for lower in range(lower, 2*upper - 1, 1):
  print([lower, lower+2],end=";")