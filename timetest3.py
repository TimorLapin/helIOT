import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor_1 = 2
sensor_2 = 3
sensor_3 = 4
temp = 9
GPIO.setup(sensor_1, GPIO.IN)
GPIO.setup(sensor_2, GPIO.IN)
GPIO.setup(sensor_3, GPIO.IN)
GPIO.setup(temp, GPIO.IN)

ventil_1 = 17
ventil_2 = 27
ventil_3 = 22
hventil = 10

GPIO.setup(ventil_1, GPIO.OUT)
GPIO.setup(ventil_2, GPIO.OUT)
GPIO.setup(ventil_3, GPIO.OUT)
GPIO.setup(hventil, GPIO.OUT)

#os.system('cls')

x=0
y=0
print('ok')

#while True:                             #Nödfall. Om jättetorrt, vattna!
if GPIO.input(sensor_1)==0:
                GPIO.output(ventil_1,1)
                GPIO.output(hventil,1)
                #delay
if GPIO.input(sensor_2)==0:
                GPIO.output(vetil_2,1)
                GPIO.output(hventil,1)
                #delay
if GPIO.input(sensor_3)==0:
                GPIO.output(ventil_3,1)
                GPIO.output(hventil,1)
                #delay


def kruka_1(dur):


        GPIO.output(ventil_1,1)
        GPIO.output(hventil,1)
                time.sleep(dur)
               
        GPIO.output(ventil_1,0)        
        GPIO.output(hventil,0)
        
def kruka_2(dur):


        GPIO.output(ventil_2,1)
        GPIO.output(hventil,1)
      
        time.sleep(dur)
        
        GPIO.output(ventil_2,0)        
        GPIO.output(hventil,0)
      
                
def kruka_3(dur):


        GPIO.output(ventil_3,1)
        GPIO.output(hventil,1)
      
        time,sleep(dur)
        
        GPIO.output(ventil_3,0)        
        GPIO.output(hventil,0)

