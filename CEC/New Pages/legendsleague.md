<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&amp;family=DM+Sans:wght@400;500;600&amp;display=swap" rel="stylesheet" />
<style type="text/css">* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
    --blue:       #0f2d52;
    --blue-mid:   #1a4373;
    --blue-light: #2a5a96;
    --gold:       #dbaa00;
    --gold-light: #f5d84a;
    --gold-pale:  #fff8dc;
    --off-white:  #f7f5f0;
}

body {
    font-family: 'DM Sans', sans-serif;
    background: var(--off-white);
    color: var(--blue);
}

/* ── Hero ── */
.ll-hero {
    background: url('/sites/g/files/ufvvjh1016/f/documents/Posyer/Poster/poster_.png') center / cover no-repeat;
    min-height: 300px;
    width: 100%;
    display: block;
}

/* ── Container ── */
.ll-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 32px;
}

/* ── Intro Section ── */
.ll-intro {
    background: var(--blue);
    padding: 64px 32px;
    position: relative;
    overflow: hidden;
}

.ll-intro::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 320px; height: 320px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(219,170,0,0.15) 0%, transparent 70%);
    pointer-events: none;
}

.ll-intro::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -40px;
    width: 280px; height: 280px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(219,170,0,0.10) 0%, transparent 70%);
    pointer-events: none;
}

.ll-intro-inner {
    position: relative;
    z-index: 1;
    max-width: 100%;
}

.ll-eyebrow {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1em;
    letter-spacing: 0.25em;
    color: var(--gold);
    margin-bottom: 16px;
    display: block;
}

.ll-intro h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3em;
    color: white;
    line-height: 1.05;
    margin-bottom: 20px;
}

.ll-intro h2 span {
    color: var(--gold);
}

.ll-intro p {
    font-size: 1.1em;
    color: rgba(255,255,255,0.85);
    line-height: 1.75;
    margin-bottom: 16px;
}

.ll-intro p a {
    color: var(--gold) !important;
    font-weight: 600;
    text-decoration: none;
    border-bottom: 1px solid rgba(219,170,0,0.4);
    transition: border-color 0.2s;
}

.ll-intro p a:hover {
    border-color: var(--gold);
}

.ll-challenge {
    display: inline-block;
    margin-top: 8px;
    background: var(--gold);
    color: var(--blue) !important;
    font-weight: 700;
    font-size: 1.05em;
    padding: 14px 32px;
    border-radius: 4px;
    text-decoration: none !important;
    letter-spacing: 0.03em;
    transition: all 0.2s;
}

.ll-challenge:hover {
    background: var(--gold-light);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(219,170,0,0.35);
}

/* ── How To Play ── */
.ll-howto {
    background: white;
    padding: 72px 32px;
}

.ll-section-label {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2em;
    color: var(--blue);
    margin-bottom: 40px;
    display: flex;
    align-items: center;
    gap: 16px;
}

.ll-section-label::after {
    content: '';
    flex: 1;
    height: 3px;
    background: linear-gradient(to right, var(--gold), transparent);
    border-radius: 2px;
}

.ll-steps {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.ll-step {
    background: var(--off-white);
    border-radius: 8px;
    padding: 32px 28px;
    border-top: 4px solid var(--gold);
    position: relative;
}

.ll-step-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 4em;
    color: rgba(15,45,82,0.08);
    position: absolute;
    top: 12px; right: 20px;
    line-height: 1;
}

.ll-step h3 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5em;
    color: var(--blue);
    letter-spacing: 0.04em;
    margin-bottom: 8px;
}

.ll-step p {
    font-size: 0.95em;
    color: #555;
    line-height: 1.7;
}

/* ── Trade In Section ── */
.ll-tradein {
    background: var(--off-white);
    padding: 72px 32px;
}

.ll-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
}

.ll-card {
    background: white;
    border-radius: 10px;
    padding: 36px 32px;
    border-left: 5px solid var(--gold);
    box-shadow: 0 4px 16px rgba(15,45,82,0.07);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.ll-card::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 80px; height: 80px;
    background: radial-gradient(circle at top right, rgba(219,170,0,0.12), transparent 70%);
}

.ll-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(15,45,82,0.12);
    border-left-color: var(--blue);
}

.ll-card-badge {
    display: inline-block;
    background: var(--gold);
    color: var(--blue);
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.85em;
    letter-spacing: 0.12em;
    padding: 4px 12px;
    border-radius: 3px;
    margin-bottom: 16px;
}

.ll-card h3 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.6em;
    color: var(--blue);
    letter-spacing: 0.03em;
    margin-bottom: 10px;
    line-height: 1.1;
}

.ll-card p {
    font-size: 0.95em;
    color: #555;
    line-height: 1.75;
}

.ll-card p strong {
    color: var(--blue);
}

/* ── Launch Banner ── */
.ll-launch {
    background: linear-gradient(135deg, var(--gold) 0%, #f0c830 100%);
    padding: 56px 32px;
    text-align: center;
}

.ll-launch-date {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1em;
    letter-spacing: 0.3em;
    color: var(--blue);
    opacity: 0.7;
    margin-bottom: 10px;
}

.ll-launch h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.2em;
    color: var(--blue);
    line-height: 1.05;
    margin-bottom: 16px;
}

