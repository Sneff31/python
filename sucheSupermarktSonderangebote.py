import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Konfiguriere die Chrome-Optionen (optional)
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # Läuft im Hintergrund ohne UI (für Performance und Automation)

# Starte den Chrome-Browser mit dem WebDriver
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

class AngebotScrapper:

    # URL der Webseite, die du scrapen möchtest
    #url = "https://www.rewe.de/angebote/nationale-angebote/"  # Ersetze dies mit der Ziel-URL
    baseURLAldi = "https://www.aldi-nord.de"
    urlAngebotAldi = "/angebote.html"
    

    def __init__(self):
        self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.aldiAngbote = {}


    def _load_webside(self,baseURL,urlPath):
        
        # Lade die Webseite
        self.__driver.get(baseURL+urlPath)

        last_height = self.__driver.execute_script("return document.body.scrollHeight")

        new_height = 0

        while True:

            # Scrolle nach unten
            print(new_height)
            self.__driver.execute_script("window.scrollTo(0, " + str(new_height) + ");")
    
            # Warte ein bisschen, damit mehr Inhalte geladen werden können
            time.sleep(3)
    
            # Breche ab, wenn das Ende der Seite erreicht ist
            
            if not new_height <= last_height:
                # Warte kurz, um sicherzustellen, dass die Seite vollständig geladen ist (insbesondere JavaScript-Inhalte)
                time.sleep(10)  # Passe die Zeit je nach Webseite an
                break
            # Berechne die neue Höhe der Seite
            new_height = new_height + 3000

        return self.__driver.page_source

    def scrapp_aldi(self):

        html_content = self._load_webside(self.baseURLAldi,self.urlAngebotAldi)

        # Extrahiere den HTML-Inhalt der Seite

        #with open('webcontent.txt','w', encoding="utf-8") as datei:
        #    datei.write(str(html_content))

         # Parsen des HTML-Inhalts der Seite
        soup = BeautifulSoup(html_content, "html.parser")

        # Beispiel: Finden der Sonderangebote, dies kann je nach Website-Struktur variieren
        # Hier gehen wir davon aus, dass die Sonderangebote in einem bestimmten HTML-Tag sind
        sonderangebote = soup.find_all("div", class_="mod-article-tile")

        # Durchlaufen der gefundenen Sonderangebote und Ausgeben
        for angebot in sonderangebote:
        # Extrahieren des Namens und Preises
            name = angebot.find("span", class_="mod-article-tile__title")
            link = angebot.find("a")
            #preis = angebot.find("div", class_="cor-offer-price__tag-price")

            #if name and preis:
            #    print(f"Angebot: {name.get_text(strip=True)} - Preis: {preis.get_text(strip=True)}")

            if name:
                print(f"Angebot: {name.get_text(strip=True)} - Link: {link.get('href')}")


scrapper = AngebotScrapper()
scrapper.scrapp_aldi()