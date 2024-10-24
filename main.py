# Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# 1. Загрузите набор данных из CSV-файла в DataFrame.
# 2. Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# 3. Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# 4. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd
from numpy.ma.extras import average

df = pd.read_csv('data.csv')
print ("Первые пять строчек из базы IMdb:")
print(df.head())
print ("Информация о базе:")
print(df.info())
print ("Статистика по базе:")
print(df.describe())

print ("Задание с базой dz.csv")
print ("Средняя зарплата по городам:")
df2 = pd.read_csv('dz.csv')
df2.columns = df2.columns.str.strip()
df2_clean = df2.dropna(subset=['City', 'Salary'])
average_salary = df2.groupby('City')['Salary'].mean()
print(average_salary)