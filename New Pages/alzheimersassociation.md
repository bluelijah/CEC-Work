<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.alz-page * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .alz-page {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        .alz-container {
            width: 100%;
            margin: 0 auto;
            padding: 0;
        }

        .alz-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
            color: white;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
        }

        .alz-header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: white;
        }

        .alz-header p {
            color: white;
        }

        .alz-header .alz-hashtag {
            color: #dbaa00;
            font-size: 1.3rem;
            font-weight: bold;
            margin-top: 1rem;
        }

        .alz-content-box {
            background: white;
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
        }

        .alz-content-box h2 {
            color: #0f2d52;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .alz-content-box p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.2rem;
        }

        .alz-volunteer-activities {
            margin: 2rem 0;
        }

        .alz-volunteer-activities ul {
            list-style: none;
            padding: 0;
        }

        .alz-volunteer-activities li {
            margin-bottom: 1rem;
            line-height: 1.8;
        }

        .alz-volunteer-activities strong {
            color: #0f2d52;
            font-size: 1.05rem;
        }

        .alz-cta-section {
            text-align: center;
            background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(219, 170, 0, 0.3);
        }

        .alz-cta-section h2 {
            color: #0f2d52;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }

        .alz-cta-section p {
            color: #0f2d52;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }

        .alz-email-link {
            display: inline-block;
            padding: 1rem 2.5rem;
            background: #0f2d52;
            color: white !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(15, 45, 82, 0.4);
        }

        .alz-email-link:hover {
            background: #1a4573;
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(15, 45, 82, 0.5);
        }

        .alz-flyer-section {
            background: white;
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
        }

        .alz-flyer-section h2 {
            color: #0f2d52;
            text-align: center;
            margin-bottom: 2rem;
            font-size: 1.8rem;
        }

        .alz-language-toggle {
            display: flex;
            justify-content: center;
            gap: 0;
            margin-bottom: 2rem;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: fit-content;
            margin-left: auto;
            margin-right: auto;
        }

        .alz-language-btn {
            padding: 1rem 2.5rem;
            border: none;
            background: #c0c0c0;
            color: #666;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
        }

        .alz-language-btn.alz-active {
            background: #0f2d52;
            color: white;
        }

        .alz-language-btn:hover:not(.alz-active) {
            background: #a0a0a0;
        }

        .alz-flyer-container {
            position: relative;
            width: 100%;
            height: auto;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        }

        .alz-flyer {
            position: relative;
            width: 100%;
            height: auto;
            display: block;
            background: #f9f9f9;
            transition: transform 0.5s ease;
        }

        .alz-flyer img {
            width: 100%;
            height: auto;
            display: block;
        }

        .alz-flyer.alz-english {
            transform: translateX(0);
        }

        .alz-flyer.alz-spanish {
            position: absolute;
            top: 0;
            left: 0;
            transform: translateX(100%);
        }

        .alz-flyer.alz-slide-out-left {
            transform: translateX(-100%);
        }

        .alz-flyer.alz-slide-in-right {
            transform: translateX(0);
        }

        .alz-flyer-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            text-align: center;
        }

        .alz-flyer-placeholder h3 {
            color: #0f2d52;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .alz-flyer-placeholder p {
            color: #666;
            font-size: 1.1rem;
        }

        @media (max-width: 768px) {
            .alz-header h1 {
                font-size: 1.8rem;
            }

            .alz-content-box, .alz-cta-section, .alz-flyer-section {
                padding: 1.5rem;
            }

            .alz-language-btn {
                padding: 0.8rem 1.5rem;
                font-size: 1rem;
            }
        }
</style>
<div class="alz-page">
	<div class="alz-container">
		<div class="alz-header">
			<h1>Join the Fight Against Alzheimer&#39;s</h1>

			<p>Volunteer with the Alzheimer&#39;s Association</p>

			<div class="alz-hashtag">#ENDALZ</div>
		</div>

		<div class="alz-content-box">
			<h2>Make a Difference in Your Community</h2>

			<p>Are you passionate about making a difference in the fight against Alzheimer&#39;s disease? The Alzheimer&#39;s Association is seeking dedicated volunteers like you to join their mission.</p>

			<div class="alz-volunteer-activities">
				<ul>
					<li><strong>Education &amp; Outreach:</strong> Educate the community about Alzheimer&#39;s and dementia</li>
					<li><strong>Tabling Events:</strong> Share vital resources at community events</li>
					<li><strong>Walk Events:</strong> Support the signature fundraising walks</li>
					<li><strong>Advocacy:</strong> Advocate for those affected by Alzheimer&#39;s</li>
					<li><strong>Connections:</strong> Foster partnerships with organizations and companies</li>
				</ul>
			</div>

			<p><strong>Volunteers are the backbone of the organization</strong>, driving impactful change and touching countless lives. Your commitment and time can truly make a difference in the collective effort to end Alzheimer&#39;s disease.</p>
		</div>

		<div class="alz-cta-section">
			<h2>Ready to Get Involved?</h2>

			<p>If you are interested in becoming a volunteer, the Alzheimer&#39;s Association would be thrilled to connect with you!</p>
			<a class="alz-email-link" href="mailto:mapena@alz.org">Contact Us: mapena@alz.org</a></div>

		<div class="alz-flyer-section">
			<h2>Volunteer Opportunity Flyer</h2>

			<div class="alz-language-toggle"><button class="alz-language-btn alz-active" id="alzEnglishBtn">English</button><button class="alz-language-btn" id="alzSpanishBtn">Español</button></div>

			<div class="alz-flyer-container">
				<div class="alz-flyer alz-english" id="alzEnglishFlyer"><img alt="Alzheimer's Association Volunteer Opportunity Flyer" src="/sites/cec.ucmerced.edu/files/images/alzenglish.jpg" /></div>

				<div class="alz-flyer alz-spanish" id="alzSpanishFlyer"><img alt="Alzheimer's Association Volunteer Opportunity Flyer - Spanish" src="/sites/cec.ucmerced.edu/files/images/alzspanish.jpg" /></div>
			</div>
		</div>
	</div>
</div>
<script>
        const alzEnglishBtn = document.getElementById('alzEnglishBtn');
        const alzSpanishBtn = document.getElementById('alzSpanishBtn');
        const alzEnglishFlyer = document.getElementById('alzEnglishFlyer');
        const alzSpanishFlyer = document.getElementById('alzSpanishFlyer');

        alzEnglishBtn.addEventListener('click', () => {
            if (!alzEnglishBtn.classList.contains('alz-active')) {
                // Switch to English
                alzEnglishBtn.classList.add('alz-active');
                alzSpanishBtn.classList.remove('alz-active');
                
                alzSpanishFlyer.style.transform = 'translateX(100%)';
                alzEnglishFlyer.style.transform = 'translateX(0)';
            }
        });

        alzSpanishBtn.addEventListener('click', () => {
            if (!alzSpanishBtn.classList.contains('alz-active')) {
                // Switch to Spanish
                alzSpanishBtn.classList.add('alz-active');
                alzEnglishBtn.classList.remove('alz-active');
                
                alzEnglishFlyer.style.transform = 'translateX(-100%)';
                alzSpanishFlyer.style.transform = 'translateX(0)';
            }
        });
    </script>