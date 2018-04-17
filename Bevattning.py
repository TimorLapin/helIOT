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

        
GPIO.cleanup()
