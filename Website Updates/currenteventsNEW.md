<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* Headline and intro */
        .head-line {
            border-bottom: 2px solid #ffbf3c;
            padding-bottom: 6px;
            margin: 24px 0 12px;
            font-size: 1.25rem;
        }
        .intro {
            margin-bottom: 1rem;
            line-height: 1.5;
        }
        
        /* Grid layout for event cards */
        .events-grid {
            display: grid;
            gap: 1rem;
            grid-template-columns: 1fr;
        }
        @media (min-width: 600px) {
            .events-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (min-width: 900px) {
            .events-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        /* Event cards */
        .event-card a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 4.5em;
            padding: 0.5em 1em;
            border: 2px solid #0077cc;
            border-radius: 8px;
            color: #0077cc;
            font-weight: bold;
            text-decoration: none;
            background: #f9f9f9;
            transition: all 0.2s ease-in-out;
        }
        .event-card a:hover {
            background: #0077cc;
            color: #fff;
        }
        
        /* Toggle button styles */
        .toggle-button {
            cursor: pointer;
            font-weight: bold;
            color: #0077cc;
            padding: 0.5em 1em;
            border: 2px solid #0077cc;
            border-radius: 6px;
            background: #f0f8ff;
            transition: all 0.2s ease-in-out;
            user-select: none;
            display: inline-block;
            margin-bottom: 1rem;
        }
        .toggle-button:hover {
            background: #0077cc;
            color: #fff;
        }
        
        /* Arrow indicator */
        .toggle-button::after {
            content: " ▼";
            font-size: 0.9em;
        }
        .toggle-button.expanded::after {
            content: " ▲";
        }
        
        /* Past events container - hidden by default */
        .past-events-container {
            display: none;
            margin-top: 1rem;
        }
        
        /* Smooth transition when showing/hiding */
        .past-events-container.show {
            display: block;
            animation: fadeIn 0.3s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
</style>
<p class="intro">Please see some of our ongoing events below and stay tuned on our social media and website for more updates!</p>

<h3 class="head-line">Regularly Scheduled Events &amp; Programs</h3>

<div class="events-grid">
	<div class="event-card"><a href="https://cec.ucmerced.edu/usda-food-distribution">USDA Food Distribution</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/d-street-shelter">D Street Shelter</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/campus-garden">Campus Garden</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/americorps">AmeriCorps Public Service Fellowship</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/jamboree">Community Jamboree</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/impact-initiatives">Our Programs</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/one-time-service-projects">One-Time Service</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/hha-week">Hunger &amp; Homelessness Awareness Week</a></div>

	<div class="event-card"><a href="https://cec.ucmerced.edu/pathways">Public Service Pathways</a></div>
</div>

<h3 class="head-line">Past Events &amp; Programs</h3>

<div class="toggle-button" id="pastEventsToggle" onclick="togglePastEvents()">View Past Events</div>

<div class="past-events-container" id="pastEventsContainer">
	<div class="events-grid">
		<div class="event-card"><a href="https://cec.ucmerced.edu/wellness-day">Wellness Day</a></div>

		<div class="event-card"><a href="https://cec.ucmerced.edu/virtual-service-talks">Virtual Service Talks</a></div>

		<div class="event-card"><a href="https://cec.ucmerced.edu/current-events/candidate-conversations">Candidates and Conversations</a></div>

		<div class="event-card"><a href="https://cec.ucmerced.edu/mlk-week">MLK Jr. Celebration</a></div>

		<div class="event-card"><a href="https://cec.ucmerced.edu/mlk-day-of-service">MLK Day of Service</a></div>
	</div>
</div>
<script>
        function togglePastEvents() {
            const container = document.getElementById('pastEventsContainer');
            const button = document.getElementById('pastEventsToggle');
            
            if (container.style.display === 'none' || container.style.display === '') {
                // Show past events
                container.style.display = 'block';
                container.classList.add('show');
                button.classList.add('expanded');
                button.textContent = 'Hide Past Events';
            } else {
                // Hide past events
                container.style.display = 'none';
                container.classList.remove('show');
                button.classList.remove('expanded');
                button.textContent = 'View Past Events';
            }
        }
    </script>