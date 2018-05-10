#import timetest3
import multiprocessing
import time

time = time.localtime()
ticks = [time[0],time[1],time[2],time[3],time[4]]
#print(ticks)
print(ticks)

#result4 = firebase.post('/blom1',{'dur':'333'})  
#result5 = firebase.put('/blom1','dur',333)  

def duration(dur,tim,minut):
#    tim = 11
#    minut = 17
    delar = 2000/60
    timmar = 0
    minuter = 0
    antal_min = dur/delar          
    brak_tal = antal_min/60   
    if brak_tal >=1:  
        while brak_tal>=1:  
            brak_tal = brak_tal-1        
            timmar=timmar +1                
        
    else:  
        minuter = brak_tal * 60  
    minuter = brak_tal*60

#if minuter>59:
#    minuter = minuter - 1

    tim = tim + timmar
    minut = minut + minuter
    if minut>=59:
        minut = minut - 60
        tim = tim +1 
    minut = int(minut)
    nutid = [time[0],time[1],time[2],tim,minut]
    
    return nutid
    
nutid1 = duration(2000,12,00)
#nutid2 = duration(2000)
#nutid3 = duration(3000)


#nutid1 = [time[0],time[1],time[2],tim1,minut1]
print(nutid1)
#print(nutid2)
#print(nutid3)

#while True:
#    if ticks==nutid1:
#        print('yes yes yes')
    
#        break

