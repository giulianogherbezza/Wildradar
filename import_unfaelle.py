import pandas as pd
import requests
import time

# Datei und Strapi-API-URL
EXCEL_FILE = "Unfaelle_KantonZH_bereinigt_neu.xlsx"
API_URL = "http://localhost:1337/api/unfaelle-kanton-zhs"  # Passe den Endpunkt an die neue Collection an

# Excel-Datei laden
df = pd.read_excel(EXCEL_FILE)

# Funktion zum Importieren eines Batches von Daten
def import_batch(data_batch):
    for index, data in enumerate(data_batch):
        try:
            # POST-Anfrage an die Strapi-API senden
            response = requests.post(API_URL, json=data)
            if response.status_code == 200 or response.status_code == 201:
                print(f"Erfolgreich importiert: Zeile {index + 1}")
            else:
                print(f"Fehler beim Importieren von Zeile {index + 1}: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Anfrage fehlgeschlagen bei Zeile {index + 1}: {e}")
        time.sleep(0.1)  # Eine kurze Pause, um die Serverlast zu reduzieren

# Daten vorbereiten und in Batches importieren
BATCH_SIZE = 20
data_batch = []

for index, row in df.iterrows():
    # Daten aus der Zeile in ein Dictionary konvertieren
    data = {
        "data": {
            "AccidentType": row["AccidentType"],
            "AccidentSeverity": row["AccidentSeverity"],
            "RoadType": row["RoadType"],
            "AccidentHour_Formatted": row["AccidentHour_Formatted"],
            "Latitude": row["Latitude"],
            "Longitude": row["Longitude"]
        }
    }
    data_batch.append(data)

    # Sobald der Batch voll ist, importieren wir die Daten
    if len(data_batch) == BATCH_SIZE:
        print(f"Importiere Zeilen {index + 1 - BATCH_SIZE + 1} bis {index + 1}")
        import_batch(data_batch)
        data_batch = []

# Wenn noch Daten übrig sind, diese auch importieren
if len(data_batch) > 0:
    print(f"Importiere verbleibende Zeilen {len(df) - len(data_batch) + 1} bis {len(df)}")
    import_batch(data_batch)

