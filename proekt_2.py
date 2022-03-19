#числа при делении с остатком 2
lower = int(input("Введите нижнюю границу диапазона:")) 
upper = int(input("Введите верхнюю границу диапазона:"))
n = int(input("Введите делитель:"))
for i in range(lower, upper + 1):
    if(i % n == 2):
        print(i)