# Crie um programa de automação que crie um repositório local 
# e envie para um repositório remoto do GitHub indicado pelo usuário.
# Ao terminar, gere um executável e envie.

# importa bibliotecas
import pyautogui
import time

# tempo que cada comando demora para executar
pyautogui.PAUSE = 1

# Ex: Repositorio remoto https://github.com/giscardpython/teste4.git
repositorio_remoto = str(input('Informe o repositório remoto do GitHub para onde devem ser enviados os arquivos: '))

pyautogui.hotkey('ctrl', 'k', 'ctrl', 'o', "'")

# espera 5 segundos para dar tempo de fazer a criação
time.sleep(15)

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

pyautogui.write('git branch -M main')
pyautogui.press('enter')

pyautogui.write('git remote add origin main', repositorio_remoto)
pyautogui.press('enter')

pyautogui.write('git push')
pyautogui.press('enter')