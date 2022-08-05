import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from msvcrt import getch

r = sr.Recognizer()
def sayi() :
    a = random.randint(1,10)
    return a
def kayıt(ask = False):
    with sr.Microphone() as source:
        if ask:
            ses(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            ses("Anlayamadım")
        except sr.RequestError:
            ses("Sistem çalışmıyor.")
        
        return voice


        
def ses(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,100)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


while True:
    basla="""Çekilişimize hoşgeldiniz.Çekilişimize katılmak için evet deyiniz"""
    ses(basla)
    voice =kayıt()
    
    if "evet" in voice:
        ses("Lütfen tahmin ettiğiniz 1 ile 10 arasında 3 rakamı giriniz")
        i =0
        tahmin =[]
        while i<3:
            metin = "Lütfen {}.tahmininizi giriniz.".format(i+1)
            ses(metin)
            gecici = int(input("Tahmininiz:"))
            tahmin.append(gecici)
            i+=1
        ses("Tahminlerinizi aldım.Şimdi çekilişi başlatıyorum.")
        sonuc=[]
        c=0
        while c<3:
            gecici2=sayi()
            sonuc.append(gecici2)
            c+=1
        kazanan =f"{sonuc[0]} {sonuc[1]} {sonuc[2]}"
        ses("Kazanan numaralarımızı açıklıyorum.")
        time.sleep(2)
        ses("Hazır mısınız")
        time.sleep(2)
        ses("Ve kazanan numaralar")
        time.sleep(2)
        ses(kazanan)
        if tahmin[0] == sonuc[0]:
            ses("İlk tahmininiz doğru")
        elif tahmin[0] != sonuc[0]:
            ses("İlk tahmininiz yanlış")    
        if tahmin[1] ==  sonuc[1]:
            ses("İkinci tahmininiz doğru")
        elif tahmin[1] != sonuc[1]:
            ses("İkinci tahmininiz yanlış")
        if tahmin[2] == sonuc[2]:
            ses("Üçüncü tahmininiz doğru")
        elif tahmin[2] != sonuc[2]:
            ses("Üçüncü tahmininiz yanlış")
        toplam =0
        d =0
        for i in tahmin:
            if i == sonuc[d]:
                toplam+=1
            d+=1
        metin2=f"{toplam} tahmininiz doğru"
        ses(metin2)
        time.sleep(1)
        ses("Çıkmak için herhangi bir tuşa basiniz")
        getch()
        exit()

    elif "hayır" in voice:
        ses("Çıkış yapmak için herhangi bir tuşa basiniz")
        getch()
        exit()

    else:
        ses("Ne dediğinizi anlayamadım lütfen evet veya hayır deyiniz")

        
getch()
input()


