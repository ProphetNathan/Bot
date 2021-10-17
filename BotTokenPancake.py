from pyautogui import press, write, position, click
import pyautogui
import time
token = input('Digite o contrato aqui: ')
pyautogui.PAUSE = 0.7
press('win')
write('Opera GX')
press('enter')

write('https://pancakeswap.finance/swap')
press('enter')
'''time.sleep(0.3)
posição para colocar o valor máximo
click(x=1008, y=411)'''
#Botão selecionar moeda
time.sleep(0.5)
click(x=1035, y=554)

write(token)

#Botão import
time.sleep(1.5)
click(x=1086, y=510)

#Botão "I understand"
time.sleep(0.5)
click(x=792, y=777)

#Botão import dentro do "I undestand"
time.sleep(0.5)
click(x=1069, y=778)
time.sleep(5)
position()
print(position())
