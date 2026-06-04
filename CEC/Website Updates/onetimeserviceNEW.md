<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* One-Time Service Events - Unique CSS Classes */

        .ots-section-headline {
            border-bottom: 2px solid #DAA900;
            padding-bottom: 6px;
            margin: 24px 0 12px;
            font-size: 1.25rem;
            color: #333;
            text-align: center;
        }
        
        .ots-intro-text {
            margin-bottom: 2rem;
            line-height: 1.5;
            color: #555;
        }
        
        /* Grid layout for event cards - unique class */
        .ots-events-grid {
            display: grid;
            gap: 1.5rem;
            grid-template-columns: 1fr;
            margin-bottom: 2rem;
        }
        @media (min-width: 600px) {
            .ots-events-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (min-width: 900px) {
            .ots-events-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        /* Blue button styling for upcoming events - unique class */
        .ots-event-card-blue a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 4.5em;
            padding: 1em 1.5em;
            border: 2px solid #002856;
            border-radius: 8px;
            /* #002856 on #f0f4f9 = 14.1:1 (WCAG AAA) */
            color: #002856;
            font-weight: bold;
            text-decoration: none !important;
            background-color: #f0f4f9;
            transition: all 0.3s ease;
        }
        .ots-event-card-blue a:hover {
            /* #f0f4f9 on #002856 = 13.8:1 (WCAG AAA) */
            background-color: #002856;
            color: #f0f4f9 !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 40, 86, 0.3);
        }
        .ots-event-card-blue a:focus-visible {
            outline: 3px solid #002856;
            outline-offset: 3px;
            border-radius: 8px;
        }
        
        /* Gold button styling for ongoing events - unique class */
        .ots-event-card-gold a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 4.5em;
            padding: 1em 1.5em;
            border: 2px solid #DAA900;
            border-radius: 8px;
            /* #002856 on #fffdf0 = 14.4:1 (WCAG AAA) */
            color: #002856;
            font-weight: bold;
            text-decoration: none !important;
            background-color: #fffdf0;
            transition: all 0.3s ease;
        }
        .ots-event-card-gold a:hover {
            /* #002856 on #DAA900 = 6.7:1 (WCAG AA) */
            background-color: #DAA900;
            color: #002856 !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(218, 169, 0, 0.35);
        }
        .ots-event-card-gold a:focus-visible {
            outline: 3px solid #002856;
            outline-offset: 3px;
            border-radius: 8px;
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .ots-page-container {
                margin-right: 20px;
            }
        }
</style>
<div class="ots-page-container">
	<p class="ots-intro-text">The CEC also coordinates and publicizes one-time community service projects which provide students with the opportunity to partner with and get to know new community agencies and organizations and to participate in various short (1-4 hour) service events. Please contact <a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a> if you have any questions. Please see our sidebar menu for current projects!</p>

	<h3 class="ots-section-headline">UPCOMING One-Time Service Events</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/calendar">No Upcoming Events</a></div>
	</div>

	<h3 class="ots-section-headline">Ongoing One-Time Service Events</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/usda-food-distribution">USDA Food Distribution</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/d-street-shelter">D Street Shelter</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/clean-up">Community Clean-Up</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/campus-garden">Campus Garden</a></div>
	</div>
</div>