import requests

# URL der Webseite, die du anfragen möchtest
url = "https://www.rewe.de/"  # Ersetze dies mit der gewünschten URL

# HTTP GET-Anfrage an die Webseite senden
response = requests.get(url)
print(response.content)
# Überprüfen, ob die Anfrage erfolgreich war (Status-Code 200)
if response.status_code == 200:
    print("Erfolgreich verbunden!")
    # Den HTML-Inhalt der Seite ausgeben
    html_content = response.text  # HTML-Inhalt der Seite
    #print(html_content)  # Gib den HTML-Inhalt aus
else:
    print(f"Fehler beim Abrufen der Seite. Status-Code: {response.status_code}")