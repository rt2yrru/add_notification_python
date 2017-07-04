import os
_notification=notification#a string which has all update info,obsolete info,etc.
   #eg 1: update for 4.12 kernel available,
   # eg 2: this [package name] is a broken package
   # eg 3: update you distro ,etc 
os.system('notify-send '+_notification)   
# and clear it afterwards
os.system('clear')
   
