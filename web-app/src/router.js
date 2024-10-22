// src/router.js
import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "./components/LandingPage.vue"; // Neue LandingPage-Komponente (anstatt App.vue)
import MapPage from "./components/MapPage.vue";

const routes = [
  {
    path: "/",
    name: "LandingPage",
    component: LandingPage, // Zeigt die Landing-Page
  },
  {
    path: "/map",
    name: "MapPage",
    component: MapPage, // Zeigt die Map-Seite
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
