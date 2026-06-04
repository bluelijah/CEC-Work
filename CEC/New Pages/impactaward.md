<style type="text/css">.award-container {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #333;
  margin: 0 auto;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

/* Welcome banner */
.award-welcome {
  background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%);
  color: white;
  padding: 40px;
  border-radius: 12px;
  margin-bottom: 40px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.award-welcome h1 {
  margin: 0 0 15px 0;
  font-size: 2.2em;
  color: white !important;
}

.award-welcome p {
  font-size: 1.1em;
  margin: 0;
  opacity: 0.95;
}

/* Shared section card */
.award-section {
  background: white;
  padding: 35px;
  margin-bottom: 30px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border-left: 5px solid #dbaa00;
}

.award-section h2 {
  color: #0f2d52;
  margin: 0 0 15px 0;
  font-size: 1.4em;
}

/* Recipient header row */
.recipient-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
}

.recipient-name {
  font-size: 1.3em;
  font-weight: 700;
  color: #0f2d52;
  margin: 0 0 4px;
}

.recipient-subtitle {
  font-size: 0.95em;
  color: #666;
  margin: 0;
}

.year-label {
  font-size: 0.85em;
  color: #555;
  display: block;
  margin-bottom: 4px;
  font-weight: 600;
}

.year-select {
  font-size: 1em;
  border: 1px solid #aaa;
  border-radius: 6px;
  padding: 8px 12px 8px 12px;
  background: #f5f5f5;
  color: #111;
  cursor: pointer;
  min-width: 260px;
  min-height: 40px;
}

.year-select:focus {
  outline: 3px solid #0f2d52;
  outline-offset: 2px;
}

.recipient-body {
  font-size: 1.05em;
  line-height: 1.7;
  color: #555;
}

.placeholder-box {
  background: #f5f5f5;
  border: 1px dashed #ccc;
  border-radius: 8px;
  padding: 1.25rem;
  text-align: center;
  color: #999;
  font-size: 1em;
  font-style: italic;
}

.recipient-img {
  width: 100%;
  max-width: 560px;
  border-radius: 8px;
  margin-top: 1rem;
  display: block;
}

/* Tab row */
.tab-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-bottom: 0;
}

.tab-btn {
  background: #f0f0f0;
  border: 1px solid #ccc;
  border-bottom: none;
  border-radius: 8px 8px 0 0;
  padding: 14px 18px;
  cursor: pointer;
  text-align: left;
  color: #555;
  font-size: 1em;
  font-weight: 600;
  font-family: inherit;
  transition: background 0.15s;
}

.tab-btn:hover {
  background: #fff;
  color: #0f2d52;
}

.tab-btn:focus {
  outline: 3px solid #0f2d52;
  outline-offset: 2px;
  z-index: 2;
  position: relative;
}

.tab-btn[aria-selected="true"] {
  background: #fff;
  color: #0f2d52;
  border-color: #bbb;
  border-bottom-color: #fff;
  z-index: 1;
  position: relative;
}

/* Tab content panel */
.tab-content {
  background: white;
  border: 1px solid #bbb;
  border-radius: 0 0 12px 12px;
  padding: 35px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  margin-bottom: 30px;
}

.tab-panel {
  display: none;
}

.tab-panel.active {
  display: block;
}

.tab-panel h3 {
  color: #0f2d52;
  font-size: 1.4em;
  margin: 0 0 15px 0;
  padding-bottom: 6px;
  border-bottom: 3px solid #dbaa00;
  display: inline-block;
}

.tab-panel p {
  color: #555;
  font-size: 1.05em;
  margin-bottom: 15px;
}

.tab-panel ul {
  margin: 0.5rem 0 0 1.5rem;
  padding: 0;
}

.tab-panel li {
  margin-bottom: 12px;
  font-size: 1.05em;
  line-height: 1.6;
  color: #555;
}

.criteria-label {
  font-weight: 700;
  color: #0f2d52;
}

.deadline-box {
  background: #fff3f3;
  border-left: 5px solid #c62828;
  border-radius: 0 6px 6px 0;
  padding: 15px 20px;
  font-size: 1.05em;
  margin-bottom: 20px;
  color: #c62828;
}

