<!--
  LEGENDARY LEAGUE – FACULTY PAGE COMPONENT
  ==========================================
  Paste this entire block into a Drupal custom block (Full HTML format).
  No global CSS selectors — everything is scoped to .ll-* classes.
  No <html>, <head>, or <body> tags needed.

  Schools:
    data-school="ssha"  → SSHA
    data-school="s2"    → SOE (School of Engineering)
    data-school="s3"    → SNS (School of Natural Sciences)

  GRAD tag: add data-grad="true" and a second <span class="ll-school-tag ll-grad">GRAD</span>
  for faculty available to graduate students.

  TO ADD A FACULTY MEMBER:
    Copy any .ll-card div, update all data-* attributes and the
    img src (or swap back to initials text inside .ll-card-photo).
    Set data-school to: "ssha" | "s2" | "s3"
-->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&amp;family=Source+Sans+3:wght@400;500;600&amp;display=swap" rel="stylesheet" />
<style type="text/css">/* ============================================================
     LEGENDARY LEAGUE – FACULTY PAGE
     All selectors scoped to .ll-* — safe for Drupal embedding.
     CSS variables live on .ll-page so they don't pollute :root.
  ============================================================ */

  .ll-page {
    --ll-navy:        #002856;
    --ll-navy-mid:    #1B4F8A;
    --ll-navy-light:  #D6E4F7;
    --ll-gold:        #F5C518;
    --ll-gold-dark:   #C49A00;
    --ll-gold-light:  #FFF8D6;
    --ll-ssha-bg:     #F5C518;
    --ll-ssha-text:   #5A3E00;
    --ll-s2-bg:       #1B8A6B;
    --ll-s2-text:     #ffffff;
    --ll-s3-bg:       #8A1B4F;
    --ll-s3-text:     #ffffff;
    --ll-grad-bg:     #002856;
    --ll-grad-text:   #F5C518;

    font-family: 'Source Sans 3', sans-serif;
    background: #f0f3f8;
    color: #1a2535;
    box-sizing: border-box;
  }

  .ll-page *,
  .ll-page *::before,
  .ll-page *::after {
    box-sizing: inherit;
  }

  /* ---------- FILTER BAR ---------- */
  .ll-filters {
    background: #ffffff;
    border-bottom: 1px solid #dce4ef;
    padding: 14px 0;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .ll-filters-label {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 12px;
    font-weight: 600;
    color: #6b7a99;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .ll-filter-btn {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 12px;
    font-weight: 600;
    padding: 5px 16px;
    border-radius: 999px;
    border: 1.5px solid #dce4ef;
    background: #f4f6fa;
    color: #4a5568;
    cursor: pointer;
    transition: background 0.18s, color 0.18s, border-color 0.18s;
    line-height: 1.4;
  }

  .ll-filter-btn:hover,
  .ll-filter-btn.ll-active-all {
    background: var(--ll-navy);
    color: #ffffff;
    border-color: var(--ll-navy);
  }

  .ll-filter-btn.ll-active-ssha { background: var(--ll-ssha-bg); color: var(--ll-ssha-text); border-color: var(--ll-gold-dark); }
  .ll-filter-btn.ll-active-s2   { background: var(--ll-s2-bg);   color: var(--ll-s2-text);   border-color: var(--ll-s2-bg); }
  .ll-filter-btn.ll-active-s3   { background: var(--ll-s3-bg);   color: var(--ll-s3-text);   border-color: var(--ll-s3-bg); }
  .ll-filter-btn.ll-active-grad { background: var(--ll-grad-bg); color: var(--ll-grad-text); border-color: var(--ll-grad-bg); }

  /* ---------- CARD GRID ---------- */
  .ll-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
    gap: 22px;
    padding: 32px 40px;
  }

  /* ---------- FACULTY CARD ---------- */
  .ll-card {
    background: #ffffff;
    border-radius: 12px;
    border: 1px solid #dce4ef;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    display: flex;
    flex-direction: column;
  }

  .ll-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(0, 40, 86, 0.14);
  }

  .ll-card-photo {
    width: 100%;
    aspect-ratio: 1 / 1;
    background: var(--ll-navy-light);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    color: var(--ll-navy);
    border-bottom: 4px solid var(--ll-gold);
    overflow: hidden;
    position: relative;
  }

  .ll-card-photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
  }

  .ll-card-body {
    padding: 16px 16px 14px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .ll-card-name {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--ll-navy);
    line-height: 1.3;
    margin: 0;
  }

  .ll-card-title {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 12px;
    color: #5a6a80;
    line-height: 1.45;
    margin: 2px 0 0;
  }

  .ll-card-pronouns {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 11px;
    color: #8a97aa;
    font-style: italic;
    margin: 0;
  }

  .ll-school-tag {
    display: inline-block;
    margin-top: 10px;
    margin-right: 4px;
    padding: 4px 11px;
    border-radius: 999px;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.03em;
    width: fit-content;
  }

  .ll-school-tag.ll-ssha { background: var(--ll-ssha-bg); color: var(--ll-ssha-text); }
  .ll-school-tag.ll-s2   { background: var(--ll-s2-bg);   color: var(--ll-s2-text); }
  .ll-school-tag.ll-s3   { background: var(--ll-s3-bg);   color: var(--ll-s3-text); }
  .ll-school-tag.ll-grad { background: var(--ll-grad-bg); color: var(--ll-grad-text); }

  /* ---------- OVERLAY ---------- */
  .ll-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0, 20, 50, 0.65);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }

  .ll-overlay.ll-open {
    display: flex;
  }

  /* ---------- MODAL ---------- */
  .ll-modal {
    background: #ffffff;
    border-radius: 14px;
    width: 100%;
    max-width: 580px;
    max-height: 88vh;
    overflow-y: auto;
    border: 1px solid #dce4ef;
    position: relative;
  }

  .ll-modal::-webkit-scrollbar          { width: 6px; }
  .ll-modal::-webkit-scrollbar-track    { background: transparent; }
  .ll-modal::-webkit-scrollbar-thumb    { background: #c8d4e8; border-radius: 999px; }

  .ll-modal-header {
    background: var(--ll-navy);
    border-bottom: 4px solid var(--ll-gold);
    padding: 24px 24px 20px;
    display: flex;
    gap: 18px;
    align-items: flex-start;
    position: sticky;
    top: 0;
    z-index: 10;
  }

  .ll-modal-avatar {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: var(--ll-navy-mid);
    border: 2.5px solid var(--ll-gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
    color: var(--ll-gold);
    flex-shrink: 0;
    overflow: hidden;
    position: relative;
  }

  .ll-modal-avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
  }

  .ll-modal-header-info {
    flex: 1;
    min-width: 0;
  }

  .ll-modal-name {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin: 0;
  }

  .ll-modal-subtitle {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 13px;
    color: #a8bdd4;
    margin: 3px 0 0;
  }

  .ll-modal-pronouns {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 12px;
    color: #7a9ec0;
    font-style: italic;
    margin: 2px 0 0;
  }

  .ll-modal-school-tag {
    display: inline-block;
    margin-top: 8px;
    margin-right: 4px;
    padding: 4px 12px;
    border-radius: 999px;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 11px;
    font-weight: 700;
  }

  .ll-modal-school-tag.ll-ssha { background: var(--ll-ssha-bg); color: var(--ll-ssha-text); }
  .ll-modal-school-tag.ll-s2   { background: var(--ll-s2-bg);   color: var(--ll-s2-text); }
  .ll-modal-school-tag.ll-s3   { background: var(--ll-s3-bg);   color: var(--ll-s3-text); }
  .ll-modal-school-tag.ll-grad { background: var(--ll-grad-bg); color: var(--ll-grad-text); }

  .ll-modal-close {
    background: rgba(255, 255, 255, 0.12);
    border: none;
    color: #ffffff;
    font-size: 18px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    padding: 0;
    line-height: 1;
    transition: background 0.15s;
  }

  .ll-modal-close:hover { background: rgba(255, 255, 255, 0.25); }

  .ll-modal-body {
    padding: 24px 24px 28px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .ll-section-label {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ll-gold-dark);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .ll-section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #edf1f7;
  }

  .ll-section-text {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 14px;
    color: #2d3a4a;
    line-height: 1.7;
    margin: 0;
  }

  .ll-advice-block {
    background: var(--ll-gold-light);
    border-left: 4px solid var(--ll-gold);
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
  }

  .ll-advice-text {
    font-family: 'Playfair Display', serif;
    font-size: 15px;
    font-style: italic;
    color: #3a2d00;
    line-height: 1.65;
    margin: 0;
  }

  /* ---------- RESPONSIVE ---------- */
  @media (max-width: 600px) {
    .ll-filters { padding: 12px 0px; }
    .ll-grid    { padding: 20px; gap: 16px; }
    .ll-modal   { max-height: 92vh; }
  }
</style>
<!-- ============================================================
     COMPONENT ROOT
============================================================ -->
<div class="ll-page"><!-- FILTER BAR -->
	<div class="ll-filters"><span class="ll-filters-label">Filter:</span><button class="ll-filter-btn ll-active-all" onclick="llFilter('all', this)">All</button><button class="ll-filter-btn" onclick="llFilter('ssha', this)">SSHA</button><button class="ll-filter-btn" onclick="llFilter('s2', this)">SOE</button><button class="ll-filter-btn" onclick="llFilter('s3', this)">SNS</button><button class="ll-filter-btn" onclick="llFilter('grad', this)">GRAD</button></div>
	<!-- ============================================================
       FACULTY GRID
  ============================================================ -->

	<div class="ll-grid" id="llGrid"><!-- CARD: SOE – Sarah Kurtz -->
		<div class="ll-card" data-advice="Think about the reputation you'd LIKE to have and then consistently behave so as to maintain that reputation." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Translating coursework into skills,Nonprofit or government careers,Career exploration or uncertainty,Research opportunities" data-fields="Engineering &amp; Manufacturing,Environmental &amp; Sustainability,Public Service &amp; Policy,Research &amp; Development" data-identity="Career Changer,Studied Abroad" data-name="Sarah Kurtz" data-pronouns="" data-reach="Office hours: Mondays 4-5 | By appointment: when my calendar has a hole | Department or program events | Email: skurtz@ucmerced.edu" data-school="s2" data-school-label="SOE" data-title="Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Sarah Kurtz" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/sarah_kurtz_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Sarah Kurtz</div>

				<div class="ll-card-title">Professor</div>

				<div class="ll-card-pronouns">&nbsp;</div>
				<span class="ll-school-tag ll-s2">SOE</span></div>
		</div>
		<!-- CARD: SOE  GRAD – Stefano Carpin -->

		<div class="ll-card" data-advice="Never be afraid of asking for advice." data-approach="Industry vs. academia,Research opportunities" data-fields="Education &amp; Student Affairs,Engineering &amp; Manufacturing,Data, Tech &amp; Analytics" data-grad="true" data-identity="First-Generation College Graduate,Worked While in School,Multilingual / Bilingual,International Scholar" data-name="Stefano Carpin" data-pronouns="" data-reach="Office hours" data-school="s2" data-school-label="SOE" data-title="Professor and Associate Dean for Research and Graduate Programs" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Stefano Carpin" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/stefano_carpin_headshot.jpg" style="object-position: center 20%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Stefano Carpin</div>

				<div class="ll-card-title">Professor and Associate Dean for Research and Graduate Programs</div>

				<div class="ll-card-pronouns">&nbsp;</div>
				<span class="ll-school-tag ll-s2">SOE</span> <span class="ll-school-tag ll-grad">GRAD</span></div>
		</div>
		<!-- CARD: SOE – Siddaiah Yarra -->

		<div class="ll-card" data-advice="Employers understand that as a student or recent graduate you may not yet have all the professional skills needed to excel in their company. They usually do not base their decision solely on that. What matters more to them is: Do you understand what the company does? Are you genuinely interested in their work? Are you willing to learn and grow so you can contribute to their team? Showing curiosity, motivation, and a willingness to learn often makes a stronger impression than already knowing everything." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Translating coursework into skills,Career exploration or uncertainty,Research opportunities" data-fields="Education &amp; Student Affairs,Engineering &amp; Manufacturing,Environmental &amp; Sustainability,Business &amp; Management,Research &amp; Development" data-identity="First-Generation College Graduate,Worked While in School,International Scholar" data-name="Siddaiah Yarra" data-pronouns="He/Him" data-reach="Office hours: Tuesdays &amp; Thursdays 2 pm - 3:30 pm | Email: syarra@ucmerced.edu" data-school="s2" data-school-label="SOE" data-title="Assistant Teaching Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Siddaiah Yarra" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/siddaiah_yarra_headshot.jpeg" style="object-position: center 20%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Siddaiah Yarra</div>

				<div class="ll-card-title">Assistant Teaching Professor</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-s2">SOE</span></div>
		</div>
		<!-- CARD: SOE – Florin Rusu -->

		<div class="ll-card" data-advice="" data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Career exploration or uncertainty,Research opportunities" data-fields="Data, Tech &amp; Analytics,Research &amp; Development" data-identity="Multilingual / Bilingual,International Scholar" data-name="Florin Rusu" data-pronouns="He/Him" data-reach="Office hours | By appointment | Email: frusu@ucmerced.edu" data-school="s2" data-school-label="SOE" data-title="Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Florin Rusu" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/florin_rusu_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Florin Rusu</div>

				<div class="ll-card-title">Professor</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-s2">SOE</span></div>
		</div>
		<!-- CARD: SNS  GRAD – Sayantani Ghosh -->

		<div class="ll-card" data-advice="Be brave enough to begin and patient enough to finish." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Career exploration or uncertainty,Research opportunities" data-fields="Education &amp; Student Affairs,Engineering &amp; Manufacturing,Research &amp; Development" data-grad="true" data-identity="Worked While in School,Multilingual / Bilingual,International Scholar,Studied Abroad" data-name="Sayantani Ghosh" data-pronouns="She/Her" data-reach="Email: sghosh@ucmerced.edu" data-school="s3" data-school-label="SNS" data-title="Professor and Associate Graduate Dean" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Sayantani Ghosh" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/sayantani_ghosh_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Sayantani Ghosh</div>

				<div class="ll-card-title">Professor and Associate Graduate Dean</div>

				<div class="ll-card-pronouns">She/Her</div>
				<span class="ll-school-tag ll-s3">SNS</span> <span class="ll-school-tag ll-grad">GRAD</span></div>
		</div>
		<!-- CARD: SSHA  GRAD – Lindsay Crawford -->

		<div class="ll-card" data-advice="They key to a well-balanced life is time management!" data-approach="Careers related to my major/field,Graduate school pathways,Translating coursework into skills" data-fields="Public Service &amp; Policy,Nonprofit / Community Organizations" data-grad="true" data-identity="First-Generation College Graduate" data-name="Lindsay Crawford" data-pronouns="She/Her" data-reach="Email: lcrawford5@ucmerced.edu" data-school="ssha" data-school-label="SSHA" data-title="Assistant Teaching Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Lindsay Crawford" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/lindsay_crawford_headshot.jpg" style="object-position: center 20%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Lindsay Crawford</div>

				<div class="ll-card-title">Assistant Teaching Professor</div>

				<div class="ll-card-pronouns">She/Her</div>
				<span class="ll-school-tag ll-ssha">SSHA</span> <span class="ll-school-tag ll-grad">GRAD</span></div>
		</div>
		<!-- CARD: SSHA – Daniel Thompson -->

		<div class="ll-card" data-advice="The skill of being a learner - practicing curiosity and finding joy in creative problem-solving - is fundamental to long-term success. Learn to love learning, and you will find yourself becoming adaptable and resilient to the inevitable challenges and setbacks life brings." data-approach="Careers related to my major/field,Graduate school pathways,Translating coursework into skills,Nonprofit or government careers" data-fields="Education &amp; Student Affairs,Public Service &amp; Policy,Nonprofit / Community Organizations" data-identity="Worked While in School,Multilingual / Bilingual,Non-Linear Path,Studied Abroad" data-name="Daniel Thompson" data-pronouns="He/Him" data-reach="Department or program events | I'm always happy to talk with students, whether about graduate school, career planning, or challenges with university life | Email: dthompson29@ucmerced.edu" data-school="ssha" data-school-label="SSHA" data-title="Associate Professor of Anthropology" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Daniel Thompson" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/daniel_thompson_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Daniel Thompson</div>

				<div class="ll-card-title">Associate Professor of Anthropology</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-ssha">SSHA</span></div>
		</div>
		<!-- CARD: SNS – Rudy M. Ortiz -->

		<div class="ll-card" data-advice="take advantage of every opportunity" data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Translating coursework into skills,Research opportunities" data-fields="Healthcare,Education &amp; Student Affairs,Research &amp; Development" data-identity="Worked While in School,Multilingual / Bilingual,Studied Abroad,Other, Training grant program director" data-name="Rudy M. Ortiz" data-pronouns="He/Him" data-reach="Office hours: W 11-12, SE1 244 | By appointment: schedule by email | Email: rortiz@ucmerced.edu" data-school="s3" data-school-label="SNS" data-title="Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Rudy M. Ortiz" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/rudy_ortiz_headshot.jpg" style="object-position: center 20%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Rudy M. Ortiz</div>

				<div class="ll-card-title">Professor</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-s3">SNS</span></div>
		</div>
		<!-- CARD: SSHA – Jason Lee -->

		<div class="ll-card" data-advice="Invest in yourself early. The skills, experiences, and relationships you build now will pay dividends throughout your career." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Career exploration or uncertainty" data-fields="Education &amp; Student Affairs,Business &amp; Management,Other:, Finance" data-identity="Career Changer" data-name="Jason Lee" data-pronouns="He/Him" data-reach="Office hours | By appointment | Department or program events" data-school="ssha" data-school-label="SSHA" data-title="Associate Teaching Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Jason Lee" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/jason_lee_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Jason Lee</div>

				<div class="ll-card-title">Associate Teaching Professor</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-ssha">SSHA</span></div>
		</div>
		<!-- CARD: SNS – Michael Scheibner -->

		<div class="ll-card" data-advice="Look beyond what things are and imagine what they could become. Explore the unknown, embrace challenges, and see failure as an opportunity to learn and grow." data-approach="Careers related to my major/field,Graduate school pathways,Internships or experiential learning,Research opportunities" data-fields="Education &amp; Student Affairs,Engineering &amp; Manufacturing,Data, Tech &amp; Analytics,Research &amp; Development,Other:, Quantum technologies, physics research, and national laboratory careers" data-identity="First-Generation College Graduate,Multilingual / Bilingual,Non-Linear Path,International Scholar" data-name="Michael Scheibner" data-pronouns="He/Him" data-reach="Office hours | By appointment | Department or program events | Email: mscheibner@ucmerced.edu" data-school="s3" data-school-label="SNS" data-title="Associate Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Michael Scheibner" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/michael_scheibner_headshot.jpg" style="object-position: center 30%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Michael Scheibner</div>

				<div class="ll-card-title">Associate Professor</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-s3">SNS</span></div>
		</div>
		<!-- CARD: SOE – Ricardo de Castro -->

		<div class="ll-card" data-advice="follow your passion" data-approach="Industry vs. academia" data-fields="Engineering &amp; Manufacturing" data-identity="Non-Linear Path,International Scholar" data-name="Ricardo de Castro" data-pronouns="" data-reach="Department or program events" data-school="s2" data-school-label="SOE" data-title="Assistant Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Ricardo de Castro" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/ricardo_decastro_headshot.jpg" style="object-position: center 25%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Ricardo de Castro</div>

				<div class="ll-card-title">Assistant Professor</div>

				<div class="ll-card-pronouns">&nbsp;</div>
				<span class="ll-school-tag ll-s2">SOE</span></div>
		</div>
		<!-- CARD: SSHA – Justin Hicks -->

		<div class="ll-card" data-advice="Plan. Implement. Reflect. Revise. Repeat." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Translating coursework into skills,Nonprofit or government careers,Career exploration or uncertainty,Research opportunities" data-fields="Data, Tech &amp; Analytics,Business &amp; Management,Nonprofit / Community Organizations,Research &amp; Development" data-identity="Community College Transfer,Worked While in School,Non-Linear Path" data-name="Justin Hicks" data-pronouns="He/Him" data-reach="Email: jhicks2@ucmerced.edu" data-school="ssha" data-school-label="SSHA" data-title="Associate Teaching Professor of Economics" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Justin Hicks" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/justin_hicks_headshot.jpg" style="object-position: 60% 15%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Justin Hicks</div>

				<div class="ll-card-title">Associate Teaching Professor of Economics</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-ssha">SSHA</span></div>
		</div>
		<!-- CARD: SNS – Dusty Ventura -->

		<div class="ll-card" data-advice="You are here to connect. Move toward what excites you." data-approach="Industry vs. academia,Internships or experiential learning,Career exploration or uncertainty,Research opportunities" data-fields="Healthcare,Education &amp; Student Affairs,Research &amp; Development" data-identity="First-Generation College Graduate,Community College Transfer,Worked While in School,Other, Raised Kids While in School" data-name="Dusty Ventura" data-pronouns="She/Her" data-reach="Office hours | Email: dventura4@ucmerced.edu" data-school="s3" data-school-label="SNS" data-title="Continuing Lecturer Chemistry and Biochemistry Department" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Dusty Ventura" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/dusty_ventura_headshot.jpg" style="object-position: 65% center;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Dusty Ventura</div>

				<div class="ll-card-title">Continuing Lecturer Chemistry and Biochemistry Department</div>

				<div class="ll-card-pronouns">She/Her</div>
				<span class="ll-school-tag ll-s3">SNS</span></div>
		</div>
		<!-- CARD: SNS – Noemi Petra -->

		<div class="ll-card" data-advice="Graduating into today’s world may feel like living in both the best of times and the most uncertain of times. Rapid technological change and global challenges can make the future seem unpredictable. Yet these same conditions create extraordinary opportunities for STEM graduates to contribute meaningfully to research, innovation, and progress. My advice is simple: stay focused, disciplined, and curious. Always strive to learn new things, and don’t settle for surface-level understanding. Dig deep—especially into the mathematics, principles, and methods that underpin your field. A strong foundation will remain valuable regardless of how technologies evolve. As generative AI tools become more common, one of the most valuable skills will be the ability to critically evaluate their outputs—to verify, validate, and understand the results they produce. Those who truly understand the fundamentals will be best positioned to use these tools responsibly and effectively. In times of rapid change, depth of knowledge, intellectual rigor, and a commitment to continuous learning will be your greatest advantages." data-approach="Careers related to my major/field,Graduate school pathways,Industry vs. academia,Internships or experiential learning,Research opportunities" data-fields="Engineering &amp; Manufacturing,Environmental &amp; Sustainability,Data, Tech &amp; Analytics,Research &amp; Development" data-identity="First-Generation College Graduate,Multilingual / Bilingual,International Scholar" data-name="Noemi Petra" data-pronouns="She/Her" data-reach="By appointment | Email: npetra@ucmerced.edu" data-school="s3" data-school-label="SNS" data-title="Professor" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Noemi Petra" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/petra_noemi_headshot.jpg" style="object-position: 75% 10%;" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Noemi Petra</div>

				<div class="ll-card-title">Professor</div>

				<div class="ll-card-pronouns">She/Her</div>
				<span class="ll-school-tag ll-s3">SNS</span></div>
		</div>
		<!-- CARD: SSHA – Yang Lor -->

		<div class="ll-card" data-advice="College is a time of exploration—discovering what you like and what you don’t. Both successes and setbacks are learning opportunities. You don’t need to have everything figured out while in college. Be open to new experiences and situations; they’re a great way to explore opportunities, resources, and careers." data-approach="Careers related to my major/field,Graduate school pathways,Career exploration or uncertainty,Research opportunities" data-fields="Healthcare,Education &amp; Student Affairs,Environmental &amp; Sustainability,Data, Tech &amp; Analytics,Public Service &amp; Policy,Business &amp; Management,Nonprofit / Community Organizations" data-identity="First-Generation College Graduate,Worked While in School,Multilingual / Bilingual" data-name="Yang Lor" data-pronouns="He/Him" data-reach="By appointment | During class check-ins | Email: ylor2@ucmerced.edu" data-school="ssha" data-school-label="SSHA" data-title="Associate Teaching Professor of Sociology" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Yang Lor" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/lor_yang_headshot.jpg" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Yang Lor</div>

				<div class="ll-card-title">Associate Teaching Professor of Sociology</div>

				<div class="ll-card-pronouns">He/Him</div>
				<span class="ll-school-tag ll-ssha">SSHA</span></div>
		</div>
		<!-- CARD: Brian O'Bruba -->

		<div class="ll-card" data-advice="You're a Bobcat - you were built for bold beginnings. As you step into the workforce, lead with curiosity, trust your preparation, and know that UC Merced students don't just follow paths… they create new ones." data-approach="Internships or experiential learning,Translating coursework into skills,Career exploration or uncertainty,Employer partnerships &amp; alumni networks" data-fields="Healthcare,Education &amp; Student Affairs,Engineering &amp; Manufacturing,Environmental &amp; Sustainability,Data, Tech &amp; Analytics,Public Service &amp; Policy,Business &amp; Management,Nonprofit / Community Organizations,Research &amp; Development" data-identity="Worked While in School" data-name="Brian O'Bruba" data-pronouns="" data-reach="Office hours | By appointment | Department or program events | Email: bobruba@ucmerced.edu | At student hosted events, too!" data-school="" data-school-label="" data-title="Associate Vice Chancellor - Student Affairs" onclick="llOpenModal(this)">
			<div class="ll-card-photo"><img alt="Brian O'Bruba" src="https://hire.ucmerced.edu/sites/g/files/ufvvjh1016/f/images/legendaryfaculty/brian_obruba_headshot.png" /></div>

			<div class="ll-card-body">
				<div class="ll-card-name">Brian O&#39;Bruba</div>

				<div class="ll-card-title">Associate Vice Chancellor - Student Affairs</div>

				<div class="ll-card-pronouns">&nbsp;</div>
			</div>
		</div>
	</div>
	<!-- /ll-grid --><!-- MODAL OVERLAY — single instance, populated by JS on card click -->

	<div class="ll-overlay" id="llOverlay" onclick="llCloseOnBackdrop(event)">
		<div class="ll-modal" id="llModal">
			<div class="ll-modal-header">
				<div class="ll-modal-avatar" id="llModalAvatar">&nbsp;</div>

				<div class="ll-modal-header-info">
					<div class="ll-modal-name" id="llModalName">&nbsp;</div>

					<div class="ll-modal-subtitle" id="llModalTitle">&nbsp;</div>

					<div class="ll-modal-pronouns" id="llModalPronouns">&nbsp;</div>

					<div id="llModalSchoolTag">&nbsp;</div>
				</div>
				<button class="ll-modal-close" onclick="llCloseModal()">✕</button></div>

			<div class="ll-modal-body">
				<div class="ll-section">
					<div class="ll-section-label">Identity</div>

					<p class="ll-section-text" id="llModalIdentity">&nbsp;</p>
				</div>

				<div class="ll-section">
					<div class="ll-section-label">Approach me about</div>

					<p class="ll-section-text" id="llModalApproach">&nbsp;</p>
				</div>

				<div class="ll-section">
					<div class="ll-section-label">Fields of professional work</div>

					<p class="ll-section-text" id="llModalFields">&nbsp;</p>
				</div>

				<div class="ll-section">
					<div class="ll-section-label">How to reach me</div>

					<p class="ll-section-text" id="llModalReach">&nbsp;</p>
				</div>

				<div class="ll-section">
					<div class="ll-section-label">A piece of advice</div>

					<div class="ll-advice-block">
						<p class="ll-advice-text" id="llModalAdvice">&nbsp;</p>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script>
    function llFilter(school, btn) {
      document.querySelectorAll('.ll-filter-btn').forEach(function(b) {
        b.className = 'll-filter-btn';
      });
      btn.classList.add('ll-active-' + school);
      document.querySelectorAll('.ll-card').forEach(function(card) {
        if (school === 'all') {
          card.style.display = '';
        } else if (school === 'grad') {
          card.style.display = card.dataset.grad === 'true' ? '' : 'none';
        } else {
          card.style.display = card.dataset.school === school ? '' : 'none';
        }
      });
    }

    function llOpenModal(card) {
      var d = card.dataset;
      var initials = d.name
        .replace('Dr. ', '').replace('Prof. ', '')
        .split(' ').map(function(w) { return w[0]; }).join('').slice(0, 2);

      // Build avatar — use card image if present
      var cardImg = card.querySelector('.ll-card-photo img');
      var avatarEl = document.getElementById('llModalAvatar');
      if (cardImg) {
        avatarEl.innerHTML = '<img src="' + cardImg.src + '" alt="' + d.name + '" />';
      } else {
        avatarEl.textContent = initials;
      }

      document.getElementById('llModalName').textContent     = d.name;
      document.getElementById('llModalTitle').textContent    = d.title;
      document.getElementById('llModalPronouns').textContent = d.pronouns || '';
      document.getElementById('llModalIdentity').textContent = d.identity;
      document.getElementById('llModalApproach').textContent = d.approach;
      document.getElementById('llModalFields').textContent   = d.fields;
      document.getElementById('llModalReach').textContent    = d.reach;
      document.getElementById('llModalAdvice').textContent   = d.advice;

      var tagHTML = '<span class="ll-modal-school-tag ll-' + d.school + '">' + d.schoolLabel + '</span>';
      if (d.grad === 'true') {
        tagHTML += ' <span class="ll-modal-school-tag ll-grad">GRAD</span>';
      }
      document.getElementById('llModalSchoolTag').innerHTML = tagHTML;

      document.getElementById('llModal').scrollTop = 0;
      document.getElementById('llOverlay').classList.add('ll-open');
      document.body.style.overflow = 'hidden';
    }

    function llCloseModal() {
      document.getElementById('llOverlay').classList.remove('ll-open');
      document.body.style.overflow = '';
    }

    function llCloseOnBackdrop(e) {
      if (e.target === document.getElementById('llOverlay')) llCloseModal();
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') llCloseModal();
    });
  </script></div>
<!-- /ll-page -->