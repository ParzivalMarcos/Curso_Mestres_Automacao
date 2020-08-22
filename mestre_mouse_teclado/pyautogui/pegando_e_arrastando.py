import pyautogui

# 716,460
# 950,823

for i in range(10):
    # Indo para a pasta A
    pyautogui.moveTo(x=716, y=460, duration=1.5)

    # Movendo para a pasta B
    pyautogui.dragTo(x=950, y=823, duration=1.5, button='left')