.ll-launch p {
    font-size: 1.1em;
    color: rgba(15,45,82,0.8);
    max-width: 560px;
    margin: 0 auto 28px;
    line-height: 1.7;
}

.ll-launch-detail {
    display: inline-block;
    background: var(--blue);
    color: var(--gold) !important;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1em;
    letter-spacing: 0.08em;
    padding: 14px 36px;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s;
}

.ll-launch-detail:hover {
    background: var(--blue-mid);
    transform: translateY(-2px);
}

/* ── Footer ── */
.ll-footer {
    background: var(--blue);
    color: white;
    padding: 40px 32px;
    text-align: center;
}

.ll-footer a,
.ll-footer a:link,
.ll-footer a:visited {
    color: var(--gold) !important;
    text-decoration: none;
    font-weight: 600;
}

.ll-footer a:hover {
    color: var(--gold-light) !important;
    text-decoration: underline;
}

.ll-footer-links {
    margin-top: 20px;
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

/* ── Mobile ── */
@media (max-width: 768px) {
    .ll-hero { min-height: 240px; }
    .ll-intro h2 { font-size: 2.2em; }
    .ll-steps { grid-template-columns: 1fr; }
    .ll-cards { grid-template-columns: 1fr; }
    .ll-launch h2 { font-size: 2.2em; }
    .ll-container { padding: 0 16px; }
    .ll-intro, .ll-howto, .ll-tradein, .ll-launch { padding-left: 16px; padding-right: 16px; }
}
</style>
<!-- Hero — banner image only -->
<div class="ll-hero">&nbsp;</div>
<!-- Intro -->

<div class="ll-intro">
	<div class="ll-container">
		<div class="ll-intro-inner"><span class="ll-eyebrow">Legends League Collectible Cards</span>

			<h2>Your Backstage Pass to the <span>People Behind the Lectures</span></h2>

			<p>Each card reveals a faculty member&#39;s real-world journey from the expertise they&#39;ve gained to the career areas they influence. Discover their professional path and the best ways to connect so you can level up your own future.</p>

			<p>Are you ready to take on the challenge to find all 16? We&#39;ve got a full deck of faculty legends waiting for you <a href="#">right here</a>.</p>
			<a class="ll-challenge" href="#" style="color: #0f2d52 !important;">View the Full Deck &rarr;</a></div>
	</div>
</div>
<!-- How to Play -->

<div class="ll-howto">
	<div class="ll-container">
		<div class="ll-section-label">How to Play</div>

		<div class="ll-steps">
			<div class="ll-step"><span class="ll-step-num">01</span>

				<h3>Collect</h3>

				<p>Pick up cards at the Career Center by connecting with staff during workshops, career events, or campus tabling sessions.</p>
			</div>

			<div class="ll-step"><span class="ll-step-num">02</span>

				<h3>Connect</h3>

				<p>Visit faculty members directly to collect their card and start a real conversation about your future.</p>
			</div>

			<div class="ll-step"><span class="ll-step-num">03</span>

				<h3>Trade</h3>

				<p>Complete your set by trading duplicates with fellow participants. The more you connect, the closer you get to a full deck.</p>
			</div>
		</div>
	</div>
</div>
<!-- Trade In -->

<div class="ll-tradein">
	<div class="ll-container">
		<div class="ll-section-label">Trade Them In</div>

		<div class="ll-cards">
			<div class="ll-card"><span class="ll-card-badge">School Set Reward</span>

				<h3>Collect Your School Set</h3>

				<p>Collect all <strong>5 cards</strong> from your corresponding school <strong>SOE, SNS, or SSHA</strong> and trade them in at the Career Center for exclusive swag.</p>
			</div>

			<div class="ll-card"><span class="ll-card-badge">Golden Card Combo</span>

				<h3>The Golden Card Combo</h3>

				<p>Collect <strong>3 cards</strong> from your corresponding school <strong>SOE, SNS, or SSHA</strong> plus a <strong>Golden Card</strong>, and exchange them for a prize at the Career Center.</p>
			</div>
		</div>
	</div>
</div>
<!-- Launch Banner -->

<div class="ll-launch">
	<div class="ll-container">
		<div class="ll-launch-date">New Deck Every Year</div>

		<h2>The 2026 Deck Drops April 22nd</h2>

		<p>A new deck releases each year so there&#39;s always more to collect. Don&#39;t miss the first launch event!</p>
		<a class="ll-launch-detail" href="#">April 22 &bull; 3:00 &ndash; 4:30 PM &bull; Conference Center</a></div>
</div>
<!-- Footer -->

<div class="ll-footer">
	<div class="ll-container">
		<p><strong>Questions?</strong> Contact the Community Engagement Center at KL 190</p>

		<p>Monday &ndash; Friday, 9:00 AM &ndash; 5:00 PM</p>

		<p>You can also <a href="/cdn-cgi/l/email-protection#3a595557574f54534e43495f484c53595f7a4f59575f48595f5e145f5e4f">email us</a></p>

		<div class="ll-footer-links"><a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a> <a href="https://cec.ucmerced.edu/calendar" target="_blank">CEC Calendar</a></div>

		<p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2026 UC Merced | Community Engag</p>
	</div>
</div>
