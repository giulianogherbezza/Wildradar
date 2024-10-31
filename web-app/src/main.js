import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "leaflet/dist/leaflet.css"; // Importiert Leaflet CSS

// Vue App erstellen und Router verwenden
const app = createApp(App);
app.use(router);
app.mount("#app");

