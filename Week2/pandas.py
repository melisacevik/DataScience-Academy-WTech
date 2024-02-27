# Series : tek boyutlu array , index taşırlar

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 25)
pd.set_option('display.precision', 3)

# DataFrame : satır ve sütunlardan oluşan tablo. veri analizlerimizin temelini oluşturur.

# NumPy kütüphanesini kullanarak DataFrame tanımla

df1 = pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))

# Dictionary(sözlük) veri tipini kullanarak DataFrame tanımlama

df2 = pd.DataFrame({
    "A": 1.,
    'B': pd.Timestamp('20200101'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'), # 4 adet 1 sayısı
    'D': np.array([3] * 4, dtype='int32'), # 3 değerini içereken 4 elemeanlı bir numpy array
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

# Verinin İçeriğini Görüntüleme
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
           'occupation', 'relationship', 'ethnicity', 'gender','capital_gain',
           'capital_loss', 'hours_per_week', 'country_of_origin','income']
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', names=columns)

df.info()
# info => DataFrame içerisinde yer alan sütunlar, bu sütunların veri tipleri, toplam kaç adet kayıt olduğu, boş değer olup olmadığı, hafızada kapladığı alan gibi, veri setimiz hakkında genel anlamda bilgi sahibi olmamızı sağlar.

# iloc : İndex numarasına göre seçer , listede list[0] ile aynı mantık

# 2'şer satır atlayarak tüm satırları seç ancak aynı zamanda sadece 3. ve 5. sütun arasını görmek istiyorum
df.iloc[::2, 2:5].head()
#satır, sütun


# loc : sütun ismine göre seçer ( SON ELEMANDA DAHİL BURADA ! )
#FARKLARI

df.iloc[0:3, :2] #SATIR, SÜTUN
df.loc[0:2, "age":"workclass"] #SATIR, SÜTUN

# Filtreleme işleminden sonra sadece seçtiğim sütunları getir
df.loc[df.age > 50, ['age', 'education', 'occupation', 'gender', 'income']]

#BOŞ DEĞERLERİ BULMA

df.isnull().sum()

# NaN değerleri silme .dropna()

# NaN değerlerin yerine başka değerleri doldurma .fillna(1000)
#null_df.fillna(null_df.column1.median()) # medyanla doldurma

############## PANDAS 2. DERS ###################

# Eğer ki veri setimi tanıyorsam ve NaN değerlere belirli bir atama yapmak istiyorsam,
# df = pd.read_csv('https://bit.ly/2JRmGC2',
#                  na_values = -1,
#                  index_col = 0)

#bu şekilde kullanabilirim.

# sep => sep fonksiyonu ile nasıl ayrılacağıını belirleyebiliriz.