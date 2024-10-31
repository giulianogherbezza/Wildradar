<template>
  <div>
    <h2>Willkommen auf der Karten-Seite!</h2>
    <p>Hier wird die Karte mit den Wildunfallstellen angezeigt.</p>
    <div id="map" style="height: 500px;"></div>
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
    };
  },
  methods: {
    async initializeMap() {
      // Standardkoordinaten für die Karte, falls Standort nicht zugelassen wird
      const defaultCoords = [47.3769, 8.5417]; // Zürich

      // Karte initialisieren
      this.map = L.map("map").setView(defaultCoords, 13);

      // OpenStreetMap Layer hinzufügen
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);

      // Benutzerposition ermitteln
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.userLatLng = [
              position.coords.latitude,
              position.coords.longitude,
            ];
            this.map.setView(this.userLatLng, 13);

            // Benutzer-Icon definieren und auf der Karte hinzufügen
            const userLocationIcon = L.icon({
              iconUrl: require("@/assets/leaflet/marker-icon.png"),
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
            });

            L.marker(this.userLatLng, { icon: userLocationIcon })
              .addTo(this.map)
              .bindPopup("Ihr Standort")
              .openPopup();

            // Wildunfallstellen laden
            this.fetchAllAccidentLocations();
          },
          () => {
            // Fehlerbehandlung, wenn Standort nicht zugelassen wird
            console.error(
              "Standortzugriff verweigert oder nicht verfügbar. Verwende Standardkoordinaten."
            );
            this.fetchAllAccidentLocations();
          }
        );
      } else {
        console.error("Geolocation wird von diesem Browser nicht unterstützt.");
        this.fetchAllAccidentLocations();
      }
    },
    async fetchAllAccidentLocations() {
      let allData = [];
      let page = 1;
      const pageSize = 100;
      let hasMore = true;

      try {
        while (hasMore) {
          const response = await axios.get("http://localhost:1337/api/unfaelle-kanton-zhs", {
            params: {
              pagination: {
                page,
                pageSize,
              },
            },
          });

          const data = response.data.data;
          allData = allData.concat(data);

          const { pageCount } = response.data.meta.pagination;
          hasMore = page < pageCount;
          page += 1;
        }

        console.log("API-Daten erfolgreich geladen:", allData);

        // Iteriere über die erhaltenen Unfall-Daten
        allData.forEach((accident) => {
          const { Latitude, Longitude, AccidentType, AccidentSeverity, RoadType } = accident;

          if (Latitude != null && Longitude != null) {
            const accidentLatLng = [parseFloat(Latitude), parseFloat(Longitude)];

            const accidentLocationIcon = L.icon({
              iconUrl: require("@/assets/leaflet/marker-icon.png"),
              iconSize: [25, 41],
              iconAnchor: [12, 41],
              popupAnchor: [1, -34],
            });

            L.marker(accidentLatLng, { icon: accidentLocationIcon })
              .addTo(this.map)
              .bindPopup(
                `<b>Unfalltyp:</b> ${AccidentType}<br>
                <b>Schwere:</b> ${AccidentSeverity}<br>
                <b>Strassentyp:</b> ${RoadType}`
              );
          } else {
            console.warn("Unfall-Daten ohne Koordinaten gefunden:", accident);
          }
        });
      } catch (error) {
        console.error("Fehler beim Laden der Unfall-Daten:", error);
      }
    },
  },
  mounted() {
    this.initializeMap();
  },
};
</script>

<style scoped>
div {
  text-align: center;
  margin-top: 20px;
  font-family: Arial, sans-serif;
}

#map {
  width: 100%;
  height: 500px;
  margin-top: 20px;
}
</style>
