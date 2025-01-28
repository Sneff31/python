import requests
from bs4 import BeautifulSoup
import time

# Die Funktion zum Crawlen einer einzelnen Webseite
def crawl(url, visited):
    if url in visited:
        return
    print(f"Besuche: {url}")
    visited.add(url)  # Markiere die URL als besucht

    try:
        # Hole die Webseite
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Seite {url}, Statuscode: {response.status_code}")
            return

        # Parse den HTML-Inhalt der Seite
        soup = BeautifulSoup(response.text, 'html.parser')

        print("My Soap Content: ")
        print(soup)
        print("My Soap Content End")

        # Extrahiere alle Links auf der Seite
        links = soup.find_all(class_="pcVideoListItem js-pop videoblock videoBox")

        print("My Soap Content: ")
        print(links)
        # print("My Soap Content End")

        for link in links:
            href = link['href']
            # Normalisiere die URL (füge Basis-URL hinzu, wenn nötig)
            full_url = requests.compat.urljoin(url, href)

            # Rufe die Webseite rekursiv auf
            if full_url.startswith("http") and full_url not in visited:
                crawl(full_url, visited)
            myInput = input("Zum Beenden exit tippen")  # Vermeide zu viele Anfragen in kurzer Zeit

            if myInput.upper() == "exit":
                break

    except Exception as e:
        print(f"Fehler beim Crawlen der Seite {url}: {e}")

# Hauptfunktion zum Starten des Crawlers
def start_crawl(start_url):
    visited = set()  # Set zum Speichern der bereits besuchten URLs
    crawl(start_url, visited)

# Starte den Crawler mit einer Start-URL
if __name__ == "__main__":
    start_url = 'https://www.youtube.com/'  # Ersetze dies mit der URL, die du crawlen möchtest
    start_crawl(start_url)