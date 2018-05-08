import timetest
from firebase import firebase
import time
import multiprocessing # eller multithreading


def get_data()
    firebase = firebase.FirebaseApplication('https://heliot-f77cc.firebaseio.com/')
    blom1_tid = firebase.get('/blom1','tim')
    blom1_min = firebase.get('/blom1','min')
    blom1_dur = firebase.get('/blom1','dur')

    blom2_tid = firebase.get('/blom2','tim')
    blom2_min = firebase.get('/blom2','min')
    blom2_dur = firebase.get('/blom2','dur')

    blom3_tid = firebase.get('/blom3','tim')
    blom3_min = firebase.get('/blom3','min')
    blom3_dur = firebase.get('/blom3','dur')

#result4 = firebase.post('/blom1',{'dur':'333'})
#result5 = firebase.put('/blom1','dur',333)

print(blom1_tid,blom1_min,blom1_dur)

# Om vi antar att 1,5 lit/tim (1500ml/60min eller 25ml/min) kommer från varje munstyck
# För enkelhetens skull anta att vi har en munstyck per planta. Två munstyck = 3000ml/tim = 50ml/min

def duration(dur)                   # ex. dur = 2000
    antal_min = dur/25 = 80         # Man vill vattna med exempelvis 2000 ml
    brak_tal = 80/60 = 1,33
    
    if brak_tal >1
        while brak_tal>1
            brak_tal = brak_tal-1       # 1,33 - 1 = 0,33
            timmar+=1                   # timmmar = 1
        minuter = brak_tal * 60         # minuter = 20
    else 
        minuter = brak_tal * 60
        
        
# Det vi får här är, 1 timme och 20 min. Tiden som vi vill ha en ventil öppen. Som vi sedan ställer mot vår time-funktion.
# Om vi använder multiprocessing/multithreading då kan vi ha en delay i varje funktion på det antal sekunder som motsvarar bevattningen. 
# ex. om dur = 1500ml/tim då blir delay = 3600 sekunder. Dela med 25, sen gånger 60


while True:
    
        tid = time.asctime()
        tid2 = (tid[0],tid[1],tid[2],tid[3],tid[4])
        tidblom1 = (tid[0],tid[1],tid[2],blom1_tid,blom1_min)
        tidblom2 = (tid[0],tid[1],tid[2],blom2_tid,blom2_min)
        tidblom3 = (tid[0],tid[1],tid[2],blom3_tid,blom3_min)

        if tid2==tidblom1:
            k = multiprocessing.Process(target=timetest.kruka_1, args(blom1_dur,))
            k.start()
            #k.join()
            avisering = firebase.put('/blom1','dur',tid)    # Avisering efter senaste bevattning
            
        if tid2==tidblom2:
            k = multiprocessing.Process(target=timetest.kruka_2, args(blom2_dur,))            
            k.start()            
            #k.join()
            avisering = firebase.put('/blom1','dur',tid)    # Avisering efter senaste bevattning
        
        if tid2==tidblom3:
            k = multiprocessing.Process(target=timetest.kruka_3, args(blom3_dur,))            
            k.start()            
            #k.join()
            avisering = firebase.put('/blom1','dur',tid)    # Avisering efter senaste bevattning
        
        get_data()                          # Hämta data igen
       
            
