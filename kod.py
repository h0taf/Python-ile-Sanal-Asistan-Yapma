#HAMSİRİ PROJESİ
#Proje için gerekli kütüphaneler
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser

#Konuşmamızı algılamamızı sağlaması için bir değişken
r = sr.Recognizer()

#Her seferinde bir şey yaptırmak isteğimizde Hamsiri dememek için bir değiken
tekrar = False

#Konuşmamızı algılamızı sağlaması için bir fonksiyon
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("Anlaşılamadı")
        except sr.RequestError:
            print("Sistem Çalışmıyor")
        return voice
     
#Sanal asistana yaptırmak istediklerimizi yaptırdığımız fonksiyon
def responce(voice):
     #Selamlaşma komudu
     if "merhaba" in voice or "selam" in voice:
       selection = ["Sana da merhaba uşağum","Sana da selam uşağum","Aleyküm selam uşağum"]
       speak(random.choice(selection))
       selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"]
       speak(random.choice(selection))
       #Teşekkür etme komudu
     if "teşekkürler" in voice or "eyvallah" in voice:
       selection = ["rica ederim uşağum","ne demek uşağum","ne demek","rica ederim"]
       speak(random.choice(selection))
       selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"]
       speak(random.choice(selection))
       #Sanal Asistanı kapatma komudu
     if "görüşürüz" in voice or "yok" in voice or "hayır" in voice or "ham siri kapan" in voice:
       selection = ["görüşürüz uşağum","görüşürüz uşağum"]
       speak(random.choice(selection))
       exit()
      #Gün sorma komudu
     if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
           selection = ["Gün Pazartesi Hamsi Kafa","Takvimin yok mu uşağum?Gün Pazartesi"]
           today = random.choice(selection)
        elif today == "Tuesday":
           selection = ["Gün Salı Hamsi Kafa","Takvimin yok mu uşağum?Gün Salı"]
           today = random.choice(selection)  
        elif today == "Wendesday":
           selection = ["Gün Çarşamba Hamsi Kafa","Takvimin yok mu uşağum?Gün Çarşamba"]
           today = random.choice(selection)
        elif today == "Thursday":
           selection = ["Gün Perşembe Hamsi Kafa","Takvimin yok mu uşağum?Gün Perşembe"]
           today = random.choice(selection)
        elif today == "Friday":
           selection = ["Gün Cuma Hamsi Kafa","Takvimin yok mu uşağum?Gün Cuma"]
           today = random.choice(selection)
        elif today == "Saturday":
           selection = ["Gün Cumartesi Hamsi Kafa","Takvimin yok mu uşağum?Gün Cumartesi"]
           today = random.choice(selection)
        elif today == "Sunday":
           selection = ["Gün Pazar Hamsi Kafa","Takvimin yok mu uşağum?Gün Pazar"]
           today = random.choice(selection)
        speak(today)
        selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"]
        speak(random.choice(selection))
      #Saat sorma komudu   
     if "saat kaç" in voice:
        selection = ["Saatimiz ","Sen İste Uşağım ","Yukardan Bakabilirdin Hamsi Kafa,Ama Neyse Söyliyeyim "]
        speak(random.choice(selection) + datetime.now().strftime("%H:%M"))
        selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"]
        speak(random.choice(selection))
      #Tarih sorma komudu
     if "hangi tarihteyiz" in voice:
        tarih = datetime.now().strftime("%Y-%m-%d")
        speak("Tarih " + tarih) 
      #Google'da arama yapma komudu
     if "google'da ara" in voice or "google" in voice or "google'da arama yap" in voice:
        selection = ["Ne aramamı istersin uşağım?","Ne aramamı istersin?"]
        speak(random.choice(selection))
        search = record()
        webbrowser.get().open("https://www.google.com/search?q={}".format(search))
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))
        selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"] 
        speak(random.choice(selection))
      #Not alma komudu
     if "not et" in voice:
        selection = ["Dosya ismi ne olsun?","Dosya ismi ne olsun uşağum"]
        speak(random.choice(selection))
        txtfile = record() + "txt"
        selection = ["Ne kaydetmek istiyorsun?","Ne kaydetmek istiyorsun uşağum?"]
        speak(random.choice(selection))
        theText = record()
        f = open(txtfile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()
        selection = ["Başka Bir İsteğin Var Mı?","Başka Bir İsteğin Var Mı Uşağum?"]
        speak(random.choice(selection))

#Sanal asistanın konuşması için gerekli fonksiyon
def speak(string):
    tts = gTTS(text=string,lang="tr",slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

#İlk çalıştığında yapay zekayı aktif etmek için gerekli fonksiyon
def test(wake):
   if "hamsiri açıl" in wake or "hamsiri" in wake or "ham siri" in wake or "ham siri açıl" in wake or "açıl" in wake:
      selection = ["Merhaba Uşağum,Ben Hamsiri.Ne araydun uşağum?","Merhaba Ben Hamsiri,Nasıl Yardımcı Olabilirim"]
      speak(random.choice(selection))
      wake = record()
      if wake != '':
       voice = wake.lower()
       print(wake.capitalize())
       responce(voice)

#Projenin çalıştığını anlamamızı sağlayan kod
print("Hazırım")

#Dediklerimizi sanal asistana aktaran döngü
while True:
   if tekrar == False:
    wake = record()
    if wake != '':
     wake = wake.lower()
     print(wake.capitalize())
     test(wake)
     tekrar = True
   else:
      wake = record()
      if wake != '':
       voice = wake.lower()
       print(wake.capitalize())
       responce(voice)

#h0taf tarafından yapıldı.
#made by h0taf.


          
