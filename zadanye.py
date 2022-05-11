#простые числа
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True
 
 
a, b = map(int, input("Два числа через пробел от a до b: ").split())
print(*list(filter(is_prime, range(a, b + 1))))