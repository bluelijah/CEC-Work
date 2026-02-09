<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.aging-page * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .aging-page {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
            background-image: url('/sites/g/files/ufvvjh561/f/images/logos/mercedcountylogo.png');
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            background-size: 30%;
            position: relative;
        }

        .aging-page::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.95);
            z-index: -1;
        }

        .aging-container {
            width: 100%;
            margin: 0 auto;
            padding: 0;
            position: relative;
            z-index: 1;
        }

        .aging-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
            color: white;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
        }

        .aging-header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: white;
        }

        .aging-header p {
            color: white;
            font-size: 1.1rem;
        }

        .aging-content-box {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
        }

        .aging-content-box h2 {
            color: #0f2d52;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }

        .aging-content-box h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        .aging-content-box h4 {
            color: #0f2d52;
            font-size: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        .aging-content-box p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.2rem;
        }

        .aging-content-box ul {
            margin-left: 2rem;
            margin-bottom: 1.5rem;
        }

        .aging-content-box li {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 0.5rem;
        }

        .aging-content-box strong {
            color: #0f2d52;
        }

        .aging-highlight-box {
            background: linear-gradient(135deg, #fffbf0 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #dbaa00;
            margin-bottom: 1.5rem;
        }

        .aging-highlight-box p {
            margin-bottom: 1rem;
        }

        .aging-highlight-box p:last-child {
            margin-bottom: 0;
        }

        .aging-program-card {
            background: #f9f9f9;
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            border-left: 4px solid #dbaa00;
        }

        .aging-program-card h3 {
            color: #0f2d52;
            font-size: 1.5rem;
            margin-top: 0;
            margin-bottom: 1rem;
        }

        .aging-three-column {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .aging-column {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .aging-column h4 {
            color: #0f2d52;
            font-size: 1.1rem;
            margin-top: 0;
            margin-bottom: 1rem;
            text-align: center;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #dbaa00;
        }

        .aging-column ul {
            margin-left: 1.5rem;
            font-size: 1rem;
        }

        .aging-column li {
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }

        .aging-contact-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
            margin-top: 2rem;
            text-align: center;
        }

        .aging-contact-section h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }

        .aging-contact-section p {
            color: #555;
            margin-bottom: 1.5rem;
        }

        .aging-contact-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }

        .aging-contact-item {
            text-align: center;
        }

        .aging-contact-item strong {
            display: block;
            color: #0f2d52;
            margin-bottom: 0.5rem;
        }

        .aging-button {
            display: inline-block;
            padding: 1rem 2.5rem;
            background: #0f2d52;
            color: white !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.1rem;
            text-transform: uppercase;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(15, 45, 82, 0.4);
            text-align: center;
            margin: 0.5rem;
        }

        .aging-button:hover {
            background: #dbaa00;
            color: #0f2d52 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(219, 170, 0, 0.5);
        }

        .aging-button-center {
            text-align: center;
            margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
            .aging-button-center {
                display: flex;
                flex-direction: column;
                gap: 1rem;
            }

            .aging-page {
                margin-right: 40px;
                background-size: 70%;
            }

            .aging-header h1 {
                font-size: 1.8rem;
            }

            .aging-content-box {
                padding: 1.5rem;
            }

            .aging-three-column {
                grid-template-columns: 1fr;
            }

            .aging-contact-info {
                flex-direction: column;
                gap: 1rem;
            }

            .aging-program-card {
                padding: 1.5rem;
            }
        }
</style>
<div class="aging-page">
	<div class="aging-container">
		<div class="aging-header">
			<h1>Merced County Area on Aging Agency</h1>

			<p>Volunteer Program Opportunities</p>
		</div>

		<div class="aging-content-box">
			<h2>About the Agency</h2>

			<p>The Merced County Area on Aging Agency works in partnership with the community to provide protection, care, and support of families and individuals, and to promote personal responsibility and self-sufficiency.</p>

			<div class="aging-highlight-box">
				<p><strong>Mission:</strong> To work in partnership with the community to provide the protection, care, and support of families and individuals, and to promote personal responsibility and self-sufficiency.</p>
			</div>

			<h3>Why Volunteer With This Agency?</h3>

			<ul>
				<li>Make a direct impact on seniors&#39; lives and well-being</li>
				<li>Build hands-on experience in social services, healthcare, and community advocacy</li>
				<li>Gain leadership, communication, and empathy skills</li>
				<li>Flexible hours and meaningful interactions</li>
				<li>Great experience for resumes, grad school, or future careers in health, public service, or psychology</li>
				<li>Potential references if needed</li>
			</ul>

			<h3>Four Volunteer Programs Available</h3>

			<p>The Merced County Area on Aging Agency offers four impactful ways to serve the senior community:</p>
		</div>
		<!-- HICAP Program -->

		<div class="aging-content-box">
			<div class="aging-program-card">
				<h3>1. HICAP (Health Insurance Counseling &amp; Advocacy Program)</h3>

				<p><strong>Purpose:</strong> Empower Medicare beneficiaries to understand their health insurance and protect their rights.</p>

				<div class="aging-three-column">
					<div class="aging-column">
						<h4>What You&#39;ll Do</h4>

						<ul>
							<li>Provide one-on-one counseling on Medicare options</li>
							<li>Assist with billing, claims, and insurance appeals</li>
							<li>Advocate for seniors&#39; healthcare rights</li>
							<li>Promote awareness of available resources</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Requirements</h4>

						<ul>
							<li>Must complete training and background check</li>
							<li>Basic computer literacy</li>
							<li>Commitment: Minimum 16 hours/month</li>
							<li>Attend monthly in-service trainings</li>
							<li>Maintain confidentiality and professionalism</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Key Takeaways</h4>

						<ul>
							<li>Make a difference in seniors&#39; healthcare decisions</li>
							<li>Gain advocacy and communication experience</li>
							<li>Receive hands-on mentorship and certification training</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<!-- Ombudsman Program -->

		<div class="aging-content-box">
			<div class="aging-program-card">
				<h3>2. Long-Term Care Ombudsman Program</h3>

				<p><strong>Purpose:</strong> Advocate for residents in nursing homes and long-term care facilities, ensuring dignity, safety, and quality of life.</p>

				<div class="aging-three-column">
					<div class="aging-column">
						<h4>What You&#39;ll Do</h4>

						<ul>
							<li>Resolve complaints made by or for residents</li>
							<li>Educate about residents&#39; rights and care standards</li>
							<li>Promote family and resident councils</li>
							<li>Report and address abuse, neglect, or violations</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Requirements</h4>

						<ul>
							<li>Must be 18+ with a valid driver&#39;s license</li>
							<li>Pass DOJ &amp; FBI background checks</li>
							<li>Complete 36 hours of classroom training and 10 hours of internship</li>
							<li>Sign confidentiality and ethics agreements</li>
							<li>Complete 18 hours of continuing training each year</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Key Takeaways</h4>

						<ul>
							<li>Be the voice for residents who can&#39;t speak up</li>
							<li>Gain experience in advocacy, social work, and law</li>
							<li>Make lasting impact in long-term care facilities</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<!-- Senior Friendship Program -->

		<div class="aging-content-box">
			<div class="aging-program-card">
				<h3>3. Senior Friendship Program</h3>

				<p><strong>Purpose:</strong> Reduce loneliness among homebound seniors through meaningful companionship and friendship.</p>

				<div class="aging-three-column">
					<div class="aging-column">
						<h4>What You&#39;ll Do</h4>

						<ul>
							<li>Visit or call assigned seniors regularly</li>
							<li>Build ongoing relationships through conversation and empathy</li>
							<li>Share stories, laughter, and friendship</li>
							<li>Provide emotional support and encouragement</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Requirements</h4>

						<ul>
							<li>Background check required</li>
							<li>Commitment level flexible (weekly or biweekly visits/calls)</li>
							<li>Kindness, reliability, and good communication skills</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Key Takeaways</h4>

						<ul>
							<li>Combat senior isolation and loneliness</li>
							<li>Build meaningful intergenerational relationships</li>
							<li>Flexible schedule that fits your availability</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<!-- A Matter of Balance Program -->

		<div class="aging-content-box">
			<div class="aging-program-card">
				<h3>4. A Matter of Balance &ndash; Volunteer Coach</h3>

				<p><strong>Purpose:</strong> Help older adults manage concerns about falls and stay active, confident, and independent.</p>

				<div class="aging-three-column">
					<div class="aging-column">
						<h4>What You&#39;ll Do</h4>

						<ul>
							<li>Co-lead small group workshops (8 sessions per class)</li>
							<li>Facilitate discussions and light exercise</li>
							<li>Encourage participants and promote positive attitudes toward aging</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Requirements</h4>

						<ul>
							<li>Attend 8 hours of certification training + annual 2.5-hour update</li>
							<li>Lead 2 classes per year</li>
							<li>Be enthusiastic, dependable, and comfortable leading groups</li>
							<li>Ability to lift up to 20 lbs and demonstrate light movement</li>
						</ul>
					</div>

					<div class="aging-column">
						<h4>Key Takeaways</h4>

						<ul>
							<li>Leadership and facilitation experience</li>
							<li>Support health and wellness in the senior community</li>
							<li>Fun, interactive way to make a difference</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<!-- Contact Section -->

		<div class="aging-contact-section">
			<h3>How to Get Involved</h3>

			<p>Choose a program that matches your interests, complete the volunteer application, attend orientation and training, and start making an impact in the community!</p>

			<div class="aging-contact-info">
				<div class="aging-contact-item"><strong>Email</strong>

					<p>hsavolprog@hsa.co.merced.ca.us</p>
				</div>

				<div class="aging-contact-item"><strong>Phone</strong>

					<p>(209) 354-2525</p>
				</div>

				<div class="aging-contact-item"><strong>Location</strong>

					<p>851 West 23rd Street<br />
						Merced, CA 95340</p>
				</div>
			</div>

			<div class="aging-button-center"><a class="aging-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_0GthSzPFtLswpHE">Sign Up Now</a></div>

			<div class="aging-highlight-box" style="margin-top: 2rem;">
				<p><em>&quot;The best way to find yourself is to lose yourself in the service of others.&quot;</em> &mdash; Mahatma Gandhi</p>
			</div>
		</div>
	</div>
</div>