.no-self {
  font-size: 1em;
  color: #555;
  margin-bottom: 15px;
}

/* CTA button — matches site style */
.cta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  background: #dbaa00;
  color: #0f2d52 !important;
  padding: 14px 28px;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
  font-size: 1.05em;
  border: 2px solid #dbaa00;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.cta-button:hover {
  background: #0f2d52;
  color: #dbaa00 !important;
  border-color: #0f2d52;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.cta-button:focus {
  outline: 3px solid #0f2d52;
  outline-offset: 2px;
}

.note-text {
  font-size: 0.9em;
  color: #888;
  margin-top: 10px;
}

/* Mobile */
@media (max-width: 768px) {
  .award-welcome {
    padding: 25px;
  }

  .award-welcome h1 {
    font-size: 1.8em;
  }

  .award-section,
  .tab-content {
    padding: 20px;
  }

  .tab-row {
    grid-template-columns: 1fr;
    gap: 4px;
  }

  .tab-btn {
    border: 1px solid #ccc;
    border-radius: 6px;
  }

  .tab-btn[aria-selected="true"] {
    border-bottom-color: #bbb;
  }

  .tab-content {
    border-radius: 6px;
    margin-top: 4px;
  }

  .recipient-header {
    flex-direction: column;
  }

  .year-select {
    min-width: 100%;
    box-sizing: border-box;
  }

  .cta-button {
    width: 100%;
    text-align: center;
    box-sizing: border-box;
  }
}
</style>
<div class="award-container">
	<h2 class="sr-only">Community Partner Impact Award</h2>

	<div class="award-welcome">
		<h1>Community Partner Impact Award</h1>

		<p>Recognizing an inspiring and thoughtful community partner who has collaborated with UC Merced to bridge campus and community in addressing community-identified challenges.</p>
	</div>
	<!-- Recipient section -->

	<div aria-label="Award recipient" class="award-section">
		<h2>Award Recipient</h2>

		<div class="recipient-header">
			<div>
				<p class="recipient-name" id="rec-name">MCSD STEAM Center!</p>

				<p class="recipient-subtitle" id="rec-subtitle">Community Partner Impact Award</p>
			</div>

			<div><label class="year-label" for="year-select">View by year</label> <select class="year-select" id="year-select" onchange="showRecipient(this.value)"><option value="2026">2026 &mdash; MCSD STEAM Center</option><option value="2025">2025 &mdash; Merced County Library</option> </select></div>
		</div>

		<div aria-atomic="true" aria-live="polite" class="recipient-body" id="rec-body">
			<div class="placeholder-box" role="note">2026 recipient information to be added.</div>
		</div>
	</div>
	<!-- Tabbed sections -->

	<div aria-label="Award information sections" class="tab-row" role="tablist"><button aria-controls="tab-about" aria-selected="true" class="tab-btn" id="tab-about-btn" onclick="showTab('about')" onkeydown="handleTabKey(event, 'about')" role="tab">About the Award</button><button aria-controls="tab-criteria" aria-selected="false" class="tab-btn" id="tab-criteria-btn" onclick="showTab('criteria')" onkeydown="handleTabKey(event, 'criteria')" role="tab" tabindex="-1">Selection Criteria</button><button aria-controls="tab-nominate" aria-selected="false" class="tab-btn" id="tab-nominate-btn" onclick="showTab('nominate')" onkeydown="handleTabKey(event, 'nominate')" role="tab" tabindex="-1">Nomination Info</button></div>

	<div class="tab-content">
		<div aria-labelledby="tab-about-btn" class="tab-panel active" id="tab-about" role="tabpanel" tabindex="0">
			<h3>About the Award</h3>

			<p>The <strong>Community Partner Impact Award</strong> recognizes an inspiring and thoughtful community partner who has collaborated with UC Merced during the past year to bridge campus and community in addressing community-identified challenges. Through dedicated leadership, meaningful action has been taken in an empathetic, resourceful, and reciprocal manner to create positive and lasting change.</p>

			<ul aria-label="Award focus areas">
				<li>Mutual benefit between UC Merced and the community</li>
				<li>Innovation in addressing community challenges</li>
				<li>Student engagement and experiential learning</li>
				<li>Lasting impact for underserved populations in Merced County</li>
			</ul>
		</div>

		<div aria-labelledby="tab-criteria-btn" class="tab-panel" hidden="" id="tab-criteria" role="tabpanel" tabindex="0">
			<h3>Selection Criteria</h3>

			<ul aria-label="Selection criteria list">
				<li><span class="criteria-label">Community Impact:</span> The partnership has produced meaningful and lasting positive change for underserved populations in Merced County.</li>
				<li><span class="criteria-label">Innovation:</span> The partnership demonstrates creative or innovative approaches to solving community-identified challenges.</li>
				<li><span class="criteria-label">Student Success:</span> The partnership supports student development through experiential learning and engagement.</li>
			</ul>
		</div>

		<div aria-labelledby="tab-nominate-btn" class="tab-panel" hidden="" id="tab-nominate" role="tabpanel" tabindex="0">
			<h3>Nomination Information</h3>

			<p>Students, faculty, staff, and members of the UC Merced community are encouraged to submit nominations.</p>

			<p class="no-self"><strong>Self-nominations are not permitted.</strong></p>

			<div class="deadline-box" role="note"><strong>Nomination Deadline:</strong> Sunday, March 1, 2026 at 11:59 PM</div>
			<a aria-label="Submit a nomination (opens in new tab)" class="cta-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_b9FtCDXaz3y4Q1E" rel="noopener noreferrer" target="_blank">Submit a Nomination </a>

			<p class="note-text">Please ensure all nomination information is complete before submitting.</p>
		</div>
	</div>
