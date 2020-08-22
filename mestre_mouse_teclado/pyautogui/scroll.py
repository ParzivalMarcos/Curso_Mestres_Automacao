import pyautogui
from time import sleep
# pyautogui.scroll(-10) para baixo
# pyautogui.scroll(10) para cima

pyautogui.moveTo(x=430, y=420, duration=1.5)

for i in range(10):
    pyautogui.scroll(-1000)
    sleep(0.5)
