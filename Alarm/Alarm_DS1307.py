#import sys
import time
#import datetime

import RPi.GPIO as GPIO
import SDL_DS1307
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarings(False)
LED = 11
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,True)
time.sleep(1)

# Main Program
print "program begins"

#print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

#print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")	
print "DS1307=\t\t%s" % ds1307.read_datetime()
print "_______________________________"
print " DS1307 Hours:", ds1307._read_hours()
print "DS1307 Mintues:", ds1307._read_minutes()
    
Alaram_Hour = int(input("set the Alaram hour"))
Alaram_Min = int (input("set the Alaram minute"))


while( 1):
    if(Alaram_Hour == ds1307._read_hours() and Alaram_Min == ds1307._read_minutes()):
        print("alaram wake up")
	GPIO.output(LED,False)
	time.sleep(1)
        break


print("exited")


