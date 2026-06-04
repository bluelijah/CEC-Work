<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About & Contact</title>
<style type="text/css">.cec-about-page {
            font-family: 'Open Sans', sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0 auto;
        }

        .cec-about-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .cec-about-header h1 {
            color: #002856;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .cec-about-intro {
            text-align: center;
            color: #555;
            font-size: 1.1rem;
            margin: 0 auto 3rem;
            max-width: 800px;
            line-height: 1.8;
        }

        .cec-contact-section {
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
            border: 2px solid #0077cc;
            border-radius: 12px;
            padding: 2.5rem;
            margin: 3rem 0;
        }

        .cec-contact-section h2 {
            color: #002856;
            font-size: 1.8rem;
            margin-bottom: 2rem;
            text-align: left;
            border-bottom: 3px solid #ffbf3c;
            padding-bottom: 0.5rem;
        }

        .cec-contact-info {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin: 0;
        }

        .cec-contact-item {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 40, 86, 0.1);
            margin-bottom: 0;
            text-align: left;
        }

        .cec-contact-item h3 {
            color: #002856;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .cec-contact-item p {
            color: #555;
            margin: 0.3rem 0;
            line-height: 1.6;
        }

        .cec-contact-item a {
            color: #0077cc;
            text-decoration: none;
        }

        .cec-contact-item a:hover {
            color: #005a99;
            text-decoration: underline;
        }

        .cec-about-section {
            margin: 0 0 3rem 0;
        }

        .cec-about-section h2 {
            color: #002856;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #ffbf3c;
        }

        .cec-about-section p {
            color: #555;
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        /* Accordion styles */
        .cec-about-accordion {
            margin: 0 0 3rem 0;
            width: 100%;
        }

        .cec-about-accordion ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .cec-about-accordion li {
            margin: 16px 0 0 0;
            padding: 0;
        }

        .cec-acc-btn {
            display: block;
            width: 100%;
            font-family: 'Open Sans', sans-serif;
            font-size: 1.3rem;
            line-height: 1.4;
            padding: 1em 1.5em;
            margin: 0;
            cursor: pointer;
            background: linear-gradient(135deg, #002856 0%, #003d7a 100%);
            border: 2px solid #002856;
            border-radius: 8px;
            color: #fff;
            font-weight: 700;
            text-transform: uppercase;
            text-align: left;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 40, 86, 0.2);
        }

        .cec-acc-btn:hover {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            border-color: #ffbf3c;
            color: #002856;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }

        .cec-acc-btn:focus {
            outline: 3px solid #ffbf3c;
            outline-offset: 2px;
        }

        .cec-acc-btn[aria-expanded="true"] {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            border-color: #ffbf3c;
            color: #002856;
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }

        .cec-about-acc-content {
            padding: 1.5em;
            background: linear-gradient(135deg, #fffbf0 0%, #fff 100%);
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            margin-top: 8px;
        }

        .cec-about-acc-content[hidden] {
            display: none;
        }

        .cec-about-acc-content h4 {
            color: #002856;
            font-size: 1.2rem;
            margin: 0 0 1rem 0;
        }

        .cec-about-acc-content ul {
            margin: 1rem 0;
            padding: 0 0 0 2rem;
        }

        .cec-about-acc-content li {
            color: #555;
            line-height: 1.8;
            margin-bottom: 1rem;
            list-style-type: square;
        }

        .cec-about-acc-content a {
            color: #0077cc;
            text-decoration: none;
        }

        .cec-about-acc-content a:hover {
            color: #005a99;
            text-decoration: underline;
        }

        .cec-cta-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .cec-cta-card {
            background: linear-gradient(135deg, #002856 0%, #003d7a 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 40, 86, 0.2);
            transition: all 0.3s ease;
        }

        .cec-cta-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 40, 86, 0.3);
        }

        .cec-cta-card h3 {
            color: #ffbf3c;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .cec-cta-card p {
            color: #e6f3ff;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }

        .cec-cta-button {
            display: inline-block;
            padding: 0.75em 2em;
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            color: #002856 !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(255, 191, 60, 0.3);
        }

        .cec-cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.5);
            background: linear-gradient(135deg, #e6a829 0%, #d49820 100%);
        }

        .cec-cta-button:focus {
            outline: 3px solid #fff;
            outline-offset: 2px;
        }

        .cec-contact-item a:focus {
            outline: 3px solid #002856;
            outline-offset: 2px;
        }

        @media (max-width: 768px) {
            .cec-about-page {
                padding: 0 15px 15px 15px;
            }

            .cec-contact-section {
                padding: 1.5rem;
            }

            .cec-contact-info {
                grid-template-columns: 1fr;
            }

            .cec-cta-section {
                grid-template-columns: 1fr;
            }
        }
</style>
<div class="cec-about-page">
	<div class="cec-about-section">
		<h2>Our Purpose and Mission</h2>

		<p>Community engagement is core to the purpose of higher education and essential to the student experience, teaching, and empowering students to become active and responsible civic participants, and central to the theme of UC Merced&#39;s Principles of Community.</p>

		<p><strong>The Community Engagement Center brings together UC Merced students, staff, faculty, and Merced community members, agencies, and organizations to create and develop reciprocal partnerships that generate student learning, build capacity, and solve problems through service, scholarship, and leadership. These actions contribute to building a healthy and sustainable community (local to global) and creating positive change.</strong></p>
	</div>

	<div class="cec-about-accordion">
		<ul>
			<li>
				<button aria-controls="cec-acc-1" aria-expanded="false" class="cec-acc-btn">Community Engagement Center Goals</button>
				<div class="cec-about-acc-content" hidden id="cec-acc-1">
					<h4>Community Engagement Center Goals</h4>

					<ul>
						<li><strong>Facilitate:</strong> equitable, effective, and reciprocal partnerships and opportunities for students, faculty, and community partners in educational and co-curricular service and research experiences.</li>
						<li><strong>Provide:</strong> opportunities to, and facilitate connections between, campus and community entities.</li>
						<li><strong>Support:</strong> positive community engagement outcomes through educational workshops, trainings, and program implementation.</li>
					</ul>
				</div>
			</li>
			<li>
				<button aria-controls="cec-acc-2" aria-expanded="false" class="cec-acc-btn">Learning Outcomes</button>
				<div class="cec-about-acc-content" hidden id="cec-acc-2">
					<h4>Learning Outcomes</h4>

					<ul>
						<li><strong>Civic Responsibility:</strong> Capacity to express an understanding of issues within the community and the responsibility to participate in democratic processes to work toward positive changes.</li>
						<li><strong>Consciousness of Self:</strong> Ability to identify individual values and interests, to gain the confidence to act consistently with values, and to respect and appreciate the perspectives, values, and life situations of others.</li>
						<li><strong>Academic Success:</strong> Ability to apply academic concepts to community issues and concepts of community issues to academic learning, alongside the development of professional skills.</li>
					</ul>
				</div>
			</li>
			<li>
				<button aria-controls="cec-acc-3" aria-expanded="false" class="cec-acc-btn">UC Merced Strategic Plan Related to the CEC</button>
				<div class="cec-about-acc-content" hidden id="cec-acc-3">
					<h4>Strategic Plans</h4>

					<ul>
						<li><strong>GOAL 1: Engage Our World and Region Through Discovery and the Advancement of Knowledge</strong><br />
							<br />
							We are a young campus already recognized for the unparalleled trajectory and quality of our research. As we move toward joining the select number of campuses at the very high research classification (R1), we will continue to establish ourselves as a national hub for interdisciplinary and transformational research that supports equity and prosperity globally and locally, with particular sensitivity for the San Joaquin Valley. Research experiences, a hallmark of our educational programs, will provide fertile ground for our undergraduate and graduate students to develop the 21st century skills and knowledge essential to creating and leading positive change at global, national, and local levels.</li>
						<li><strong>GOAL 2: Develop Future Scholars and Leaders</strong><br />
							<br />
							As our campus continues to grow, we will provide our students with the personal and academic support to succeed through world-class educational experiences delivered by outstanding educators and researchers. Honoring our students&#39; experiences as strengths upon which to build, our offerings will develop lifelong learners empowered by the habits of mind and tools of a researcher and address whole-student development, lead to career readiness, and encourage and enable civic engagement. Through a supportive community and educational experiences that are inclusive, high-impact, experiential, and research-based, we will foster the intellectual and personal development of diverse scholars and leaders. Our students will leave our campus recognizing the importance of global and local community and having contributed to the San Joaquin Valley. They will be prepared to be the next generation of diverse scholars, leaders, and agents of change.</li>
						<li><strong>GOAL 3: Cultivate a Culture of Dignity and Respect for All</strong><br />
							<br />
							Bold scholarship requires us to dismantle long-standing exclusionary practices in higher education. We aim to adopt research-grounded practices that drive our campus toward inclusive excellence. To do so, we will invest in the resources, and cultivate the skills, knowledge, and comprehensively inclusive and anti-racist attitudes necessary to ensure that each unit, department, division, and stakeholder clearly demonstrates their contribution to our Principles of Community.</li>
					</ul>

					<p><a href="https://strategicplan.ucmerced.edu/goals-and-objectives" target="_blank">View UC Merced Strategic Plan Goals and Objectives (opens in new tab)</a></p>
				</div>
			</li>
		</ul>
	</div>

	<div class="cec-contact-section">
		<h2>Community Engagement Center Information</h2>

		<div class="cec-contact-info">
			<div class="cec-contact-item">
				<h3>Hours</h3>

				<p>Monday - Friday<br />
					9:00 AM - 5:00 PM</p>
			</div>

			<div class="cec-contact-item">
				<h3>Email</h3>

				<p><a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu (opens email)</a></p>
			</div>

			<div class="cec-contact-item">
				<h3>Location</h3>

				<p>Our office is at <strong>KL 190</strong>. Please feel free to stop by any time during our hours!</p>

				<p>Visit <a href="http://www.ucmerced.edu/directions-map" target="_blank">Maps and Directions (opens in new tab)</a> and <a href="https://registrar.ucmerced.edu/resources/maps" target="_blank">Classroom Maps (opens in new tab)</a> for further details.</p>
			</div>
		</div>
	</div>

	<div class="cec-cta-section">
		<div class="cec-cta-card">
			<h3>Meet Our Team</h3>

			<p>Get to know the passionate staff members who make the Community Engagement Center a welcoming and impactful space for students and the community.</p>
			<a class="cec-cta-button" href="https://cec.ucmerced.edu/staff">Meet Our Staff</a></div>

		<div class="cec-cta-card">
			<h3>Join Our Mailing List</h3>

			<p>Stay updated on upcoming events, volunteer opportunities, and all the ways you can get involved with community engagement at UC Merced.</p>
			<a class="cec-cta-button" href="https://cec.ucmerced.edu/mailing-list">Join the Mailing List</a></div>
	</div>
</div>
<script>
document.querySelectorAll('.cec-acc-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var expanded = this.getAttribute('aria-expanded') === 'true';
        var content = document.getElementById(this.getAttribute('aria-controls'));
        this.setAttribute('aria-expanded', expanded ? 'false' : 'true');
        if (expanded) {
            content.setAttribute('hidden', '');
        } else {
            content.removeAttribute('hidden');
        }
    });
});
</script>
