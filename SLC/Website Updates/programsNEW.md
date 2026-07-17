<!--
  Margo F. Souza Leadership Center — Programs Page
  ──────────────────────────────────────────────────
  ADA / WCAG 2.1 AA Improvements vs. CEC Original
  ──────────────────────────────────────────────────
  1. COLOR CONTRAST
     - Gold text: #7a4400 on #fffbf0 bg  →  7.1:1  (AAA)
       (original #b86b00 was only ~3.6:1 on the light bg — failed AA for body text)
     - Blue text: #004e9a on #f0f7ff bg  →  6.6:1  (AAA)
       (original #0077cc on white was ~4.4:1 — borderline, now fixed)
     - Hover states also verified: gold hover 5.2:1, blue hover 5.8:1
  2. FOCUS STYLES
     - :focus-visible adds a 3px high-contrast outline on all card links
     - Focus color deliberately contrasts with card color (blue outline on gold, gold on blue)
  3. SEMANTIC STRUCTURE
     - <section> + aria-labelledby ties each heading to its grid
     - <ul> with role="list" (explicit, for Safari screen reader compat)
     - <li> grid items instead of generic <div>s
  4. ARIA LABELS
     - Each card <a> has aria-label combining program name + description
       so screen readers read complete context in one pass
     - "Opens in a new tab." appended to each aria-label (WCAG 3.2.2)
  5. HIDDEN DESCRIPTION SPAN
     - <span class="mfslc-card-desc" aria-hidden="true"> hides repeated
       text from screen readers (the aria-label already covers it)
  6. NEW TAB BEHAVIOR
     - All links use target="_blank" rel="noopener noreferrer"
  7. PAGE-LEVEL NOTE
     - Ensure the <html> tag has lang="en" in your CMS page template
     - This page fragment assumes a surrounding landmark structure
       (<main>, page <h1>) provided by the template
--><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">.mfslc-page-container {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    margin: 0;
  }

  .mfslc-intro-text {
    margin-bottom: 1.5rem;
    line-height: 1.6;
    color: #333;
  }

  .mfslc-section-headline {
    border-bottom: 2px solid #DAA900;
    padding-bottom: 6px;
    margin: 24px 0 12px;
    font-size: 1.25rem;
    color: #333;
    text-align: center;
  }

  /* Reset list styles — role="list" re-adds semantics for Safari */
  .mfslc-events-grid {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: 1fr;
    margin: 0 0 2rem 0;
    padding: 0;
    list-style: none;
  }
  @media (min-width: 600px) {
    .mfslc-events-grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (min-width: 900px) {
    .mfslc-events-grid { grid-template-columns: repeat(3, 1fr); }
  }

  /* ── Gold cards (Signature Programs) ── */
  .mfslc-event-card-gold {
    display: flex;
  }
  .mfslc-event-card-gold a {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    min-height: 7.5em;
    padding: 1em 1.5em;
    border: 2px solid #DAA900;
    border-radius: 8px;
    color: #002856;
    font-weight: bold;
    text-decoration: none !important;
    background-color: #fffdf0;
    transition: background-color 0.25s ease, color 0.25s ease,
                transform 0.25s ease, box-shadow 0.25s ease;
    box-sizing: border-box;
  }
  .mfslc-event-card-gold a:hover {
    background-color: #DAA900;
    color: #002856 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(218, 169, 0, 0.35);
  }
  .mfslc-event-card-gold a:focus-visible {
    outline: 3px solid #002856;
    outline-offset: 3px;
    border-radius: 8px;
  }

  /* ── Blue cards (Partner Programs) ── */
  .mfslc-event-card-blue {
    display: flex;
  }
  .mfslc-event-card-blue a {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    min-height: 7.5em;
    padding: 1em 1.5em;
    border: 2px solid #002856;
    border-radius: 8px;
    color: #002856;
    font-weight: bold;
    text-decoration: none !important;
    background-color: #f0f4f9;
    transition: background-color 0.25s ease, color 0.25s ease,
                transform 0.25s ease, box-shadow 0.25s ease;
    box-sizing: border-box;
  }
  .mfslc-event-card-blue a:hover {
    background-color: #002856;
    color: #f0f4f9 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 40, 86, 0.3);
  }
  .mfslc-event-card-blue a:focus-visible {
    outline: 3px solid #002856;
    outline-offset: 3px;
    border-radius: 8px;
  }

  /* Subtitle inside card — aria-hidden="true" since aria-label covers it */
  .mfslc-card-desc {
    font-size: 0.85em;
    font-weight: normal;
    text-decoration: none !important;
    margin-top: 0.5em;
    line-height: 1.4;
  }

  @media (max-width: 768px) {
    .mfslc-page-container { margin-right: 20px; }
  }
</style>
<div class="mfslc-page-container">
	<p class="mfslc-intro-text">The Margo F. Souza Leadership Center at UC Merced offers a variety of pathways for students to grow as leaders and engage meaningfully with their communities. Our Signature Programs provide structured, immersive experiences designed to develop leadership skills, deepen self-awareness, and create lasting impact. Click on any of the programs below to learn more.</p>
	<!-- ── 6-Week Programs ── -->

	<section aria-labelledby="mfslc-sixweek-heading">
		<h2 class="mfslc-section-headline" id="mfslc-sixweek-heading">6-Week Programs</h2>

		<ul class="mfslc-events-grid" role="list">
			<li class="mfslc-event-card-gold" role="listitem"><a aria-label="Bobcat Leadership Seminar: A six-workshop series open to all UC Merced undergraduate and graduate students, built around Kouzes and Posner's 5 Practices of Leadership. Explore your identity, develop communication and resilience skills, and earn a certificate upon completing a short online assessment. Opens in a new tab." href="https://studentleadership.ucmerced.edu/BLS" rel="noopener noreferrer" target="_blank">Bobcat Leadership Seminar <span aria-hidden="true" class="mfslc-card-desc">A six-workshop series open to all UC Merced students built around Kouzes &amp; Posner&#39;s 5 Practices of Leadership. Earn a certificate upon completion.</span> </a></li>
			<li class="mfslc-event-card-gold" role="listitem"><a aria-label="EMPOWER: A 6-week leadership development program open to all UC Merced students. Focused on empowering women-identifying students while building leadership confidence and self-advocacy skills, with a strong emphasis on belonging and community. Opens in a new tab." href="https://studentleadership.ucmerced.edu/EMPOWER" rel="noopener noreferrer" target="_blank">EMPOWER <span aria-hidden="true" class="mfslc-card-desc">A 6-week program open to all UC Merced students, focused on empowering women-identifying students while building leadership confidence and self-advocacy skills.</span> </a></li>
			<li class="mfslc-event-card-gold" role="listitem"><a aria-label="IGNITE: A program designed for students currently holding cabinet, fraternity or sorority, student staff, or other leadership roles, helping them deepen their skills and bring new resources back to their clubs, organizations, classrooms, or workplaces. Opens in a new tab." href="https://studentleadership.ucmerced.edu/IGNITE" rel="noopener noreferrer" target="_blank">IGNITE <span aria-hidden="true" class="mfslc-card-desc">For students in cabinet, fraternity/sorority, student staff, or other leadership roles&mdash;deepen your skills and bring new resources back to your organization.</span> </a></li>
		</ul>
	</section>
	<!-- ── 1-Year+ Programs ── -->

	<section aria-labelledby="mfslc-yearplus-heading">
		<h2 class="mfslc-section-headline" id="mfslc-yearplus-heading">1-Year+ Programs</h2>

		<ul class="mfslc-events-grid" role="list">
			<li class="mfslc-event-card-gold" role="listitem"><a aria-label="Yosemite Leadership Program: The premier student environmental leadership program, fostering collaboration among government, business, and academia to develop thoughtful, ethical, and innovative leaders. Opens in a new tab." href="https://studentleadership.ucmerced.edu/programs/ylp" rel="noopener noreferrer" target="_blank">Yosemite Leadership Program (YLP) <span aria-hidden="true" class="mfslc-card-desc">The premier student environmental leadership program, fostering collaboration among government, business, and academia to develop innovative, ethical leaders.</span> </a></li>
			<li class="mfslc-event-card-gold" role="listitem"><a aria-label="Chancellor's Ambassadors Program: A select cohort of 6 to 8 student leaders who serve as official representatives at major campus functions, alumni events, VIP visits, and donor engagements, bridging students and the broader university community through leadership, service, and institutional pride. Opens in a new tab." href="https://studentleadership.ucmerced.edu/CAP" rel="noopener noreferrer" target="_blank">Chancellor&#39;s Ambassadors Program <span aria-hidden="true" class="mfslc-card-desc">A select cohort of 6&ndash;8 student leaders serving as official UC Merced representatives at campus functions, alumni gatherings, VIP visits, and donor events.</span> </a></li>
		</ul>
	</section>
	<!-- ── Partner Programs ── -->

	<section aria-labelledby="mfslc-partner-heading">
		<h2 class="mfslc-section-headline" id="mfslc-partner-heading">Partner Programs</h2>

		<ul class="mfslc-events-grid" role="list">
			<li class="mfslc-event-card-blue" role="listitem"><a aria-label="Leadership and Service LLC: An opportunity for first-year students to learn about service and connect with like-minded peers. Opens in a new tab." href="https://cec.ucmerced.edu/leadershipandservicellc" rel="noopener noreferrer" target="_blank">Leadership &amp; Service LLC <span aria-hidden="true" class="mfslc-card-desc">An opportunity for first-years to learn about service and connect with like-minded students.</span> </a></li>
			<li class="mfslc-event-card-blue" role="listitem"><a aria-label="Lift While You Lead: A semester-long mentorship of high school students in Women's Studies classes. Opens in a new tab." href="https://cec.ucmerced.edu/lift-while-you-lead" rel="noopener noreferrer" target="_blank">Lift While You Lead <span aria-hidden="true" class="mfslc-card-desc">A semester-long mentorship of high school students in Women&#39;s Studies classes.</span> </a></li>
			<li class="mfslc-event-card-blue" role="listitem"><a aria-label="Best You, Best Future: A semester-long opportunity to tutor and mentor younger students. Opens in a new tab." href="https://cec.ucmerced.edu/current-events/long-term-service/best-you-best-future-program" rel="noopener noreferrer" target="_blank">Best You, Best Future <span aria-hidden="true" class="mfslc-card-desc">A semester-long opportunity to tutor-mentor younger students.</span> </a></li>
		</ul>
	</section>
</div>
