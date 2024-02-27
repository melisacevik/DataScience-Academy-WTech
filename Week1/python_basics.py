# python versiyonu için

import sys
print('Python Versiyonu:', sys.version)

list = ["1", 1,3,4,"bla"]
list.append("NEW DATA") # sona ekliyor
list.insert(1, "New Data") # istenilen indexe ekleme yapma

list.remove(1) # eleman = 1 'i çıkar

list.pop(2) # 2. indexteki elemanı çıkar

list_A = [0,1,2,3,4]
list_B = [2,3,4,5,6,7]

print("Union: ", list_A.union(list_B))
print("Intersect: ", list_A.intersection(list_B))

# hata verir çünkü UNION VE INTERSECTION set'e ait bir özellik
# AttributeError: 'list' object has no attribute 'union'

# DICTIONARY => KEYLER DEĞİŞEMEZ O YÜZDEN LİSTE YAPAMAZSIN

import this

table1 = [['Sam', 36, 85.95],
 ['Carol', 75, 53.65],
 ['Sam', 90, 95.37],
 ['Doug', 61, 19.8],
 ['Sam', 41, 45.22],
 ['Doug', 29, 42.98],
 ['Oliver', 61, 95.74],
 ['Carol', 32, 17.12],
 ['Tari', 27, 68.83],
 ['Tari', 81, 62.47]]

name_counter = {}
for row in table1:
    name = row[0]
    if name in name_counter.keys():
        name_counter[name] += 1 #value
    else:
        name_counter[name] = 1 #value
print(name_counter)

def count_names_in_tables(table_to_count):
    """
    İlk sütunu kullanıcının adından oluşacak şekilde, bir tablo verisi alır
    ve her bir kullanıcının tabloda kaç defa geçtiğini bulur.
    ---
    Girdi: Tablo (bir çok listeden oluşan bir liste)
    Çıktı: Sözlük (İsimler key değerleri, kaç defa geçtikleri value değerleri)
    """
    name_counter = {}
    for row in table_to_count:
        name = row[0]
        if name in name_counter.keys():
            name_counter[name] += 1
        else:
            name_counter[name] = 1
    return name_counter

print(count_names_in_tables(table1))

# iyi kod yazımı
for row in table1:
    print(row)

# kötü kod yazımı

for i in range(len(table1)):
    print(table1[i])

# sorted metodu değişiklik yapmaz
# sort metodu kalıcı değişiklik yapar

# Lambda fonksiyonları, kaydetmek istemediğimiz fonksiyon tanımlamalarıdır

alumni = [('bob',32,72000),
          ('alice',29,115000),
          ('charlie',25,95000)]

print(sorted(alumni, key=lambda row: row[2])) #maaşa göre sıralama yapıldı ama kalıcı değişiklik yapmadı ( küçükten büyüğe )

alumni.sort(key=lambda row: row[2], reverse=True) #maaşa göre sıralama yapıldı ama kalıcı değişiklik yapmadı ( büyükten küçüğe )

# Hata Mesajları

class_list = [1,2,3]
if len(class_list) % 2 !=0:
    raise ValueError("List should have an even number of elements!")

def sum_up_a_list(list_to_sum):
    """
    Girdi olarak bir sayı listesi alır ve liste
    içerisindeki sayıların toplamını hesaplar.
    """
    # Girdi olarak verilen değerler list yapısında olsun istiyorum
    assert type(list_to_sum) == list, "Input must be a list!"
    return sum(list_to_sum)

print(sum_up_a_list(3))

# TRY - Except

#try-except fonksiyonu, hatalara anında tepki verebilen kod oluşturmanın harika bir yoludur.
# Yapmamız gereken, try ifadesinin içine çalışmasını istediğimiz kod bloğu koymak,
# ardından except ifadesine de try kısmında yazdığımız kodda bir hata meydana geldiğinde de "nasıl bir davranış izlemesini istediğimizi belirtiriz".


x = "1"  # 1 sayısının string versiyonu, bununla matematiksel işlemler gerçekleştirilemez

try:
    print("Trying to divide")
    print(x / 2)
    print("This won't happen because of the error")

except:
    print("\nOops, forgot to make it a number")
    print(int(x) / 2)



del x # del fonksiyonu tanımladığımız değişkeni tamamen silmemizi sağlar

try:
    str(x)
except:
    print("¯\_(ツ)_/¯")

a = [1,2,3]
b = a
b.append(4) # ikisine de ekleme yaptı!

a = [1,2,3]
b = a.copy()
b.append(4)

print(a)
print(b) # kopyasını almamız lazımdı!

