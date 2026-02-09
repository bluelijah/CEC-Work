<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lights of Hope 5k Santa Run - Volunteer</title>
<style type="text/css">* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .loh-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 0 20px;
        }
        
        /* Hero Section */
        .loh-hero {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4373 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .loh-hero::before {
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
            animation: lohSnowFloat 10s ease-in-out infinite;
            z-index: 0;
        }
        
        @keyframes lohSnowFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        .loh-hero > .loh-container {
            position: relative;
            z-index: 1;
        }
        
        .loh-hero-description {
            font-size: 1.2em;
            max-width: 800px;
            margin: 0 auto 30px;
            line-height: 1.8;
        }
        
        .loh-hero-dates {
            font-size: 1.4em;
            color: #dbaa00;
            font-weight: 600;
            margin-top: 25px;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        .loh-hero-dates div {
            margin: 5px 0;
        }
        
        .loh-partners {
            margin-top: 40px;
            padding: 25px;
            border-radius: 10px;
        }
        
        .loh-partners-label {
            font-size: 0.95em;
            opacity: 0.9;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .loh-partners-logos {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 40px;
            flex-wrap: wrap;
        }
        
        .loh-partner-logo {
            max-width: 220px;
            height: auto;
        }
        
        .loh-partner-logo img {
            width: 100%;
            height: auto;
            display: block;
            filter: drop-shadow(0 0 20px rgba(255,255,255,0.8));
            padding: 15px;
            background: white;
            border-radius: 10px;
        }
        
        /* Info Section */
        .loh-info-section {
            background: white;
            padding: 60px 20px;
        }
        
        .loh-section-title {
            font-size: 2.5em;
            color: #0f2d52;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .loh-section-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            max-width: 800px;
            margin: 0 auto 40px;
            line-height: 1.8;
        }
        
        .loh-info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .loh-info-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 5px solid #dbaa00;
        }
        
        .loh-info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
            border-left-color: #0f2d52;
        }
        
        .loh-info-card h3 {
            color: #0f2d52;
            font-size: 1.6em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .loh-info-card p {
            line-height: 1.7;
            color: #555;
            margin-bottom: 10px;
        }
        
        .loh-info-card ul {
            margin-left: 20px;
            color: #555;
            line-height: 1.8;
        }
        
        /* Event Details Section */
        .loh-details-section {
            background: #f8f9fa;
            padding: 60px 20px;
        }
        
        .loh-details-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .loh-detail-card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-top: 4px solid #dbaa00;
        }
        
        .loh-detail-card h3 {
            color: #0f2d52;
            font-size: 1.4em;
            margin-bottom: 15px;
            font-weight: 700;
        }
        
        .loh-detail-card p {
            color: #555;
            line-height: 1.7;
            margin-bottom: 10px;
        }
        
        /* Flyer Section */
        .loh-flyer-section {
            background: white;
            padding: 60px 20px;
        }
        
        .loh-flyer-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        
        .loh-flyer-container img {
            width: 100%;
            max-width: 600px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            margin: 20px auto;
        }
        
        /* CTA Section */
        .loh-cta-section {
            background: linear-gradient(135deg, #dbaa00 0%, #ffc107 100%);
            padding: 60px 20px;
        }
        
        .loh-cta-section h2 {
            text-align: center;
            font-size: 2.5em;
            color: #0f2d52;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .loh-cta-section p {
            text-align: center;
            font-size: 1.2em;
            color: #333;
            max-width: 700px;
            margin: 0 auto 30px;
        }
        
        .loh-cta-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .loh-btn {
            display: inline-block;
            padding: 15px 40px;
            background: #dbaa00;
            color: #0f2d52;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 700;
            font-size: 1.1em;
            transition: all 0.3s ease;
            border: 2px solid #dbaa00;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .loh-btn:hover {
            background: #0f2d52;
            color: white;
            border-color: #0f2d52;
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }
        
        .loh-btn-secondary {
            background: white;
            color: #0f2d52;
            border: 2px solid #0f2d52;
        }
        
        .loh-btn-secondary:hover {
            background: #0f2d52;
            color: white;
        }
        
        .loh-alert {
            background: #FFF8E7;
            border-left: 5px solid #dbaa00;
            padding: 20px;
            margin: 30px 0;
            border-radius: 5px;
            font-size: 1.1em;
        }
        
        .loh-alert strong {
            color: #0f2d52;
        }
        
        /* Footer */
        .loh-footer {
            background: #0f2d52;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .loh-footer a,
        .loh-footer a:link,
        .loh-footer a:visited {
            color: #dbaa00 !important;
            text-decoration: none;
            font-weight: 600;
        }
        
        .loh-footer a:hover,
        .loh-footer a:active {
            color: #ffc107 !important;
            text-decoration: underline;
        }
        
        .loh-footer-links {
            margin-top: 20px;
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .loh-container {
                padding: 0 15px;
            }
            
            .loh-hero {
                padding: 50px 15px;
            }
            
            .loh-hero-description {
                font-size: 1em;
            }
            
            .loh-hero-dates {
                font-size: 1.1em;
            }
            
            .loh-section-title {
                font-size: 2em;
            }
            
            .loh-info-grid,
            .loh-details-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .loh-info-card,
            .loh-detail-card {
                padding: 20px;
            }
            
            .loh-partners-logos {
                flex-direction: column;
                gap: 20px;
            }
            
            .loh-partner-logo {
                max-width: 200px;
            }
        }
</style>

<!-- Hero Section -->
<div class="loh-hero">
    <div class="loh-container">
        <p class="loh-hero-description">Join us in making a difference this holiday season! The Lights of Hope 5k Santa Run needs dedicated volunteers to help make this festive community event a success. All proceeds benefit Merced College for Kids and the Merced Cancer Society Foundation.</p>
        
        <div class="loh-hero-dates">
            <div><strong>Setup Day:</strong> Friday, December 12, 2025</div>
            <div><strong>Event Day:</strong> Saturday, December 13, 2025</div>
        </div>
    </div>
</div>

<!-- Event Details Section -->
<div class="loh-details-section">
    <div class="loh-container">
        <div class="loh-info-grid">
            <div class="loh-info-card">
                <h3>Support Local Causes</h3>
                <p>100% of proceeds go directly to:</p>
                <ul>
                    <li>Merced College for Kids</li>
                    <li>Merced Cancer Society Foundation</li>
                </ul>
                <p style="margin-top: 15px;">Your volunteer work helps ensure these organizations receive maximum support from this event.</p>
            </div>
            
            <div class="loh-info-card">
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
        
        <h2 class="loh-section-title" style="margin-top: 60px;">Volunteer Responsibilities</h2>
        
        <div style="max-width: 900px; margin: 0 auto;">
            <div class="loh-detail-card" style="border-top-width: 5px;">
                <h3>Setup Day - Friday, December 12, 2025</h3>
                <ul>
                    <li>Help prepare the event space</li>
                    <li>Set up registration areas</li>
                    <li>Organize materials for the event</li>
                    <li>Arrange course signage and markers</li>
                    <li>Prepare volunteer stations</li>
                </ul>
                
                <h3 style="margin-top: 30px;">Event Day - Saturday, December 13, 2025</h3>
                <ul>
                    <li>Assist with participant registration</li>
                    <li>Guide participants along the course</li>
                    <li>Manage water stations</li>
                    <li>Course marshaling and safety</li>
                    <li>Help with event cleanup</li>
                    <li>Ensure a smooth, fun experience for all runners</li>
                </ul>
                
                <div style="margin-top: 30px; text-align: center;">
                    <a class="loh-btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_2toG7bApJpKudAq" target="_blank">Sign Up to Volunteer</a>
                    <p style="font-size: 0.85em; color: #666; margin-top: 15px; line-height: 1.6;">
                        <em>You must also register with ASBMB. An email will be sent following your sign up with their registration information, or scan the QR code on the flyer below.</em>
                    </p>
                </div>
            </div>
        </div>
        
        <div class="loh-alert">
            <strong>What to Expect:</strong> All training and materials will be provided. Event location details and specific volunteer assignments will be shared upon registration.
        </div>
    </div>
</div>

<!-- Flyer Section -->
<div class="loh-flyer-section">
    <div class="loh-container">
        <div class="loh-flyer-container">
            <img alt="Lights of Hope 5k Santa Run Flyer" src="/sites/cec.ucmerced.edu/files/images/flyers/santarunflyer.jpg" />
        </div>
    </div>
</div>

<!-- Footer -->
<div class="loh-footer">
    <div class="loh-container">
        <p style="font-size: 1.1em; margin-bottom: 10px;"><strong>Questions?</strong> Contact the Community Engagement Center</p>
        <p><strong>Community Engagement Center</strong></p>
        <p>Kolligian Library, Room 190</p>
        <p>Monday - Friday, 9:00 AM - 5:00 PM</p>
        <p style="margin-top: 15px;"><a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a></p>
        
        <div class="loh-footer-links">
            <a href="https://www.instagram.com/ucmercedcec/" target="_blank">Instagram</a>
            <a href="https://cec.ucmerced.edu/calendar" target="_blank">CEC Calendar</a>
            <a href="https://cec.ucmerced.edu/" target="_blank">Visit CEC</a>
        </div>
        
        <p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2025 UC Merced | Community Engagement Center</p>
    </div>
</div>