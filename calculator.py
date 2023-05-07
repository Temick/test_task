'''Простой калькулятор, при необходимости можно улучшить функционал операциями из модуля math'''
import math
from decimal import Decimal

a,b = [Decimal(i) for i in input('Введите два числа через пробел: ').split()]
operation = input('Введите операцию +, -, /, *, //, %, **(возведение в степень): ')
slovar = {'+': a + b,'-': a - b, '/': a / b, '*': a * b, '//': a//b, '%': a%b, '**': a**b}

print(slovar[operation])