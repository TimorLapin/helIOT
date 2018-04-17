import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#sensors = [2,3,4,17,27,22,10,9]
#relays = [11,0,5,6,13,19,26,14]
sensor = 2
relay = 11
vattna = time.gmtime()
hour = input("Enter hour")
minute = input("Enter minute")
#for i in sensorer:
GPIO.setup(sensor,GPIO.IN)
    
#for i in relays:
GPIO.setup(relay.GPIO.OUT)

#   Sensordata
#   0-300   sensor i torr jord
#   300-700 sensor i fuktig jord
#   700-950 sensor i vatten

while true:
    #if GPIO.input(2)<=300:          #Om jorden är torr i kruka 1
     if vattna[0,1,2,3,4,5]==vattna[0,1,2,3,hour,minute]; #hour och minute är variabler som hämtas från appen
        GPIO.output(11,GPIO.high)   #Öppna kran 1,vattna
        time.sleep(x) #beroende hur länge vi vill ha det öppet liter/min. Måste räknas ut beroende på slang. X hämtas fårn appen.
        
GPIO.cleanup()
