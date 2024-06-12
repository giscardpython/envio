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

#pyautogui.hotkey('ctrl', 'k', 'ctrl', 'o', "'")
#time.sleep(5)

pyautogui.hotkey('ctrl', 'shift', "'")

pyautogui.write('git init .')
pyautogui.press('enter')

pyautogui.write('git add .')
pyautogui.press('enter')

pyautogui.write('git commit -m "Repositorio atualizado por automacao."')

# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)

# continua as instruções
pyautogui.press('enter')

pyautogui.write('git branch -M main')
pyautogui.press('enter')

pyautogui.write('git remote add origin http://github.com/giscardpython/envio.git')
pyautogui.press('enter')

pyautogui.write('git push -u origin main')
pyautogui.press('enter')
