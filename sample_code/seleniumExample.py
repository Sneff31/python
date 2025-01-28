from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Konfiguriere die Chrome-Optionen (optional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Läuft im Hintergrund ohne UI (für Performance und Automation)

# Starte den Chrome-Browser mit dem WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL der Webseite, die du scrapen möchtest
url = "https://www.rewe.de/"  # Ersetze dies mit der Ziel-URL

# Lade die Webseite
driver.get(url)

# Warte kurz, um sicherzustellen, dass die Seite vollständig geladen ist (insbesondere JavaScript-Inhalte)
time.sleep(5)  # Passe die Zeit je nach Webseite an

# Extrahiere den HTML-Inhalt der Seite
html_content = driver.page_source

print(type(html_content))

# Jetzt kannst du BeautifulSoup verwenden, um den HTML-Inhalt zu parsen, wie bei statischen Seiten
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

print(type(soup))

# Beispiel: Alle Links auf der Seite extrahieren
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Schließe den Browser
driver.quit()