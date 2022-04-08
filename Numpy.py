
#------------------------------------------------------------
#--Numpy kullanımının sebebi  nedir ?
#------------------------------------------------------------

import numpy as np
# Çok hızlı sabit tipte veri tuttuğu için
a = [1,2,3,4]
b = [2,3,4,5]

ab = []
# bu iki elemanın çarpılması için normalde for ile döngüye sokup i üzerinden tek tek gezip çarpıp ab'ye append etmeliyiz

for i in range(0, len(a)):
    ab.append(a[i]*b[i])# append ile listeye eleman ekleyebiliriz.

# Numpy kullanmasaydık bu şekilde bir döngü oluşturmamız gerekiyordu.
# Numpy kullanımında ise
a = np. array([1,2,3,4])#listeler numpy array'ine çevrilip
b = np. array([2,3,4,5])
a*b # sadece bu şekilde çarpma işlemini yazmamız yeterli
# çıktı  Out[3]: array([ 2,  6, 12, 20]) bu şekilde gelecektir.

#------------------------------------------------------------
#--Creating Numpy Arrays--
#------------------------------------------------------------

# Numpy arrayleri genel olarak sıfırdan oluşturulmazlar
## Çektiğimiz verilerin dönüştürülmesi yoluyla meydana getirilirler
### Sıfırdan oluşturması azda olsa kullanılır

import numpy as np
np.array([1,2,3,4,5])# Liste üzerinden numpy arrayi oluşturma çıktı Out[3]: array([ 2,  6, 12, 20])
type(np.array([1,2,3,4,5])) # Type şeklinde ise çıktı Out[8]: numpy.ndarray numpy array şeklindedir

np.zeros(10,dtype=int) # Komutu sayesinde 10 tane 0'dan olusan bir numpy array olusturabiliriz.
#dtype sayesinde oluşturulacak arrayin tipi ayarlanabilir.
np.random.randint(0,10,size = 10) # bu komut sayesinde 0-10 arasinda toplam 10 değer random bir şekilde oluşturulur.
np.random.normal(10,4,(3,4)) # Ortalamasi 10 olan standart sapmasi 4 olan ve 3x4 lük bir sayı dizimi oluşturur.
# Kodun sonucu asagidaki gibidir. random olduğu icin her seferinde farkli degerler olusturur.
###array([[13.86548313, 11.05340769, 11.93192377, 11.02396981],
    ##   [ 5.71100333,  9.37436793, 12.45762069, 15.3872912 ],
    ##   [10.01839069, 11.42317953, 14.6898519 ,  0.56313507]])

#------------------------------------------------------------
#-- Numpy Array Özellikleri--
#------------------------------------------------------------

import numpy as np
a= np.random.randint(0,10,size = 5)
a.ndim #ndim burada bizim arrayimizin boyut sayisini bize verir.
a.shape # shape komutumuz ise boyut bilgisini bize verir her boyutta kaç eleman var gibi
a.size # Arrayimizdeki toplam eleman sayisini verir
a.dtype  # arrayimizdeki degerlerin tip bilgisini vermektedir.

#--Reshaping ( Yeniden Boyutlandırma)

np.random.randint(1,10, size = 9) # Randint tarzında arryimizi oluşturduktan sonra yeniden boyutlandırmak istersek
#::: Out[21]: array([5, 7, 6, 2, 9, 2, 5, 6, 3])
np.random.randint(1,10, size = 9).reshape(3,3)# sonuna ekledigimiz reshape() komutu ile boyutlarını giriyoruz.
#::: Out[22]:
#array([[7, 2, 8],
 #      [4, 7, 4],
  #     [5, 1, 9]]) olarak sonucu alinir. Unutulmamlidir ki burada olusturma islemi olsada atama islemi yoktur.

# Sabit bir array tekrar boyutlandıracagimizi dusunursek
ar = np.random.randint(1,10, size = 9)
ar.reshape(3,3) # islemi bu sekilde yapabiliriz.
# ONEMLİ NOT : Arrayin eleman sayisi ile boyutlandirma toplamindaki eleman sayisi ayni olmalidir.

#------------------------------------------------------------
#--INDEX SECİMİ
#------------------------------------------------------------

