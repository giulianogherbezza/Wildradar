<template>
  <div id="landing-page" class="container">
    <!-- Header mit Logo und Navigationsleiste -->
    <header class="header">
      <div class="header-container">
        <img src="@/assets/Preview.png" alt="Wildradar Logo" class="logo" />
        <nav class="nav">
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#features">Funktionen</a></li>
            <li><a href="#prototypes">Prototyp</a></li>
            <li><a href="#contact">Kontakt</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- Hauptinhalt der Landing-Page -->
    <main>
      <!-- Begrüßung und Beschreibung -->
      <section class="hero-section">
        <div class="hero-content">
          <h1>Wildradar - Vermeiden Sie Wildunfälle</h1>
          <p>
            Wildradar hilft Ihnen dabei, gefährliche Unfallstellen zu erkennen und sicher zu navigieren.
            Mit einer intuitiven Kartenfunktion können Sie alle gefährdeten Zonen einfach einsehen und sich schützen.
          </p>
          <!-- Start Button als Router-Link -->
          <router-link to="/map">
            <button class="cta-button">Standort anzeigen</button>
          </router-link>
        </div>
      </section>

      <!-- Features Section -->
      <section id="features" class="features-section">
        <div class="features-content">
          <h2>Unsere Funktionen</h2>
          <ul class="features-list">
            <li>
              <h3>Echtzeit-Warnungen</h3>
              <p>Erhalten Sie Warnungen über Wildunfall-Hotspots in Echtzeit.</p>
            </li>
            <li>
              <h3>GPS-Standorterkennung</h3>
              <p>Teilen Sie Ihren Standort, um die Gefahr von Wildunfällen zu minimieren.</p>
            </li>
            <li>
              <h3>Detaillierte Unfallkarte</h3>
              <p>Sehen Sie gefährliche Zonen in Ihrer Umgebung auf einen Blick.</p>
            </li>
          </ul>
        </div>
      </section>

      <!-- Prototype Section -->
      <section id="prototypes" class="prototypes-section">
        <div class="prototypes-content">
          <h2>Unser Prototyp</h2>
          <p>Werfen Sie einen Blick auf die Entwicklung unserer App:</p>
          <div class="prototypes-gallery">
            <div class="prototype-item">
              <img src="@/assets/registrieren.png" alt="Prototyp 1" />
              <p>Prototyp-Ansicht: Registrierungsseite</p>
            </div>
            <div class="prototype-item">
              <img src="@/assets/Home.png" alt="Prototyp 2" />
              <p>Prototyp-Ansicht: Home Bildschirm</p>
            </div>
            <div class="prototype-item">
              <img src="@/assets/GPS.png" alt="Prototyp 3" />
              <p>Prototyp-Ansicht: Wild Warnung im GPS</p>
            </div>
            <div class="prototype-item">
              <img src="@/assets/NachNotruf.png" alt="Prototyp 3" />
              <p>Prototyp-Ansicht: Schritt für Schritt Anleitung, bei Unfallscenario</p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2023 Wildradar. Alle Rechte vorbehalten.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style scoped>
/* Allgemeines Seitenlayout */
#landing-page {
  background: linear-gradient(to bottom right, #116613, #3c693e);
  font-family: Arial, sans-serif;
  color: #333;
  line-height: 1.6;
}

/* Header */
.header {
  background-color: rgba(0, 0, 0, 0.7); /* Halbtransparenter Hintergrund für den Header */
  padding: 20px;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  max-width: 150px;
}

.nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}

.nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav a:hover {
  text-decoration: underline;
}

/* Hero Section */
.hero-section {
  text-align: center;
  padding: 80px 20px;
  color: white;
}

.hero-content h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.hero-content p {
  font-size: 1.2rem;
  margin-bottom: 40px;
}

.cta-button {
  padding: 15px 30px;
  background-color: #ff5722;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  cursor: pointer;
}

.cta-button:hover {
  background-color: #e64a19;
}

/* Features Section */
.features-section {
  padding: 40px 20px;
  background-color: #fff;
  text-align: center;
}

.features-content h2 {
  font-size: 2rem;
  margin-bottom: 40px;
}

.features-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
}

.features-list li {
  background-color: #f5f5f5;
  padding: 20px;
  width: 300px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.features-list h3 {
  margin-bottom: 10px;
  color: #116613;
}

/* Prototypes Section */
.prototypes-section {
  padding: 40px 20px;
  background-color: #e8e8e8;
  text-align: center;
}

.prototypes-content h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.prototypes-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.prototype-item {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 250px;
  text-align: center;
  padding: 10px;
}

.prototype-item img {
  max-width: 100%;
  height: auto;
  border-bottom: 1px solid #ddd;
  margin-bottom: 10px;
}

.prototype-item p {
  font-size: 1rem;
  color: #666;
}

/* Footer */
.footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
}
</style>

  