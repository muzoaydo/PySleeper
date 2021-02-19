from tkinter import *
import os
from PIL import ImageTk,Image
os.system('cls')


def kapat(): #Bilgisayarı kapatacak fonksiyon
    girilenSure = sureKutusu.get()
    saniye = int(girilenSure) * 60
    os.system('cmd /c "shutdown -s -f -t %d"'% saniye)
    return True

def uyut():  #Bilgisayarı uyutacak fonksiyon
    girilenSure = sureKutusu.get()
    saniye = int(girilenSure) * 60
    os.system('cmd /k "timeout /t %d&&rundll32.exe powrprof.dll,SetSuspendState Sleep"'% saniye)
    return True

def iptal():  #Kapatma işlemini iptal eden fonksiyon
    os.system('cmd /c "shutdown -a"')
    return True

app =  Tk()  #Pencereyi oluşturan fonksiyon

app.configure(background="MidnightBlue", cursor="star")

app.title("pySleeper - Uyku Zamanı")  #Başlık
bg_path = (r"C:\Users\muzo1\Desktop\Coding\pySleeper\bg.jpg")
#Arkaplan resmi
bg_img = ImageTk.PhotoImage(Image.open(bg_path))
canvas = Canvas(app, width=600, height=300, background="NavyBlue")
canvas.create_image(1280, 720, image = bg_img, anchor=SE)
canvas.pack(expand=TRUE, fill=BOTH)

app.geometry("1024x700") #Boyutlandırma

baslik = Label(
    app,
    text= "Gerekli süreyi girdikten sonra uyut veya kapat butonuna basınız.",
    background="MidnightBlue",
    foreground="MediumSlateBlue"

)
baslik.place(relx=0.34,rely=0.6, relwidth=0.35,relheight=0.05)

sureKutusu = Entry(app, width = 15, background="SlateBlue",relief="sunken",foreground="White")
sureKutusu.place(relx=0.42,rely=0.65, relwidth=0.2,relheight=0.05)

uyut = Button(app, text="UYUT", command=uyut, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
uyut.place(relx=0.42,rely=0.75, relwidth=0.2,relheight=0.05)

kapat = Button(app, text="KAPAT", command=kapat, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
kapat.place(relx=0.42,rely=0.70, relwidth=0.2,relheight=0.05)

iptal = Button(app, text="Kapatmayı iptal et!", command=iptal, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
iptal.place(relx=0.42,rely=0.8, relwidth=0.2,relheight=0.05)



app.mainloop()

"""

TODO exeye çevirilecek!

"""
