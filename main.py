# Crie um programa de automação que crie um repositório local 
# e envie para um repositório remoto do GitHub indicado pelo usuário.
# Ao terminar, gere um executável e envie.

# importa bibliotecas
import pyautogui
import time

# tempo que cada comando demora para executar
pyautogui.PAUSE = 1

# continua git pushas instruções

valor = str(input('Informe o repositório remoto do GitHub para onde devem ser enviados elo usuário: '))

pyautogui.hotkey('ctrl', 'k', "'")
pyautogui.hotkey('ctrl', 'o', "'")

pyautogui.hotkey('ctrl', 'shift', "'")

pyautogui.write('git init .')
pyautogui.press('enter')
pyautogui.write('git add .')
pyautogui.press('enter')
pyautogui.write('git commit -m "Repositório atualizado por automação."')
# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)
# continua as instruções
pyautogui.press('enter')
pyautogui.write('git push')