#взаимно простые числа
a = int(input())
b = int(input())
c = int(input())
main_num = a 
lmain_div = []
for num in range(1, main_num):
    if main_num % num == 0:
        lmain_div.append(num)
print('a % range(1, a) = ', lmain_div)
count_num = 0
for num in range(b, c):
    for div in lmain_div:
        if num % div == 0:
            count_num += 1
            break
print('Count num = ', count_num)