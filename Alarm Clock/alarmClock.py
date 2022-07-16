from tkinter import *
import datetime
import time
import winsound
from datetime import datetime
from datetime import date


alarm = Tk()


#alarm framework yerleşimi
alarm.geometry("750x150")
alarm.configure(bg="#DBDBDB")
alarm.title("Alarm")


#framework içerisindeki bileşenler
soru = Label(alarm, text="Hangi Gün ve Saat Kaça Alarm Kurmak İstiyorsunuz?", bg="#DBDBDB")
gun = Label (alarm, text="Ay ve Gün", bg="#DBDBDB")
saat = Label (alarm, text="Saat", bg="#DBDBDB")
dakika = Label (alarm, text="Dakika", bg="#DBDBDB")


#bileşenlerin yerleşimi
soru.grid(row=0,column=0)
gun.grid(row= 1, column= 0)
saat.grid(row= 2, column= 0)
dakika.grid(row= 3, column= 0)


#kullanıcıdan giriş alma
gun_girisi = Entry (alarm, width=60)
saat_girisi = Entry (alarm, width=60)
dakika_girisi = Entry (alarm, width=60)



#bilgilendirme mesajları
gun_girisi.insert(0,"Ayı ve günü başında sıfır olmadan ve arasına nokta koyarak girin")
saat_girisi.insert(0,"24 saatlik dilime uygun şekilde girin")
dakika_girisi.insert(0,"0-59 dakika arasında girin")


#kullanıcı girişinin yerleşimi
gun_girisi.grid(row= 1, column= 1)
saat_girisi.grid(row= 2, column= 1)
dakika_girisi.grid(row= 3, column= 1)


#buraya kadar arayüz programalama kısmıydı.


#alarmı kontrol eden fonksiyon
def setalarm():
    alarmtime = f"{gun_girisi.get()}-{saat_girisi.get()}:{dakika_girisi.get()}"
    print(f"Alarmı {alarmtime} anına kurdunuz.")
    if alarmtime != "::":
        alarm_clock(alarmtime)


#alarm döngüsü
def alarm_clock(alarmtime):
    while True:
        time.sleep(1)
        bugun_gun = date.today().day
        bugun_gun = str(bugun_gun)
        bugun_ay = date.today().month
        bugun_ay = str(bugun_ay)
        bugun = str(bugun_gun) + "." + str(bugun_ay)
        bugun = str(bugun)
        time_now = bugun + "-" + datetime.now().strftime("%H:%M")
        print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(alarm, font=('arial',16 ,'bold'),
            text="Get up and go to POMODOR", bg="red", fg="white").grid(row=6, columnspan=6)
            print("Get up and go to POMODOR")
            winsound.Beep(1500, 2000)
            break


#alarmı kuran buton
buton = Button(alarm, text="Alarmı Kur", command = setalarm)
buton.grid(row=4,column = 1)


alarm.mainloop()