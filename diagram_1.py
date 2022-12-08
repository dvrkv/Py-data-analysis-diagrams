import pandas as pd
import numpy as np
import seaborn as sns
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

# Создание столбчатой диаграммы
#plt.bar(np.arange(TOP_COUNTRY), country_count_values)
plt.rcParams['figure.figsize'] = (8, 5) # Размер окна
f, a = plt.subplots()
plt.axhline(35, 0, ls='--', color='r', linewidth=2.5) # Красная линия границы

# Название графика и подписи
plt.title('Страны с наибольшим количеством наблюдений', fontsize=12, color='#404040')
plt.ylabel('Количество наблюдений', fontsize=12, color='#404040')
plt.xlabel('Страны', fontsize=12, color='#404040')
plt.xticks(np.arange(TOP_COUNTRY), country_count_keys, rotation=0, fontsize=10)
plt.yticks(fontsize=10)

# Линии
a.set_axisbelow(True)
a.yaxis.grid(True, color='#e3e3e3', linewidth=0.8)
a.xaxis.grid(False)

# Надписи и цвет столбцов
splot=sns.barplot(x=country_count_keys,y=country_count_values)
plt.bar_label(splot.containers[0], size=14,label_type='edge')

# Крайние оси
a.spines['top'].set_visible(False)
a.spines['right'].set_visible(False)
a.spines['left'].set_visible(False)
a.spines['bottom'].set_color('#c4c4c4')

f.tight_layout() # Вписываеи диаграмму в окно
#---------------
# Диаграмма в виде кривой
# plt.plot(np.arange(TOP_COUNTRY), country_count_values, '-', linewidth=1.0)
# plt.plot(np.arange(TOP_COUNTRY), country_count_values, 'bo', linewidth=230.0, color='darkblue', markersize=6, marker='o')
#---------------

# Вывод графика на экран
plt.show()
