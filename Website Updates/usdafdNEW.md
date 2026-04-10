<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* --- Infinite Scroller --- */
.infinite-slider {
  overflow: hidden;
  width: 100%;
  padding: 0;
  background: transparent;
  margin-bottom: 0;
  display: block;
}

.infinite-slider .track {
  display: flex;
  gap: 16px;
  width: max-content;
  animation: scroll-left 35s linear infinite;
  will-change: transform;
}

.infinite-slider .track.paused {
  animation-play-state: paused;
}

.infinite-slider .slide {
  flex: 0 0 auto;
  width: clamp(220px, 28vw, 360px);
  height: clamp(140px, 18vw, 220px);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,.12);
}

.infinite-slider img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transform: scale(1.05);
  transition: transform .35s ease;
}

.infinite-slider .slide:hover img {
  transform: scale(1.1);
}

@keyframes scroll-left {
  to { transform: translateX(-50%); }
}

@media (prefers-reduced-motion: reduce) {
  .infinite-slider .track { animation: none; }
}

/* Carousel wrapper for button positioning */
.usda-slider-wrapper {
  position: relative;
}

#sliderToggleBtn {
  position: absolute;
  top: 1rem;
  left: 1rem;
  min-height: 44px;
  padding: 8px 16px;
  border: 2px solid #ffffff;
  cursor: pointer;
  background-color: rgba(15, 45, 82, 0.7);
  color: white;
  border-radius: 5px;
  font-size: 0.8rem;
  transition: all 0.3s ease-in-out;
  z-index: 10;
  backdrop-filter: blur(4px);
}

#sliderToggleBtn:hover {
  background-color: rgba(15, 45, 82, 0.9);
  transform: scale(1.05);
}

#sliderToggleBtn.paused-state {
  background-color: rgba(255,255,255,0.9);
  color: #003366;
  border-color: white;
}

#sliderToggleBtn.paused-state:hover {
  background-color: white;
  transform: scale(1.05);
}

/* USDA Page Styles */
.usda-page * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.usda-page {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
}

.usda-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.usda-header {
    text-align: center;
    padding: 3rem 0;
    background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
}

.usda-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
}

.usda-header p {
    color: #dbaa00;
    font-size: 1.2rem;
    font-weight: bold;
}

.usda-content-box {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
}

.usda-content-box h2 {
    color: #0f2d52;
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
    text-align: center;
}

.usda-content-box h3 {
    color: #0f2d52;
    font-size: 1.4rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.usda-content-box p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-bottom: 1.2rem;
    text-align: center;
}

.usda-content-box strong {
    color: #0f2d52;
}

.usda-content-box em {
    color: #dbaa00;
}

.usda-highlight-box {
    background: linear-gradient(135deg, #fffbf0 0%, #fff9e6 100%);
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #dbaa00;
    margin: 2rem 0;
    text-align: center;
}

.usda-highlight-box p {
    margin: 0;
    font-size: 1.1rem;
    color: #0f2d52;
    font-weight: bold;
}

.usda-dates-section {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #0f2d52;
}

.usda-dates-section h2 {
    color: #0f2d52;
    font-size: 2rem;
    margin-bottom: 2rem;
    text-align: center;
    text-transform: uppercase;
}

.usda-event-item {
    display: flex;
    gap: 1.5rem;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-left: 5px solid #dbaa00;
    transition: all 0.3s ease;
}

.usda-event-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    border-left-color: #0f2d52;
}

.usda-event-date {
    min-width: 100px;
    text-align: center;
    background: #0f2d52;
    color: white;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(15, 45, 82, 0.3);
}

.usda-event-month {
    font-size: 1rem;
    text-transform: uppercase;
    color: #dbaa00;
    font-weight: bold;
}

.usda-event-day {
    font-size: 2.5rem;
    font-weight: bold;
    line-height: 1;
    margin-top: 0.3rem;
}

.usda-event-details {
    flex: 1;
}

.usda-event-details h4 {
    color: #0f2d52;
    margin-bottom: 0.8rem;
    font-size: 1.3rem;
}

.usda-event-details p {
    margin: 0.5rem 0;
    font-size: 1rem;
    color: #555;
    text-align: left;
}

.usda-event-details a {
    color: #dbaa00;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
}

.usda-event-details a:hover {
    color: #0f2d52;
    text-decoration: underline;
}

.usda-volunteer-section {
    background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
    padding: 3rem 0;
    border-radius: 0;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(219, 170, 0, 0.4);
}

.usda-volunteer-section h2 {
    color: #0f2d52;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    text-align: center;
}

.usda-iframe-container {
    margin: 2rem 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    background: white;
}

.usda-iframe-container iframe {
    display: block;
    width: 100%;
    height: 500px;
    border: none;
}

.usda-fallback-link {
    margin-top: 1rem;
    text-align: center;
}

.usda-fallback-link p {
    text-align: center;
}

.usda-fallback-link a {
    color: #0f2d52;
    font-weight: bold;
    text-decoration: none;
    transition: color 0.3s ease;
}

.usda-fallback-link a:hover {
    color: white;
    text-decoration: underline;
}

@media (max-width: 768px) {
    .usda-header h1 {
        font-size: 1.8rem;
    }

    .usda-content-box {
        padding: 1.5rem;
    }

    .usda-event-item {
        flex-direction: column;
        gap: 1rem;
    }

    .usda-event-date {
        min-width: auto;
        width: 100px;
        margin: 0 auto;
    }

    .usda-event-details p {
        text-align: center;
    }

    .usda-volunteer-section {
        padding: 2rem 0;
    }
}
</style>

