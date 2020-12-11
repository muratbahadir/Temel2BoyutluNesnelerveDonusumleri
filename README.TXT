Nesneler ve dönüşümler örnek bir black.png dosyası üzerinden gösteriliyor.
Programın ilk arayüzünde 3 bölüm bulunmaktadır.
1. seçimde nesne çizme fonksiyonu çalıştırılır ve şekilen seçime göre şekil default değerler ile çizdirilir.

2. seçimde nesne dönüşümleri için fonksiyon çalıştırılır. Dönüşüm yapmadan önce hangi nesneye dönüşüm uygulanacağını kullanıcı seçer.
Ardından dönüşüm seçimi yapılır ve ekranda hem çizimin ilk hali hemde dönüşüm uygulandıktan sonraki hali gösterilir.
Not: Kendi testlerimde çizgi nesnesi üzerinde dönüşümleri test ettim. Diğer nesneler üzerinde piksel taşma hataları olabilir.

3. Kırpma işlemi için fonksiyon çalıştırılır. Kırpılma işlemi öncesinde ekrandaki nesneler gerektiğinden
ilk olarak kullanıcıdan nesne veya nesneler çizdirilmesi istenir ve ardından kırpma işlemi yapılır.


Genel Not: Tüm işlemler fonksiyonlar üzerinden gerçekleştirilmiştir.(nesneCiz(...),kirpma(...),birlesikDonusumler(...) vs.)
Program kullanımı kolay olması açısından bu fonksiyonların parametreleri kullanıcıdan alınmayıp default olarak program içinde atama yapıldı.
Parametreleri değiştirerek test etmek isterseniz fonksiyonun çağrıldığı yerden kolaylıkla değişiklikler yapabilirsiniz.
(Hangi parametrenin neyi temsil ettiği kolay anlaşılır şekilde kodlandı.)
Parametre değişerek kontrol etmek isterseniz bazı işlemlerde (özellikle yıldız doldurma ve poligon doldurma) programın hızlı çalışması için
nesnenin alanınu düşük tutmaya çalışmanızı tavsiye ederim.


Python 3.7 kullanılarak Windows 10 platformunda yazılmıştır.