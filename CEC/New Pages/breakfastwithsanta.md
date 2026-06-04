<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .bws-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 0 20px;
        }
        
        /* Hero Section */
        .bws-hero {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4373 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .bws-hero::before {
            content: '';
            position: absolute;
            width: 450px;
            height: 450px;
            background-image: url('/sites/cec.ucmerced.edu/files/images/snowflake.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.2;
            top: 50%;
            left: 50%;
            margin-top: -225px;
            margin-left: -225px;
            animation: bwsSnowFloat 10s ease-in-out infinite;
            z-index: 0;
        }
        
        @keyframes bwsSnowFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .bws-hero > .bws-container {
            position: relative;
            z-index: 1;
        }
        
        .bws-hero-description {
            font-size: 1.2em;
            max-width: 800px;
            margin: 0 auto 30px;
            line-height: 1.8;
        }
        
        .bws-hero-dates {
            font-size: 1.4em;
            color: #dbaa00;
            font-weight: 600;
            margin-top: 25px;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        .bws-hero-dates div {
            margin: 5px 0;
        }
        
        /* Info Section */
        .bws-info-section {
            background: white;
            padding: 60px 20px;
        }
        
        .bws-section-title {
            font-size: 2.5em;
            color: #0f2d52;
            text-align: center;
            margin-bottom: 40px;
            font-weight: 700;
        }
        
        .bws-info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .bws-info-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 5px solid #dbaa00;
        }
        
        .bws-info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
            border-left-color: #0f2d52;
        }
        
        .bws-info-card h3 {
            color: #0f2d52;
            font-size: 1.6em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .bws-info-card p {
            line-height: 1.7;
            color: #555;
            margin-bottom: 10px;
        }
        
        .bws-info-card ul {
            margin-left: 20px;
            color: #555;
            line-height: 1.8;
        }
        
        /* Details Section */
        .bws-details-section {
            background: #f8f9fa;
            padding: 60px 20px;
        }
        
        .bws-details-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .bws-detail-card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-top: 4px solid #dbaa00;
        }
        
        .bws-detail-card h3 {
            color: #0f2d52;
            font-size: 1.4em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .bws-detail-card p {
            color: #555;
            line-height: 1.7;
            margin-bottom: 10px;
        }

        .bws-detail-card ul {
            margin-left: 20px;
            color: #555;
            line-height: 1.8;
        }
        
        /* Flyer Section */
        .bws-flyer-section {
            background: white;
            padding: 60px 20px;
        }
        
        .bws-flyer-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        
        .bws-flyer-container img {
            width: 100%;
            max-width: 600px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            margin: 20px auto;
        }
        
        /* CTA Section */
        .bws-cta-section {
            background: linear-gradient(135deg, #dbaa00 0%, #ffc107 100%);
            padding: 60px 20px;
        }
        
        .bws-cta-section h2 {
            text-align: center;
            font-size: 2.5em;
            color: #0f2d52;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .bws-cta-section p {
            text-align: center;
            font-size: 1.2em;
            color: #333;
            max-width: 700px;
            margin: 0 auto 30px;
        }
        
        .bws-cta-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .bws-btn {
            display: inline-block;
            padding: 15px 40px;
            background: #0f2d52;
            color: white !important;
            text-decoration: none !important;
            border-radius: 25px;
            font-weight: 700;
            font-size: 1.1em;
            transition: all 0.3s ease;
            border: 2px solid #0f2d52;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .bws-btn:hover {
            background: white;
            color: #0f2d52 !important;
            border-color: #0f2d52;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }
        
        .bws-alert {
            background: #FFF8E7;
            border-left: 5px solid #dbaa00;
            padding: 20px;
            margin: 30px 0;
            border-radius: 5px;
            font-size: 1.1em;
        }
        
        .bws-alert strong {
            color: #0f2d52;
        }
        
        /* Footer */
        .bws-footer {
            background: #0f2d52;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .bws-footer a,
        .bws-footer a:link,
        .bws-footer a:visited {
            color: #dbaa00 !important;
            text-decoration: none;
            font-weight: 600;
        }
        
        .bws-footer a:hover,
        .bws-footer a:active {
            color: #ffc107 !important;
            text-decoration: underline;
        }
        
        .bws-footer-links {
            margin-top: 20px;
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .bws-container {
                padding: 0 15px;
            }
            
            .bws-hero {
                padding: 50px 15px;
            }
            
            .bws-hero-description {
                font-size: 1em;
            }
            
            .bws-hero-dates {
                font-size: 1.1em;
            }
            
            .bws-section-title {
                font-size: 2em;
            }
            
            .bws-info-grid,
            .bws-details-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .bws-info-card,
            .bws-detail-card {
                padding: 20px;
            }
        }
</style>
<!-- Hero Section -->
<div class="bws-hero">
	<div class="bws-container">
		<p class="bws-hero-description">We are excited to share that our annual Breakfast with Santa event is right around the corner, and we have some great volunteer opportunities available! This is one of our most popular community events of the year, and we couldn&#39;t make it happen without your support.</p>

		<div class="bws-hero-dates">
			<div><strong>Setup Day:</strong> Friday, December 12, 2025</div>

			<div><strong>Event Day:</strong> Saturday, December 13, 2025</div>

			<div><strong>Location:</strong> Merced Senior Community Center 755 W 15th St</div>
		</div>
	</div>
</div>
<!-- Info Section -->

<div class="bws-info-section">
	<div class="bws-container">
		<h2 class="bws-section-title">Why Volunteer?</h2>

		<div class="bws-info-grid">
			<div class="bws-info-card">
				<h3>Support Local Community</h3>

				<p>Help us create magical memories for families in our community during the holiday season. Your volunteer work directly contributes to making this festive event special for everyone.</p>
			</div>

			<div class="bws-info-card">
				<h3>Earn Community Service Hours</h3>

				<p>Volunteers will receive verified community service hours for their time, perfect for:</p>

				<ul>
					<li>Academic requirements</li>
					<li>Scholarship applications</li>
					<li>Resume building</li>
					<li>Personal growth</li>
				</ul>
			</div>
		</div>
	</div>
</div>
<!-- Details Section -->

<div class="bws-details-section">
	<div class="bws-container">
		<h2 class="bws-section-title">Volunteer Responsibilities</h2>

		<div style="max-width: 900px; margin: 0 auto;">
			<div class="bws-detail-card">
				<h3>Setup Day - Friday, December 12, 2025</h3>

				<p><strong>Time:</strong> 4:00 PM &ndash; 8:00 PM | <strong>Positions:</strong> 5 Volunteers</p>

				<ul>
					<li>Help prepare the event space</li>
					<li>Decorate for the holiday</li>
					<li>Arrange tables and chairs</li>
					<li>Set up craft and activity stations</li>
					<li>Prepare volunteer stations</li>
				</ul>

				<h3 style="margin-top: 30px;">Event Day - Saturday, December 13, 2025</h3>

				<p><strong>Time:</strong> 7:30 AM &ndash; 12:30 PM | <strong>Positions:</strong> 8 Volunteers</p>

				<ul>
					<li>Greet families and check in attendees</li>
					<li>Assist with crafts and activities</li>
					<li>Help serve breakfast</li>
					<li>Support photo area with Santa</li>
					<li>General event assistance</li>
				</ul>

				<div style="margin-top: 30px; text-align: center;"><a class="bws-btn" href="https://www.cervistech.com/acts/console.php?console_id=0188&amp;console_type=event_list&amp;ht=1&amp;event_id=266" target="_blank">Sign Up to Volunteer</a></div>
			</div>
		</div>

		<div class="bws-alert"><strong>Dress Code:</strong> Please come dressed appropriately and festively for the event!</div>

		<div class="bws-alert"><strong>What to Expect:</strong> All training and materials will be provided. Event location details and specific volunteer assignments will be shared upon registration.</div>
	</div>
</div>
<!-- Footer -->

<div class="bws-footer">
	<div class="bws-container">
		<p style="font-size: 1.1em; margin-bottom: 10px;"><strong>Questions?</strong> Contact the Community Engagement Center</p>

		<p><strong>Community Engagement Center</strong></p>

		<p>Kolligian Library, Room 190</p>

		<p>Monday - Friday, 9:00 AM - 5:00 PM</p>

		<p style="margin-top: 15px;"><a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a></p>

		<div class="bws-footer-links"><a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a> <a href="https://cec.ucmerced.edu/calendar" target="_blank">CEC Calendar</a> <a href="https://cec.ucmerced.edu/" target="_blank">Visit CEC</a></div>

		<p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2025 UC Merced | Community Engagement Center</p>
	</div>
</div>
