import pyautogui
import time

# Wartezeit, um sicherzustellen, dass das Ziel geöffnet ist
time.sleep(3)

# Beispiel: Mausposition ansteuern und klicken
# Koordinaten auf dem Bildschirm (x=100, y=200)
pyautogui.click(x=100, y=200)

# Beispiel: Tastatureingabe simulieren
pyautogui.write('Hallo, dies ist eine RPA-Automatisierung!', interval=0.1)

# Beispiel: Mausbewegung zu einer anderen Position und klicken
pyautogui.moveTo(400, 400, duration=1)
pyautogui.click()

# Beispiel: Screenshot machen
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

print("RPA-Skript wurde ausgeführt!")