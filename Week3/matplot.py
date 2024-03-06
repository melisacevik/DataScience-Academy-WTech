## Matplotlib ve Seaborn Dersi

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot => Liste, Numpy Array, Pandas Series, DataFrame , çoklu grafik(legend ile kullan ) ile kullanılır
# listeler

# tek bir liste belirlersen y eksenine yazar.

data_list = [1,2,1,3]
print(data_list, type(data_list))
plt.plot(data_list)
plt.show()

# SORU: Y ekseninde bizim tanımladığımız liste yapısındaki değerler yer alıyor. Peki ya x ekseninde?

x = [10,20,21,30]
plt.plot(x, data_list)
plt.show()

# Şimdi de sıra Numpy Array, Pandas Series ve DataFrame de.

data_numpy = np.array(data_list)
print(data_numpy, type(data_numpy))
plt.plot(data_numpy)
plt.show()

data_pandas_series = pd.Series(data_list)
print(data_pandas_series, type(data_pandas_series))
plt.plot(data_pandas_series)
plt.show()

data_frame = pd.DataFrame(data_list)
print(data_frame, type(data_frame))
plt.plot(data_frame)
plt.show()


##### Temel Grafik Türleri #####

# Bar => kategoriler arasında karşılaştırma yapmak için kullanılır

new_x = np.arange(20) # bu ifade belirli bir aralıktaki değerlerden oluşan bir dizi oluşturur. 0-19'a kadar olan sayıları içeren dizi oluşturur.
new_y = np.random.randint(5,10,20) #belirli bir aralıktaki rastgele tam sayıları içeren bir dizi oluşturur. 5 ile 10 arasındaki rrastgele 20 tam sayı içeren bir dizi oluşturur.
# random => modül , randint modüle ait metot
#plt.bar(new_x, new_y)
plt.barh(new_x, new_y)
plt.show()

# Hist => veri dağılımlarını görüntülemek için

nex_x = np.random.randn(100000)
plt.hist(nex_x)
plt.show()

# randn ( ) => normal dağılıma sahip rastgele sayıları üretmek için kullanılır.

# Pie => verileri bir bütünün yüzdesi olarak düzenlemeye ve göstermeye yardımcı olur.

new_x = np.arange(1,4)
plt.pie(new_x, labels=["a","b","c"])
plt.show()

# line => biz dizi veri noktasını birbirine bağlar.
# zaman içindeki verileri göstermek istediğinizde kullanmak harika seçim!
# x tarih y nicel alan olsun

new_x = np.arange(100)
new_y = np.random.randint(0,10,100)
plt.plot(new_x, new_y)
plt.show()

# scatter => dağılım grafiği | iki ölçü arasındaki ilişkiyi incelemek istediğimizde kullanışlıdır.
# değişkenlerin arasında bir ilişki var mı? varsa ne ölçüde?
# boy ve kilo arasındaki ilişki

# X ve Y ekseninin başlangıç ve bitiş noktalarına elinizdeki verinin minimum ve maksimum değerlerine göre karar verin

new_x = np.random.randn(1000)
new_y = np.random.randn(1000)
plt.scatter(new_x, new_y)
plt.show()

# heatmap => metin tablosu olarak görüntülenen verileri görselleştirmeye yardımcı olmak için renk kullanır.
# detayları seaborn'da.

# box plot => veri noktalarının dağılımını gösterirken kullanmak için harika bir araçtır.
# aykırı değer tespiti!

##### Görsel ögeleri #####

# grafik başlığı
plt.plot(data_list)
plt.title("Graph Title")
plt.show()

# renklendirme
plt.plot(data_list)
plt.title("Serif Title", fontsize = 30, loc="left", color="red", style="italic", weight="bold" )
plt.show()

# x ve y başlıkları

plt.plot(data_list)
plt.xlabel("Label on the X axis")
plt.ylabel("Label on the Y axis", fontsize= 15, weight="bold", color="green")
plt.show()

# Grid

plt.plot(data_list)
plt.grid()
plt.show()

# gridlerin hangi aralıklarıda gösterilmesini istiyorsak, plt.xticks() ve plt.yticks()

plt.plot(data_list)
plt.grid()
ticks_x = np.linspace(0, 3, 10)
ticks_y = np.linspace(1, 3, 3)
plt.xticks(ticks_x)
plt.yticks(ticks_y)
plt.show()

# çoklu grafik

data_list = [1,2,1,3]
data_list2 = [1,2.4,3,4.2]
plt.plot(data_list)
plt.plot(data_list2)
plt.show()

# legend ile grafiğin hangi veriye ait olduğunu gösterebilirsin

plt.plot(data_list)
plt.plot(data_list2)
plt.legend(["First Line", "Second Line"], shadow = True)
plt.show()

# Renkler

#Alias Kullanmak https://matplotlib.org/2.2.5/api/_as_gen/matplotlib.pyplot.colors.html
#Hex Kodu Kullanmak https://www.w3schools.com/cssref/css_colors.asp

# Çizgi Stilleri

plt.plot(data_list, linestyle = '--', linewidth = 3, color = 'b')
plt.plot(data_list2, linestyle = '-.', linewidth = 5, color = 'r')
plt.plot(np.array(data_list2)+1, linestyle = ':', linewidth = 2, color = 'k')
plt.plot(np.array(data_list)-1, linestyle = '-', linewidth = 4, color = 'g')
plt.show()

# grafik boyutları

# grafiğin boyutunu değiştirme => figure()

plt.figure(figsize = [12,5]) # genişlik, yükseklik
new_x = np.random.randn(100000)
plt.hist(new_x, 50)
plt.show()

# Eksen aralığı
#grafikte oluşturulan eksenlerin başlangıç ve bitiş noktalarını değiştirmek için plt.axis()

new_x = np.arange(100)
new_y = np.random.randint(0,10,100)
plt.plot(new_x,new_y)
plt.axis([-10, 110, -10, 20]) # [x_min, x_max, y_min, y_max]
plt.show()

# Yazı Ekleme

new_x = np.arange(100)
new_y = np.random.randint(0,10,100)+(0.05*new_x)**2
plt.plot(new_x,new_y)
plt.text(60, 5, 'Sample Text', fontsize = 20, backgroundcolor = 'k', color = 'white') # Yazının başlama yeri(x, y)
plt.show()

# Çoklu grafikler oluşturma


# yan yana => subplot
new_x = np.arange(20)
new_y = np.random.randint(5,10,20)

plt.figure(figsize=[15,5])

plt.suptitle('Main Title', fontsize = 16)

plt.subplot(1,3,1) # (Satır Sayısı, Sütun Sayısı, Grafik No)
plt.plot(new_x, new_y)
plt.title('Line Chart')

plt.subplot(1,3,2)
plt.bar(new_x, new_y)
plt.title('Bar Chart')

plt.subplot(1,3,3)
plt.bar(new_x, new_y)
plt.title('Bar Chart')
plt.show()

# alt alta

new_x = np.arange(20)
new_y = np.random.randint(5,10,20)

plt.figure(figsize=[15,10])

plt.suptitle('Main Title', fontsize = 16)

plt.subplot(2,1,1)
plt.plot(new_x, new_y)
plt.title('Line Chart')

plt.subplot(2,1,2)
plt.bar(new_x, new_y)
plt.title('Bar Chart')
plt.show()