<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Public Service and Leadership Certificate</title>
<style type="text/css">body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
}

.pslc-container {
    box-sizing: border-box;
    margin: 0 auto;
    max-width: 100%;
    padding: 0 15px;
}

.pslc-container > h2:first-child,
.pslc-container > h1:first-child {
    margin-top: 0;
}

h1, h2, h3 {
    font-weight: 700;
    color: #003366;
    margin-top: 30px;
    margin-bottom: 15px;
}

h1 {
    text-align: left;
}

h2 {
    border-bottom: 3px solid #dbaa00;
    display: inline-block;
    padding-bottom: 5px;
}

p {
    margin-bottom: 15px;
}

ul, ol {
    margin-left: 20px;
    margin-bottom: 20px;
}

.highlight-box {
    background: #fdf7e3;
    border-left: 6px solid #dbaa00;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.steps {
    margin: 40px 0;
}

.step {
    background: #f9f9f9;
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 25px;
}

.step h3 {
    margin-top: 0;
    color: #b86b00;
}

.qr-section {
    display: flex;
    align-items: center;
    gap: 20px;
    background: #f5faff;
    border: 1px solid #cce0ff;
    padding: 20px;
    border-radius: 12px;
    margin: 30px 0;
}

.qr-section img {
    width: 140px;
    height: auto;
    border: 3px solid #003366;
    border-radius: 12px;
}

.course-list {
    columns: 2;
    -webkit-columns: 2;
    -moz-columns: 2;
    margin-top: 15px;
}

.course-list li {
    margin-bottom: 8px;
}

iframe {
    width: 100%;
    height: 500px;
    border: none;
    border-radius: 8px;
    margin: 15px 0;
}

.note {
    font-size: 0.9em;
    color: #666;
}

/* Dropdown */
.content-box {
    background: rgba(255, 255, 255, 0.95);
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
}

.dropdown {
    margin-bottom: 2rem;
}

.dropdown-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
    color: white;
    padding: 1.5rem;
    cursor: pointer;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.2rem;
    text-transform: uppercase;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(15, 45, 82, 0.2);
    width: 100%;
    text-align: left;
    border: none;
    font-family: "Helvetica Neue", Arial, sans-serif;
    box-sizing: border-box;
}

.dropdown-arrow {
    font-size: 1rem;
    margin-left: 1rem;
    transition: transform 0.3s ease;
    display: inline-block;
    flex-shrink: 0;
}

.dropdown-header[aria-expanded="true"] .dropdown-arrow {
    transform: rotate(180deg);
}

.dropdown-subtitle {
    font-size: 0.85rem;
    font-weight: normal;
    text-transform: none;
    margin-top: 0.3rem;
    opacity: 0.9;
    display: block;
}

.dropdown-header:hover {
    background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
    box-shadow: 0 4px 15px rgba(219, 170, 0, 0.4);
}

.dropdown-header:focus {
    outline: 3px solid #dbaa00;
    outline-offset: 2px;
}

.dropdown-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background: white;
    border: 2px solid #e0e0e0;
    border-top: none;
    border-radius: 0 0 8px 8px;
}

.dropdown-content.active {
    max-height: 2000px;
    padding: 1.5rem;
    margin-top: -8px;
    overflow-y: auto;
}

.session-item {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 8px;
    background: #f9f9f9;
    border-left: 3px solid #dbaa00;
}

.session-date {
    min-width: 80px;
    text-align: center;
    background: #0f2d52;
    color: white;
    padding: 0.5rem;
    border-radius: 8px;
}

.session-month {
    font-size: 0.9rem;
    text-transform: uppercase;
}

.session-day {
    font-size: 1.5rem;
    font-weight: bold;
}

.session-details h4 {
    color: #0f2d52;
    margin-bottom: 0.5rem;
}

.session-details p {
    margin: 0;
    font-size: 1rem;
}

.forms-section {
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
    margin-top: 2rem;
}

.forms-section h3 {
    color: #0f2d52;
    font-size: 1.4rem;
    margin-bottom: 1rem;
    text-align: center;
}

.forms-section p {
    color: #555;
    margin-bottom: 1.5rem;
    text-align: center;
}

