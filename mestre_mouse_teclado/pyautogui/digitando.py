import pyautogui
import pyperclip


def digitando():
    # x=422, y=551

    pyautogui.moveTo(x=422, y=551, duration=1.5)
    pyautogui.click()

    # pyautogui.typewrite('Automação é incrível !!') -> Não copia caracter especial

    def digitar_frase(frase):
        pyperclip.copy(frase)
        pyautogui.hotkey('ctrl', 'v')


    digitar_frase('Automação é incrível !!')


def combinacao_tecla():

    pyautogui.moveTo(x=422, y=551, duration=1.0)
    pyautogui.click()

    pyautogui.press('f12')

    # press
    pyautogui.keyDown('f12')
    pyautogui.keyUp('f12')

    # Combinação
    pyautogui.hotkey('ctrl', 'k', 'c')

if __name__ == "__main__":
    # digitando()
    # combinacao_tecla()
    pass