<div class="usda-page">
  <!-- Image Slider at Top -->
  <div class="usda-slider-wrapper">
    <button id="sliderToggleBtn" onclick="toggleSlider()" aria-label="Pause photo carousel">Pause carousel</button>
    <div class="infinite-slider">
    <div class="track" id="sliderTrack">
      <!-- SET A -->
      <div class="slide"><img alt="USDA Food Distribution volunteers handing out food bags" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda1.jpeg" /></div>
      <div class="slide"><img alt="Community members receiving food at a USDA distribution event" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda2.jpg" /></div>
      <div class="slide"><img alt="UC Merced students volunteering at a USDA food distribution" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda3.jpg" /></div>
      <div class="slide"><img alt="Volunteers in yellow vests organizing food boxes" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda4.jpg" /></div>
      <div class="slide"><img alt="Food distribution line at a community site in Merced" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda5.jpg" /></div>
      <div class="slide"><img alt="Volunteers loading food into vehicles at a distribution event" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda6.jpg" /></div>
      <div class="slide"><img alt="Students and community members at a USDA food distribution site" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda7.jpg" /></div>
      <!-- SET B (duplicate for seamless loop) -->
      <div class="slide"><img alt="USDA Food Distribution volunteers handing out food bags" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda1.jpeg" /></div>
      <div class="slide"><img alt="Community members receiving food at a USDA distribution event" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda2.jpg" /></div>
      <div class="slide"><img alt="UC Merced students volunteering at a USDA food distribution" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda3.jpg" /></div>
      <div class="slide"><img alt="Volunteers in yellow vests organizing food boxes" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda4.jpg" /></div>
      <div class="slide"><img alt="Food distribution line at a community site in Merced" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda5.jpg" /></div>
      <div class="slide"><img alt="Volunteers loading food into vehicles at a distribution event" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda6.jpg" /></div>
      <div class="slide"><img alt="Students and community members at a USDA food distribution site" src="/sites/g/files/ufvvjh561/f/images/usdaFoodDistribution/usda7.jpg" /></div>
    </div>
  </div>

  <!-- Header -->
  <div class="usda-header">
    <div class="usda-container">
      <h1>Calling All Bobcats!</h1>
      <p>USDA Food Distribution Program</p>
    </div>
  </div>

  <div class="usda-container">
    <!-- Main Content -->
    <div class="usda-content-box">
      <p>USDA&#39;s food distribution programs strengthen the nutrition safety net through the distribution of USDA Foods and other nutrition assistance to children, low-income families, emergency feeding programs, and the elderly. This service is <strong>open to all students, staff, and community members</strong> in need of food assistance!</p>

      <div class="usda-highlight-box" role="note">
        <p><strong><em>Food distributions no longer occur on a regular schedule, please check our calendar for more details such as time and location.</em></strong></p>
        <p style="margin-top: 0.5rem;"><strong><em>Transportation will NOT be provided.</em></strong></p>
      </div>

      <p>For questions or accommodations, please contact the Community Engagement Center at <a href="mailto:communityservice@ucmerced.edu" style="color: #0f2d52; font-weight: bold;">communityservice@ucmerced.edu</a>.</p>
    </div>

    <!-- Upcoming Dates -->
    <div class="usda-dates-section">
      <h2>Upcoming Distribution Dates</h2>

      <div class="usda-event-item">
        <div class="usda-event-date">
          <div class="usda-event-month">April</div>
          <div class="usda-event-day">17</div>
        </div>
        <div class="usda-event-details">
          <h4><a href="https://calendly.com/ucm-cec/usda-food-distribution-clone-1">Friday, April 17th at 12:30 PM</a></h4>
          <p><strong>Location:</strong> <a href="https://maps.app.goo.gl/yzDpgPN3nFG44vj39" target="_blank">St. Patrick&#39;s Parish Catholic Church at 671 E Yosemite Ave, Merced, CA 95340 (opens in new tab)</a></p>
        </div>
      </div>

      <div class="usda-event-item">
        <div class="usda-event-date">
          <div class="usda-event-month">April</div>
          <div class="usda-event-day">22</div>
        </div>
        <div class="usda-event-details">
          <h4><a href="https://calendly.com/ucm-cec/usda-food-distribution-april-17th-clone">Wednesday, April 22nd at 12:30 PM</a></h4>
          <p><strong>Location:</strong> <a href="https://maps.app.goo.gl/PtakcTp6JTgTNoJg9" target="_blank">Sacred Heart Church at 519 W 12th St. Merced, CA 95341 (opens in new tab)</a></p>
        </div>
      </div>
    </div>
  </div>

  <!-- Volunteer Section -->
  <div class="usda-volunteer-section">
    <div class="usda-container">
      <h2>Volunteers: Sign Up Today!</h2>
      <div class="usda-iframe-container">
        <iframe
          src="https://calendly.com/ucm-cec/usda-food-distribution-clone-1"
          title="Volunteer sign-up form for USDA Food Distribution via Calendly">
        </iframe>
      </div>
      <div class="usda-fallback-link">
        <p>If the link above does not work, <a href="https://calendly.com/ucm-cec/usda-food-distribution-clone-1" target="_blank">please click here (opens in new tab)</a>.</p>
      </div>
    </div>
  </div>
</div>

<script>
  var sliderPaused = false;

  function toggleSlider() {
    var track = document.getElementById('sliderTrack');
    var btn = document.getElementById('sliderToggleBtn');
    sliderPaused = !sliderPaused;
    if (sliderPaused) {
      track.classList.add('paused');
      btn.textContent = 'Resume carousel';
      btn.setAttribute('aria-label', 'Resume photo carousel');
      btn.classList.add('paused-state');
    } else {
      track.classList.remove('paused');
      btn.textContent = 'Pause carousel';
      btn.setAttribute('aria-label', 'Pause photo carousel');
      btn.classList.remove('paused-state');
    }
  }
</script>