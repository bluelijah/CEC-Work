<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.mlk-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 40px 0 20px;
}

/* Hero Section */
.mlk-hero {
    background: linear-gradient(135deg, rgba(15, 45, 82, 0.8) 0%, rgba(26, 67, 115, 0.92) 100%), 
                url('/sites/cec.ucmerced.edu/files/images/mlk.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: white;
    padding: 80px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.mlk-hero::before {
    content: '';
    position: absolute;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(219, 170, 0, 0.2) 0%, transparent 70%);
    top: 10%;
    left: 5%;
    animation: mlkFloat 15s ease-in-out infinite;
}

.mlk-hero::after {
    content: '';
    position: absolute;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(219, 170, 0, 0.15) 0%, transparent 70%);
    bottom: 5%;
    right: 10%;
    animation: mlkFloat 12s ease-in-out infinite reverse;
}

@keyframes mlkFloat {
    0%, 100% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-30px) scale(1.1); }
}

.mlk-hero > .mlk-container {
    position: relative;
    z-index: 1;
}

.mlk-hero-title {
    font-size: 3.5em;
    color: #dbaa00;
    font-weight: 700;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.mlk-hero-subtitle {
    font-size: 1.5em;
    color: #dbaa00;
    font-style: italic;
    margin-bottom: 15px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.mlk-hero-description {
    font-size: 1.2em;
    max-width: 1000px;
    margin: 0 auto 20px;
    line-height: 1.8;
}

.mlk-hero-quote {
    font-size: 1.3em;
    font-style: italic;
    max-width: 900px;
    margin: 30px auto 10px;
    padding: 20px;
    border-left: 4px solid #dbaa00;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 5px;
}

.mlk-hero-quote-author {
    font-size: 0.9em;
    text-align: right;
    margin-top: 10px;
    color: #dbaa00;
}

/* Info Section */
.mlk-info-section {
    background: white;
    padding: 60px 20px;
}

.mlk-section-title {
    font-size: 2.5em;
    color: #0f2d52;
    text-align: center;
    margin-bottom: 20px;
    font-weight: 700;
}

.mlk-section-subtitle {
    text-align: center;
    font-size: 1.2em;
    color: #666;
    max-width: 1000px;
    margin: 0 auto 40px;
    line-height: 1.8;
}

/* Events Section */
.mlk-events-section {
    background: #f8f9fa;
    padding: 60px 20px;
}

.mlk-event-card {
    background: white;
    border-left: 5px solid #dbaa00;
    padding: 30px;
    margin-bottom: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.mlk-event-card:hover {
    border-left-color: #0f2d52;
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    transform: translateY(-3px);
}

.mlk-event-card.no-events {
    text-align: center;
    padding: 60px 30px;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.mlk-event-card.no-events h3 {
    color: #0f2d52;
    font-size: 2em;
    margin-bottom: 15px;
}

.mlk-event-card.no-events p {
    color: #666;
    font-size: 1.2em;
    margin-bottom: 20px;
}

/* Split Event Card Layout */
.mlk-event-card-split {
    padding: 0;
}

.mlk-event-content-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    min-height: 500px;
}

.mlk-event-text-content {
    padding: 30px;
}

.mlk-event-flyer-content {
    background: #f8f9fa;
    padding: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.mlk-event-flyer-content img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.mlk-event-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 15px;
    flex-wrap: wrap;
}

.mlk-event-title {
    color: #0f2d52;
    font-size: 1.8em;
    font-weight: 700;
    margin-bottom: 5px;
}

.mlk-event-subtitle {
    color: #dbaa00;
    font-weight: 600;
    font-size: 1.1em;
    font-style: italic;
}

.mlk-event-description {
    line-height: 1.8;
    color: #555;
    margin-bottom: 20px;
}

.mlk-event-details {
    background: #FFF8E7;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
    border-left: 3px solid #dbaa00;
}

.mlk-event-details h4 {
    color: #0f2d52;
    font-size: 1.1em;
    margin-bottom: 10px;
}

.mlk-event-details ul {
    margin-left: 20px;
    color: #555;
    line-height: 1.8;
}

.mlk-alert {
    background: #FFF8E7;
    border-left: 5px solid #dbaa00;
    padding: 15px;
    margin: 20px 0;
    border-radius: 5px;
}

.mlk-btn {
    display: inline-block;
    padding: 12px 30px;
    background: #dbaa00;
    color: #0f2d52;
    text-decoration: none;
    border-radius: 25px;
    font-weight: 700;
    transition: all 0.3s ease;
    border: 2px solid #dbaa00;
    margin-top: 10px;
    margin-right: 10px;
}

.mlk-btn:hover {
    background: #0f2d52;
    color: white;
    border-color: #0f2d52;
    transform: scale(1.05);
}

.mlk-btn-secondary {
    background: white;
    color: #0f2d52;
    border: 2px solid #0f2d52;
}

.mlk-btn-secondary:hover {
    background: #0f2d52;
    color: white;
}

/* CTA Section */
.mlk-cta-section {
    background: linear-gradient(135deg, #dbaa00 0%, #ffc107 100%);
    padding: 60px 20px;
}

.mlk-cta-section h2 {
    text-align: center;
    font-size: 2.5em;
    color: #0f2d52;
    margin-bottom: 20px;
    font-weight: 700;
}

.mlk-cta-section p {
    text-align: center;
    font-size: 1.2em;
    color: #333;
    max-width: 700px;
    margin: 0 auto 30px;
}

.mlk-cta-buttons {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
}

/* Footer */
.mlk-footer {
    background: #0f2d52;
    color: white;
    padding: 40px 20px;
    text-align: center;
}

.mlk-footer a,
.mlk-footer a:link,
.mlk-footer a:visited {
    color: #dbaa00 !important;
    text-decoration: none;
    font-weight: 600;
}

.mlk-footer a:hover,
.mlk-footer a:active {
    color: #ffc107 !important;
    text-decoration: underline;
}

.mlk-footer-links {
    margin-top: 20px;
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .mlk-container {
        padding: 0 10px;
    }
    
    .mlk-hero,
    .mlk-info-section,
    .mlk-events-section,
    .mlk-cta-section,
    .mlk-footer {
        margin-right: 20px;
    }
    
    .mlk-hero {
        padding: 50px 20px;
    }
    
    .mlk-hero-title {
        font-size: 2.2em;
    }
    
    .mlk-hero-subtitle {
        font-size: 1.2em;
    }
    
    .mlk-hero-description {
        font-size: 1em;
    }
    
    .mlk-hero-quote {
        font-size: 1.1em;
    }
    
    .mlk-info-section,
    .mlk-events-section {
        padding: 40px 10px;
    }
    
    .mlk-event-card {
        padding: 20px 15px;
    }
    
    .mlk-event-card-split {
        padding: 0;
    }
    
    .mlk-event-content-wrapper {
        grid-template-columns: 1fr;
        min-height: auto;
    }
    
    .mlk-event-text-content {
        padding: 20px 15px;
    }
    
    .mlk-event-flyer-content {
        padding: 20px 15px;
        min-height: 400px;
    }
    
    .mlk-section-title {
        font-size: 2em;
    }
    
    .mlk-event-header {
        flex-direction: column;
    }
    
    /* Fix email overflow */
    .mlk-alert a {
        word-break: break-word;
        overflow-wrap: break-word;
    }
}
</style>
<!-- Hero Section -->
<div class="mlk-hero">
	<div class="mlk-container">
		<h1 class="mlk-hero-title">MLK Day of Service</h1>

		<p class="mlk-hero-subtitle">A Day On, Not a Day Off</p>

		<p class="mlk-hero-description">Join UC Merced in honoring Dr. Martin Luther King Jr.&#39;s legacy through service to our community. This national day of service is a time to come together, give back, and work toward the beloved community Dr. King envisioned.</p>

		<div class="mlk-hero-quote">&quot;Life&#39;s most persistent and urgent question is, &#39;What are you doing for others?&#39;&quot;
			<div class="mlk-hero-quote-author">&mdash; Dr. Martin Luther King Jr.</div>
		</div>
	</div>
</div>
<!-- Info Section -->

<div class="mlk-info-section">
	<div class="mlk-container">
		<h2 class="mlk-section-title">About MLK Day of Service</h2>

		<p class="mlk-section-subtitle">Monday, January 19, 2025 is Martin Luther King Jr. Day - a National Day of Remembrance for one of America&#39;s greatest equality activists, and a true symbol of justice. The National Museum of African American History &amp; Culture states the &quot;King Holiday&quot; Bill was signed into law on November 2, 1983, designating the 3rd Monday in January a federal holiday.</p>

		<p class="mlk-section-subtitle">The Community Engagement Center invites the UC Merced Campus: students, staff, faculty, &amp; alumni to engage in service to honor the legacy of Martin Luther King Jr. Provided below is a menu of different service projects you can join in honor of MLK Day.</p>

		<div class="mlk-alert" style="max-width: 900px; margin: 30px auto;"><strong>Important Information:</strong>

			<ul style="margin-top: 10px; margin-left: 20px; line-height: 1.8;">
				<li>All service projects listed are <strong>Catlife and CollegeCorps eligible</strong></li>
				<li>Certain service projects provide limited transportation while others do not - please read the details carefully</li>
				<li>If you have questions or need accommodations, please email <a href="mailto:communityservice@ucmerced.edu" style="color: #0f2d52; font-weight: bold;">communityservice@ucmerced.edu</a></li>
			</ul>
		</div>
	</div>
</div>
<!-- Events Section -->

<div class="mlk-events-section">
	<div class="mlk-container">
		<h2 class="mlk-section-title">Service Opportunities</h2>
		<!-- No Events Card -->

		<div class="mlk-event-card no-events">
			<h3>Events Coming Soon</h3>

			<p>Service opportunities for MLK Day 2026 are currently being planned. Check back soon for opportunities to serve our community!</p>

			<p style="font-size: 0.95em; color: #888; margin-top: 15px;">Want to be notified when events are announced? Contact us below.</p>
		</div>
	</div>
</div>
<!-- CTA Section -->

<div class="mlk-cta-section">
	<div class="mlk-container">
		<h2>Be the Change</h2>

		<p>Service is more than a single day&mdash;it&#39;s a commitment to building a better community. Join us in honoring Dr. King&#39;s vision through action and service.</p>

		<div class="mlk-cta-buttons"><a class="mlk-btn mlk-btn-secondary" href="https://cec.ucmerced.edu/" target="_blank">Visit the CEC</a> <a class="mlk-btn mlk-btn-secondary" href="https://cec.ucmerced.edu/calendar" target="_blank">View Calendar</a></div>
	</div>
</div>
<!-- Footer -->

<div class="mlk-footer">
	<div class="mlk-container">
		<p><strong>Questions?</strong> Contact the Community Engagement Center at KL 190</p>

		<p>Monday - Friday, 9:00 AM - 5:00 PM</p>

		<p>You can also <a href="mailto:communityservice@ucmerced.edu">email us</a></p>

		<div class="mlk-footer-links"><a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a> <a href="https://cec.ucmerced.edu/calendar" target="_blank">CEC Calendar</a> <a href="https://cec.ucmerced.edu/service-hours" target="_blank">Submit Service Hours</a></div>

		<p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2026 UC Merced | Community Engagement Center</p>
	</div>
</div>
