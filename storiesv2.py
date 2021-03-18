import pyautogui
import time
from time import sleep
#print(pyautogui.size())

# TODO future use this https://pypi.org/project/webbot/
#pyautogui.moveTo(344,54, duration = 10)

#pyautogui.moveRel(0, 50, duration = 1)
sleep(2)
#print(pyautogui.position())

#user input

num_cliques = input("How many stories?")
print(num_cliques + " times")
num_cliques = int(num_cliques)
#print(type(num_cliques))


#open microsoft edge
pyautogui.click(503, 749)
sleep(10)

#open search bar
pyautogui.click(211,58)
pyautogui.typewrite("instagram.com")
#open instagram
pyautogui.click(212,94)
sleep(8)



#open first stories
pyautogui.hotkey("tab", "enter")
#pyautogui.click(237,204)
print("Bot starting")
sleep(4)



#num_cliques = 100

#counter
contador = 1
# início de assistir os stories
while num_cliques > contador > 0:
    sleep(0.7)
    pyautogui.hotkey("right")
    #pyautogui.click(882, 407)
    print("cliques",contador)
    contador = contador + 1
    