import time
import uiautomator2 as u2
import os
import random

device_id = 'R9CT4000AAM'
appChoices = ["com.whatsapp"]
packagename = random.choice(appChoices)
filename = 'videoplayback.mp4'
targetnumber = '6281311951704'

d = u2.connect(device_id)

def sendMessage():
     message = input('Please enter your message: ')
     targetnumber = input('Please enter your target number: ')
     os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ targetnumber +'" '+ packagename +'')
     d(text='Ketik pesan').set_text(message)
     d(resourceId="com.whatsapp:id/send").click()


# Saat muncul pop-up dari api.whatsapp.com karena nomor tidak terdaftar
# def noNumberPopup():
#     d(resourceId="android:id/button1").click()
# if d(resourceId="android:id/message").get_text().split()[0] == "Nomor":
#     noNumberPopup()

# Saat muncul pop-up bagikan dari api.whatsapp.com
def bagikanPopup():
    if d(resourceId="android:id/message").get_text().split()[0] == "Bagikan":
            d(text="OKE").click()


def pushVideo():
    os.system(f'adb -s '+ device_id +' push MEDIA/'+ filename +' /storage/emulated/0/DCIM/')
    time.sleep(2)
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "'+ targetnumber +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/'+ filename +' -p '+ packagename+'')
    time.sleep(1)
    bagikanPopup()
    d(resourceId="com.whatsapp:id/send").click()




pushVideo()