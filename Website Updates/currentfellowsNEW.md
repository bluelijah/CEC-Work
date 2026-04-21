<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0;
}

.welcome-section {
    background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%);
    color: white;
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.welcome-section h1 { margin: 0 0 15px 0; font-size: 2.2em; color: white; }
.welcome-section p { font-size: 1.05em; opacity: 0.95; line-height: 1.8; }

.content-section {
    background: white;
    padding: 35px;
    margin-bottom: 25px;
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

.btn-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 15px;
}
.btn-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 15px;
}
.btn-grid-1 {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    margin-top: 15px;
}

.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    background: #dbaa00;
    color: #0f2d52 !important;
    padding: 14px 16px;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    font-size: 0.98em;
    border: 2px solid #dbaa00;
    text-align: center;
    text-shadow: none !important;
    background-clip: padding-box !important;
    -webkit-background-clip: padding-box !important;
}
.btn:hover {
    background: #0f2d52;
    color: #dbaa00 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    border-color: #0f2d52;
}
.btn:focus {
    outline: 3px solid #0f2d52;
    outline-offset: 2px;
}

.btn-dark {
    background: #0f2d52;
    color: white !important;
    border-color: #0f2d52;
}
.btn-dark:hover {
    background: #dbaa00;
    color: #0f2d52 !important;
    border-color: #dbaa00;
}

/* Collapsible toggle headers */
.toggle-section-wrapper {
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-left: 5px solid #dbaa00;
    margin-bottom: 25px;
    overflow: hidden;
    scroll-margin-top: 20px;
}

.toggle-header {
    width: 100%;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 25px 35px;
    background: white;
    border: none;
    text-align: left;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    font-size: 1rem;
    color: inherit;
    line-height: 1.2;
}
.toggle-header:focus {
    outline: none;
}
.toggle-header-heading {
    margin: 0;
    color: #0f2d52;
    font-size: 1.8em;
    font-weight: 600 !important;
    pointer-events: none;
    font-family: "Open Sans", sans-serif !important;
    line-height: 1.2;
}

.sub-toggle-header {
    width: 100%;
    cursor: pointer;
    background: #0f2d52;
    color: white;
    padding: 14px 20px;
    font-weight: 600;
    font-size: 1.05em;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: none;
    text-align: left;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}
.sub-toggle-header:focus {
    outline: 3px solid #dbaa00;
    outline-offset: 2px;
}
.sub-toggle-header:hover { background: #1a4a7a; }

.map-container {
    background: rgba(15,45,82,0.05);
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 15px;
    text-align: center;
}
.map-container img {
    width: 100%;
    max-width: 600px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    margin: 15px auto 20px;
    display: block;
}

.questions-section {
    background: #0f2d52;
    padding: 35px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 25px;
}
.questions-section h2 { color: white; margin-bottom: 15px; font-size: 1.8em; }
.questions-section p { color: rgba(255,255,255,0.9); margin-bottom: 20px; }
.questions-section .btn:focus {
    outline: 3px solid #fff;
    outline-offset: 2px;
}

#extra-body, #transport-body {
    overflow: hidden;
    transition: height 0.35s ease, opacity 0.35s ease;
}

