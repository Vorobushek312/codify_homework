# Дан файл с данными:
# name,age,salary
# Tom,28,500
# Alice,23,1200
# Bob,34,2400
# Mark,23,700
# Frank,20,900
# Fill,23,1200
# Jonh,44,2330
# Greg,53,1500
# Peter,18,100
# 1. Посчитать среднюю зп.
# 2. Посчитать средний возраст.
import os
import sys
import csv

FILE_NAME = os.path.join(sys.path[0], 'file_employees.csv')
with open(FILE_NAME, encoding='utf-8') as file:
    reader_object = csv.reader(file, delimiter = ',')
    count = 0
    summ_salary = 0
    summ_age = 0
    for row in reader_object:
        if count == 0:
            count += 1
        else:
            count += 1
            summ_salary += int(row[2])
            summ_age += int(row[1])
print(f'Средний возрост сотрудников {summ_age / (count -1 )}, средняя заработная плата {summ_salary / (count -1 )}.')
