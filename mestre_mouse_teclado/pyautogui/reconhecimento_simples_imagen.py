import pyautogui

print(pyautogui.locateOnScreen('number_5.png'))
centro_da_imagem = pyautogui.locateCenterOnScreen('number_5.png')

print(type(centro_da_imagem))
print(centro_da_imagem)
# pyautogui.click(centro_da_imagem, duration=2)