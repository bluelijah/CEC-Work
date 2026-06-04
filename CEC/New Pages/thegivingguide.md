<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .sog-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 0 20px;
        }
        
        /* Hero Section */
        .sog-hero {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4373 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .sog-hero::before {
            content: '';
            position: absolute;
            width: 200px;
            height: 200px;
            background-image: url('/sites/cec.ucmerced.edu/files/images/snowflake.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.15;
            top: 20%;
            left: 10%;
            animation: snowFloat 10s ease-in-out infinite;
        }
        
        .sog-hero::after {
            content: '';
            position: absolute;
            width: 300px;
            height: 300px;
            background-image: url('/sites/cec.ucmerced.edu/files/images/present.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.15;
            bottom: 10%;
            right: 15%;
            animation: snowFloat 12s ease-in-out infinite reverse;
        }
        
        @keyframes snowFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .sog-hero > .sog-container {
            position: relative;
            z-index: 1;
        }
        
        .sog-hero-title {
            font-size: 3.5em;
            color: #dbaa00;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .sog-hero-subtitle {
            font-size: 1.5em;
            color: #dbaa00;
            font-style: italic;
            margin-bottom: 15px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        
        .sog-hero-description {
            font-size: 1.2em;
            max-width: 800px;
            margin: 0 auto 20px;
            line-height: 1.8;
        }
        
        .sog-partners {
            margin-top: 30px;
            padding: 25px;
            border-radius: 10px;
        }
        
        .sog-partners-label {
            font-size: 0.95em;
            opacity: 0.9;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .sog-partners-logos {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            flex-wrap: wrap;
        }
        
        .sog-partner-logo {
            max-width: 300px;
            height: auto;
        }
        
        .sog-partner-logo img {
            width: 100%;
            height: auto;
            display: block;
            filter: drop-shadow(0 0 40px rgba(255,255,255,1)) drop-shadow(0 0 40px rgba(255,255,255,1));
            padding: 20px;
        }
        
        /* Info Section */
        .sog-info-section {
            background: white;
            padding: 60px 20px;
        }
        
        .sog-section-title {
            font-size: 2.5em;
            color: #0f2d52;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .sog-section-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            max-width: 800px;
            margin: 0 auto 40px;
        }
        
        /* Events Section */
        .sog-events-section {
            background: #f8f9fa;
            padding: 60px 20px;
        }
        
        .sog-event-card {
            background: white;
            border-left: 5px solid #dbaa00;
            padding: 30px;
            margin-bottom: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .sog-event-card:hover {
            border-left-color: #0f2d52;
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            transform: translateY(-3px);
        }
        
        /* Split Event Card Layout */
        .sog-event-card-split {
            padding: 0;
        }
        
        .sog-event-content-wrapper {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0;
            min-height: 500px;
        }
        
        .sog-event-text-content {
            padding: 30px;
        }
        
        .sog-event-flyer-content {
            background: #f8f9fa;
            padding: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .sog-event-flyer-content img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .sog-event-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        
        .sog-event-title {
            color: #0f2d52;
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .sog-event-subtitle {
            color: #dbaa00;
            font-weight: 600;
            font-size: 1.1em;
            font-style: italic;
        }
        
        .sog-event-description {
            line-height: 1.8;
            color: #555;
            margin-bottom: 20px;
        }
        
        .sog-event-details {
            background: #FFF8E7;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 3px solid #dbaa00;
        }
        
        .sog-event-details h4 {
            color: #0f2d52;
            font-size: 1.1em;
            margin-bottom: 10px;
        }
        
        .sog-event-details ul {
            margin-left: 20px;
            color: #555;
            line-height: 1.8;
        }
        
        .sog-status-badge {
            display: inline-block;
            padding: 5px 15px;
            background: #dbaa00;
            color: #0f2d52;
            border-radius: 15px;
            font-size: 0.9em;
            font-weight: 600;
            margin-left: 10px;
        }
        
        .sog-status-badge.completed {
            background: #dbaa00;
        }
        
        .sog-alert {
            background: #FFF8E7;
            border-left: 5px solid #dbaa00;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        .sog-btn {
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
        
        .sog-btn:hover {
            background: #0f2d52;
            color: white;
            border-color: #0f2d52;
            transform: scale(1.05);
        }
        
        .sog-btn-secondary {
            background: white;
            color: #0f2d52;
            border: 2px solid #0f2d52;
        }
        
        .sog-btn-secondary:hover {
            background: #0f2d52;
            color: white;
        }
        
        /* CTA Section */
        .sog-cta-section {
            background: linear-gradient(135deg, #dbaa00 0%, #ffc107 100%);
            padding: 60px 20px;
        }
        
        .sog-cta-section h2 {
            text-align: center;
            font-size: 2.5em;
            color: #0f2d52;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .sog-cta-section p {
            text-align: center;
            font-size: 1.2em;
            color: #333;
            max-width: 700px;
            margin: 0 auto 30px;
        }
        
        .sog-cta-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Footer */
        .sog-footer {
            background: #0f2d52;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .sog-footer a,
        .sog-footer a:link,
        .sog-footer a:visited {
            color: #dbaa00 !important;
            text-decoration: none;
            font-weight: 600;
        }
        
        .sog-footer a:hover,
        .sog-footer a:active {
            color: #ffc107 !important;
            text-decoration: underline;
        }
        
        .sog-footer-links {
            margin-top: 20px;
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .sog-container {
                padding: 0 10px;
            }
            
            .sog-hero {
                padding: 50px 20px;
            }
            
            .sog-hero-title {
                font-size: 2.2em;
            }
            
            .sog-hero-subtitle {
                font-size: 1.2em;
            }
            
            .sog-hero-description {
                font-size: 1em;
            }
            
            .sog-info-section,
            .sog-events-section {
                padding: 40px 10px;
            }
            
            .sog-event-card {
                padding: 20px 15px;
            }
            
            .sog-event-card-split {
                padding: 0;
            }
            
            .sog-event-content-wrapper {
                grid-template-columns: 1fr;
                min-height: auto;
            }
            
            .sog-event-text-content {
                padding: 20px 15px;
            }
            
            .sog-event-flyer-content {
                padding: 20px 15px;
                min-height: 400px;
            }
            
            .sog-section-title {
                font-size: 2em;
            }
            
            .sog-event-header {
                flex-direction: column;
            }
            
            .sog-partners-logos {
                flex-direction: column;
                gap: 20px;
            }
            
            .sog-partner-logo {
                max-width: 250px;
            }
        }
</style>
<!-- Hero Section -->
<div class="sog-hero">
	<div class="sog-container">
		<p class="sog-hero-subtitle">Share Joy. Spread Hope. Make a Difference.</p>

		<p class="sog-hero-description">Join UC Merced in spreading holiday cheer and supporting our local community. Your generosity can make a meaningful difference in the lives of families and youth in need this holiday season.</p>

		<div class="sog-partners">
			<div class="sog-partners-label">A Collaboration Between</div>

			<div class="sog-partners-logos">
				<div class="sog-partner-logo"><img alt="Community Engagement Center Logo" src="/sites/cec.ucmerced.edu/files/images/logos/cecgoldbluelogo1.png" style="width: 250px; height: auto;" /></div>

				<div class="sog-partner-logo"><img alt="Guardian Scholars Program Logo" src="/sites/cec.ucmerced.edu/files/documents/guardainscholarslogo.png" style="width: 170px; height: auto;" /></div>
			</div>
		</div>
	</div>
</div>
<!-- Events Section -->

<div class="sog-events-section">
	<div class="sog-container"><!-- Active Involvement Section -->
		<h3 class="sog-section-title" style="font-size: 2em; margin-top: 40px; margin-bottom: 30px;">Intentional Giving</h3>

		<p style="text-align: center;">Make a personal impact by engaging directly in the joy of giving. Select a family, purchase meaningful gifts, and wrap them with care. These hands-on contributions create memorable experiences and remind children and families that they are valued and supported.</p>

		<p style="text-align: center;">&nbsp;</p>
		<!-- Event: Home for the Holidays -->

		<div class="sog-event-card">
			<div class="sog-event-header">
				<div>
					<h3 class="sog-event-title">A Home for the Holidays</h3>

					<p class="sog-event-subtitle">Community Engagement Center</p>
				</div>
			</div>

			<div class="sog-event-description">We invite all members of the campus community to &quot;adopt a family&quot; by selecting an envelope from any of four wreaths&nbsp;on campus. When adopting a family, you commit to purchasing a gift for each child.</div>

			<div class="sog-event-details">
				<h4>How to Participate:</h4>

				<ul>
					<li>Visit one of the wreaths on campus</li>
					<li>Select an envelope with family information</li>
					<li>Purchase a gift for each child and <strong>wrap </strong>the gifts!</li>
					<li>Drop off your gifts at: <strong>Community Engagement Center (KL 190)&nbsp;</strong></li>
					<li><strong>Drop-off Hours:</strong> Monday - Friday, 9:00 AM - 4:00 PM</li>
					<li><strong>Deadline:</strong> All gifts must be dropped off by Wednesday, December 17th at 4:00 PM at the CEC or DCC</li>
					<li>Unwrapped toys can be dropped off at the same location</li>
				</ul>
			</div>

			<div class="sog-event-details">
				<h4>Wreath Locations:</h4>

				<ul>
					<li>Location 1: The Downtown Campus Center (DCC)</li>
					<li>Location 2: Administration Building 3rd Floor</li>
					<li>Location 3: The Community Engagement Center (KL 190)</li>
					<li>Location 4: Engineering Suite 315</li>
				</ul>
			</div>

			<div class="sog-alert"><strong>Note:</strong> All gifts and toys will be distributed through All Dads Matter &amp; Merced County HSA. If you have questions, please email us at <a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a>.</div>
		</div>
		<!-- Event: SSHA Holiday Toy Drive -->

		<div class="sog-event-card sog-event-card-split">
			<div class="sog-event-content-wrapper">
				<div class="sog-event-text-content">
					<div class="sog-event-header">
						<div>
							<h3 class="sog-event-title">SSHA Annual Holiday Toy Drive</h3>

							<p class="sog-event-subtitle">Merced Police &amp; Fire Department</p>
						</div>
					</div>

					<div class="sog-event-description">Join the SSHA (School of Social Sciences, Humanities and Arts) in partnership with the Merced Police &amp; Fire Department for their annual Holiday Toy Drive! Help bring joy to children in our community by donating unwrapped toys and books.</div>

					<div class="sog-event-details">
						<h4>Donation Details:</h4>

						<ul>
							<li><strong>Accepting:</strong> All unwrapped toys, books, and supplementary supplies to enable youth activity.</li>
							<li><strong>Especially Need:</strong> Ages 10-12 years old gifts (art kits, bracelet kits, sports balls, legos, etc.)</li>
							<li><strong>Collection Period:</strong> November 20th - December 4th</li>
						</ul>
					</div>

					<div class="sog-event-details">
						<h4>Drop-Off Locations:</h4>

						<ul>
							<li><strong>SSHA Dean&#39;s Suite Reception</strong> (COB-1 259)</li>
							<li><strong>UC Merced Beginnings Lighting Event</strong><br />
								CTK Quad | December 4th, 2025 at 4:30 PM</li>
						</ul>
					</div>

					<div class="sog-alert"><strong>Questions?</strong> Contact Ericka Garcia at <a href="mailto:egarcia225@ucmerced.edu" style="color: #0f2d52; font-weight: bold;">egarcia225@ucmerced.edu</a></div>
				</div>

				<div class="sog-event-flyer-content"><img alt="SSHA Holiday Toy Drive Flyer" src="/sites/cec.ucmerced.edu/files/images/toydrive.png" /></div>
			</div>
		</div>
		<!-- Event: Items for Youth -->

		<div class="sog-event-card">
			<div class="sog-event-header">
				<div>
					<h3 class="sog-event-title">Items for Youth</h3>

					<p class="sog-event-subtitle">Guardian Scholars Program</p>
				</div>
			</div>

			<div class="sog-event-description">Help support local foster youth by donating essential items they need. Your contributions of personal care items and household essentials can make a significant impact in the lives of young people in our community.</div>

			<div class="sog-alert"><b>Drop Off Location:&nbsp;</b>KL 222 (Bright Success Center)</div>
		</div>
		<!-- Monetary Involvement Section -->

		<h3 class="sog-section-title" style="font-size: 2em; margin-top: 60px; margin-bottom: 30px;">Financial Contributions</h3>

		<p style="text-align: center;">Support our community through direct donations. Your gift provides essential resources such as holiday meals, household necessities, and program funding. Monetary contributions ensure that families and youth receive consistent, reliable support during the season of giving.</p>

		<p style="text-align: center;">&nbsp;</p>
		<!-- Event: Meals for Families -->

		<div class="sog-event-card">
			<div class="sog-event-header">
				<div>
					<h3 class="sog-event-title">Meals for Families</h3>

					<p class="sog-event-subtitle">Community Engagement Center</p>
				</div>
			</div>

			<div class="sog-event-description">This holiday season, we&#39;re teaming up with All Dads Matter to raise donations for meals to families in need across the Merced community. Your support is more than just a donation; it&#39;s a gift of comfort during a time when it&#39;s needed most.</div>

			<div class="sog-event-details">
				<h4>Impact of Your Donation:</h4>

				<ul>
					<li>Each meal provided costs approximately $70</li>
					<li>Every contribution, no matter the amount, can make a lasting difference</li>
					<li>Whether your gift is large or small, it will directly benefit local families</li>
					<li>Brighten the holiday season and help families feel the power of community support</li>
				</ul>
			</div>

			<div class="sog-event-description" style="margin-top: 15px;">By contributing to the Thanks for Giving initiative, you&#39;re playing a vital role in our mission to support families through the holidays and beyond. Join us in creating a ripple of kindness that extends across our community, bringing joy and relief to those who need it most.</div>

			<div class="sog-alert"><strong>When donating:</strong> On the donation page, under &quot;My gift is in support of&quot; please designate <strong>The Community Engagement Center</strong>.</div>
			<a class="sog-btn" href="https://engage.ucmerced.edu/holiday-season" target="_blank">Donate</a></div>
		<!-- Event: Gift Box Project -->

		<div class="sog-event-card">
			<div class="sog-event-header">
				<div>
					<h3 class="sog-event-title">Gift Card&nbsp;Project</h3>

					<p class="sog-event-subtitle">Guardian Scholars Program</p>
				</div>
			</div>

			<div class="sog-event-description">The Guardian Scholars Program&#39;s annual Gift Box Project is a community engagement and outreach initiative that raises funds, warm clothing items, and personal hygiene items for local foster youth.</div>

			<div class="sog-event-details">
				<h4>About the Project:</h4>

				<ul>
					<li>Gift cards and gift boxes provided for local foster youth</li>
					<li>Serves youth in the Merced and Turlock communities</li>
					<li>Partnership with Creative Alternatives program</li>
				</ul>
			</div>

			<div class="sog-alert"><strong>When donating:</strong> On the donation page, under &quot;My gift is in support of&quot; please designate <strong>Guardian Scholars Program Support</strong>.</div>
			<a class="sog-btn" href="https://engage.ucmerced.edu/holiday-season" target="_blank">Donate</a></div>
	</div>
</div>
<!-- CTA Section -->

<div class="sog-cta-section">
	<div class="sog-container">
		<h2>Every Gift Makes a Difference</h2>

		<p>Whether you adopt a family, donate a meal, or contribute items, your generosity brings hope and joy to those who need it most this holiday season.</p>

		<p class="sog-section-subtitle" style="font-size: 0.85em; font-style: italic;">In accordance with the policy of the University of California, Merced and the UC Merced Foundation, a modest portion of the gift principal and/or income may be used to partially defray the costs of raising and administering funds.</p>

		<div class="sog-cta-buttons"><a class="sog-btn sog-btn-secondary" href="https://cec.ucmerced.edu/" target="_blank">Community Engagement Center</a> <a class="sog-btn sog-btn-secondary" href="https://guardianscholars.ucmerced.edu/" target="_blank">Guardian Scholars Program</a></div>
	</div>
</div>
<!-- Footer -->

<div class="sog-footer">
	<div class="sog-container">
		<p><strong>Questions?</strong> Contact the Community Engagement Center at KL 190</p>

		<p>Monday - Friday, 9:00 AM - 5:00 PM</p>

		<p>You can also <a href="mailto:communityservice@ucmerced.edu">email us</a></p>

		<div class="sog-footer-links"><a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a> <a href="https://cec.ucmerced.edu/calendar" target="_blank">CEC Calendar</a> <a href="https://guardianscholars.ucmerced.edu/" target="_blank">Guardian Scholars</a></div>

		<p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2025 UC Merced | Community Engagement Center &amp; Guardian Scholars</p>
	</div>
</div>
