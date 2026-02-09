<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>D Street Shelter</title>
<style type="text/css">
/* --- Infinite Scroller --- */
.infinite-slider {
  overflow: hidden;
  width: 100%;
  padding: 0;
  background: transparent;
  margin-bottom: 2rem;
}

.infinite-slider .track {
  display: flex;
  gap: 16px;
  width: max-content;
  animation: scroll-left 35s linear infinite;
  will-change: transform;
}

/* One "card" */
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
  transition: transform .35s ease;
}

.infinite-slider .slide:hover img {
  transform: scale(1.06);
}

@keyframes scroll-left {
  to { transform: translateX(-50%); }
}

/* accessibility: respect users who prefer less motion */
@media (prefers-reduced-motion: reduce) {
  .infinite-slider .track { animation: none; }
}

/* D Street Page Styles */
.dstreet-page * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.dstreet-page {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
}

.dstreet-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.dstreet-header {
    text-align: center;
    padding: 3rem 0;
    background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
}

.dstreet-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
}

.dstreet-header p {
    color: #dbaa00;
    font-size: 1.2rem;
    font-weight: bold;
}

.dstreet-content-box {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
}

.dstreet-content-box h2 {
    color: #0f2d52;
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
    text-align: center;
}

.dstreet-content-box p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-bottom: 1.2rem;
    text-align: center;
}

.dstreet-content-box strong {
    color: #0f2d52;
}

.dstreet-highlight {
    color: #dbaa00;
    font-weight: bold;
}

.dstreet-donations-section {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #0f2d52;
}

.dstreet-donations-section h2 {
    color: #0f2d52;
    font-size: 2rem;
    margin-bottom: 2rem;
    text-align: center;
    text-transform: uppercase;
}

.dstreet-items-grid {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: 1fr;
}

@media (min-width: 768px) {
    .dstreet-items-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

.dstreet-items-column {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 5px solid #dbaa00;
    transition: all 0.3s ease;
}

.dstreet-items-column:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    border-left-color: #0f2d52;
}

.dstreet-items-column h3 {
    color: #0f2d52;
    font-size: 1.3rem;
    margin-bottom: 1rem;
    text-align: center;
    text-transform: uppercase;
}

.dstreet-items-list {
    margin: 0;
    padding: 0;
}

.dstreet-item {
    display: block;
    margin: 0.6rem 0;
    font-size: 1rem;
    color: #555;
    line-height: 1.4;
    padding-left: 1.5rem;
    position: relative;
}

.dstreet-item:before {
    content: "•";
    color: #dbaa00;
    font-weight: bold;
    position: absolute;
    left: 0;
    font-size: 1.2rem;
}

.dstreet-note {
    margin-top: 2rem;
    text-align: center;
    font-size: 1rem;
    color: #666;
    font-style: italic;
}

.dstreet-contact-section {
    background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
    padding: 3rem 0;
    border-radius: 0;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(219, 170, 0, 0.4);
}

.dstreet-contact-section h2 {
    color: #0f2d52;
    font-size: 2rem;
    margin-bottom: 1rem;
    text-transform: uppercase;
    text-align: center;
}

.dstreet-contact-section p {
    text-align: center;
    font-size: 1.1rem;
    color: #333;
    margin-bottom: 1.5rem;
}

.dstreet-phone {
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    color: #0f2d52;
    margin: 1.5rem 0;
    padding: 1rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
}

.dstreet-thank-you {
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
    color: #0f2d52;
    margin-top: 1.5rem;
}

@media (max-width: 768px) {
    .dstreet-header h1 {
        font-size: 1.8rem;
    }

    .dstreet-content-box {
        padding: 1.5rem;
    }

    .dstreet-donations-section {
        padding: 1.5rem;
    }

    .dstreet-items-grid {
        grid-template-columns: 1fr;
    }

    .dstreet-contact-section {
        padding: 2rem 0;
    }

    .dstreet-phone {
        font-size: 1.5rem;
    }
}
</style>

