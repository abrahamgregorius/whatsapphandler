import subprocess
import os
import random
import time
import uiautomator2 as u2

appChoices = ["com.whatsapp", "com.whatsapp.w4b", "com.aero"]
device_id = 'R9CT4007GBM'
filename = 'videoplayback.mp4'
targetnumber = '628159823987'
name = "Bambang"
number = ['6281311951704', '6281212321232']
packageName = ['whatsapp', 'whatsapp.w4b', 'aero']


d = u2.connect(device_id)
 
# def checkCurrentState():
#     return os.system(f'adb -s R9CT4000AAM shell dumpsys activity | findstr mCurrentFocus')
    

def adb(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    return out.decode('utf-8')

def newNumber(name, phone_number):
    os.system('adb -s '+ device_id +' shell "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name '+ name +' -e phone '+ phone_number +' ')
    d(packageName="com.samsung.android.app.contacts", resourceId="com.samsung.android.app.contacts:id/menu_done").click()
    sess = d.session('com.samsung.android.app.contacts')    
    message = os.system('adb -s '+ device_id +' shell dumpsys activity | findstr mCurrentFocus')
    if message == "com.samsung.android.app.contacts/com.samsung.android.contacts.detail.ContactDetailActivity":
        sess.close()


# Sending media via original WhatsApp
def bagikanPopup():
    if d(resourceId="android:id/message").get_text().split()[0] == "Bagikan":
            d(text="OKE").click()

def sendVideoWhatsapp(appChoice, device_id):
    os.system(f'adb -s '+ device_id +' push MEDIA/'+ filename +' /storage/emulated/0/DCIM/')
    time.sleep(2)
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "'+ targetnumber +'@s.whatsapp.net" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/'+ filename +' -p '+ appChoice +'')
    time.sleep(1)
    bagikanPopup()
    d(resourceId="com.whatsapp:id/send").click()


def sendMessageWhatsapp(message, device_id, number):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ number +'" com.whatsapp')
    d(resourceId="com.whatsapp:id/entry").set_text(message)
    d(resourceId="com.whatsapp:id/send").click()


# SENDING MESSAGE WITH WHATSAPP FOR BUSINESS
def sendMessageBusiness(message, device_id, number):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ number +'" com.whatsapp.w4b')
    d(resourceId="com.whatsapp.w4b:id/entry").set_text(message)
    d(resourceId="com.whatsapp.w4b:id/send").click()



# SEND MESSAGE WITH WHATSAPP AERO
def sendMessageAero(message, device_id, number):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ number +'" com.aero')
    d(resourceId="com.aero:id/entry").set_text(message)
    d(resourceId="com.aero:id/send").click()

def sendMessageByPackageName(message, device_id, number, packageName):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone='+ number +'" com.' + packageName + '')
    d(resourceId="com."+ packageName +":id/entry").set_text(message)
    d(resourceId="com."+ packageName +":id/send").click()

# sendMessageWhatsapp("kamu suka warna apa?", device_id, '6281212321232')
# sendMessageBusiness("kamu suka warna apa?", device_id, '6281212321232')
# sendMessageAero("kamu suka warna apa?", device_id, '6281212321232')


def clickAirplane():
    d.swipe(500, 10, 500, 2061, 0.1)
    d.click(792, 416)
    d.swipe(500, 2061, 500, 10, 0.1)

def mencariPopup():
    if d(resourceId="android:id/message").get_text().split()[0] == "Tidak":
        d(text="OKE").click()

# for i in range(1000):
#     # RANDOMIZE 
#     item = random.choice(packageName)
#     itemNumber = random.choice(number)
#     
#     # SEND MESSAGE DAN NYALAKAN AIRPLANE MODE
#     sendMessageByPackageName("kamu suka warna apa? " + str(i), device_id, itemNumber, item)
#     clickAirplane()
#     time.sleep(2)
#     clickAirplane()
#     time.sleep(5)




def backupPage():
    a = adb(f'adb shell dumpsys activity | findstr "mCurrentFocus"')
    while "com.whatsapp/com.whatsapp.backup.google.GoogleDriveNewUserSetupActivity" in a:
        d(text="SELESAI").click()
        break

backupPage()
