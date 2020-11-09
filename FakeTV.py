# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:08:25 2020

@author: Maciej
"""

from yeelight import Bulb
from time import sleep
import datetime
import random


max_date = datetime.date(2020, 7, 1)
today = datetime.date.today()
print(f"maxdate: {max_date}")
print(f"today:{today}")
print(f"are we before max_date?:{today<max_date}") #is today BEFORE max_date?

dusk = datetime.time(19,00)
curr_time = datetime.datetime.now().time()
print(f"dusk:{dusk}")
print(f"curr_time:{curr_time}")
print(f"are we after dusk? {curr_time>dusk}") #are we AFTER DUSK?

dusk_plus = datetime.time(23,30)
print(f"dusk_plus:{dusk_plus}")
print(f"are we between dusk and dusk_plus? {(curr_time>dusk)&(curr_time<dusk_plus)}")

correct_date = today<max_date #TRUE

bulbR = Bulb("192.168.0.157")
bulbL = Bulb("192.168.0.45")

bulb_turned = False #simple flag

while(correct_date):
    
    curr_time = datetime.datetime.now().time()
    correct_time = (curr_time>dusk)&(curr_time<dusk_plus)
    sysRandom = random.SystemRandom()
    print('correct date') #heartbeat 
    if(correct_time):
        print(f'correct_time {curr_time}') #just for debug purpose
        if(not bulb_turned):
            bulbR.turn_on()
            bulbL.turn_on()
            bulb_turned = True

        #I want to change brightness more often
        bulbL.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)
        bulbR.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)            

        sleep(sysRandom.randint(1,3)) 
        
        bulbL.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)
        bulbR.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)
        
        sleep(sysRandom.randint(1,3))  
        
        #once a while new set of colors
        bulbL.set_rgb(sysRandom.randint(0,255),sysRandom.randint(0,255),sysRandom.randint(0,255))
        bulbR.set_rgb(sysRandom.randint(0,255),sysRandom.randint(0,255),sysRandom.randint(0,255))
    
        sleep(sysRandom.randint(1,5))  
        
        bulbL.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)
        bulbR.set_brightness(sysRandom.randint(0,70))
        sleep(0.5)
        
    else:
        bulbR.turn_off()
        bulbL.turn_off()
        bulb_turned = False
    sleep(sysRandom.randint(0,5))       
     
    correct_date = datetime.date.today()<max_date #check  





