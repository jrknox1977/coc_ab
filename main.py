import pyautogui
import gi
import time
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from gi.repository import GObject
while True:
    elixer = pyautogui.locateOnScreen('images/elixer.png')
    print("elixer " + str(elixer))
    gold = pyautogui.locateOnScreen('images/gold.png')
    print("gold " + str(gold))
    if elixer is not None:
        pyautogui.click((elixer.left + 20), (elixer.top + 20))
        pyautogui.click((elixer.left + 20), (elixer.top + 20))
    if gold is not None:
        pyautogui.click((gold.left + 20), (gold.top + 20))
        pyautogui.click((gold.left + 20), (gold.top + 20))
    time.sleep(60)






