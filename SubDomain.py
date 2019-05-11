print("""                  Yahoo Domain Sorgulayıcı PROGRAMI --- By Laurange")
\n 
 Duyuru : 200,404 ve 500 geri dönüşleri, klasörde otomatik olarak bir txt dosyası oluşturarak oraya kaydedilecektir.\n      """)


import requests

def httpistintak():

    with open("SiteAdresleri.txt", "r", encoding="utf-8") as dosya:
        SiteAdresleri = [ad.replace('\n', '') for ad in dosya.readlines()]
        for ad in SiteAdresleri:

                try:
                    response = requests.get(ad)

                    if response.status_code == 404:
                        with open("404.txt", "a", encoding="utf-8") as dosya2:
                            dosya2.write(ad+'\n')

                    elif response.status_code == 200:
                        with open("200.txt", "a", encoding="utf-8") as dosya3:
                            dosya3.write(ad+'\n')

                    elif response.status_code == 500:
                        with open("500.txt", "a", encoding="utf-8") as dosya4:
                            dosya4.write(ad+'\n')

                except (ConnectionError and requests.exceptions.ConnectionError):
                    print("Diğer siteye erişim sağlanamadı..")

try:
    sorgu = input("İşlem yapmak için '1' yazınız... : ")
    if sorgu == "1":
        print("İşlem başlıyor lütfen biraz bekleyiniz...")
        httpistintak()
    else:
        print("İşlemin gerçekleşmesini istiyorsanız '1' değerini girmelisiniz.")
except (FileNotFoundError):
    print("Lütfen 'DomainSiteleri.txt' dosyasını klasöre ekleyiniz..")
