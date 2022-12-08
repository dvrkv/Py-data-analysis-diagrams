import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


# Вспомогательная функция для генерации цветовой схемы
# Принимает количество цветов, которое необходимо сгенерировать и возвращает связный список с цветами
def getColors(n):
    COLORS = []
    cmget = plt.cm.get_cmap('winter', n)
    for i in np.arange(n):
        COLORS.append(cmget(i))
    return COLORS

# Вспомогательная функция для сортировки объектов
def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)

############## Данные ##############

# Для чтения файла с таблицей  используем метод read_csv библиотеки pandas
# escapechar - символы, которые следует игнорировать
# low_memory - настройка обработки файла. Задаем False для считывание файла целиком, а не частями
df = pd.read_csv('./dataset.csv', escapechar='`', low_memory=False)

# Замена none на строку unknown
# df = df.replace({'shape':None}, 'unknown')

# Подсчет количества стран
country_count = pd.value_counts(df['country'].values, sort=True)
country_count_keys, country_count_values = dict_sort(dict(country_count))    
TOP_COUNTRY = len(country_count_keys)

MONTH_COUNT = [0,0,0,0,0,0,0,0,0,0,0,0]
MONTH_LABEL = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь' ,'Октябрь' ,'Ноябрь' ,'Декабрь']

for i in df['datetime']:
    d,m,y =  i.split('.')
    MONTH_COUNT[int(m)-1] = MONTH_COUNT[int(m)-1] + 1

plt.rcParams['figure.figsize'] = (8, 5) # Размер окна

plt.bar(np.arange(12), MONTH_COUNT, color=getColors(12))
plt.xticks(np.arange(12), MONTH_LABEL, rotation=90, fontsize=10)
plt.ylabel('Частота появления', fontsize=12)
plt.yticks(fontsize=10)
plt.title('Частота появления объектов по месяцам', fontsize=12)

# Вывод графика на экран
plt.show()