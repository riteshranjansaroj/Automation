import pyautogui as pg
import time
import random

#for know msg location
#time.sleep(10)
#print(pg.position())

n=int(input("Enter no of times:"))
time.sleep(10)
msg_list=['hi','hlo']
#pg.click(x=1524,y=814) 
for i in range(n):
    time.sleep(1)
    #pg.click(x=1576,y=922)
    pg.write(random.choice(msg_list),interval=0.05)
    pg.press("enter")
    print(i)