import numpy as np
a = np.random.randint(10,size=10) # random bir array olusturuyoruz
a[0] # tek bir secim yapmis ve ilk karakteri cagirmis oluruz
a[0:5]# Bu islemde ise dilimle yöntemi ile 0'dan 5 indeksine sahip olan sayilari cagirma komutudur
#ciktisi Out[4]: array([9, 0, 8, 3, 4]) seklinde olusur
a[0] = 55 # diye komut girerek 0. indexi degistirmis oluruz
m= np.random.randint(10, size=(3,5))# bu islemde 3 satır 5 sutunda 0 ile 10 arasinda bir array olusturulur
m[0,0] # burada ise 1.satirin 1. sutunundaki elemani cagirmis oluruz
m[0,2] = 12 # gibi bir komut kullanarak bu indexte bulunan degeri degistirebiliriz.
m[1,2] =1.2 #gibi bir float deger atamaya calisirsak numpy kutuphanesi tek tipte deger tuttugu icin
#bu degeri direkt olarak int degerine ceviriyor.
m[:,0] # bu sekilde ":" ile girilen satir veya sutun index o kisimdaki butun elemanlari ifade eder
#yani buradaki degerde ilk sutunda bulunan butun degerler olarak diyebiliriz.

m[0:2,0:3] # bu degerimizde ise satir ve sutunlardaki degerin arasinda bulunan kisimi cagirmis oluruz

#------------------------------------------------------------
#--FANCY INDEX
#------------------------------------------------------------

import numpy as np

v= np.arange(0,30,3)# 0'dan 30'a kadar 3'er 3'er artan numpy array oluştur demektir.
v[1]
v[4]# bizim burada yaptigimiz tek tek secim islemini fancy index ile tek seferde yapabilecegiz
# buyuk verilerde bu islem bizim cok isimize yarayacaktir.
catch = [1,2,3] #gibi bir liste olusturup
v[catch] # islemini yaptigimizda ilk 3 index'e kolay bir sekilde erisebiliyor oluyoruz.
#:: kod ciktisi Out[7]: array([3, 6, 9]) seklinde gorulmektedir.

#------------------------------------------------------------
#-- MATHEMATİCAL OPERATİONS
#------------------------------------------------------------

# yukarıdaki atadıgımız v arrayini kullanacagim
import numpy as np

v= np.arange(0,30,3)
v/5 # bu islemi matematiksel olarak bolup sonucu yeni bir array olarak bize verecektir.
v**2 #karesini alma islemidir.
v-1 #cikarma islemide ayni sekilde direkt islemi yapacaktir.
#Direkt olarak islemlerin haricinde bazi metodlarda vardir
#Ornek olarak gösterecek olursak
np.subtract(v,1) #Cikarma islemi yapar
np.add(v,1) # Toplama islemi yapar
np.mean(v) # Ortalamasini alir
np.sum(v) # Butun elemanlari toplar
np.min(v) # Minimum degerini alir
np.max(v) # Maksimum degerini alir
np.var(v) # Varyans degerini getirir.
# ONEMLİ NOT : Buradaki islemlerin hicbiri atama seklinde degildir. Sadece cikti gösterilir. Bunu unutmamak gerekir!!!

#İKİ BİLİNMEYENLİ DENKLEM COZUMU
#Denklem :  5*x0 + x1    = 12
#           x0   + 3*x1  = 10
# Numpyin ozelligi bu kat sayilari belirli bir özellikte kendisine gonderebilirsek bize direkt olarak sonucu verebilir.

a = np.array([[5,1],[1,3]])
b = np.array([12,10])
np.linalg.solve(a,b)
#yukarida yazmis oldugumuz kodla bu islemi kolayca yapabiliyoruz.
#------------------------------------------------------------
#-- Numpy'da kosullu islemler (Conditions on Numpy)
#------------------------------------------------------------
import numpy as np
v = np.array([1,2,3,4,5])

# Numpy olmadan klasik olarak 3'ten kucuk olanlara nasil erisebiliriz.
ab = []
for i in v: # For dongusuyle v içinde i basamaklari olarak geziyoruz.
    if i <3: # if koutuyla 3ten kuucuk olan sayilari sorgulatiyoruz.
        ab.append(i) # 3'ten kucuk olan sayilarin append komutuyla ab icine atanmasini saglyoruz

ab #:::  Out[12]: [1, 2]

# Klasik olarak yapmamiz gereken islem budur.

# Numpy ile bu islemi yapmak istersek

v < 3 # Burada direkt olarak true,false olarak butun elemanlari sorgular
#:: Out[13]: array([ True,  True, False, False, False])

v[v < 3] #dersek eger sadece True olanlari yazdiracaktir.
#:: Out[14]: array([1, 2])

v[v > 3] # 3'ten buyuk olanları gosterir
#:: Out[15]: array([4, 5])

v[v != 3] # 3'ten farkli olanlarin gelmesini saglar
#:: Out[16]: array([1, 2, 4, 5])

v[v == 3] #3'e esit olanlar
#:: Out[17]: array([3])

v[v <= 3] # 3'den kucuk ve esitler
#:: Out[18]: array([1, 2, 3])

# Bu cagirma islemlerinde asil mantik fancy indexe dayanmaktadir.


