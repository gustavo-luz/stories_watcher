import pyautogui
import time
from time import sleep
print(pyautogui.size())

# TODO future use this https://pypi.org/project/webbot/
#pyautogui.moveTo(344,54, duration = 10)

#pyautogui.moveRel(0, 50, duration = 1)
sleep(2)
print(pyautogui.position())


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
pyautogui.click(237,204)
print("início do bot")
sleep(4)

#user input
"""
num_cliques = input("Quantas vezes quer clicar?")
print(num_cliques + " vezes")
num_cliques = int(num_cliques)
print(type(num_cliques))
"""
num_cliques = 15

#counter
contador = 1
# início de assistir os stories
while num_cliques > contador > 0:
    sleep(1.5)
    pyautogui.click(882, 407)
    print("cliques",contador)
    contador = contador + 1
    

