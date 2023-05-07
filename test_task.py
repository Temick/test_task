'''Програма для тестого задания, которая получает на вход файл с данными в виде чеков и сортирует их, выводит статистическую информацию'''
import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

with open('чеки.txt', encoding='utf-8') as file:
    no_spase = [x.strip() for x in file.readlines()]
    
    GKXservises = list(set([x[:x.find('_')].replace('\ufeff','') for x in no_spase]))

    months = [x.lower() for x in calendar.month_name][1:]
    
    slovar = {}
    
    for month in months:
        slovar[month] = []
    
    for month in months:
        for elem in no_spase:
            if month in elem:
                slovar[month].append(elem[:elem.find('_')])

    paidservises = []

    for month in slovar:
        for servises in sorted(slovar[month]):
            paidservises.append(f'/{month}/{servises}_{month}.pdf')
    
    notpaidservises = {}
    for month in months:
        notpaidservises[month] = []

    for servise in GKXservises:
        for month in slovar:
            if servise not in slovar[month]:
                notpaidservises[month].append(servise)
    
    for month in notpaidservises:
        notpaidservises[month].sort()
    
    with open('чеки_по_папкам.txt','w',encoding='utf-8') as f:
        for elem in paidservises:
            print(elem,file=f)
        print('не оплачено',file=f)
        for month in notpaidservises:
            if notpaidservises[month] != []:
                print(month + ':',file=f)
                for elem in notpaidservises[month]:
                    print(elem,file=f)