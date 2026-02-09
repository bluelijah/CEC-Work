<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .hhaw-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 0 20px;
        }
        
        /* Hero Section */
        .hhaw-hero {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4373 100%);
            color: white;
            padding: 60px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .hhaw-hero::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 400px;
            height: 400px;
            background-image: url('/sites/cec.ucmerced.edu/files/styles/large/public/page/images/hhaw-logo-screen.png?itok=WDlQHEjs');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.25;
            z-index: 0;
        }
        
        .hhaw-hero > .hhaw-container {
            position: relative;
            z-index: 1;
        }
        
        .hhaw-hero-dates {
            font-size: 1.8em;
            color: #dbaa00;
            font-weight: 600;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .hhaw-hero-subtitle {
            font-size: 1.2em;
            max-width: 800px;
            margin: 0 auto 30px;
            line-height: 1.8;
        }
        
        .hhaw-partners {
            margin-top: 40px;
            padding: 25px;
            border-radius: 10px;
        }
        
        .hhaw-partners-label {
            font-size: 0.95em;
            opacity: 0.9;
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .hhaw-partners-logos {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            flex-wrap: wrap;
        }
        
        .hhaw-partner-logo {
            max-width: 200px;
            height: auto;
        }
        
        .hhaw-partner-logo img {
            width: 100%;
            height: auto;
            display: block;
            filter: drop-shadow(0 0 20px rgba(255,255,255,0.8));
            padding: 20px;
        }
        
        /* Info Section */
        .hhaw-info-section {
            background: white;
            padding: 60px 20px;
        }
        
        .hhaw-section-title {
            font-size: 2.5em;
            color: #0f2d52;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .hhaw-section-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            max-width: 800px;
            margin: 0 auto 40px;
        }
        
        .hhaw-info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .hhaw-info-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px 40px 30px 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hhaw-info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
        }
        
        .hhaw-info-card h3 {
            color: #0f2d52;
            font-size: 1.5em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .hhaw-info-card p {
            line-height: 1.7;
            color: #555;
        }
        
        /* Events Section */
        .hhaw-events-section {
            background: #f8f9fa;
            padding: 60px 20px;
        }
        
        .hhaw-event-card {
            background: white;
            border-left: 5px solid #dbaa00;
            padding: 30px;
            margin-bottom: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .hhaw-event-card:hover {
            border-left-color: #0f2d52;
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        
        /* Split Event Card Layout */
        .hhaw-event-card-split {
            padding: 0;
        }
        
        .hhaw-event-content-wrapper {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0;
            min-height: 500px;
        }
        
        .hhaw-event-text-content {
            padding: 30px;
        }
        
        .hhaw-event-carousel-content {
            background: #f8f9fa;
            padding: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        
        .hhaw-event-flyer-content {
            background: #f8f9fa;
            padding: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .hhaw-event-flyer-content img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .hhaw-event-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        
        .hhaw-event-title {
            color: #0f2d52;
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .hhaw-event-date {
            color: #dbaa00;
            font-weight: 600;
            font-size: 1.1em;
        }
        
        .hhaw-event-location {
            color: #666;
            margin-bottom: 15px;
            font-size: 0.95em;
        }
        
        .hhaw-event-description {
            line-height: 1.6;
            color: #555;
            margin-bottom: 15px;
        }
        
        .hhaw-event-description p {
            margin-bottom: 10px;
        }
        
        .hhaw-status-badge {
            display: inline-block;
            padding: 5px 15px;
            background: #ffc107;
            color: #333;
            border-radius: 15px;
            font-size: 0.9em;
            font-weight: 600;
            margin-left: 10px;
        }
        
        .hhaw-alert {
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        .hhaw-btn {
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
        }
        
        .hhaw-btn:hover {
            background: #0f2d52;
            color: white;
            border-color: #0f2d52;
            transform: scale(1.05);
        }
        
        .hhaw-btn-secondary {
            background: white;
            color: #0f2d52;
            border: 2px solid #0f2d52;
        }
        
        .hhaw-btn-secondary:hover {
            background: #0f2d52;
            color: white;
        }
        
        /* Instagram Carousel */
        .hhaw-instagram-carousel {
            width: 100%;
            max-width: 500px;
            position: relative;
        }
        
        .hhaw-carousel-container {
            position: relative;
            width: 100%;
            height: 600px;
            overflow: hidden;
        }
        
        .hhaw-carousel-slide {
            display: none;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        
        .hhaw-carousel-slide iframe {
            max-height: 600px;
        }
        
        .hhaw-carousel-slide.active {
            display: block;
            animation: hhawFadeIn 0.5s ease-in-out;
        }
        
        @keyframes hhawFadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        .hhaw-carousel-dots {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
        
        .hhaw-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #ccc;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .hhaw-dot.active {
            background: #dbaa00;
            transform: scale(1.2);
        }
        
        .hhaw-dot:hover {
            background: #0f2d52;
        }
        
        /* CTA Section */
        .hhaw-cta-section {
            background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
            padding: 60px 20px;
        }
        
        .hhaw-cta-section h2 {
            text-align: center;
            font-size: 2.5em;
            color: #0f2d52;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .hhaw-cta-section p {
            text-align: center;
            font-size: 1.2em;
            color: #333;
            max-width: 700px;
            margin: 0 auto 30px;
        }
        
        .hhaw-cta-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Footer */
        .hhaw-footer {
            background: #0f2d52;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .hhaw-footer a,
        .hhaw-footer a:link,
        .hhaw-footer a:visited {
            color: #dbaa00 !important;
            text-decoration: none;
            font-weight: 600;
        }
        
        .hhaw-footer a:hover,
        .hhaw-footer a:active {
            color: #ffc107 !important;
            text-decoration: underline;
        }
        
        .hhaw-footer-links {
            margin-top: 20px;
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .hhaw-container {
                padding: 0 10px;
            }
            
            .hhaw-info-section,
            .hhaw-events-section,
            .hhaw-shelter-section {
                padding: 40px 10px;
            }
            
            .hhaw-info-card {
                padding: 20px 15px;
                margin-bottom: 15px;
            }
            
            .hhaw-event-card {
                padding: 20px 15px;
            }
            
            .hhaw-event-card-split {
                padding: 0;
            }
            
            .hhaw-event-content-wrapper {
                grid-template-columns: 1fr;
                min-height: auto;
            }
            
            .hhaw-event-text-content {
                padding: 20px 15px;
            }
            
            .hhaw-event-carousel-content,
            .hhaw-event-flyer-content {
                padding: 20px 15px;
                min-height: 400px;
            }
            
            .hhaw-carousel-container {
                height: 500px;
            }
            
            .hhaw-carousel-slide iframe {
                max-height: 500px;
            }
            
            .hhaw-info-grid {
                gap: 15px;
            }
            
            .hhaw-hero-dates {
                font-size: 1.3em;
            }
            
            .hhaw-hero-subtitle {
                font-size: 1em;
            }
            
            .hhaw-section-title {
                font-size: 2em;
            }
            
            .hhaw-event-header {
                flex-direction: column;
            }
            
            .hhaw-info-grid {
                grid-template-columns: 1fr;
            }
            
            .hhaw-partners-logos {
                flex-direction: column;
                gap: 20px;
            }
            
            .hhaw-partner-logo {
                max-width: 250px;
            }
        }
</style>
<!-- Hero Section -->
<div class="hhaw-hero">
	<div class="hhaw-container">
		<h2 class="hhaw-hero-dates">November 16-22, 2025</h2>

		<p class="hhaw-hero-subtitle">Take part in a national movement to confront hunger and homelessness. UC Merced invites you to join a week of action, learning, and community support from November 16&ndash;22. Together, we can raise awareness, spark change, and uplift those facing housing and food insecurity.</p>

		<div class="hhaw-partners">
			<div class="hhaw-partners-label"><strong>A Collaboration Between</strong></div>

			<div class="hhaw-partners-logos">
				<div class="hhaw-partner-logo"><img alt="Community Engagement Center Logo" src="/sites/cec.ucmerced.edu/files/images/logos/cecgoldbluelogo1.png" style="width: 230px; height: auto;" /></div>

				<div class="hhaw-partner-logo"><img alt="Basic Needs Services Logo" src="/sites/cec.ucmerced.edu/files/documents/mercedbasicneedslogo.png" style="width: 230px; height: auto;" /></div>

				<div class="hhaw-partner-logo"><img alt="Guardian Scholars Program Logo" src="/sites/cec.ucmerced.edu/files/documents/guardainscholarslogo.png" style="width: 170px; height: auto;" /></div>
			</div>
		</div>
	</div>
</div>
<!-- Info Section -->

<div class="hhaw-info-section">
	<div class="hhaw-container">
		<h2 class="hhaw-section-title">Why This Matters</h2>

		<p class="hhaw-section-subtitle">Hunger and Homelessness Awareness Week is an annual program bringing together over 700 colleges, high schools, and community groups nationwide to address critical issues facing our communities.</p>

		<div class="hhaw-info-grid">
			<div class="hhaw-info-card">
				<h3>Students Are Affected</h3>

				<p>Food and housing insecurity affect college students across the country, including right here at UC Merced. Through programs like Basic Needs and Guardian Scholars, we are committed to supporting every Bobcat&rsquo;s well-being and success.</p>
			</div>

			<div class="hhaw-info-card">
				<h3>Your Impact Reaches the Community</h3>

				<p>By participating, you help strengthen local organizations such as the Merced County Community Action Agency and the D Street Shelter &mdash; extending care and resources to those who need it most.</p>
			</div>

			<div class="hhaw-info-card">
				<h3>Small Actions Create Big Change</h3>

				<p>Whether through education, service, or simply showing up, your involvement helps raise awareness and drive meaningful change in our campus and beyond.</p>
			</div>
		</div>
	</div>
</div>
<!-- Events Section -->

<div class="hhaw-events-section">
	<div class="hhaw-container">
		<h2 class="hhaw-section-title">Week of Events</h2>
		<!-- Event: Kick Off Event -->

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Rooted in Resilience</h3>
				</div>

				<div class="hhaw-event-date">Monday, Nov 17</div>
			</div>

			<div class="hhaw-event-location">Location: Commuter Lounge&nbsp;| 5:00 PM - 7:00 PM</div>

			<div class="hhaw-event-description">
				<p>Join us for our Hunger &amp; Homelessness Awareness Week Kickoff!<br />
					We will be watching &quot;Homeless to Harvard&quot; as we reflect on the realities many individuals face and the importance of advocacy, resilience, and compassion within our community. During the film, immerse yourself in the spirit of the season with meaningful arts and crafts that symbolize the growth you&rsquo;ve made during your time on campus.</p>

				<p>We look forward to creating, learning, and reflecting together.&nbsp;</p>
			</div>
		</div>
		<!-- Event: Social Media Campaign -->

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Social Media Campaign</h3>
				</div>

				<div class="hhaw-event-date">Wednesday, Nov 19</div>
			</div>

			<div class="hhaw-event-location">Join us on Instagram!</div>

			<div class="hhaw-event-description">Follow along on Instagram as we share stories, facts, and ways to get involved during&nbsp;Hunger and Homelessness Awareness Week!</div>

			<div style="display: flex; gap: 10px; flex-wrap: wrap;"><a class="hhaw-btn" href="https://www.instagram.com/ucmercedcec/" target="_blank">Follow @ucmercedcec</a> <a class="hhaw-btn" href="https://www.instagram.com/ucmbasicneeds/?hl=en" target="_blank">Follow @ucmbasicneeds</a> <a class="hhaw-btn" href="https://www.instagram.com/guardianscholars_ucm/?hl=en" target="_blank">Follow @ucmguardianscholars</a></div>
		</div>
		<!-- Event: Empty Bowl Project -->

		<div class="hhaw-event-card hhaw-event-card-split">
			<div class="hhaw-event-content-wrapper">
				<div class="hhaw-event-text-content">
					<div class="hhaw-event-header">
						<div>
							<h3 class="hhaw-event-title">Empty Bowl Project</h3>
							<span class="hhaw-status-badge">Limited Space</span></div>

						<div class="hhaw-event-date">Thursday, Nov 20</div>
					</div>

					<div class="hhaw-event-location">Location: California Room</div>

					<div class="hhaw-event-description">
						<p>Join us for an evening of service and learning!&nbsp;All painted bowls will be part of a fundraiser benefiting the Merced County Community Action Agency!</p>

						<p>Plus, earn <strong>1 hour of community service</strong>!</p>
					</div>

					<div class="hhaw-alert"><strong>Registration Required:</strong> Space is limited for this event. Register early to secure your spot!</div>
					<a class="hhaw-btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_1U0zAsL7MQD6M6i" target="_blank">Register Now</a></div>

				<div class="hhaw-event-carousel-content">
					<div class="hhaw-instagram-carousel">
						<div class="hhaw-carousel-container">
							<div class="hhaw-carousel-slide active">
								<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/CW61tZDv418/" data-instgrm-version="14" style="background:#FFF; border:0; border-radius:3px; 
                                    box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 0; 
                                    max-width:100%; min-width:326px; padding:0; width:100%;">&nbsp;</blockquote>
							</div>

							<div class="hhaw-carousel-slide">
								<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/CXNDaVBBS7v/" data-instgrm-version="14" style="background:#FFF; border:0; border-radius:3px; 
                                    box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 0; 
                                    max-width:100%; min-width:326px; padding:0; width:100%;">&nbsp;</blockquote>
							</div>

							<div class="hhaw-carousel-slide">
								<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/CW9M3bBvzV1/" data-instgrm-version="14" style="background:#FFF; border:0; border-radius:3px; 
                                    box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 0; 
                                    max-width:100%; min-width:326px; padding:0; width:100%;">&nbsp;</blockquote>
							</div>
						</div>

						<div class="hhaw-carousel-dots">
							<div class="hhaw-dot active">&nbsp;</div>

							<div class="hhaw-dot">&nbsp;</div>

							<div class="hhaw-dot">&nbsp;</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- Event: Campus Garden -->

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Campus Garden Volunteering</h3>
				</div>

				<div class="hhaw-event-date">Friday, Nov 21</div>
			</div>

			<div class="hhaw-event-location">Campus Garden | 9:00 AM - 11:00 AM</div>

			<div class="hhaw-event-description">Get your hands dirty and help grow fresh produce for our community! Join us at the Campus Garden to learn about sustainable food systems and contribute to food security efforts. No experience necessary &ndash; just bring your enthusiasm and willingness to help!</div>
			<a class="hhaw-btn" href="https://cec.ucmerced.edu/campus-garden" target="_blank">Learn More</a></div>
		<!-- Collaborative Events Section -->

		<h2 class="hhaw-section-title" style="margin-top: 60px;">Collaborative Events</h2>

		<p class="hhaw-section-subtitle">Partner organizations across campus are joining the effort to support our community during Hunger and Homelessness Awareness Week.</p>
		<!-- Event: Gratitude Cards for Community -->

		<div class="hhaw-event-card hhaw-event-card-split">
			<div class="hhaw-event-content-wrapper">
				<div class="hhaw-event-text-content">
					<div class="hhaw-event-header">
						<div>
							<h3 class="hhaw-event-title">Gratitude Cards for Community</h3>

							<h4><strong>Eligible for CatLife Hours!</strong></h4>
						</div>

						<div class="hhaw-event-date">Nov 17-18</div>
					</div>

					<div class="hhaw-event-location">Graduate Cultural Resource Center (COB 2,190) &amp; Asian &amp; Pacific Islander Resource Center (SR 101) | 9:00 AM - 5:00 PM</div>

					<div class="hhaw-event-description">
						<p>Express gratitude and support your community by creating beautiful, creative cards! Students can earn CatLife community service hours by making gratitude cards during the two-day event.</p>

						<p><strong>How it works:</strong></p>

						<ul style="margin-left: 20px; margin-bottom: 15px;">
							<li>Create 1 card = Earn 1 CatLife hour</li>
							<li>Create 2 cards = Earn 2 CatLife hours</li>
							<li>Create 3 cards = Earn 3 CatLife hours (maximum)</li>
						</ul>

						<p>Stop by either location during the two days to participate. All materials will be provided! This event is hosted by Social Justice Initiatives &amp; Identity Programs.</p>
					</div>
				</div>

				<div class="hhaw-event-flyer-content"><img alt="Gratitude Cards Event Flyer" src="/sites/cec.ucmerced.edu/files/images/sjiflyer2.png" /></div>
			</div>
		</div>
		<!-- Event: Cards of Care -->

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Cards of Care</h3>

					<h4><strong>Eligible for CatLife Hours!</strong></h4>
				</div>

				<div class="hhaw-event-date">Tuesday, November 17</div>
			</div>

			<div class="hhaw-event-location">KL 184&nbsp;| 11:00 AM - 1:00 PM</div>

			<div class="hhaw-event-description">We will be showing a short documentary titled, &quot;Silent Voices,&quot; which highlights the experiences of the homeless population in the Central Valley, specifically in Merced. After the video, students will write encouragement cards that will be delivered to the D Street Shelter. In addition, we will be collecting donations of hygiene products to donate to the shelter.</div>
		</div>
		<!-- Event: Care Package Creation & Basic Needs Resource Fair -->

		<div class="hhaw-event-card hhaw-event-card-split">
			<div class="hhaw-event-content-wrapper">
				<div class="hhaw-event-text-content">
					<div class="hhaw-event-header">
						<div>
							<h3 class="hhaw-event-title">Care Package Creation &amp; Resource Fair</h3>
							<span class="hhaw-status-badge">Limited to 50 Students</span>

							<h4><strong>Eligible for CatLife Hours!</strong></h4>
						</div>

						<div class="hhaw-event-date">Tuesday, Nov 19</div>
					</div>

					<div class="hhaw-event-location">Granite 101 | 12:00 PM - 3:00 PM</div>

					<div class="hhaw-event-description">
						<p>Join us for a meaningful afternoon of service! The first 50 students will create care packages to distribute to those in need in our community.</p>

						<p><strong>Event includes:</strong></p>

						<ul style="margin-left: 20px; margin-bottom: 15px;">
							<li>Presentation about Hunger &amp; Homelessness Awareness Week</li>
							<li>Care package assembly (materials provided for 50 packages)</li>
							<li>Basic Needs resource distribution and information</li>
							<li>Complimentary sandwiches and drinks</li>
							<li>Opportunity to distribute packages after creation</li>
						</ul>

						<p>Students will complete a Microsoft Form to confirm attendance and earn CatLife hours. This event is a collaboration with Basic Needs Services, hosted by Social Justice Initiatives &amp; Identity Programs.</p>
					</div>

					<div class="hhaw-alert"><strong>Limited Capacity:</strong> Only 50 students can participate due to materials availability!</div>
				</div>

				<div class="hhaw-event-flyer-content"><img alt="Care Package Event Flyer" src="/sites/cec.ucmerced.edu/files/images/sjiflyer1.png" /></div>
			</div>
		</div>

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Health Promotion Open House</h3>
				</div>

				<div class="hhaw-event-date">Thursday, November 20</div>
			</div>

			<div class="hhaw-event-location">Granite Pass 159&nbsp;| 12:00 PM - 2:00 PM</div>

			<div class="hhaw-event-description">
				<p>The <a href="https://healthpromotion.ucmerced.edu//" style="color: #0f2d52; font-weight: bold; text-decoration: underline;" target="_blank">Health Promotion</a>&nbsp;team is hosting an opportunity to learn about Health Promotion Programs &amp; services and participate in a gratitude activity!</p>

				<p><em>*This event is not eligible for CatLife hours</em></p>
			</div>
		</div>
		<!-- Event: Rotaract Club Meeting -->

		<div class="hhaw-event-card">
			<div class="hhaw-event-header">
				<div>
					<h3 class="hhaw-event-title">Rotaract Club Meeting</h3>

					<h4><strong>Eligible for CatLife Hours!</strong></h4>
				</div>

				<div class="hhaw-event-date">Thursday, November 20</div>
			</div>

			<div class="hhaw-event-location">Glacier 120&nbsp;| 7:00 PM</div>

			<div class="hhaw-event-description">The <a href="https://www.mercedsunriserotary.org/featured-causes" style="color: #0f2d52; font-weight: bold; text-decoration: underline;" target="_blank">Rotaract Club</a>&nbsp;is writing cards of encouragement to people experiencing homelessness.&nbsp;</div>
		</div>
		<!-- CTA Section -->

		<div class="hhaw-cta-section">
			<div class="hhaw-container">
				<h2>Every Action Makes a Difference</h2>

				<p>Whether you participate in events, volunteer, or spread awareness, your involvement matters. Join the UC Merced community in supporting those experiencing hunger and homelessness.</p>

				<div class="hhaw-cta-buttons"><a class="hhaw-btn hhaw-btn-secondary" href="https://basicneeds.ucmerced.edu/" target="_blank">Visit Basic Needs</a> <a class="hhaw-btn hhaw-btn-secondary" href="https://guardianscholars.ucmerced.edu/" target="_blank">Visit Guardian Scholars</a> <a class="hhaw-btn hhaw-btn-secondary" href="https://hhweek.org/" target="_blank">About NHHAW&nbsp;Week</a></div>
			</div>
		</div>
		<!-- Footer -->

		<div class="hhaw-footer">
			<div class="hhaw-container">
				<p><strong>Questions?</strong> Visit us at the&nbsp;Community Engagement Center -&nbsp;KL 190</p>

				<p>Monday - Friday, 9:00 AM - 5:00 PM</p>

				<p><a href="mailto:communityservice@ucmerced.edu">Contact Us</a></p>

				<div class="hhaw-footer-links"><a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a> <a href="https://basicneeds.ucmerced.edu/" target="_blank">Basic Needs</a> <a href="https://guardianscholars.ucmerced.edu/" target="_blank">Guardian Scholars</a> <a href="https://hhweek.org/" target="_blank">National HH Week</a></div>

				<p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2025 UC Merced | Community Engagement Center, Basic Needs, &amp; Guardian Scholars</p>
			</div>
		</div>
		<script async src="//www.instagram.com/embed.js"></script><script>
// Instagram Carousel Functionality
let currentSlide = 0;
const slides = document.querySelectorAll('.hhaw-carousel-slide');
const dots = document.querySelectorAll('.hhaw-dot');
const slideInterval = 5000; // 5 seconds per slide
let autoPlayInterval;

function showSlide(index) {
	slides.forEach(slide => slide.classList.remove('active'));
	dots.forEach(dot => dot.classList.remove('active'));
	
	slides[index].classList.add('active');
	dots[index].classList.add('active');
	
	if (window.instgrm) {
		window.instgrm.Embeds.process();
	}
}

function nextSlide() {
	currentSlide = (currentSlide + 1) % slides.length;
	showSlide(currentSlide);
}

function goToSlide(index) {
	currentSlide = index;
	showSlide(currentSlide);
	resetAutoPlay();
}

function startAutoPlay() {
	autoPlayInterval = setInterval(nextSlide, slideInterval);
}

function resetAutoPlay() {
	clearInterval(autoPlayInterval);
	startAutoPlay();
}

dots.forEach((dot, index) => {
	dot.addEventListener('click', () => goToSlide(index));
});

window.addEventListener('load', () => {
	startAutoPlay();
	setTimeout(() => {
		if (window.instgrm) {
			window.instgrm.Embeds.process();
		}
	}, 1000);
});

const carousel = document.querySelector('.hhaw-instagram-carousel');
if (carousel) {
	carousel.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
	carousel.addEventListener('mouseleave', () => startAutoPlay());
}
</script></div>
</div>
