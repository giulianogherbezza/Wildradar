<template>
  <div id="app" class="container">
    <!-- Header mit Logo und Titel -->
    <header>
      <img src="@/assets/Preview.png" alt="Wildradar Logo" class="logo" />
  
    </header>

    <!-- Hauptinhalt mit Beschreibung und Start-Button -->
    <main>
      <p class="description">
        Willkommen bei Wildradar! Unsere Anwendung hilft Ihnen dabei, Wildunfälle zu vermeiden,
        indem Sie Informationen zu gefährdeten Gebieten erhalten. Klicken Sie auf "Start", um Ihren
        Standort zu teilen und herauszufinden, wo besondere Vorsicht geboten ist.
      </p>
      <!-- Start Button für die Weiterleitung zur nächsten Seite -->
      <button @click="goToNextPage" class="start-button">Start</button>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    goToNextPage() {
      // Hier kannst du die Logik hinzufügen, um zur nächsten Seite zu navigieren.
      // Ein Beispiel: Route zur nächsten Seite wechseln (wenn du Vue Router verwendest)
      this.$router.push("/map"); // Platzhalter für die zweite Seite
    }
  }
};
</script>

<style scoped>
/* Grundlegendes CSS, um die Landing-Page zu gestalten */
.container {
  text-align: center;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
}

header {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #4CAF50;
  color: white;
  padding: 20px;
}

.logo {
  max-width: 150px;
  height: auto;
  margin-bottom: 10px;
}

main {
  margin-top: 20px;
  padding: 0 20px;
}

.description {
  font-size: 1.2rem;
  line-height: 1.5;
  margin-bottom: 20px;
}

.start-button {
  padding: 15px 30px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.start-button:hover {
  background-color: #45a049;
}

/* Responsive Design */
@media (max-width: 768px) {
  .description {
    font-size: 1rem;
  }

  .start-button {
    padding: 10px 20px;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .logo {
    max-width: 120px;
  }

  header {
    padding: 15px;
  }

  .description {
    font-size: 0.9rem;
  }

  .start-button {
    padding: 8px 16px;
    font-size: 0.8rem;
  }
}
</style>
