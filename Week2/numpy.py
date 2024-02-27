# from timeit import timeit

import numpy as np
data = np.random.uniform(size=10000) # Dağılımlar hakkında ilerleyen derslerde çok daha detaylı konuşacağız
data_as_list = list(data)

#2 ile toplayalım
data + 2
data_as_list + 2 # error

new_list = []

for row in data_as_list:
    new_list.append(row + 2)

# hızlarına bakmak için

## %timeit
[row+2 for row in data_as_list]

## %%timeit
new_data = data + 2

new_data > 2

# kaç tane True

np.sum(new_data > 2.5)

# değerleri görmek istersem

new_data[new_data > 2.5]

# çok boyutlu NumPy

vector = np.random.uniform(size=(2,4)) # 2 satır 4 sütundan oluşan bir vektör

vector + np.array([1,2]) #satır ve sütun sayısı eşleşmeyen işlemlerde hata alırız

vector - np.array([1,2,3,4])

vector.T + np.array([1,2])


