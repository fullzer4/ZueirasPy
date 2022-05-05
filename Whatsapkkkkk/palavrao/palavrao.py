import pyautogui as pg
import time
contador = 0
time.sleep(10)

txt = open("palavrao.txt","r")
for i in txt:
    pg.write(i)
    pg.press("Enter")
    contador + 1
    