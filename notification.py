import os
_notification=notification#a string which has all update info,obsolete info,etc.
   #eg 1: update for 4.12 kernel available from offical source,source:ubuntu,level :5,risk :high risk,
   # eg 2: this [package name] is a broken package
   # eg 3: update you distro ,etc ,source:mint,level:1,risk:minimum
os.system('notify-send '+_notification)   
# and clear it afterwards
os.system('clear')
   