</div>
<script>
var tabIds = ['about', 'criteria', 'nominate'];

var recipients = {
  "2026": {
    name: "MCSD STEAM Center",
    subtitle: "2026 Community Partner Impact Award",
    body: '<img class="recipient-img" src="/sites/g/files/ufvvjh561/f/images/impactaward2026.jpg" alt="Merced County Library award recipients at the 2025 Community Partner Impact Award ceremony" />'
  },
  "2025": {
    name: "Merced County Library",
    subtitle: "2025 Community Partner Impact Award",
    body: '<p>The Merced County Library was recognized for its outstanding partnership with UC Merced and its commitment to expanding access to educational resources, supporting student engagement, and strengthening the Merced community through innovative and inclusive programming.</p><img class="recipient-img" src="/sites/g/files/ufvvjh561/f/images/impactaward2025.jpeg" alt="Merced County Library award recipients at the 2025 Community Partner Impact Award ceremony" />'
  }
};

function showRecipient(year) {
  var r = recipients[year];
  document.getElementById("rec-name").textContent = r.name;
  document.getElementById("rec-subtitle").textContent = r.subtitle;
  document.getElementById("rec-body").innerHTML = r.body;
}

function showTab(id) {
  tabIds.forEach(function(t) {
    var btn = document.getElementById('tab-' + t + '-btn');
    var panel = document.getElementById('tab-' + t);
    var isActive = t === id;
    btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
    btn.setAttribute('tabindex', isActive ? '0' : '-1');
    panel.classList.toggle('active', isActive);
    if (isActive) {
      panel.removeAttribute('hidden');
    } else {
      panel.setAttribute('hidden', '');
    }
  });
}

function handleTabKey(event, currentId) {
  var idx = tabIds.indexOf(currentId);
  var nextIdx = null;
  if (event.key === 'ArrowRight') nextIdx = (idx + 1) % tabIds.length;
  else if (event.key === 'ArrowLeft') nextIdx = (idx - 1 + tabIds.length) % tabIds.length;
  else if (event.key === 'Home') nextIdx = 0;
  else if (event.key === 'End') nextIdx = tabIds.length - 1;
  if (nextIdx !== null) {
    event.preventDefault();
    var nextId = tabIds[nextIdx];
    showTab(nextId);
    document.getElementById('tab-' + nextId + '-btn').focus();
  }
}
showRecipient("2026");
</script>