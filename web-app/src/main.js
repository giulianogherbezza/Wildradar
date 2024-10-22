import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Vue App erstellen und Router verwenden
const app = createApp(App);
app.use(router);
app.mount("#app");

