<!-- =====================================================================
     SLC CONFERENCES PAGE - paste this whole block into a "Full HTML"
     content area in the CMS. No page-level H1 is included here on
     purpose, since the Drupal page template already renders its own
     title above this content.

     DESIGN SYSTEM (shared by every conference on this page):
       - Colors: UC Merced blue (#003C6C) and gold (#FDB515) are the
         shared frame. Each conference also gets its own accent color
         for its full-width hero: Student Leadership Conference uses
         a banner photo with a blue scrim, We Are Here uses solid
         green with purple headline accents (its established sub-brand).
       - Typography, buttons, cards, and the speakers accordion are
         shared components so every conference feels like part of the
         same page, not a separate design pasted in.

     HOW TO SWAP THE PAGE HERO BANNER IMAGE:
       Find the <img> inside the "page-hero" div near the top of the
       body and replace its src with the new image path. It is a real
       <img>, not a CSS background, so it always shows the full photo
       at its natural aspect ratio (no cropping, no fixed height).
       This banner spans the whole page, above the welcome text, not
       any single conference's hero.

     HOW TO ADD A THIRD CONFERENCE LATER:
       1. Duplicate one <section class="conf-section"> block below
          (start to end), give it a new id (e.g. id="new-conf").
       2. Add a matching link inside the "conf-nav" list near the top.
       3. Pick an accent color/background for its hero (add a new
          ".hero-XXX" rule near the other hero rules).

     HOW THE DATE / COUNTDOWN WIDGET WORKS:
       Each hero has one "date-status" element, e.g.:
         <div class="date-status" data-target="TBD"
              data-location="Building, Room"
              data-tbd-text="Date & Location: To Be Announced"></div>
       - While data-target="TBD", it shows only the data-tbd-text pill.
       - Once a real date is set (e.g. data-target="2026-09-25T15:00:00"),
         it automatically shows the formatted date/location and a live
         countdown, then switches to a "concluded" message afterward.
       This is the ONLY place date status is shown in the hero, so
       there is never more than one "To Be Announced" message.

     HOW "THEME & DETAILS" AND "REGISTRATION" WORK:
       Both conferences show a "To Be Announced" placeholder for their
       theme and for registration until that year's details are ready.
       Directly below each placeholder is a commented-out template.
       When the theme is announced or registration opens: delete the
       placeholder paragraph, uncomment the template, and fill it in.

     HOW TO ADD / REMOVE A GUEST SPEAKER:
       Each conference has a "Meet Our Guest Speakers" section near
       the bottom. Inside it is a commented-out template. To add a
       speaker: copy the template block, delete the comment markers
       wrapping it, and fill in the headshot image URL, name, title,
       and about text. To remove a speaker, delete their whole
       "speaker-card" block. Each speaker card is independent, so
       add or delete as many as needed.
===================================================================== -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet" />
<style type="text/css">/* ============================================================
   SHARED DESIGN SYSTEM - colors, type, and components used by
   every conference on this page.
============================================================ */
.conf-page{
  --c-blue:#003C6C;
  --c-gold:#FDB515;
  --c-green:#184D3A;
  --c-purple:#C8A2D1;
  --c-ink:#1d2733;
  --c-muted:#5b6774;
  --c-bg:#F5F7FA;
  --radius:14px;
  font-family:'Poppins',sans-serif;
  color:var(--c-ink);
  background:#fff;
}
.conf-page h1,.conf-page h2,.conf-page h3,.conf-page h4{font-family:'Poppins',sans-serif;font-weight:700;margin:0;}
.conf-page p{margin:0 0 16px;}
.conf-page a{color:var(--c-blue);}

/* ---- page-wide hero banner (sits above the welcome text) ----
   Uses a real <img>, not a background-image, so the height is not
   fixed/cropped - it scales naturally with the image's own aspect
   ratio at full page width. */
.page-hero{width:100vw;margin-left:calc(-50vw + 50%);line-height:0;}
.page-hero img{width:100%;height:auto;display:block;}

/* ---- page intro ---- */
.conf-welcome{text-align:center;max-width:820px;margin:0 auto;padding:36px 20px 10px;}
.conf-welcome p{font-size:16px;line-height:1.7;color:var(--c-muted);}
.conf-nav{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin:24px 0 56px;padding:0;list-style:none;}
.conf-nav a{background:var(--c-gold);color:var(--c-blue);font-weight:600;font-size:14px;padding:10px 22px;border-radius:999px;text-decoration:none;transition:.2s ease;display:inline-block;}
.conf-nav a:hover{background:#e0a800;transform:scale(1.03);}

/* ---- full-width hero (shared shape, styled per conference) ---- */
.conf-hero{width:100vw;margin-left:calc(-50vw + 50%);padding:70px 20px 56px;text-align:center;color:#fff;}
.conf-hero .eyebrow{font-size:13px;letter-spacing:1.5px;text-transform:uppercase;font-weight:600;opacity:.85;margin-bottom:14px;color:#fff;}
.conf-hero h2{font-size:46px;margin-bottom:14px;font-weight:800;}
.conf-hero .tagline{font-size:18px;max-width:700px;margin:0 auto 22px;opacity:.92;line-height:1.6;}

.hero-slc{background:var(--c-blue);}
.hero-slc h2,.hero-slc .eyebrow,.hero-slc .tagline{color:#fff !important;}

.hero-wah{background:var(--c-green);}
.hero-wah h2{color:var(--c-purple) !important;font-size:52px;}
.hero-wah h3{color:var(--c-purple);font-size:22px;font-weight:600;margin-bottom:6px;}

/* ---- date / countdown widget (shared, single source of truth) ---- */
.date-status{margin-top:6px;}
.date-pill{display:inline-block;background:var(--c-gold);color:var(--c-blue);padding:12px 26px;border-radius:999px;font-weight:600;font-size:15px;margin-bottom:4px;}
.date-line{font-weight:600;font-size:15px;margin-bottom:14px;opacity:.95;}
.countdown-boxes{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:4px;}
.countdown-boxes .cd-box{background:rgba(255,255,255,.16);border-radius:10px;padding:12px 16px;min-width:74px;text-align:center;}
.countdown-boxes .cd-box span.cd-num{display:block;font-size:26px;font-weight:700;line-height:1;}
.countdown-boxes .cd-box span.cd-label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.5px;margin-top:6px;opacity:.85;}
.countdown-past{font-weight:600;font-size:15px;text-align:center;padding:12px 24px;border-radius:999px;display:inline-block;background:rgba(255,255,255,.16);}

/* ---- content sections below the hero ---- */
.conf-section-body{max-width:820px;margin:0 auto;padding:56px 20px 0;}
.conf-section-body h3.block-title{font-size:24px;margin-bottom:18px;text-align:center;}
.details-slc h3.block-title{color:var(--c-blue);}
.details-wah h3.block-title{color:var(--c-green);}

.placeholder-card{border:2px dashed #cfd8e3;background:var(--c-bg);border-radius:var(--radius);padding:26px 24px;text-align:center;font-style:italic;color:var(--c-muted);margin-bottom:10px;}

.conf-section-body p{font-size:16px;line-height:1.7;color:var(--c-ink);}
.conf-section-body p.muted{color:var(--c-muted);}

/* registration card */
.register-card{border-radius:var(--radius);background:var(--c-bg);padding:28px 24px;text-align:center;margin-top:8px;}
.register-card .btn{display:inline-block;margin-top:6px;padding:11px 24px;background:var(--c-gold);color:var(--c-blue);font-weight:600;font-size:14px;border-radius:999px;text-decoration:none;transition:.2s ease;}
.register-card .btn:hover{background:#e0a800;transform:scale(1.03);}
.register-card .embed-wrap{margin-top:18px;}

/* sponsor strip (We Are Here) */
.sponsor-strip{text-align:center;margin-top:34px;padding-top:26px;border-top:1px solid #e3e8ee;}
.sponsor-strip .sponsor-title{font-weight:600;font-size:13px;margin-bottom:10px;color:var(--c-muted);}
.sponsor-strip img{max-width:190px;width:100%;height:auto;margin:0 auto;display:block;}

/* speaker link line */
.speaker-link-line{text-align:center;margin-top:16px;font-size:14px;}

/* ---- guest speakers accordion (shared) ---- */
.speakers-section{max-width:820px;margin:56px auto 70px;padding:0 20px;}
.speakers-toggle{width:100%;text-align:center;font-size:22px;font-weight:700;padding:16px;border-radius:var(--radius);cursor:pointer;list-style:none;color:#fff;}
.speakers-toggle::-webkit-details-marker{display:none;}
.speakers-toggle::after{content:"\25BE";margin-left:8px;display:inline-block;transition:transform .2s;}
.speakers-section details[open]>.speakers-toggle::after{transform:rotate(180deg);}
.speakers-slc .speakers-toggle{background:var(--c-blue);}
.speakers-wah .speakers-toggle{background:var(--c-green);}
.speakers-empty-msg{text-align:center;font-size:15px;color:var(--c-muted);font-style:italic;margin:22px 0 0;}
.speakers-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;margin-top:22px;}
.speaker-card{border:1px solid #e3e8ee;border-radius:var(--radius);padding:16px;background:#fff;}
.speaker-card summary{display:flex;align-items:center;gap:14px;cursor:pointer;list-style:none;}
.speaker-card summary::-webkit-details-marker{display:none;}
.speaker-card img{width:60px;height:60px;border-radius:50%;object-fit:cover;flex-shrink:0;}
.speaker-card .sp-name{font-weight:700;font-size:15px;}
.speaker-card .sp-title{font-size:12px;color:var(--c-muted);}
.speaker-card .sp-about{margin-top:14px;font-size:14px;line-height:1.6;color:var(--c-ink);}
.speaker-card summary::before{content:"+";margin-left:auto;font-size:18px;font-weight:700;color:#9aa5b1;}
.speaker-card[open] summary::before{content:"\2212";}

@media (max-width:600px){
  .conf-hero h2{font-size:34px;}
  .hero-wah h2{font-size:38px;}
}
</style>
<div class="conf-page"><!-- ============================================================
       PAGE HERO BANNER (whole page, not a specific conference)
  ============================================================= -->
	<div class="page-hero"><img alt="UC Merced Student Leadership Center conferences banner" src="/sites/studentleadership.ucmerced.edu/files/images/banners/conference_page_banner.png" /></div>
	<!-- ============================================================
       WELCOME SECTION (no H1 here - the CMS page title covers it)
  ============================================================= -->

	<div class="conf-welcome">
		<p>The Margo F. Souza Student Leadership Center hosts conferences throughout the year to help UC Merced students grow as leaders, connect with community, and build confidence. Explore our conferences below.</p>

		<ul class="conf-nav">
			<li><a href="#slc-conference">Student Leadership Conference</a></li>
			<li><a href="#wah-conference">We Are Here</a></li>
		</ul>
	</div>
	<!-- ============================================================
       CONFERENCE 1: STUDENT LEADERSHIP CONFERENCE
  ============================================================= -->

	<section aria-labelledby="slc-title" class="conf-section" id="slc-conference"><!-- ---- Hero + Countdown ---- -->
		<div class="conf-hero hero-slc">
			<div class="eyebrow">Margo F. Souza Student Leadership Center</div>

			<h2 id="slc-title">Student Leadership Conference</h2>

			<p class="tagline">A full day of leadership development for UC Merced students, alumni, and guest speakers, built around workshops, connection, and confidence-building.</p>
			<!-- Set data-target to an ISO date (e.g. 2026-09-25T15:00:00) once confirmed -->

			<div class="date-status" data-location="Lakireddy Grand Ballroom, UC Merced Conference Center" data-target="TBD" data-tbd-text="Date &amp; Location: To Be Announced">&nbsp;</div>
		</div>
		<!-- ---- Theme & Details ---- -->

		<div class="conf-section-body details-slc">
			<h3 class="block-title">This Year&#39;s Theme &amp; Details</h3>

			<div class="placeholder-card">This year&#39;s theme and conference details will be posted here once finalized.</div>
			<!-- UNCOMMENT AND FILL IN ONCE THE THEME IS ANNOUNCED, THEN DELETE THE PLACEHOLDER CARD ABOVE

      <h4 style="text-align:center;color:var(--c-blue);font-size:20px;margin-bottom:12px;">Theme: [This Year's Theme]</h4>
      <p>[Theme description goes here.]</p>

      -->

			<p class="muted" style="text-align:center;margin-top:10px;">Questions? Contact us at <a href="mailto:lead@ucmerced.edu">lead@ucmerced.edu</a>.</p>
		</div>
		<!-- ---- Registration ---- -->

		<div class="conf-section-body">
			<h3 class="block-title" style="color:var(--c-blue);">Registration</h3>

			<div class="register-card">
				<p class="muted" style="margin-bottom:0;">Registration will open once the date is confirmed. Check back soon!</p>
				<!-- UNCOMMENT AND FILL IN THE FORM URL ONCE REGISTRATION OPENS, THEN DELETE THE PLACEHOLDER TEXT ABOVE

        <div class="embed-wrap">
          <iframe height="500" loading="lazy" src="[Qualtrics form URL]" style="border:0;width:100%;" title="Student Leadership Conference Registration Form"></iframe>
        </div>

        --></div>
		</div>
		<!-- ---- Guest Speakers (expandable, currently empty) ---- -->

		<div class="speakers-section speakers-slc">
			<details><summary class="speakers-toggle">Meet Our Guest Speakers</summary>

				<p class="speakers-empty-msg">Speaker lineup coming soon. Check back for updates!</p>

				<div class="speakers-grid"><!-- COPY THE BLOCK BELOW FOR EACH NEW SPEAKER. DELETE THE COMMENT MARKERS WRAPPING IT, THEN FILL IN DETAILS.

          <details class="speaker-card">
            <summary>
              <img alt="Headshot of [Speaker Name]" src="[headshot image URL]" />
              <span>
                <span class="sp-name">[Speaker Name]</span><br />
                <span class="sp-title">[Speaker Title / Organization]</span>
              </span>
            </summary>
            <p class="sp-about">[Speaker bio / about text goes here.]</p>
          </details>

          --></div>
			</details>
		</div>
	</section>
	<!-- ============================================================
       CONFERENCE 2: WE ARE HERE
  ============================================================= -->

	<section aria-labelledby="wah-title" class="conf-section" id="wah-conference"><!-- ---- Hero + Countdown ---- -->
		<div class="conf-hero hero-wah">
			<div class="eyebrow">Margo F. Souza Student Leadership Center</div>

			<h2 id="wah-title">WE ARE HERE</h2>

			<h3>Women of the Central Valley / Mujeres del Valle Central</h3>

			<p class="tagline">Convening for Connection &amp; Empowerment / Convivio para la conexión y el empoderamiento</p>
			<!-- Set data-target to an ISO date once confirmed -->

			<div class="date-status" data-location="Historic Mondo Building, 1715 Canal St., Merced, CA 95340" data-target="TBD" data-tbd-text="Save the Date: To Be Announced / Guarde la fecha: Por anunciar">&nbsp;</div>
		</div>
		<!-- ---- Theme & Details ---- -->

		<div class="conf-section-body details-wah">
			<h3 class="block-title">This Year&#39;s Theme &amp; Details</h3>

			<div class="placeholder-card">This year&#39;s theme and full schedule will be posted here once finalized. / El tema y horario de este año se publicarán aquí una vez confirmados.</div>
			<!-- UNCOMMENT AND FILL IN ONCE THE THEME IS ANNOUNCED, THEN DELETE THE PLACEHOLDER CARD ABOVE

      <h4 style="text-align:center;color:var(--c-green);font-size:20px;margin-bottom:12px;">Theme: [This Year's Theme]</h4>
      <p>[Theme description goes here.]</p>

      -->

			<p>Join us during Womxn&rsquo;s History Month for a one-day convivio celebrating the incredible womxn of California&rsquo;s Central Valley. Open to all womxn-identifying individuals and allies, this is a powerful opportunity to connect, learn, and be empowered by the voices shaping our community. Sessions will cover health and wellness, financial literacy, policy and politics, and technology and innovation. Spanish interpretation is available, entry is free, and lunch will be provided.</p>

			<p>Acompáñanos durante el Mes de la Historia de la Mujer para un convivio de un día en celebración de las increíbles mujeres del Valle Central de California. Abierto a todas las personas que se identifiquen como mujeres y a sus aliades, esta es una oportunidad para conectar, aprender y empoderarse con las voces que están dando forma a nuestra comunidad. Las sesiones cubrirán salud y bienestar, educación financiera, políticas públicas, y tecnología e innovación. Habrá interpretación en español, la entrada es gratuita, y se ofrecerá almuerzo.</p>
		</div>
		<!-- ---- Registration ---- -->

		<div class="conf-section-body">
			<h3 class="block-title" style="color:var(--c-green);">Registration</h3>

			<div class="register-card">
				<p class="muted" style="margin-bottom:0;">Registration will open once the date is confirmed. Check back soon! / El registro abrirá una vez confirmada la fecha.</p>
				<!-- UNCOMMENT AND FILL IN THE FORM URL ONCE REGISTRATION OPENS, THEN DELETE THE PLACEHOLDER TEXT ABOVE

        <a class="btn" href="[Qualtrics form URL]" target="_blank">Register Now / &iexcl;Reg&iacute;strate hoy!</a>

        --></div>

			<div class="sponsor-strip">
				<p class="sponsor-title">Thank you to our Sponsor / Gracias a Nuestro Patrocinador</p>
				<img alt="Sponsor Logo" src="https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/page/images/cta-logo-blue-png.png" /></div>
		</div>
		<!-- ---- Guest Speakers (expandable, currently empty) ---- -->

		<div class="speakers-section speakers-wah">
			<details><summary class="speakers-toggle">Meet Our Guest Speakers / Conozca a Nuestras Oradoras</summary>

				<p class="speakers-empty-msg">Speaker lineup coming soon. Check back for updates! / Próximamente más información.</p>

				<div class="speakers-grid"><!-- COPY THE BLOCK BELOW FOR EACH NEW SPEAKER. DELETE THE COMMENT MARKERS WRAPPING IT, THEN FILL IN DETAILS.

          <details class="speaker-card">
            <summary>
              <img alt="Headshot of [Speaker Name]" src="[headshot image URL]" />
              <span>
                <span class="sp-name">[Speaker Name]</span><br />
                <span class="sp-title">[Speaker Title / Organization]</span>
              </span>
            </summary>
            <p class="sp-about">[Speaker bio / about text goes here.]</p>
          </details>

          --></div>

				<p class="speaker-link-line"><a href="https://studentleadership.ucmerced.edu/wearehereguestspeakers" target="_blank">View announced speakers on their own page / Conozca a Nuestras Oradoras Invitadas</a></p>
			</details>
		</div>
	</section>
</div>
<script>
(function(){
  function pad(n){ return String(n).padStart(2,'0'); }

  function renderDateStatus(el){
    var target = el.getAttribute('data-target');
    var location = el.getAttribute('data-location') || '';
    var tbdText = el.getAttribute('data-tbd-text') || 'Date To Be Announced';

    var targetDate = (!target || target.toUpperCase() === 'TBD') ? NaN : new Date(target).getTime();

    if(isNaN(targetDate)){
      el.innerHTML = '<div class="date-pill">'+tbdText+'</div>';
      return;
    }

    var dateLabel = new Date(target).toLocaleDateString(undefined,{weekday:'long',year:'numeric',month:'long',day:'numeric'});
    var lineText = location ? (dateLabel + ' &middot; ' + location) : dateLabel;
    var timer;

    function tick(){
      var diff = targetDate - new Date().getTime();
      if(diff <= 0){
        el.innerHTML = '<div class="countdown-past">This conference has concluded. Thank you to everyone who joined us!</div>';
        clearInterval(timer);
        return;
      }
      var d = Math.floor(diff/(1000*60*60*24));
      var h = Math.floor((diff/(1000*60*60))%24);
      var m = Math.floor((diff/(1000*60))%60);
      var s = Math.floor((diff/1000)%60);
      el.innerHTML =
        '<div class="date-line">'+lineText+'</div>'+
        '<div class="countdown-boxes">'+
          '<div class="cd-box"><span class="cd-num">'+d+'</span><span class="cd-label">Days</span></div>'+
          '<div class="cd-box"><span class="cd-num">'+pad(h)+'</span><span class="cd-label">Hours</span></div>'+
          '<div class="cd-box"><span class="cd-num">'+pad(m)+'</span><span class="cd-label">Min</span></div>'+
          '<div class="cd-box"><span class="cd-num">'+pad(s)+'</span><span class="cd-label">Sec</span></div>'+
        '</div>';
    }
    tick();
    timer = setInterval(tick, 1000);
  }

  document.querySelectorAll('.date-status').forEach(renderDateStatus);
})();
</script>