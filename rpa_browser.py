import time
import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Starte den Browser und öffne die Webseite
def open_browser():
    # Lade den Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com")  # Ersetze dies durch die Ziel-URL
    time.sleep(2)  # Warte 2 Sekunden, bis die Seite geladen ist
    return driver

# 2. Navigiere und klicke auf bestimmte Elemente der Webseite
def navigate_website(driver):
    try:
        # Beispiel: Finde ein Element und klicke darauf (z.B. ein Button)
        button = driver.find_element(By.ID, "submit_button")  # Beispiel-ID
        button.click()
        time.sleep(2)
    except Exception as e:
        print(f"Fehler beim Navigieren: {e}")

# 3. Extrahiere Daten von der Webseite
def extract_data(driver):
    try:
        # Extrahiere Text oder andere Daten von der Webseite
        extracted_data = []
        items = driver.find_elements(By.CLASS_NAME, "data-class")  # Beispiel-Selektor
        for item in items:
            extracted_data.append(item.text)
        return extracted_data
    except Exception as e:
        print(f"Fehler beim Extrahieren von Daten: {e}")
        return []

# 4. Speichere die extrahierten Daten in einer CSV-Datei
def save_to_csv(data):
    df = pd.DataFrame(data, columns=["Extracted Data"])
    df.to_csv("extracted_data.csv", index=False)
    print("Daten wurden erfolgreich gespeichert!")

# 5. Steuere die Maus und die Tastatur (z.B. Interaktion mit einer Desktop-Anwendung)
def automate_desktop_task():
    pyautogui.click(100, 200)  # Klick an Koordinaten (X=100, Y=200)
    pyautogui.typewrite("Hallo Welt!", interval=0.1)  # Tippe Text mit Verzögerung
    pyautogui.press("enter")  # Drücke die Eingabetaste

def main():
    # Schritt 1: Starte den Browser und öffne die Webseite
    driver = open_browser()

    # Schritt 2: Navigiere auf der Webseite
    navigate_website(driver)

    # Schritt 3: Extrahiere die benötigten Daten
    data = extract_data(driver)

    # Schritt 4: Speichere die extrahierten Daten in einer CSV-Datei
    save_to_csv(data)

    # Schritt 5: Automatisiere eine Desktop-Anwendung
    automate_desktop_task()

    # Schließe den Browser
    driver.quit()

if __name__ == "__main__":
    main()