import pyautogui

while True:
    print(pyautogui.position())  # Mostra a posição do cursor (x, y)
    pyautogui.sleep(1)  # Atualiza a posição a cada 1 segundo
