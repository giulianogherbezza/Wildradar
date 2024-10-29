import pandas as pd
import requests

# Excel-Datei und URL
EXCEL_FILE = "Unfaelle_KantonZH_bereinigt.xlsx"
API_URL = "http://localhost:1337/api/unfaelle-kanton-zhs"

# Excel-Datei laden
df = pd.read_excel(EXCEL_FILE)

# Header für die POST-Anfrage festlegen
headers = {
    "Content-Type": "application/json"
}

# Daten durchlaufen und jede Zeile senden
for index, row in df.iterrows():
    # Daten aus der Zeile in ein Dictionary konvertieren
    data = {
        "data": {
            "AccidentType": row["AccidentType"],  # Übereinstimmung mit Strapi-Feldnamen
            "AccidentSeverity": row["AccidentSeverity"],  # Übereinstimmung mit Strapi-Feldnamen
            "RoadType": row["RoadType"],  # Übereinstimmung mit Strapi-Feldnamen
            "Latitude": row["Latitude"],  # Übereinstimmung mit Strapi-Feldnamen
            "Longitude": row["Longitude"]  # Übereinstimmung mit Strapi-Feldnamen
            # "AccidentHour_Formatted": row["AccidentHour_Formatted"]  # Vorerst entfernt zum Testen
        }
    }

    # POST-Anfrage an die Strapi-API senden
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            print(f"Erfolgreich importiert: Zeile {index + 1}")
        else:
            print(f"Fehler beim Importieren von Zeile {index + 1}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Anfrage fehlgeschlagen bei Zeile {index + 1}: {e}")


