'''Пример архиватора на Python'''
from zipfile import ZipFile

with ZipFile('test_task.zip',mode='w') as zip:
    zip.write('test_task.py')
    zip.write('Задание.txt')
    zip.write('чеки.txt')
    zip.write('чеки_по_папкам.txt')
    zip.write('functions.sql')
    zip.write('function3.sql')