@media (max-width: 768px) {
    .welcome-section { padding: 25px; margin: 0 15px 25px; }
    .content-section { padding: 20px; margin: 0 15px 20px; }
    .toggle-section-wrapper { margin: 0 15px 20px; }
    .questions-section { margin: 0 15px 20px; }
    .btn-grid, .btn-grid-2 { grid-template-columns: 1fr; }
    .toggle-header { padding: 20px; }
}
</style>
<div class="container"><!-- Welcome -->
	<div class="welcome-section">
		<h1>Welcome Current College Corps Fellows!</h1>

		<p>This page is your comprehensive guide for the fellowship. Find planning resources, stay updated with newsletters, explore service and training opportunities, and access key contacts and campus resources. If you have additional questions, feel free to reach out to our College Corps team!</p>
	</div>
	<!-- Official Fellow Resources -->

	<div class="content-section" id="official-resources">
		<h2>Official Fellow Resources</h2>

		<div class="btn-grid"><a class="btn" href="https://drive.google.com/file/d/1wXjAkecwSAJ6Tti3YybwpaLSmIPb4Hl-/view?usp=sharing" target="_blank">Fellows Handbook (opens in new tab)</a> <a class="btn" href="https://drive.google.com/file/d/1Z98EIenNjVtQSJijkZyxu_9Ayi0_76H9/view?usp=sharing" target="_blank">Fellow Training Plan (opens in new tab)</a> <a class="btn" href="https://drive.google.com/file/d/1jWfzVdD6Wu5gLWnzUwbCgAWsCBD8u0vc/view?usp=sharing" target="_blank">Living Stipend Disbursements (opens in new tab)</a> <a class="btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_2hmVgu41OvlsWwK" target="_blank">Winter Break Service Plan (opens in new tab)</a> <a class="btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_cDfdlZP2mFbyRr8" target="_blank">Spring Break Service Plan (opens in new tab)</a> <a class="btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_b4s7T6zwmDes6b4" target="_blank">Summer Service Plan (opens in new tab)</a> <a class="btn" href="https://ucmerced.app.box.com/file/1558780453477?s=o3bz9fwwdck9pfjsgemb3fzzkvn43k9p" target="_blank">Personal Learning Plan (opens in new tab)</a></div>
	</div>
	<!-- Extra Fellow Resources (collapsible) -->

	<div class="toggle-section-wrapper" id="extra-resources"><button aria-controls="extra-body" aria-expanded="false" class="toggle-header" onclick="toggleSection('extra-body', 'extra-arrow', this)"><span class="toggle-header-heading">Extra Fellow Resources</span> <span aria-hidden="true" id="extra-arrow" style="font-size:1.2em; color:#0f2d52; transition: transform 0.3s; display:inline-block; flex-shrink:0;">▼</span></button>

		<div id="extra-body" style="padding: 0 35px 30px; display:none; border-top: 1px solid #e0e0e0; margin-top: 0; padding-top: 25px;"><!-- Transportation sub-dropdown -->
			<div style="border:1px solid #dbaa00; border-radius:8px; margin-bottom: 15px; overflow:hidden;"><button aria-controls="transport-body" aria-expanded="false" class="sub-toggle-header" onclick="toggleSection('transport-body', 'transport-arrow', this)"><span>Transportation Information</span> <span aria-hidden="true" id="transport-arrow" style="font-size:0.8em; transition: transform 0.3s; display:inline-block;">▼</span></button>

				<div aria-label="Transportation Information" id="transport-body" role="region" style="display:none; padding:25px; background:#f9f9f9;">
					<div class="map-container">
						<p>Explore the map showcasing all host sites that UC Merced College Corps has partnered with for the 2025-2026 academic year.</p>
						<img alt="Map of College Corps host sites across Merced County for the 2025-2026 academic year" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/map_ss_0.png" /> <a class="btn" href="https://www.google.com/maps/d/edit?mid=13OMlFhUbYOvoUY6LaD38tyz01H2trJY&amp;usp=sharing" target="_blank">View Interactive Map (opens in new tab)</a></div>

					<div class="btn-grid"><a class="btn" href="https://drive.google.com/file/d/1RGiLt8o4R_JbXIUThXiKxbu6vXHoa4v8/view?usp=sharing" target="_blank">Transportation Policy (opens in new tab)</a> <a class="btn" href="https://merced.sharepoint.com/:b:/s/CollegeCorpsCohort3-UCM/EdaIp0E6CLFLswf_1vmvBngBT2TBS5XwQQjRj3tutTztqQ?e=b07fzX" target="_blank">Survey Schedule (opens in new tab)</a> <a class="btn" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_0D0KvH5owtGnhoq" target="_blank">Transportation Survey (opens in new tab)</a></div>
				</div>
			</div>

			<div class="btn-grid"><a class="btn" href="https://ucmerced.box.com/s/xcx7i48k0gprl1e26dpv9543w3d5ifv0" target="_blank">Lunch and Learn Lessons (opens in new tab)</a> <a class="btn" href="#">Seminar Powerpoints</a> <a class="btn" href="https://account.box.com/login" target="_blank">Box (opens in new tab)</a> <a class="btn" href="https://admitted.ucmerced.edu/student-resources" target="_blank">Campus Resources (opens in new tab)</a> <a class="btn" href="https://international.ucmerced.edu/university-california-statement-guidance-and-resources-international-and-undocumented" target="_blank">Guidance for International &amp; Undocumented Students (opens in new tab)</a> <a class="btn" href="#">Newsletter</a></div>
		</div>
	</div>
	<!-- America Learns -->

	<div class="content-section" id="america-learns">
		<h2>America Learns</h2>

		<p style="color:#555; margin-bottom: 15px; font-size: 1.05em;">This is where all your hours are tracked. Log in regularly to keep your timesheets up to date.</p>

		<div class="btn-grid-1"><a class="btn" href="https://americalearns.net/index.cfm?event=user.login" target="_blank">America Learns Timesheet (opens in new tab)</a></div>
	</div>
	<!-- Finding Service Opportunities -->

	<div class="content-section" id="service-opportunities">
		<h2>Resources for Finding Service Opportunities</h2>

		<div class="btn-grid"><a class="btn" href="https://cec.ucmerced.edu/" target="_blank">CEC Website (opens in new tab)</a> <a class="btn" href="https://cec.ucmerced.edu/current-community-partners" target="_blank">Community Host Partners (opens in new tab)</a> <a class="btn" href="https://www.volunteermatch.org/" target="_blank">Volunteer Match (opens in new tab)</a></div>
	</div>
	<!-- Post-Commitment -->

	<div class="content-section" id="post-commitment">
		<h2>Now That You&#39;ve Completed Your College Corps Commitments</h2>

		<div class="btn-grid-2"><a class="btn" href="https://egrants.cns.gov/espan/main/login.jsp" target="_blank">AmeriCorps Portal (opens in new tab)</a> <a class="btn" href="https://cec.ucmerced.edu/psl-certificate" target="_blank">PSL Award (opens in new tab)</a></div>
	</div>
	<!-- Questions -->

	<div class="questions-section">
		<h2>Still Have Questions?</h2>

		<p>Reach out to the College Corps team -- we&#39;re here to help!</p>
		<a class="btn" href="https://cec.ucmerced.edu/college-corps-contact" target="_blank">Contact College Corps (opens in new tab)</a></div>
</div>
<script>
    function toggleSection(bodyId, arrowId, trigger) {
        var body = document.getElementById(bodyId);
        var arrow = document.getElementById(arrowId);
        var isOpen = body.classList.contains('open');

        if (isOpen) {
            body.style.height = body.scrollHeight + 'px';
            body.offsetHeight;
            body.style.height = '0';
            body.style.opacity = '0';
            arrow.style.transform = 'rotate(0deg)';
            trigger.setAttribute('aria-expanded', 'false');
            body.addEventListener('transitionend', function handler() {
                body.style.display = 'none';
                body.classList.remove('open');
                body.removeEventListener('transitionend', handler);
            });
        } else {
            body.style.display = 'block';
            body.style.height = '0';
            body.style.opacity = '0';
            body.offsetHeight;
            body.style.height = body.scrollHeight + 'px';
            body.style.opacity = '1';
            arrow.style.transform = 'rotate(180deg)';
            trigger.setAttribute('aria-expanded', 'true');
            body.classList.add('open');
            body.addEventListener('transitionend', function handler() {
                body.style.height = 'auto';
                body.removeEventListener('transitionend', handler);
            });
        }
    }
</script>