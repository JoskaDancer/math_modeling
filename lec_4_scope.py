x0 = 10 # Переменная в глобальной области видимости

def move(t):
  x = x0 * t
  return x # Локальная переменная

print(move(3)) 
a = 'Good'

def my_func():
  a = 'Bad'
  print(a)

my_func()\
print(a)