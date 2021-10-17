import pyautogui
from pyautogui import press, write, click, position
import time
token = input('Digite o token aqui:')
pyautogui.PAUSE = 0.7

press('win')
write('Opera GX')
press('enter')

write('https://poocoin.app')
press('enter')
#Botão para selecionar a caixa de texto do endereço/nome do token
time.sleep(1)
click(x=993, y=616)
write(token)
#Botão de seleção do token
time.sleep(0.5)
click(x=995, y=679)
#Botão do trade
click(x=1451, y=216)
click(x=1012, y=507)
'''time.sleep(5)
position()
print(position())'''