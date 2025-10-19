<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* Halloween Events Page - Unique CSS Classes */
        
        .halloween-page-headline {
            border-bottom: 3px solid #ff6600;
            padding-bottom: 8px;
            font-size: 2rem;
            color: #1a1a1a;
            text-align: center;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .halloween-intro-text {
            margin-bottom: 2.5rem;
            line-height: 1.6;
            color: #333;
            text-align: center;
            font-size: 1.1rem;
        }
        
        /* Grid layout for event cards */
        .halloween-events-grid {
            display: grid;
            gap: 1.5rem;
            grid-template-columns: 1fr;
            margin-bottom: 2rem;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        
        @media (min-width: 600px) {
            .halloween-events-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        /* Halloween-themed event cards */
        .halloween-event-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 8em;
            padding: 1.5em;
            border: 3px solid #ff6600;
            border-radius: 12px;
            color: #1a1a1a;
            font-weight: bold;
            text-decoration: none;
            background: linear-gradient(135deg, #fff5e6 0%, #ffe6cc 100%);
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(255, 102, 0, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .halloween-event-card:hover {
            background: linear-gradient(135deg, #1a1a1a 0%, #000 100%);
            color: #ff6600;
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 8px 20px rgba(255, 102, 0, 0.6);
            border-color: #ff6600;
        }
        
        /* Event info wrapper */
        .halloween-event-info {
            width: 100%;
            line-height: 1.6;
        }
        
        .halloween-event-info strong {
            font-size: 1.3rem;
            display: block;
            margin-bottom: 0.3rem;
        }
        
        .halloween-event-card:hover .halloween-event-info {
            opacity: 1;
        }
        
        /* Spooky accent elements */
        .halloween-page-headline::before,
        .halloween-page-headline::after {
            content: "★";
            margin: 0 15px;
            color: #ff6600;
        }
        
        /* Decorative divider */
        .halloween-divider {
            height: 2px;
            background: linear-gradient(to right, transparent, #ff6600, transparent);
            margin: 2rem auto;
            max-width: 600px;
        }
        
        /* Bat decorations */
        .halloween-bat-decoration {
            width: 40px;
            height: 40px;
            background-image: url('bats.jpg');
            background-size: cover;
            display: inline-block;
            margin: 0 10px;
            vertical-align: middle;
        }
</style>
<div>
	<h1 class="halloween-page-headline">Halloween Events</h1>

	<p class="halloween-intro-text">Join us for a spooktacular October filled with fun events and community celebrations! Check out all our Halloween happenings below.</p>

	<div class="halloween-divider">&nbsp;</div>

	<div class="halloween-events-grid">
		<div class="halloween-event-info"><a class="halloween-event-card" href="https://cec.ucmerced.edu/events/merced-nut-festival"><strong>Merced Nut Festival</strong><br />
			October 12, 2024 </a></div>

		<div class="halloween-event-info"><a class="halloween-event-card" href="https://cec.ucmerced.edu/events/zombie-bike-ride"><strong>Zombie Bike Ride</strong><br />
			October 19, 2024 </a></div>

		<div class="halloween-event-info"><a class="halloween-event-card" href="https://cec.ucmerced.edu/events/zoo-boo"><strong>Zoo Boo</strong><br />
			October 24-26, 2024 </a></div>

		<div class="halloween-event-info"><a class="halloween-event-card" href="https://cec.ucmerced.edu/events/halloween-dance-party"><strong>Halloween Dance Party</strong><br />
			October 31, 2024 </a></div>
	</div>

	<div class="halloween-divider">&nbsp;</div>

	<p class="halloween-intro-text" style="font-size: 0.95rem; margin-top: 2rem;">For more information about any of these events, click on the event card or contact us at <a href="mailto:communityservice@ucmerced.edu" style="color: #ff6600; text-decoration: underline;">communityservice@ucmerced.edu</a></p>
</div>
