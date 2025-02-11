import pyautogui

print("Mova o mouse e pressione Ctrl + C para sair.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição do cursor: X={x}, Y={y}", end="\r")
except KeyboardInterrupt:
    print("\nPrograma encerrado.")