.cta-link {
    display: inline-flex;
    align-items: center;
    min-height: 44px;
    padding: 0.75em 2em;
    background-color: #dbaa00;
    color: #003366 !important;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.1em;
    transition: background-color 0.3s ease;
    border: 2px solid #dbaa00;
}

.cta-link:hover {
    background-color: #c99a00;
    border-color: #c99a00;
}

.cta-link:focus {
    outline: 3px solid #003366;
    outline-offset: 2px;
}

.button-center {
    text-align: center;
}

@media (max-width: 768px) {
    .pslc-container {
        padding-left: 15px;
        padding-right: 15px;
    }

    .step {
        padding: 15px;
    }

    .qr-section {
        flex-direction: column;
        align-items: flex-start;
    }

    .course-list {
        columns: 1;
    }

    iframe {
        width: 100%;
        height: auto;
    }

    .button-center {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .content-box {
        padding: 1.5rem;
    }

    .session-item {
        flex-direction: column;
    }

    .session-date {
        min-width: auto;
    }
}
</style>
<div class="pslc-container">
    <h2>Want to get a Public Service &amp; Leadership Certificate?</h2>

    <p>If you are a student who:</p>

    <ul>
        <li>Demonstrates commitment to public service and leadership through co-curricular experiences</li>
        <li>Likes gaining hands-on experience</li>
        <li>Wants to develop their interpersonal skills</li>
    </ul>

    <h2>Benefits of PSLC</h2>

    <ul>
        <li>Graduation cord and certificate</li>
        <li>LinkedIn Endorsement from professional staff</li>
        <li>Letter of recommendation upon request</li>
    </ul>

    <h2>How to Get Started</h2>

    <div class="steps">
        <div class="step">
            <h3>Step 1: Pathways to Public Service Assessment</h3>
            <p>Discover which pathway(s) to public service most speak to your interests and goals. After completing the survey - <strong>please make sure to take a screenshot of your results</strong> - you will need it to complete the application!</p>

            <div class="qr-section">
                <img alt="QR code to take the Pathways to Public Service Assessment" src="/sites/g/files/ufvvjh561/f/images/pathwaysqr.png" />
                <p><a href="https://stanforduniversity.qualtrics.com/jfe/form/SV_2sO52GgyYDCVUkm" target="_blank">Take the Pathways to Public Service Assessment and save your results (opens in new tab)</a></p>
            </div>

            <p><strong>Pathways include:</strong> Direct Service, Philanthropy, Community Organizing &amp; Activism, Community-Engaged Learning &amp; Research, Policy &amp; Governance, Social Entrepreneurship, and Corporate Social Responsibility.</p>
        </div>

        <div class="step">
            <h3>Step 2: Complete Direct Service Hours (80)</h3>
            <p>Direct service hours involve working to address the immediate needs of individuals or communities, often involving direct contact with those served.</p>

            <p><strong>Notes:</strong></p>

            <ul>
                <li>Only <em>direct community service</em> should be submitted in CatLife.</li>
                <li>Service can be completed outside Merced, but must include contact info for verification.</li>
                <li><strong>Not Service:</strong> Tabling for a fraternity, sorority, or club to recruit members.</li>
            </ul>

            <p>Refer to the <a href="https://cec.ucmerced.edu/calendar" target="_blank"><strong>CEC Calendar (opens in new tab)</strong></a>, the <a href="https://cec.ucmerced.edu/one-time-service-projects" target="_blank"><strong>One-Time Service page (opens in new tab)</strong></a>, the <a href="https://cec.ucmerced.edu/Long/Term/Service" target="_blank"><strong>Long-Term Service page (opens in new tab)</strong></a>, and <a href="https://cec.ucmerced.edu/signature-opportunities" target="_blank"><strong>Signature Opportunities (opens in new tab)</strong></a> to find volunteer work.</p>

            <p><a href="https://ucmerced.presence.io/form/apply-for-opportunity" target="_blank">Submit your hours on CatLife (opens in new tab)</a> -- if you don't know how to submit, visit the <a href="https://cec.ucmerced.edu/service-hours" target="_blank">CatLife hours submission guide (opens in new tab)</a>.</p>
        </div>

        <div class="step">
            <h3>Step 3: Community-Engaged Course</h3>
            <p>Complete a community-engaged course with a passing grade of C or above. These courses include assignments that benefit the community while enhancing student learning.</p>

            <p><strong>Examples of Community-Engaged Courses:</strong></p>

            <ul class="course-list">
                <li>ENGR 096, 097, 197</li>
                <li>USTU 092</li>
                <li>CRS 010, 100, 195</li>
                <li>SPAN 107, 108, 160</li>
                <li>PH 181</li>
                <li>PSY 156, 191, 196, 115</li>
                <li>MIST 207</li>
                <li>IH 203</li>
                <li>ANTH 170</li>
                <li>GASP 192</li>
                <li>EDUC X304, X306, X313, X400</li>
                <li>NSED 024, 034, 064, 074, 150, 174, 184</li>
            </ul>

            <p class="note">If you believe your course qualifies but is not listed, email <a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a>.</p>
        </div>

        <div class="step">
            <h3>Step 4: Community-Focused Capstone Project</h3>
            <p>Develop a project with a clear focus on community engagement. This project can be completed through a previous course or program while at UC Merced - ex. YLP, SSI Internships. If students have not or will not complete a capstone project through a course or program, they can submit a capstone proposal to the CEC at least one semester prior to expected graduation date; once approved, the project can be completed independently or with CEC support.</p>

            <p><strong>Example:</strong> A student helped a local non-profit launch an anti-vape campaign for rural middle school students by creating a website and social media campaign. The project lasted 6 months and included a survey to measure impact.</p>
        </div>

        <div class="step">
            <h3>Step 5: Submit Your Application</h3>
            <p>Once you have completed all the requirements (Steps 1-4), fill out the formal application for the Public Service &amp; Leadership Certificate. The CEC will verify your information and confirm your completion of all requirements.</p>

            <div style="margin: 20px 0;">
                <a class="cta-link" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_9QyRUheXdSuIMui" target="_blank">Complete the PSL Certificate Application (opens in new tab)</a>
            </div>

            <p class="note">Make sure you have completed all previous steps before submitting your application.</p>
        </div>
    </div>

    <div class="highlight-box" role="note">
        <h3 style="margin-top: 0; color: #b86b00;">Official PSL Certificate Guide</h3>
        <p>Want all this information in one convenient document?</p>
        <a class="cta-link" href="https://ucmerced.box.com/s/6uem1v2q9a9dl3reglyg1s83jknfkvk5" target="_blank">Download the Official Guide (PDF, opens in new tab)</a>
    </div>

    <h2>Why Should I Apply?</h2>

    <ul>
        <li>Become a more active member within the UC Merced community</li>
        <li>Collaborate with others and develop transferrable skills (leadership, communication, etc.)</li>
        <li>Add it to your resume!</li>
        <li>Earn the <strong>Public Service &amp; Leadership Certificate</strong></li>
    </ul>

    <h2>Want to Learn More?</h2>

    <div class="content-box" role="note">
        <div class="dropdown">
            <button
                class="dropdown-header"
                id="sessions-toggle"
                aria-expanded="false"
                aria-controls="sessionsDropdown"
                onclick="toggleDropdown(this)"
                onkeydown="handleDropdownKey(event, this)"
            >
                Public Service &amp; Leadership Certificate Info Sessions
                <span class="dropdown-arrow" aria-hidden="true">&#9660;</span>
            </button>

            <div class="dropdown-content" id="sessionsDropdown" role="region" aria-labelledby="sessions-toggle">
                <div class="session-item">
                    <div class="session-details">
                        <p>Time: <strong>None currently scheduled</strong></p>
                        <p>Invite link: <strong>None currently scheduled</strong></p>
                        <p>Meeting ID: <strong>None currently scheduled</strong></p>
                    </div>
                </div>

                <p>If you would like to schedule a personal Zoom info meeting, please email <a href="mailto:austingrey@ucmerced.edu">austingrey@ucmerced.edu</a></p>
            </div>
        </div>
    </div>
</div>

<script>
    function toggleDropdown(btn) {
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
        var content = document.getElementById(btn.getAttribute('aria-controls'));
        content.classList.toggle('active', !expanded);
    }

    function handleDropdownKey(event, btn) {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            toggleDropdown(btn);
        }
    }
</script>