<template>
  <div id="map-container">
    <div id="controls">
      <label for="location-select">Wählen Sie einen Standort:</label>
      <select
        id="location-select"
        v-model="selectedLocation"
        @change="setLocation"
      >
        <option value="location1">Standort 1 (Zürich Altstadt)</option>
        <option value="location2">Standort 2 (Zürich Enge)</option>
        <option value="location3">Standort 3 (Zürich Oerlikon)</option>
        <option value="location4">Standort 4 (Zürich Seebach)</option>
        <option value="location5">Standort 5 (Zürich Wollishofen)</option>
        <option value="location6">Standort 6 (Zürich Wiedikon)</option>
        <option value="location7">Standort 7 (Zürich Leimbach)</option>
        <option value="location8">Standort 8 (Zürich Affoltern)</option>
        <option value="location9">Standort 9 (Zürich Albisrieden)</option>
        <option value="location10">Standort 10 (Zürich Schwamendingen)</option>
        <option value="location11">Standort 11 (Zürich Wipkingen)</option>
        <option value="location12">Standort 12 (Zürich Höngg)</option>
        <option value="location13">Standort 13 (Zürich Seefeld)</option>
        <option value="location14">Standort 14 (Zürich Fluntern)</option>
        <option value="location15">Standort 15 (Zürich Hottingen)</option>
        <option value="location16">Standort 16 (Zürich Oberstrass)</option>
        <option value="location17">Standort 17 (Zürich Unterstrass)</option>
        <option value="location18">Standort 18 (Zürich Friesenberg)</option>
        <option value="location19">Standort 19 (Zürich Hirzenbach)</option>
        <option value="location20">Standort 20 (Zürich Albisguetli)</option>
      </select>
    </div>
    <div id="map"></div>
  </div>
</template>

<script>
import axios from "axios";
import L from "leaflet";

