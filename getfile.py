import timetest
from firebase import firebase
import time


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

while True:
    
        tid = time.gmtime()
        tid2 = (tid[0],tid[1],tid[2],tid[3],tid[4])
        tidblom1 = (tid[0],tid[1],tid[2],blom1_tid,blom1_min)
        tidblom2 = (tid[0],tid[1],tid[2],blom2_tid,blom2_min)
        tidblom3 = (tid[0],tid[1],tid[2],blom3_tid,blom3_min)

        if tid2==tidblom1:
            timetest.kruka_1()

        if tid2==tidblom2:
            timetest.kruka_2()

        if tid2==tidblom3:
            timetest.kruka_3()


       # time.sleep(100)
            
