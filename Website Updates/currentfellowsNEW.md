<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        .current-fellows-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0;
        }
        
        .welcome-section {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%);
            color: white;
            padding: 40px;
            border-radius: 12px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .welcome-section h1 {
            margin: 0 0 15px 0;
            font-size: 2.2em;
            color: white !important;
        }
        
        .welcome-section p {
            font-size: 1.1em;
            margin: 0;
            opacity: 0.95;
            line-height: 1.8;
        }

        /* Table of Contents Grid */
        .toc-section {
            background: white;
            padding: 35px;
            margin-bottom: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border: 2px solid #dbaa00;
        }

        .toc-section h2 {
            color: #0f2d52;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2em;
        }

        .toc-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0;
            margin-top: 20px;
        }

        .toc-grid-row-2 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0;
            margin-top: 0;
        }

        .toc-card {
            background: #0f2d52;
            padding: 25px 15px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 1px solid #dbaa00;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .toc-card:hover {
            background: #dbaa00;
            transform: scale(1.02);
            z-index: 1;
        }

        .toc-card a {
            color: white !important;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.05em;
            display: block;
        }

        .toc-card:hover a {
            color: #0f2d52 !important;
        }
        
        .content-section {
            background: white;
            padding: 35px;
            margin-bottom: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border-left: 5px solid #dbaa00;
            scroll-margin-top: 20px;
        }
        
        .content-section h2 {
            color: #0f2d52;
            margin: 0 0 20px 0;
            font-size: 1.8em;
        }

        .content-section h3 {
            color: #0f2d52;
            margin: 25px 0 15px 0;
            font-size: 1.4em;
        }

        .content-section h4 {
            color: #0f2d52;
            margin: 20px 0 10px 0;
            font-size: 1.2em;
            background-color: rgba(15, 45, 82, 0.1);
            padding: 10px;
            border-radius: 5px;
        }
        
        .content-section p {
            color: #555;
            margin-bottom: 15px;
            font-size: 1.05em;
        }

        .content-section ul {
            margin-left: 30px;
            margin-bottom: 15px;
        }

        .content-section li {
            margin-bottom: 10px;
            color: #555;
        }

        .content-section strong {
            color: #0f2d52;
        }
        
        .button-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin: 20px 0;
        }
        
        .button-grid-2col {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin: 20px 0;
        }
        
        .cta-button {
            display: inline-block;
            background: #dbaa00;
            color: #0f2d52 !important;
            padding: 14px 20px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            font-size: 1em;
            border: 2px solid #dbaa00;
            text-align: center;
        }
        
        .cta-button:hover {
            background: #0f2d52;
            color: #dbaa00 !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            border: 2px solid #0f2d52;
        }

        .cta-button-secondary {
            background: #0f2d52;
            color: white !important;
            border: 2px solid #0f2d52;
        }

        .cta-button-secondary:hover {
            background: #dbaa00;
            color: #0f2d52 !important;
            border: 2px solid #dbaa00;
        }

        .info-box {
            background: #e8f4f8;
            border-left: 4px solid #0f2d52;
            padding: 20px;
            margin: 20px 0;
            border-radius: 4px;
        }
        
        .info-box p {
            margin: 0;
            color: #0f2d52;
            font-weight: 600;
        }

        /* Map Container */
        .map-container {
            background: rgba(15, 45, 82, 0.05);
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
        }

        .map-container h3 {
            text-align: center;
            color: #0f2d52;
            margin-bottom: 15px;
        }

        .map-container p {
            text-align: center;
            margin-bottom: 20px;
        }

        .map-container img {
            width: 100%;
            max-width: 600px;
            display: block;
            margin: 0 auto 20px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .map-button-container {
            text-align: center;
        }

        @media (max-width: 768px) {
            .current-fellows-container {
                padding: 0;
            }
            
            .welcome-section {
                padding: 25px;
                margin: 0 15px 40px 15px;
            }
            
            .welcome-section h1 {
                font-size: 1.8em;
            }

            .toc-section {
                margin: 0 15px 40px 15px;
            }

            .toc-grid,
            .toc-grid-row-2 {
                grid-template-columns: 1fr;
                gap: 0;
            }

            .toc-card {
                border-radius: 0;
            }
            
            .content-section {
                padding: 20px;
                margin: 0 15px 30px 15px;
            }

            .button-grid,
            .button-grid-2col {
                grid-template-columns: 1fr;
            }

            .content-section p {
                font-size: 1em;
            }
        }
</style>
<div class="current-fellows-container">
	<div class="welcome-section">
		<h1>Welcome Current College Corps Fellows!</h1>

		<p>This page is your comprehensive guide for the fellowship. Find planning resources like the Target Hours Calendar and Living Stipend Disbursement schedule to manage your time, and stay updated with our Monthly Newsletter. Explore extra service and training opportunities, and get guidelines for timesheet submission and workshop participation. Navigate your host site easily with our interactive map of site locations. Access essential links, transportation surveys, and key contacts. Whether you need staff support, financial aid answers, or mental health resources, everything you need is right here. If you have any additional questions, feel free to reach out to our College Corps team!</p>
	</div>
	<!-- Planning Your Year of Service -->

	<div class="content-section" id="planning">
		<h2>Planning Your Year of Service</h2>

		<p>This handbook will support Fellows throughout the program, equipping them with the essential tools for success during their year of service.</p>

		<div class="button-grid-2col"><a class="cta-button" href="https://drive.google.com/file/d/1wXjAkecwSAJ6Tti3YybwpaLSmIPb4Hl-/view?usp=sharing" target="_blank">Fellows Handbook</a> <a class="cta-button" href="https://merced-my.sharepoint.com/:b:/g/personal/dparga_ucmerced_edu/EXeV3czx24NOs7SBGYVpfi8BV69jDFCRdR2j25HpApBVQA?e=8dCJO5" target="_blank">Target Hours Calendar</a></div>

		<div class="button-grid"><a class="cta-button" href="https://cec.ucmerced.edu/d-street-shelter" target="_blank">Projected Hours: Planning Tool</a> <a class="cta-button" href="https://drive.google.com/file/d/1Z98EIenNjVtQSJijkZyxu_9Ayi0_76H9/view?usp=sharing" target="_blank">Major Checkpoints &amp; Dates</a> <a class="cta-button" href="https://drive.google.com/file/d/1jWfzVdD6Wu5gLWnzUwbCgAWsCBD8u0vc/view?usp=sharing" target="_blank">Living Stipend Disbursements</a></div>
	</div>
	<!-- AmericaLearns/Extra Service/Training Opportunities -->

	<div class="content-section" id="americlearns">
		<h2>AmericaLearns / Extra Service / Training Opportunities</h2>

		<h4>Monthly Workshops</h4>

		<div class="button-grid"><a class="cta-button-secondary cta-button" href="https://drive.google.com/file/d/18DjqhBMroEypFp1DcgqeIV6dXSfLg8uC/view?usp=sharing" target="_blank">AmericaLearns Resources</a> <a class="cta-button-secondary cta-button" href="https://ucmerced.box.com/s/xcx7i48k0gprl1e26dpv9543w3d5ifv0" target="_blank">Lunch and Learn Lessons</a></div>

		<h4>October 25th Saturday Seminar Powerpoints</h4>

		<div class="button-grid-2col"><a class="cta-button-secondary cta-button" href="https://ucmerced.box.com/s/hjr1hzjvftkmfxoc8cinab8v3u2ezcue" target="_blank">October 25th Saturday Seminar Slides</a></div>

		<h4>Service Back Home</h4>

		<p><strong><u>Fellows are responsible for serving 12-15 hours per week!</u></strong></p>

		<p>Those hours should be done at their assigned site. We understand Fellows may choose to go back home during spring break and winter break. If that is the case, Fellows are responsible for finding a site back home and providing that info to College Corps Staff.</p>

		<h3>Service outside of Merced / Holiday Break</h3>

		<ul>
			<li>Identify organization in home community &ndash; non-profit / government agency (similar to host sites)</li>
			<li>Outline your plan and provide information to College Corps staff (Eliza) prior to committing to the service</li>
			<li>Connect with the main contact at that site. They will need to confirm / verify your hours with the College Corps staff through an email or letter</li>
			<li>Those hours would be entered in America Learns under &quot;CEC&quot; &ndash; with a comment in America Learns that you arranged that time with CC staff in advance</li>
		</ul>

		<h3>Some guidance on the type of hours that &#39;counts&#39;</h3>

		<ul>
			<li>Service that &#39;counts&#39; is service that meets an immediate need for an organization / host site</li>
			<li>The service may fall within any of the six pathways but MUST have a &#39;hands on&#39; component</li>
			<li>Tabling for your club, giving items or money to a cause, these types of activities would not count for College Corps service hours</li>
		</ul>

		<h3>Where to find Volunteer Opportunities</h3>

		<ul>
			<li><a href="https://www.volunteermatch.org/" style="color: #dbaa00; font-weight: 600;" target="_blank">Volunteer Match website</a></li>
			<li>Google Maps: Look up &quot;Volunteer&quot; or &quot;Food Pantry&#39;s&quot; &quot;Recreation Centers&quot; &quot;Food Banks&quot; &quot;Non-Profit&quot;</li>
			<li>Contact Eliza for additional help</li>
		</ul>

		<h3>Academic Break Service Plans</h3>

		<p>Please select the survey that best fits your time frame:</p>

		<ul>
			<li>WINTER BREAK SERVICE PLAN: December 13-January 17, 2025 (OPENS NOVEMBER 13, 2024) (CLOSES DECEMBER 1, 2024)</li>
			<li>SPRING BREAK SERVICE PLAN: March 24-28, 2025 (OPENS FEBRUARY 1, 2025)</li>
			<li>SUMMER SERVICE PLAN: May 16-June 5, 2025 (OPENS APRIL 1, 2025)</li>
		</ul>

		<div class="button-grid"><a class="cta-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_2hmVgu41OvlsWwK" target="_blank">Winter Break Service Plan</a> <a class="cta-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_cDfdlZP2mFbyRr8" target="_blank">Spring Break Service Plan</a> <a class="cta-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_b4s7T6zwmDes6b4" target="_blank">Summer Service Plan</a></div>

		<h4>Additional Service Opportunities</h4>

		<p>Click <a href="https://cec.ucmerced.edu/current-events" style="color: #dbaa00; font-weight: 600;">HERE</a> for additional service opportunities offered by CEC (must sign up through the CEC).</p>

		<div class="info-box" style="margin-top: 30px;">
			<p style="margin-bottom: 15px;"><strong>Looking for more ways to complete your service hours?</strong></p>

			<p style="margin-bottom: 15px;">Explore our comprehensive list of Community Host Partners - organizations across Merced County where you can serve and make a difference in areas like K-12 Education, Climate Action, Food Security, and Public Health.</p>

			<div style="text-align: center; margin-top: 20px;"><a class="cta-button" href="https://cec.ucmerced.edu/current-community-partners" style="display: inline-block;" target="_blank">View Community Host Partners</a></div>
		</div>
	</div>
	<!-- Transportation Information -->

	<div class="content-section" id="transportation">
		<h2>Transportation Information</h2>

		<div class="map-container">
			<h3>Where do Fellows Serve?</h3>

			<p>Explore the map showcasing all the host sites that UC Merced College Corps has partnered with for the 2025-2026 academic year. This map highlights the various locations where our students will be making a positive impact in their communities. Discover the breadth of our partnerships and see where our efforts are taking place!</p>
			<img alt="College Corps Host Sites Map" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/map_ss_0.png" />
			<div class="map-button-container"><a class="cta-button" href="https://www.google.com/maps/d/edit?mid=13OMlFhUbYOvoUY6LaD38tyz01H2trJY&amp;usp=sharing" target="_blank">View Interactive Map</a></div>
		</div>

		<div class="button-grid"><a class="cta-button" href="https://drive.google.com/file/d/1RGiLt8o4R_JbXIUThXiKxbu6vXHoa4v8/view?usp=sharing" target="_blank">Transportation Policy</a> <a class="cta-button" href="https://merced.sharepoint.com/:b:/s/CollegeCorpsCohort3-UCM/EdaIp0E6CLFLswf_1vmvBngBT2TBS5XwQQjRj3tutTztqQ?e=b07fzX" target="_blank">Survey Schedule</a> <a class="cta-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_0D0KvH5owtGnhoq" target="_blank">Transportation Survey (12/02-12/15)</a></div>
	</div>
	<!-- Important Links -->

	<div class="content-section" id="important-links">
		<h2>Important Links</h2>

		<div class="button-grid"><a class="cta-button-secondary cta-button" href="https://americalearns.net/index.cfm?event=user.login" target="_blank">America Learns Timesheet</a> <a class="cta-button-secondary cta-button" href="https://account.box.com/login" target="_blank">BOX</a> <a class="cta-button-secondary cta-button" href="https://egrants.cns.gov/espan/main/login.jsp" target="_blank">AmeriCorps Portal</a></div>

		<h3 style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #dbaa00;">Monthly Newsletters</h3>

		<div class="button-grid"><a class="cta-button" href="https://septembernewsletter2025.my.canva.site/" target="_blank">September Newsletter</a></div>
	</div>
	<!-- Campus Resources -->

	<div class="content-section" id="resources">
		<h2>Campus Resources</h2>

		<p>UC Merced offers a variety of support services to help you succeed. Explore these resources for academic, personal, and community support.</p>

		<div class="button-grid"><a class="cta-button-secondary cta-button" href="https://international.ucmerced.edu/university-california-statement-guidance-and-resources-international-and-undocumented" target="_blank">Guidance &amp; Resources for International &amp; Undocumented Students</a> <a class="cta-button-secondary cta-button" href="https://studentaffairs.ucmerced.edu/dean-students" target="_blank">Dean of Students</a> <a class="cta-button-secondary cta-button" href="https://counseling.ucmerced.edu/about" target="_blank">Counseling &amp; Psychological Services (CAPS)</a> <a class="cta-button-secondary cta-button" href="https://undoc.ucmerced.edu/" target="_blank">Services for Undocumented Students</a> <a class="cta-button-secondary cta-button" href="https://care.ucmerced.edu/" target="_blank">Campus Advocacy/Resources/Education (CARE)</a> <a class="cta-button-secondary cta-button" href="https://access.ucmerced.edu/" target="_blank">Student Accessibility Services</a></div>

		<p style="margin-top: 20px;">Click <a href="https://admitted.ucmerced.edu/student-resources" style="color: #dbaa00; font-weight: 600;">HERE</a> to find more Student Services.</p>
	</div>
	<!-- Footer Contact -->

	<div class="content-section" style="border-left-color: #0f2d52;">
		<h2 style="display: block; margin-bottom: 15px;">Still Have Questions?</h2>

		<p style="margin-bottom: 10px;"><strong>Visit us:</strong><br />
			Community Engagement Center - KL 172<br />
			Monday - Friday, 9:00 AM - 5:00 PM</p>

		<p style="margin-bottom: 10px;"><strong>Email us:</strong><br />
			<a href="mailto:collegecorps@ucmerced.edu" style="color: #dbaa00;">collegecorps@ucmerced.edu</a></p>

		<p style="margin-bottom: 0;"><strong>Follow us on Instagram:</strong><br />
			<a href="https://www.instagram.com/ucmcollegecorps/" style="color: #dbaa00;" target="_blank">@ucmcollegecorps</a> | <a href="https://www.instagram.com/ucmercedcec/" style="color: #dbaa00;" target="_blank">@ucmercedcec</a></p>
	</div>
</div>
