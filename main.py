import time
import uiautomator2 as u2
import os

d = u2.connect('R9CT4000AAM')

data = d.info

if data['screenOn'] == False:
    d.screen_on()
    d.swipe(460, 1847, 460, 0, 0.1)
    d.app_start("com.whatsapp") 
else:
    d.app_start("com.whatsapp")

while True:
    d.screen_on()
    try:
        d(className="android.widget.TextView", text="CHATS").click()
        d(className="android.widget.TextView", resourceId="com.whatsapp:id/conversations_row_message_count").click()
        d.press('back')
    except:
        print("Tidak ditemukan message baru")
    time.sleep(1)