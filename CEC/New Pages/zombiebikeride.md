<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    background: #fff;
    color: #333;
    text-align: center;
    line-height: 1.6;
}
h1 {
    text-align: left;
}

p {
    max-width: 800px;
    margin: 0 auto 25px auto;
    font-size: 1.1rem;
}

.zombie-bike-header {
    color: #39ff14;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 2px 2px 4px #000;
}

.subheader {
    color: #7a4ca8;
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 30px;
    font-style: italic;
}

.highlight {
    font-weight: bold;
    color: #228b22;
}


.schedule-box {
    padding: 25px;
    margin: 25px auto;
    max-width: 700px;
    min-height: 220px;
    box-sizing: border-box;
    background: linear-gradient(135deg, rgba(57, 255, 20, 0.15), rgba(57, 255, 20, 0.05));
    border-radius: 15px;
    border: 3px solid #39ff14;
    box-shadow: 0 4px 15px rgba(57, 255, 20, 0.3);
}

.activities-box {
    padding: 25px;
    border-radius: 15px;
    margin: 25px auto;
    max-width: 700px;  /* unified width for all */
    min-height: 220px; /* keeps height uniform */
    box-sizing: border-box;
    background: linear-gradient(135deg, rgba(57, 255, 20, 0.08), rgba(57, 255, 20, 0.02));
    border: 3px solid #39ff14;
    box-shadow: 0 4px 15px rgba(57, 255, 20, 0.2);
}

.activities-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    max-width: 600px;
    margin: 20px auto 0;
    list-style: none;
    padding: 0;
}

.activities-list li {
    background: rgba(255, 255, 255, 0.7);
    padding: 12px 18px;
    border-radius: 25px;
    color: #333;
    font-weight: 500;
    border: 2px solid #39ff14;
    transition: all 0.3s ease;
    text-align: center;
}

.activities-list li:hover {
    background: rgba(57, 255, 20, 0.1);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(57, 255, 20, 0.3);
}

.zombie-hand {
    color: #39ff14;
    font-size: 1.2em;
}

.flyer {
    width: 95%;
    max-width: 800px;
    margin: 20px auto;
}

.event-text {
    color: #228b22;
    font-weight: bold;
    font-size: 1.3rem;
}

.location-text {
    font-weight: bold;
    color: #8a2be2;
    font-size: 1.3rem;
}

.location-info {
    padding: 25px;
    border-radius: 15px;
    margin: 25px auto;
    max-width: 700px;  /* unified width for all */
    min-height: 100px; /* keeps height uniform */
    box-sizing: border-box;
    background: linear-gradient(135deg, rgba(122, 76, 168, 0.15), rgba(122, 76, 168, 0.05));
    border: 3px solid #7a4ca8;
    box-shadow: 0 4px 15px rgba(122, 76, 168, 0.2);
}

.volunteer-box {
    padding: 25px;
    border-radius: 15px;
    margin: 25px auto;
    max-width: 700px;  /* unified width for all */
    min-height: 220px; /* keeps height uniform */
    box-sizing: border-box;
    background: linear-gradient(135deg, rgba(138, 43, 226, 0.15), rgba(138, 43, 226, 0.05));
    border: 3px solid #8a2be2;
    box-shadow: 0 4px 15px rgba(138, 43, 226, 0.3);
    text-align: left;
}

.volunteer-highlight {
    display: block;
    font-weight: bold;
    color: #8a2be2;
    font-size: 1.3rem;
    text-align: center;
}

.signup-box {
    padding: 25px;
    border-radius: 15px;
    margin: 25px auto;
    max-width: 700px;  /* unified width for all */
    min-height: 220px; /* keeps height uniform */
    box-sizing: border-box;
    background: rgba(211, 47, 47, 0.08);
    border: 2px solid #d32f2f;
    box-shadow: 0 0 15px rgba(211, 47, 47, 0.3);
    text-align: center;
}

.signup-box h2 {
    color: #d32f2f;
    margin-bottom: 15px;
}

.signup-box a {
    display: inline-block;
    background-color: #d32f2f;
    color: #fff;
    text-decoration: none;
    padding: 12px 25px;
    border-radius: 6px;
    font-weight: bold;
    transition: background 0.3s;
}