export default {
  name: "MapPage",
  data() {
    return {
      map: null,
      userLatLng: null,
      allAccidentData: [], // Alle Unfalldaten speichern
      selectedLocation: "location1", // Standardauswahl für den ersten Standort in Zürich
      zurichLocations: {
        location1: [47.37174, 8.54226], // Zürich Altstadt
        location2: [47.36593, 8.53298], // Zürich Enge
        location3: [47.41031, 8.54419], // Zürich Oerlikon
        location4: [47.42349, 8.55076], // Zürich Seebach
        location5: [47.34758, 8.53283], // Zürich Wollishofen
        location6: [47.36151, 8.51906], // Zürich Wiedikon
        location7: [47.33453, 8.53379], // Zürich Leimbach
        location8: [47.42342, 8.51213], // Zürich Affoltern
        location9: [47.37885, 8.49478], // Zürich Albisrieden
        location10: [47.39705, 8.56838], // Zürich Schwamendingen
        location11: [47.39319, 8.52933], // Zürich Wipkingen
        location12: [47.40021, 8.50349], // Zürich Höngg
        location13: [47.35544, 8.55863], // Zürich Seefeld
        location14: [47.37778, 8.56633], // Zürich Fluntern
        location15: [47.36933, 8.55221], // Zürich Hottingen
        location16: [47.38316, 8.54896], // Zürich Oberstrass
        location17: [47.38822, 8.54259], // Zürich Unterstrass
        location18: [47.36507, 8.51501], // Zürich Friesenberg
        location19: [47.40304, 8.58292], // Zürich Hirzenbach
        location20: [47.33599, 8.51431], // Zürich Albisguetli
      },
    };
  },
  methods: {
    async initializeMap() {
      // Standardkoordinaten für die Karte, falls Standort nicht zugelassen wird
      const defaultCoords = this.zurichLocations["location1"]; // Zürich Altstadt

      // Karte initialisieren
      this.map = L.map("map").setView(defaultCoords, 13);

      // OpenStreetMap Layer hinzufügen
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);

      // Benutzerposition ermitteln (mit Dropdown zum Simulieren)
      this.setLocation();

      // Wildunfallstellen laden
      this.fetchAllAccidentLocations();
    },
    setLocation() {
      // Setzt den Standort basierend auf der Auswahl im Dropdown-Menü
      this.userLatLng = this.zurichLocations[this.selectedLocation];
      this.map.setView(this.userLatLng, 13);

      // Benutzer-Icon definieren und auf der Karte hinzufügen
      this.checkAccidentDensity(); // Überprüfen der Unfallanzahl im Umkreis
    },
    async fetchAllAccidentLocations() {
      let allData = [];
      let page = 1;
      const pageSize = 100;
      let hasMore = true;

      try {
        while (hasMore) {
          const response = await axios.get(
            "http://localhost:1337/api/unfaelle-kanton-zhs",
            {
              params: {
                pagination: {
                  page,
                  pageSize,
                },
              },
            }
          );

          const data = response.data.data;
          allData = allData.concat(data);

          const { pageCount } = response.data.meta.pagination;
          hasMore = page < pageCount;
          page += 1;
        }

        // Filtere die Standorte, um nur die relevanten aus dem Kanton Zürich auszuwählen
        const filteredData = allData.filter((accident) => {
          const { Latitude, Longitude } = accident;
          return (
            Latitude != null &&
            Longitude != null &&
            parseFloat(Latitude) >= 47.0 &&
            parseFloat(Latitude) <= 47.7 &&
            parseFloat(Longitude) >= 8.4 &&
            parseFloat(Longitude) <= 8.7
          );
        });

        console.log("Gefilterte API-Daten erfolgreich geladen:", filteredData);
        this.allAccidentData = filteredData; // Speichere alle Unfalldaten für die Radiusprüfung
      } catch (error) {
        console.error("Fehler beim Laden der Unfall-Daten:", error);
      }
    },
    checkAccidentDensity() {
      let accidentCount = 0;

      // Iteriere über die erhaltenen Unfall-Daten und überprüfe, ob sie im Radius sind
      this.allAccidentData.forEach((accident) => {
        const accidentLatLng = [
          parseFloat(accident.Latitude),
          parseFloat(accident.Longitude),
        ];
        const distance = this.calculateDistance(
          this.userLatLng,
          accidentLatLng
        );
        if (distance <= 750) {
          accidentCount++;
        }
      });

      // Setze die Markerfarbe basierend auf der Anzahl der Unfälle im Radius
      let markerColor = "green";
      if (accidentCount > 4) {
        markerColor = "red";
      } else if (accidentCount > 2) {
        markerColor = "yellow";
      }

      // Benutzer-Icon definieren und auf der Karte hinzufügen
      const userLocationIcon = L.icon({
        iconUrl: require(`@/assets/leaflet/marker-icon-${markerColor}.png`),
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
      });

      // Benutzer-Icon hinzufügen (neues Icon mit Farbe)
      L.marker(this.userLatLng, { icon: userLocationIcon }).addTo(this.map);
      /* .bindPopup("Ihr Standort")
        .openPopup(); */
    },
    calculateDistance(coord1, coord2) {
      const [lat1, lon1] = coord1;
      const [lat2, lon2] = coord2;

      const R = 6371e3; // Radius der Erde in Metern
      const φ1 = (lat1 * Math.PI) / 180; // φ, λ in radians
      const φ2 = (lat2 * Math.PI) / 180;
      const Δφ = ((lat2 - lat1) * Math.PI) / 180;
      const Δλ = ((lon2 - lon1) * Math.PI) / 180;

      const a =
        Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
        Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

      const distance = R * c; // in meters
      return distance;
    },
  },
  mounted() {
    this.initializeMap();
  },
};
</script>
<style scoped>
/* Allgemeiner Container für die Karte und Steuerung */
#map-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  padding: 20px;
}

/* Bereich für die Steuerelemente */
#controls {
  margin-bottom: 15px;
  text-align: center;
  background-color: #ffffff;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Dropdown-Label */
#controls label {
  font-size: 16px;
  font-weight: bold;
  margin-right: 10px;
  color: #333333;
}

/* Dropdown-Liste */
#location-select {
  padding: 8px 12px;
  font-size: 14px;
  border: 1px solid #dddddd;
  border-radius: 4px;
  background-color: #ffffff;
  color: #333333;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  outline: none;
  transition: border-color 0.3s ease;
}

/* Dropdown-Hover und Fokus */
#location-select:hover,
#location-select:focus {
  border-color: #007bff;
}

/* Kartenbereich */
#map {
  width: 100%;
  height: 500px;
  border: 2px solid #dddddd;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
