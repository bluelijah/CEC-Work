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

        /* Staff Cards */
        .staff-section-title {
            text-align: center;
            color: #0f2d52;
            border-bottom: 3px solid #ffbf3c;
            padding-bottom: 10px;
            margin-bottom: 30px;
            font-size: 1.6em;
        }

        .card-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            padding: 20px 0;
            justify-content: center;
        }

        .flip-card {
            background-color: transparent;
            width: 100%;
            max-width: 325px;
            height: 434px;
            perspective: 1000px;
            margin: 0 auto;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            border-radius: 15px;
        }

        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-card-front, .flip-card-back {
            border-radius: 15px;
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            overflow: hidden;
        }

        .flip-card-front {
            background-color: #fff;
        }

        .flip-card-back {
            background: linear-gradient(300deg, #a6beea, #f4cd2a);
            color: #0F2D52;
            transform: rotateY(180deg);
            box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
            padding: 20px;
            box-sizing: border-box;
            font-size: 0.9rem;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: rgba(15, 45, 82, 0.5) transparent;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        .flip-card-back::-webkit-scrollbar {
            width: 6px;
        }

        .flip-card-back::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
        }

        .flip-card-back::-webkit-scrollbar-thumb {
            background: rgba(15, 45, 82, 0.5);
            border-radius: 3px;
        }

        .flip-card-back::-webkit-scrollbar-thumb:hover {
            background: rgba(15, 45, 82, 0.7);
        }

        .flip-card-back h1 {
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 10px;
            flex-shrink: 0;
        }

        .flip-card-back p {
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: #0F2D52;
        }

        .flip-card-back a {
            color: #0f2d52;
            font-weight: 600;
        }

        .flip-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
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

            .flip-card {
                max-width: 100%;
            }

            .card-container {
                grid-template-columns: 1fr;
            }
        }
</style>
<div class="current-fellows-container">
	<div class="welcome-section">
		<h1>Welcome Current College Corps Fellows!</h1>

		<p>This page is your comprehensive guide for the fellowship. Find planning resources like the Target Hours Calendar and Living Stipend Disbursement schedule to manage your time, and stay updated with our Monthly Newsletter. Explore extra service and training opportunities, and get guidelines for timesheet submission and workshop participation. Navigate your host site easily with our interactive map of site locations. Access essential links, transportation surveys, and key contacts. Whether you need staff support, financial aid answers, or mental health resources, everything you need is right here. If you have any additional questions, feel free to reach out to our College Corps team!</p>
	</div>
	<!-- Table of Contents -->

	<div class="toc-section">
		<h2>Quick Navigation</h2>

		<div class="toc-grid">
			<div class="toc-card"><a href="#planning">Planning Your Year of Service</a></div>

			<div class="toc-card"><a href="#americlearns">AmericaLearns &amp; Training</a></div>

			<div class="toc-card"><a href="#transportation">Transportation Information</a></div>
		</div>

		<div class="toc-grid-row-2">
			<div class="toc-card"><a href="#important-links">Important Links</a></div>

			<div class="toc-card"><a href="#staff">Meet the Staff</a></div>

			<div class="toc-card"><a href="#resources">Campus Resources</a></div>
		</div>
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
			<img alt="College Corps Host Sites Map" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/map_ss_0.png" />
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
	<!-- Staff Section -->

	<div class="content-section" id="staff">
		<h2>Have Questions? Meet the Staff</h2>

		<div class="card-container">
			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Eliza Sanchez" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/image_9-26-24_2.35.09_pm.jpg" /></div>

					<div class="flip-card-back">
						<h1>Eliza Sanchez</h1>

						<p><strong>Fellow Program Coordinator</strong></p>

						<p>Eliza is here to assist Fellows with any questions/concerns/suggestions they may have. Eliza is your main contact for AmericaLearns, additional service opportunities, training, and service back home.</p>

						<p><a href="https://outlook.office.com/bookwithme/user/64ade8c431a44fbfacd81e578fd32366%40ucmerced.edu/meetingtype/060f98a8-05a9-471a-b92e-803cc89370dc?anonymous" target="_blank">Book with me</a></p>

						<p><a class="__cf_email__" data-cfemail="690c1a08070a010c13585850291c0a040c1b0a0c0d470c0d1c" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>

			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Alondra Franco Hernandez" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/alondra.jpg" /></div>

					<div class="flip-card-back">
						<h1>Alondra Franco Hernandez</h1>

						<p><strong>Program Manager</strong></p>

						<p>Alondra assists with any general questions about the program and with any issues/questions about transportation.</p>

						<p><a href="https://outlook-sdf.office.com/bookwithme/user/95b08b725e044511b35161d0daf9dab4@ucmerced.edu?anonymous&amp;ep=pcard" target="_blank">Book with me</a></p>

						<p><a class="__cf_email__" data-cfemail="88e9e4e7e6ecfae9e9e4fee9faedf2c8fdebe5edfaebedeca6edecfd" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>

			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Kyla Perez" src="/sites/cec.ucmerced.edu/files/people/portraits/k.perez_cc_headshot.png" /></div>

					<div class="flip-card-back">
						<h1>Kyla Perez</h1>

						<p><strong>Program Data Specialist</strong></p>

						<p>Kyla is here to assist anyone with questions regarding DSIG Payment Request Forms and Mileage Reimbursement.</p>

						<p><a href="https://outlook-sdf.office.com/bookwithme/user/fce3fc4acd984cacab383a701968b6a5%40ucmerced.edu/meetingtype/11d6251b-820c-4501-ad90-cb958e75f02c?anonymous" target="_blank">Book with me</a></p>

						<p><a class="__cf_email__" data-cfemail="bed5c7d2dfcedbccdbc4fecbddd3dbccdddbda90dbdacb" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>

			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Danielle Parga" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/danielle.jpg" /></div>

					<div class="flip-card-back">
						<h1>Danielle Parga</h1>

						<p><strong>Public Service Program Specialist</strong></p>

						<p>Danielle is here to assist Host Site Supervisors with any questions/concerns/suggestions they may have.</p>

						<p><a class="__cf_email__" data-cfemail="9ffbeffeedf8fedfeafcf2faedfcfafbb1fafbea" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>

			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Debra Fitzgerald" src="/sites/cec.ucmerced.edu/files/people/portraits/d.fitzgerald_cc_headshot.png" /></div>

					<div class="flip-card-back">
						<h1>Debra Fitzgerald</h1>

						<p><strong>Grant Administrative Officer</strong></p>

						<p>Debi is here to provide direction and oversight of administrative operations, including grant writing and day to day administration of budgets and recordkeeping systems.</p>

						<p><a class="__cf_email__" data-cfemail="b6d2d0dfc2ccd1d3c4d7dad285f6c3d5dbd3c4d5d3d298d3d2c3" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>

			<div class="flip-card">
				<div class="flip-card-inner">
					<div class="flip-card-front"><img alt="Lisa Silveira" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/lisa_-_photo_1.png" /></div>

					<div class="flip-card-back">
						<h1>Lisa Silveira</h1>

						<p><strong>Financial Aid Advisor</strong></p>

						<p>Lisa is here to assist with any inquiries regarding financial aid or living disbursements.</p>

						<p><a class="__cf_email__" data-cfemail="bfd9d6d1ded6dbdcd0d3d3dad8dadcd0cdcfccffcadcd2dacddcdadb91dadbca" href="/cdn-cgi/l/email-protection">[email&nbsp;protected]</a></p>
					</div>
				</div>
			</div>
		</div>
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
