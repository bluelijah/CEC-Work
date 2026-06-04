<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* One-Time Service Events - Unique CSS Classes */
        .ots-section-headline {
            text-align: center;
            border-bottom: 2px solid #ffbf3c;
            padding-bottom: 6px;
            margin: 24px 0 12px;
            font-size: 1.25rem;
            color: #333;
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
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 7.5em;
            max-height: 7.5em;
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
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 7.5em;
            max-height: 7.5em;
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
        
        /* Toggle button styles for past events - unique class */
        .ots-past-events-toggle {
            cursor: pointer;
            font-weight: bold;
            color: #0077cc;
            padding: 0.75em 1.5em;
            border: 2px solid #0077cc;
            border-radius: 8px;
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
            transition: all 0.3s ease;
            user-select: none;
            display: inline-block;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 119, 204, 0.1);
        }
        .ots-past-events-toggle:hover {
            background: linear-gradient(135deg, #0077cc 0%, #005a99 100%);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 119, 204, 0.3);
        }
        
        /* Arrow indicator for toggle button - unique class */
        .ots-past-events-toggle::after {
            content: " ▼";
            font-size: 0.9em;
            margin-left: 8px;
        }
        .ots-past-events-toggle.ots-toggle-expanded::after {
            content: " ▲";
        }
        
        /* Past events container - hidden by default - unique class */
        .ots-past-events-container {
            display: none;
            margin-top: 1rem;
        }
        
        /* Smooth transition when showing/hiding - unique class */
        .ots-past-events-container.ots-container-show {
            display: block;
            animation: otsFadeIn 0.4s ease-in;
        }
        
        @keyframes otsFadeIn {
            from { 
                opacity: 0; 
                transform: translateY(-10px); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0); 
            }
        }
        
        /* Past events use blue styling but smaller - unique class */
        .ots-event-card-past a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 3.5em;
            padding: 0.75em 1em;
            border: 2px solid #0077cc;
            border-radius: 6px;
            color: #0077cc;
            font-weight: 600;
            font-size: 0.9em;
            text-decoration: none;
            background: linear-gradient(135deg, #f8fbff 0%, #f0f7ff 100%);
            transition: all 0.3s ease;
            box-shadow: 0 1px 4px rgba(0, 119, 204, 0.1);
        }
        .ots-event-card-past a:hover {
            background: linear-gradient(135deg, #0077cc 0%, #005a99 100%);
            color: #fff;
            transform: translateY(-1px);
            box-shadow: 0 3px 10px rgba(0, 119, 204, 0.25);
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .sig-page-container {
                margin-right: 20px;
            }
        }
</style>
<div class="sig-page-container">
	<p class="ots-intro-text">In addition to providing service hours, we are also happy to present additional community engagement opportunities! This includes informational sessions, awareness events, and philanthropy. Please see below to learn more about our signature opportunities.</p>

	<h3 class="ots-section-headline">Community Service</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/pathways">Pathways of Public Service and Civic Engagement<br />
			<span style="font-size: 0.85em; font-weight: normal;">Find the area of community service that works best for you! </span> </a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/psa">Public Service Announcements<br />
			<span style="font-size: 0.85em; font-weight: normal;">An info session of upcoming opportunities followed by an arts-and-crafts service event </span> </a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/Alternative/Spring/Break/2026">Alternative Spring Break 2026<br />
			<span style="font-size: 0.85em; font-weight: normal;">Learn as guests on Yurok land in this unique experience! </span> </a></div>
	</div>

	<h3 class="ots-section-headline">Events &amp; Happenings</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/HHAW-23">Hunger &amp; Homelessness Awareness Week<br />
			<br />
			<span style="font-size: 0.85em; font-weight: normal;">A national awareness week co-led by multiple UC Merced departments</span></a></div>

		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/psa">Public Service Announcements<br />
			<br />
			<span style="font-size: 0.85em; font-weight: normal;">An info session of upcoming opportunities followed by an arts-and-crafts service event</span></a></div>

		<div class="ots-event-card-blue"><a href="https://cec.ucmerced.edu/Donald/A/Strauss/Foundation/Scholarship">Donald A. Strauss Foundation Scholarship Opportunity<br />
			<br />
			<span style="font-size: 0.85em; font-weight: normal;">A Scholarship Opportunity for our Service Oriented students!</span></a></div>
	</div>

	<h3 class="ots-section-headline">Philanthropy</h3>

	<div class="ots-events-grid">
		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/Thanks/for/Giving">Holiday Meals<br />
			<br />
			<span style="font-size: 0.85em; font-weight: normal;">A food drive for local families</span></a></div>

		<div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/meals-for-families">Home for the Holidays<br />
			<br />
			<span style="font-size: 0.85em; font-weight: normal;">Support a family</span></a></div>
	</div>
</div>
