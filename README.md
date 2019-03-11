# Jump-Fist

Web kameranızdan bilgisayarınız kontrol edebileceğiniz OpenCV tabanlı proje.

## Getting Started

Web kamerasından alınan görüntüyü bilgisayar kontrolünde kullanmak üzere yazılan bu basit proje HaarCascade modelleri ile farklı tanımlamalar yapabilir. 

HaarCascade modelleri görüntü üzerinde çeşitli etmenlerin tanınmasında kullanılmak üzere eğitilmiş modellerdir. Farklı çalışmalar için bu modeller değiştirilerek yumruk, insan yüzü, vücut, göz, gülümseme gibi çeşitlendirilebilir.

Görüntü üzerinde bu model ilgili tetikleyiciyi bulduktan sonra, PyAutoGui kütüphanesiyle bilgisayara gönderilecek komutlar, klavye girdileri, mouse hareketleri veya isteğe bağlı diğer komutlar olarak değiştirilip, çalışmaya uygun hale getirilip kullanılabilir.

### Prerequisites

```
Python 3.x.x
webbrowser
cv2
pyautogui
```

### Installing
Klasör dizininde komut penceresini açıp "python yumrukoyunu.py" komutunu girdikten sonra oyun başlayacaktır.

Kamera açıldıktan sonra oyun penceresine tıklayın ve yumruğunuzu sıkarak dinozoru zıplatın.

![](https://media.giphy.com/media/w85QqVSEGyioxBqre7/giphy.gif) 

### Notes:
Diğer HaarCascade modellerine aşağıdaki github reposundan ulaşılabilir.

[OpenCV - HaarCascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## Authors

* **Mert Çobanoğlu** - [Cobanov](https://github.com/cobanov)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


