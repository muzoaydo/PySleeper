from tkinter import *
import os
from PIL import Image, ImageTk
os.system('cls')

bg_path = (r"C:\Users\muzo1\Desktop\Coding\Projects\pySleeper\night.jpg")#You should change this path with yours!

def shutdown(): #Shutdown Mode
    time = timeBox.get()
    seconds = int(time) * 60
    os.system('cmd /c "shutdown -s -f -t %d"'% seconds)

def sleep():  #Sleep Mode
    time = timeBox.get()
    seconds = int(time) * 60
    #subprocess.run('cmd /k "timeout /t %d&&rundll32.exe powrprof.dll,SetSuspendState Sleep"' %seconds)
    os.system('cmd /k "timeout /t %d&&rundll32.exe powrprof.dll,SetSuspendState Sleep"'% seconds)
    os.system("exit")


def cancel():  #Cancel Shutdown
    os.system('cmd /c "shutdown -a')

app =  Tk()  #Create the window

app.configure(background="MidnightBlue", cursor="star")

app.title("pySleeper - Sleep Time")  #Header

#Background Image Implemantation
bg_img = ImageTk.PhotoImage(Image.open(bg_path))
canvas = Canvas(app, width=600, height=300, background="NavyBlue")
canvas.create_image(1280, 720, image = bg_img, anchor=SE)
canvas.pack(expand=TRUE, fill=BOTH)

app.geometry("1024x700") #Scale

header = Label(
    app,
    text= "Type the minutes you need and choose the operation :)",
    background="MidnightBlue",
    foreground="MediumSlateBlue"

)

#Positioning
header.place(relx=0.34,rely=0.6, relwidth=0.35,relheight=0.05)

timeBox = Entry(app, width = 15, background="SlateBlue",relief="sunken",foreground="White")
timeBox.place(relx=0.42,rely=0.65, relwidth=0.2,relheight=0.05)

sleep = Button(app, text="UYUT", command=sleep, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
sleep.place(relx=0.42,rely=0.75, relwidth=0.2,relheight=0.05)

shutdown = Button(app, text="KAPAT", command=shutdown, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
shutdown.place(relx=0.42,rely=0.70, relwidth=0.2,relheight=0.05)

cancel = Button(app, text="Kapatmayı iptal et!", command=cancel, height=2, width=15,background="MidnightBlue",relief="ridge",foreground="MediumSlateBlue")
cancel.place(relx=0.42,rely=0.8, relwidth=0.2,relheight=0.05)



app.mainloop()