<div class="dstreet-page">
    <!-- Image Slider at Top -->
    <div class="infinite-slider">
        <div class="track">
            <!-- SET A -->
            <div class="slide">
                <img alt="D Street Shelter 1" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter1.jpg" />
            </div>
            <div class="slide">
                <img alt="D Street Shelter 2" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter2.jpg" />
            </div>
            <div class="slide">
                <img alt="D Street Shelter 3" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter3.jpg" />
            </div>
            
            <!-- SET B (duplicate for seamless loop) -->
            <div class="slide">
                <img alt="D Street Shelter 1" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter1.jpg" />
            </div>
            <div class="slide">
                <img alt="D Street Shelter 2" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter2.jpg" />
            </div>
            <div class="slide">
                <img alt="D Street Shelter 3" src="/sites/cec.ucmerced.edu/files/images/dstreet/dstreetshelter3.jpg" />
            </div>
        </div>
    </div>

    <!-- Header -->
    <div class="dstreet-header">
        <div class="dstreet-container">
            <h1>D Street Shelter</h1>
            <p>Volunteer & Donation Opportunities</p>
        </div>
    </div>

    <div class="dstreet-container">
        <!-- Main Content -->
        <div class="dstreet-content-box">
            <p><strong>D Street Shelter is looking for volunteers!</strong></p>

            <p>Located at <span class="dstreet-highlight">317 E 15th St.</span>, they are a 50 bed capacity shelter that is open <span class="dstreet-highlight">7 days a week, 24 hours per day</span>. The shelter is accepting volunteers to use their kitchen to prepare dinner and serve on site. They serve a light breakfast, lunch and dinner and accept food donations, as well.</p>
        </div>

        <!-- Donations Section -->
        <div class="dstreet-donations-section">
            <h2>Donations That Would Be Appreciated</h2>

            <div class="dstreet-items-grid">
                <div class="dstreet-items-column">
                    <h3>Bread & Grains</h3>
                    <div class="dstreet-items-list">
                        <div class="dstreet-item">White sliced bread</div>
                        <div class="dstreet-item">Hot dog buns</div>
                        <div class="dstreet-item">Pasta noodles</div>
                        <div class="dstreet-item">Spaghetti</div>
                        <div class="dstreet-item">Cereal</div>
                    </div>
                </div>

                <div class="dstreet-items-column">
                    <h3>Proteins & Dairy</h3>
                    <div class="dstreet-items-list">
                        <div class="dstreet-item">Hot dogs</div>
                        <div class="dstreet-item">Lunch meat</div>
                        <div class="dstreet-item">Hamburger</div>
                        <div class="dstreet-item">Tuna</div>
                        <div class="dstreet-item">Peanut butter</div>
                        <div class="dstreet-item">Milk</div>
                    </div>
                </div>

                <div class="dstreet-items-column">
                    <h3>Produce & Other</h3>
                    <div class="dstreet-items-list">
                        <div class="dstreet-item">Fruit</div>
                        <div class="dstreet-item">Lettuce</div>
                        <div class="dstreet-item">Vegetables</div>
                        <div class="dstreet-item">Pasta sauce</div>
                        <div class="dstreet-item">Jelly</div>
                    </div>
                </div>
            </div>

            <p class="dstreet-note">All food donations are greatly appreciated and help us serve our community!</p>
        </div>
    </div>

    <!-- Contact Section -->
    <div class="dstreet-contact-section">
        <div class="dstreet-container">
            <h2>Ready to Volunteer or Donate?</h2>
            
            <p>Please contact the D Street Homeless Shelter to find out about an upcoming service opportunity.</p>

            <div class="dstreet-phone">(209) 725-8188</div>

            <p class="dstreet-thank-you">Thank you for making a difference!</p>
        </div>
    </div>
</div>