.signup-box a:hover {
    background-color: #b71c1c;
}


.flyer-container {
    position: relative;
    width: 95%;
    max-width: 800px;
    margin: 20px auto;
    overflow: hidden; /* keeps things tidy */
}

/* All images stack */
.flyer-container img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(122, 76, 168, 2);
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    animation: fadeCycle 10s infinite;
}

/* First image shows first */
.flyer-container img:nth-child(1) {
    position: relative; /* keeps container height */
    animation-delay: 0s;
}

/* Second image starts later */
.flyer-container img:nth-child(2) {
    animation-delay: 5s;
}

@keyframes fadeCycle {
    0%   { opacity: 0; }
    5%   { opacity: 1; }
    45%  { opacity: 1; }
    50%  { opacity: 0; }
    100% { opacity: 0; }
}
</style>
<p class="zombie-bike-header">ZOMBIES INVADE APPLEGATE PARK!</p>

<p class="subheader">4th Annual Zombie Bike Ride - October 18, 2025</p>

<p>Join <span class="highlight">Cultiva Central Valley &amp; community partners</span> for a <span class="highlight">FREE FAMILY FUN EVENT</span> filled with spooky thrills and zombie chills! Get ready for the most frightening bike ride of the year!</p>

<div class="location-info"><span class="location-text">LOCATION:</span><br />
	Applegate Park<br />
	1045 W. 25th Street<br />
	Merced, CA</div>

<div class="schedule-box"><span class="event-text">EVENT SCHEDULE:</span><br />
	Doors Open: 3:30 PM<br />
	Zombie Ride Launch: 5:00 PM<br />
	<strong>Spooky Movie Night: 7:00 PM</strong><br />
	<em style="color: #7a4ca8;">Bring your favorite blanket, chair &amp; snacks for movie night!</em></div>

<div class="activities-box"><span class="highlight" style="font-size: 1.3rem;">ACTIVITIES INCLUDE:</span> &nbsp;

	<ul class="activities-list">
		<li>Zombie Face Painting</li>
		<li>Zombie Crawler Trail</li>
		<li>Zombie Ride Kick-Off</li>
		<li>Food &amp; Raffle Prizes</li>
		<li>Costume Showcase</li>
		<li>Spooky Fright-Dance Featuring Nintendo Switch</li>
	</ul>
</div>

<div class="volunteer-box"><span class="volunteer-highlight">VOLUNTEER OPPORTUNITIES:</span>

	<p style="margin: 15px 0; font-size: 1.1rem; color: #333;">Help make this spook-tacular event a success! We&#39;re looking for enthusiastic volunteers to join our zombie crew. Stay tuned &mdash; volunteer responsibilities will be posted soon!</p>

	<ul>
		<li><span class="highlight">TBD</span></li>
	</ul>
</div>

<div class="signup-box">
	<h2>Sign Up to Volunteer</h2>

	<p>Click the button below to register as a volunteer for the Merced Zombie Bike Ride.</p>
	<a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_cOaCfDzjORtmrLU" target="_blank">Volunteer Sign-Up</a></div>

<p><strong style="color: #228b22;">Trail Options Available:</strong></p>

<p>Short Trail: 4.7 miles (1 hr 50 min)<br />
	Long Trail: 7.8 miles (3 hr 20 min)<br />
	Both trails feature the <span class="highlight">Long Trail Loop at G Street &amp; Bear Creek</span></p>

<p style="color: #228b22; font-size: 1.2rem; margin-top: 30px;">Don&#39;t miss out on this spine-tingling adventure! Come dressed in your best zombie costume and join the undead cycling brigade for an unforgettable Halloween experience!</p>

<div class="flyer-container"><img alt="Zombie Bike Ride Flyer 1" src="/sites/cec.ucmerced.edu/files/images/event/zombiebikerideflyer2025.jpg" /> <img alt="Zombie Bike Ride Flyer 2" src="/sites/cec.ucmerced.edu/files/images/event/zombiebikerideflyer2025-2.jpg" /></div>
