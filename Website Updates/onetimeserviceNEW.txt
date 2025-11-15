<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* One-Time Service Events - Unique CSS Classes */

        .ots-section-headline {
            border-bottom: 2px solid #ffbf3c;
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
            border: 2px solid #0077cc;
            border-radius: 8px;
            color: #0077cc;
            font-weight: bold;
            text-decoration: none;
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 119, 204, 0.1);
        }
        .ots-event-card-blue a:hover {
            background: linear-gradient(135deg, #0077cc 0%, #005a99 100%);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 119, 204, 0.3);
        }
        
        /* Gold button styling for ongoing events - unique class */
        .ots-event-card-gold a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 4.5em;
            padding: 1em 1.5em;
            border: 2px solid #ffbf3c;
            border-radius: 8px;
            color: #d4851e;
            font-weight: bold;
            text-decoration: none;
            background: linear-gradient(135deg, #fffbf0 0%, #fff4e6 100%);
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(255, 191, 60, 0.1);
        }
        .ots-event-card-gold a:hover {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .ots-page-container {
                margin-right: 20px;
            }
        }
</style>
<div class="ots-page-container">
	<p class="ots-intro-text">The CEC also coordinates and publicizes one-time community service projects which provide students with the opportunity to partner with and get to know new community agencies and organizations and to participate in various short (1-4 hour) service events. Please contact communityservice@ucmerced.edu if you have any questions. Please see our sidebar menu for current projects!</p>

	<h3 class="ots-section-headline">UPCOMING One-Time Service Events</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/events/merced-field-honor-volunteer-opportunities">Field of Honor</a></div>

		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/HHAW">Hunger &amp; Homelessness Awareness Week</a></div>

		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/events/mvpgr-clear-cocklebur">MVPGR Cocklebur Cleanup</a></div>

		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/events/turkey-distribution">Turkey Distribution</a></div>
	</div>

	<h3 class="ots-section-headline">Ongoing One-Time Service Events</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/usda-food-distribution">USDA Food Distribution</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/d-street-shelter">D Street Shelter</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/clean-up">Community Clean-Up</a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/campus-garden">Campus Garden</a></div>
	</div>
</div>