<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.training-page {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0 auto;
}

.training-hero {
    background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%);
    color: white;
    padding: 32px 40px;
    border-radius: 12px;
    margin-bottom: 25px;
    text-align: center;
    box-sizing: border-box;
}
.training-hero h1 {
    margin: 0 0 8px 0;
    font-size: 2em;
    color: white !important;
}
.training-hero p {
    margin: 0;
    opacity: 0.95;
    font-size: 1.05em;
}

.training-note {
    background: #f8f9fa;
    border-left: 4px solid #dbaa00;
    border-radius: 8px;
    padding: 22px 28px;
    margin: 0 0 35px 0;
    font-size: 0.98em;
    color: #444;
    box-sizing: border-box;
}
.training-note p {
    margin: 0 0 12px 0;
}
.training-note p:last-child {
    margin-bottom: 0;
}
.training-note a {
    color: #0f2d52;
    font-weight: 600;
}

.training-section-heading {
    color: #0f2d52;
    font-size: 1.4em;
    margin: 0 0 6px 0;
    text-align: center;
}
.training-section-sub {
    text-align: center;
    color: #666;
    margin: 0 0 22px 0;
    font-size: 0.95em;
}

/* Tab bar */
.training-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-bottom: 24px;
}
.training-tab {
    font-family: inherit;
    font-size: 0.92em;
    font-weight: 600;
    color: #444;
    background: #f0f0f0;
    border: 2px solid transparent;
    border-radius: 8px;
    padding: 12px 18px;
    cursor: pointer;
    transition: all 0.2s ease;
}
.training-tab:hover:not(.active) {
    background: #e4e4e4;
}
.training-tab.active {
    background: var(--accent, #0f2d52);
    color: #fff;
    border-color: var(--accent, #0f2d52);
}

/* Panel — fixed height, content overlaid so size never changes */
.training-panel {
    position: relative;
    height: 220px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    border-top: 6px solid #dbaa00;
    overflow: hidden;
    margin-bottom: 25px;
    transition: border-color 0.2s ease;
}
.training-panel-content {
    position: absolute;
    inset: 0;
    padding: 28px 36px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow-y: auto;
    box-sizing: border-box;
}
.training-panel-content[hidden] {
    display: none;
}
.training-panel-content h3 {
    margin: 0 0 8px 0;
    color: #0f2d52;
    font-size: 1.3em;
}
.training-panel-content .panel-blurb {
    margin: 0 0 12px 0;
    color: #555;
}
.training-panel-content .panel-duration {
    display: inline-block;
    align-self: flex-start;
    background: #f0f4f9;
    color: #0f2d52;
    font-size: 0.82em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    padding: 5px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
}
.training-panel-content .panel-workshops {
    margin: 0;
    color: #555;
}

.training-footnote {
    text-align: center;
    color: #444;
    font-size: 1em;
    margin: 10px 0 0 0;
}
.training-footnote strong {
    color: #0f2d52;
}

@media (max-width: 620px) {
    .training-page {
        margin-right: 20px;
    }
    .training-panel {
        height: 260px;
    }
}
</style>
<div class="training-page">
	<div class="training-hero">
		<h1>Leadership Training Request</h1>

		<p>Our office offers leadership training workshops for campus departments, clubs, organizations, and Greek life. Choose a session below, or work with us to create a custom workshop tailored to your group.</p>
	</div>

	<div class="training-note">
		<p><strong>Requests must be submitted at least two weeks in advance</strong> so our team can prepare the best workshop possible &mdash; requests with less notice will be declined. For time-sensitive needs or accommodations, email <a href="mailto:sbarrera7@ucmerced.edu?subject=Leadership%20Training%20Inquiry">sbarrera7@ucmerced.edu</a>.</p>

		<p>This is a collaborative process: after you submit your request, we&#39;ll reach out to schedule an intake meeting to discuss goals, strategies, and workshop ideas. For additional questions, email <a href="mailto:lead@ucmerced.edu?subject=Leadership%20Training%20Inquiry">lead@ucmerced.edu</a>.</p>
	</div>

	<h2 class="training-section-heading">Choose a Training</h2>

	<p class="training-section-sub">Select a category to see the workshops included.</p>

	<div aria-label="Training categories" class="training-tabs" role="tablist"><button aria-controls="panel-intro" aria-selected="true" class="training-tab active" data-target="intro" id="tab-intro" role="tab" style="--accent:#003366;" tabindex="0">Intro to Leadership</button><button aria-controls="panel-college" aria-selected="false" class="training-tab" data-target="college" id="tab-college" role="tab" style="--accent:#005b4f;" tabindex="-1">College 101</button><button aria-controls="panel-core" aria-selected="false" class="training-tab" data-target="core" id="tab-core" role="tab" style="--accent:#b8860b;" tabindex="-1">Souza Core Skills</button><button aria-controls="panel-team" aria-selected="false" class="training-tab" data-target="team" id="tab-team" role="tab" style="--accent:#7a003c;" tabindex="-1">Team Building</button><button aria-controls="panel-bobcat" aria-selected="false" class="training-tab" data-target="bobcat" id="tab-bobcat" role="tab" style="--accent:#cc5500;" tabindex="-1">Building a Bobcat Leader</button><button aria-controls="panel-custom" aria-selected="false" class="training-tab" data-target="custom" id="tab-custom" role="tab" style="--accent:#333333;" tabindex="-1">Create Your Own</button></div>

	<div class="training-panel">
		<div aria-labelledby="tab-intro" class="training-panel-content" id="panel-intro" role="tabpanel">
			<h3>Intro to Leadership</h3>

			<p class="panel-blurb">Foundational leadership theory and identity exploration.</p>
			<span class="panel-duration">1 hr per workshop</span>

			<p class="panel-workshops">Workshops include: Intro to Leadership, Leadership Best Practices, Finding Your Style, Student Leadership, Values &amp; Ethics, and Identity in Leadership.</p>
		</div>

		<div aria-labelledby="tab-college" class="training-panel-content" hidden="" id="panel-college" role="tabpanel">
			<h3>College 101</h3>

			<p class="panel-blurb">Essential academic and personal success skills.</p>
			<span class="panel-duration">1 hr per workshop</span>

			<p class="panel-workshops">Workshops include: Goal Setting, Time Management, Study Strategies, Email Etiquette, Public Speaking, and Interview Skills.</p>
		</div>

		<div aria-labelledby="tab-core" class="training-panel-content" hidden="" id="panel-core" role="tabpanel">
			<h3>Souza Core Skills</h3>

			<p class="panel-blurb">Development of the five core leadership competencies.</p>
			<span class="panel-duration">45 min per workshop</span>

			<p class="panel-workshops">Workshops include: Self-Awareness, Confidence, Cultural Fluency, Communication, and Empathy.</p>
		</div>

		<div aria-labelledby="tab-team" class="training-panel-content" hidden="" id="panel-team" role="tabpanel">
			<h3>Team Building</h3>

			<p class="panel-blurb">Interactive and collaborative community-building sessions.</p>
			<span class="panel-duration">2&ndash;4 hrs per session</span>

			<p class="panel-workshops">Workshops include: Identity Maps, Acid River, Silent Opera, Pitch Battles, and Adventure Race.</p>
		</div>

		<div aria-labelledby="tab-bobcat" class="training-panel-content" hidden="" id="panel-bobcat" role="tabpanel">
			<h3>Building a Bobcat Leader</h3>

			<p class="panel-blurb">Specialized training for RCOs and Greek life.</p>
			<span class="panel-duration">30&ndash;120 min per workshop</span>

			<p class="panel-workshops">Workshops include: Tabling Tips, Outreach Superstar, Event Planning, Conflict Resolution, and Professional Leadership.</p>
		</div>

		<div aria-labelledby="tab-custom" class="training-panel-content" hidden="" id="panel-custom" role="tabpanel">
			<h3>Create Your Own</h3>

			<p class="panel-blurb">A fully customized workshop designed specifically for your group.</p>

			<p class="panel-workshops">Work with our Leadership Coaches to design a training tailored to your group&rsquo;s specific goals and needs.</p>
		</div>
	</div>

	<p class="training-footnote"><strong>Found your fit?</strong> Fill out the request form below and we&#39;ll be in touch to schedule an intake meeting.</p>
</div>
<script>
(function () {
  var tabs = document.querySelectorAll('.training-tab');
  var panel = document.querySelector('.training-panel');

  function selectTab(tab) {
    tabs.forEach(function (t) {
      var isActive = t === tab;
      t.classList.toggle('active', isActive);
      t.setAttribute('aria-selected', isActive ? 'true' : 'false');
      t.tabIndex = isActive ? 0 : -1;
    });
    document.querySelectorAll('.training-panel-content').forEach(function (p) {
      p.hidden = p.id !== 'panel-' + tab.dataset.target;
    });
    panel.style.borderTopColor = getComputedStyle(tab).getPropertyValue('--accent') || '#dbaa00';
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { selectTab(tab); });
    tab.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        e.preventDefault();
        var next = e.key === 'ArrowRight' ? (i + 1) % tabs.length : (i - 1 + tabs.length) % tabs.length;
        tabs[next].focus();
        selectTab(tabs[next]);
      }
    });
  });
})();
</script>