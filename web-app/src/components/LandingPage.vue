<template>
    <div id="landing-page" class="container">
      <!-- Header mit Logo und Titel -->
      <header>
        <img src="@/assets/Preview.png" alt="Wildradar Logo" class="logo" />
        <h1>Wildradar</h1>
      </header>
  
      <!-- Hauptinhalt der Landing-Page mit Beschreibung -->
      <main>
        <p class="description">
          Willkommen bei Wildradar! Unsere Anwendung hilft Ihnen dabei, Wildunfälle zu vermeiden,
          indem Sie Informationen zu gefährdeten Gebieten erhalten. Klicken Sie auf "Start", um Ihren
          Standort zu teilen und herauszufinden, wo besondere Vorsicht geboten ist.
        </p>
        
        <!-- Start Button als Router-Link -->
        <router-link to="/map">
          <button class="start-button">Start</button>
        </router-link>
      </main>
    </div>
  </template>
  
  <script>
  export default {
    name: "LandingPage",
  };
  </script>
  
  <style scoped>

#landing-page {
  position: relative; /* Setzt den Container relativ, um Overlay korrekt zu positionieren */
  background-image: url("@/assets/Background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
  padding: 20px;
  overflow: hidden; /* Verhindert Überläufe von Inhalt */
}

/* Overlay für Transparenz */
.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.2); /* Weißes Overlay mit 40% Transparenz */
  pointer-events: none; /* Verhindert, dass das Overlay Interaktionen blockiert */
}
  /* CSS für die Landing-Page */
  .container {
    text-align: center;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
  }
  
  header {
    background-color: #116613;
    padding: 20px;
    color: white;
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
    background-color: #116613;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }
  
  .start-button:hover {
    background-color: #3c693e;
  }
  </style>
  