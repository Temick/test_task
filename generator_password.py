'''Простой генератор паролей'''
import random

n = int(input('Введите желаемую длину пароля: '))

symbols = 'qwertyuiopasdfghjklzxcvbnm'

password = str()

for i in range(n):
    x = random.randint(0,51)
    if x % 2 == 0:
        password += random.choice(symbols)
    else:
        password += str(random.randint(0,9))

print(password)