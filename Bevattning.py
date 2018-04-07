import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

sensors = [2,3,4,17,27,22,10,9]
relays = [11,0,5,6,13,19,26,14]

for i in sensorer:
    GPIO.setup(i,GPIO.IN)
    
for i in relays:
    GPIO.setup(i.GPIO.OUT)

#   Sensordata
#   0-300   sensor i torr jord
#   300-700 sensor i fuktig jord
#   700-950 sensor i vatten

while true:
    if GPIO.input(2)<=300:          #Om jorden är torr i kruka 1
        GPIO.output(11,GPIO.high)   #Öppna kran 1,vattna
    if GPIO.input(3)<=300:          #Om jorden är torr i kruka 2
        GPIO.output(0,GPIO.high)    #Öppna kran 2,vattna
    if GPIO.input(4)<=300:          #Om jorden är torr i kruka 3
        GPIO.output(5,GPIO.high)    #Öppna kran 3,vattna
    if GPIO.input(17)<=300:         #Om jorden är torr i kruka 4
        GPIO.output(6,GPIO.high)    #Öppna kran 4,vattna
    if GPIO.input(27)<=300:         #Om jorden är torr i kruka 5
        GPIO.output(13,GPIO.high)   #Öppna kran 5,vattna
    if GPIO.input(22)<=300:         #Om jorden är torr i kruka 6
        GPIO.output(19,GPIO.high)   #Öppna kran 6,vattna
    if GPIO.input(10)<=300:         #Om jorden är torr i kruka 7
        GPIO.output(26,GPIO.high)   #Öppna kran 7,vattna
    if GPIO.input(9)<=300:          #Om jorden är torr i kruka 8
        GPIO.output(14,GPIO.high)   #Öppna kran 8,vattna
        
GPIO.cleanup()
