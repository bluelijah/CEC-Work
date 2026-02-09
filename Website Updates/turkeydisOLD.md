<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* --- Infinite Scroller --- */
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
<div class="usda-page"><!-- Image Slider at Top -->
	<div class="infinite-slider">
		<div class="track"><!-- SET A -->
			<div class="slide"><img alt="USDA Food Distribution 1" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda1.jpeg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 2" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda2.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 3" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda3.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 4" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda4.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 5" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda5.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 6" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda6.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 7" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda7.jpg" /></div>
			<!-- SET B (duplicate for seamless loop) -->

			<div class="slide"><img alt="USDA Food Distribution 1" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda1.jpeg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 2" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda2.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 3" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda3.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 4" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda4.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 5" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda5.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 6" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda6.jpg" /></div>

			<div class="slide"><img alt="USDA Food Distribution 7" src="/sites/cec.ucmerced.edu/files/images/usdaFoodDistribution/usda7.jpg" /></div>
		</div>
	</div>
	<!-- Header -->

	<div class="usda-header">
		<div class="usda-container">
			<h1>Calling All Bobcats!</h1>

			<p>Turkey Distribution</p>
		</div>
	</div>

	<div class="usda-container"><!-- Main Content -->
		<div class="usda-content-box">
			<p>USDA&#39;s food distribution programs strengthen the nutrition safety net through the distribution of USDA Foods and other nutrition assistance to children, low-income families, emergency feeding programs, and the elderly. This service is <strong>open to all students, staff, and community members</strong> in need of food assistance!</p>

			<div class="usda-highlight-box">
				<p><strong><em>Volunteers will help with set up, food organization, distribution, and safety of the event. Come ready, rain or shine, to help bring cheer to this holiday season.</em></strong></p>

				<p style="margin-top: 0.5rem;"><strong><em>Limited Transportation WILL&nbsp;be provided.</em></strong></p>

				<p style="margin-top: 0.5rem;"><strong><em>We thank you for your continued efforts to give back and give thanks to the Merced Community.</em></strong></p>
			</div>

			<p>For questions or accommodations, please contact the Community Engagement Center at <strong>communityservice@ucmerced.edu</strong>.</p>
		</div>
		<!-- Upcoming Dates -->

		<div class="usda-dates-section">
			<h2>Turkey Distribution Date</h2>

			<div class="usda-event-item">
				<div class="usda-event-date">
					<div class="usda-event-month">Nov.</div>

					<div class="usda-event-day">24</div>
				</div>

				<div class="usda-event-details">
					<h4>Monday, November 24th&nbsp;at 6:30 AM</h4>

					<p><strong>Location:</strong> <a href="https://maps.app.goo.gl/yzDpgPN3nFG44vj39" target="_blank">St. Patrick&#39;s at 671 E Yosemite Avenue Merced, CA</a></p>
				</div>
			</div>
			<!-- Volunteer Section -->

			<div class="flyer"><img alt="Downtown Merced Trick-or-Treat Street Flyer" src="/sites/g/files/ufvvjh561/f/event/turkey_distribution_2025.png" style="height: 675px; width: 540px; margin-left: 250px; margin-right: 250px;" /></div>

			<div class="usda-volunteer-section">
				<div class="usda-container">
					<h2>Volunteers: Sign Up Today!</h2>

					<div class="usda-iframe-container"><iframe src="https://ucmerced.az1.qualtrics.com/jfe/form/SV_eS46KqYwTXGHcA6"></iframe></div>

					<div class="usda-fallback-link">
						<p>If the link above does not work, <a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_eS46KqYwTXGHcA6" target="_blank">please click here</a>.</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
