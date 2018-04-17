import RPi.GPIO as GPIO
import time

vattna = time.gmtime()
vattna[0,1,2,3,4,5] or vattna[year,mounth,day,hour, minute]
#om vi lägger in två variabler hour och minute så ka vi få vattna[0,1,2,3,hour,minute]
hour=input()
minute=input()
vattna[0,1,2,3,hour,minute] # Kan användas som en timer för bevattning?

GPIO.setmode(GPIO.BCM)

#sensors = [2,3,4,17,27,22,10,9]
#relays = [11,0,5,6,13,19,26,14]
sensor = 2
relay = 11
#for i in sensorer:
GPIO.setup(sensor,GPIO.IN)
    
#for i in relays:
GPIO.setup(relay.GPIO.OUT)

#   Sensordata
#   0-300   sensor i torr jord
#   300-700 sensor i fuktig jord
#   700-950 sensor i vatten

while true:
    if GPIO.input(2)<=300:          #Om jorden är torr i kruka 1
    if vattna[0,1,2,3,4,5]==vattna[0,1,2,3,hour,minute]:
        GPIO.output(11,GPIO.high)   #Öppna kran 1,vattna
   
        
GPIO.cleanup()
