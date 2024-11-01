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
      accidentLocations: [], // Unfallstellen werden hier gespeichert
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

            // Wildunfallstellen laden
            this.fetchAllAccidentLocations().then(() => {
              // Benutzer-Icon definieren und Radius überprüfen
              this.updateUserMarkerWithRadius();
            });
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

        // Unfall-Daten speichern, ohne sie auf der Karte anzuzeigen
        allData.forEach((accident) => {
          const { Latitude, Longitude } = accident;

          if (Latitude != null && Longitude != null) {
            this.accidentLocations.push([parseFloat(Latitude), parseFloat(Longitude)]);
          } else {
            console.warn("Unfall-Daten ohne Koordinaten gefunden:", accident);
          }
        });
      } catch (error) {
        console.error("Fehler beim Laden der Unfall-Daten:", error);
      }
    },
    updateUserMarkerWithRadius() {
      const radius = 550; // 300 Meter Radius

      // Zählt die Anzahl der Unfälle innerhalb des Radius
      const accidentCount = this.accidentLocations.filter((location) => {
        const distance = this.map.distance(this.userLatLng, location);
        return distance <= radius;
      }).length;

      // Benutzer-Icon basierend auf der Unfallanzahl definieren
      let iconUrl;
      if (accidentCount < 2) {
        iconUrl = require("@/assets/leaflet/marker-icon-green.png");
      } else if (accidentCount <= 4) {
        iconUrl = require("@/assets/leaflet/marker-icon-yellow.png");
      } else {
        iconUrl = require("@/assets/leaflet/marker-icon-red.png");
      }

      const userLocationIcon = L.icon({
        iconUrl: iconUrl,
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
      });

      // Benutzer-Marker auf der Karte hinzufügen
      L.marker(this.userLatLng, { icon: userLocationIcon })
        .addTo(this.map)
        .bindPopup("Ihr Standort")
        .openPopup();

      // Radius-Kreis um den Benutzer zeichnen
      L.circle(this.userLatLng, {
        radius: radius,
        color: "#3388ff",
        fillColor: "#3388ff",
        fillOpacity: 0.2,
      }).addTo(this.map);
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
