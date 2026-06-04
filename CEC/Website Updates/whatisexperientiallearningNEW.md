<style type="text/css">/* Slideshow Styles */
.slideshow-container {
    position: relative;
    max-width: 1200px;
    height: 500px;
    margin: 0 30px 0 auto;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 5px solid #dbaa00;
}
.slideshow-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.mySlides {
    display: none;
    position: relative;
    height: 100%;
}

.mySlides img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-panels {
    position: absolute;
    top: 40px;
    left: 0;
    z-index: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.hero-panel {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    cursor: pointer;
    position: relative;
}

.hero-panel-bookmark {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    flex-shrink: 0;
    position: relative;
    z-index: 2;
}

.hero-panel-tab {
    background: #0f2d52;
    color: #dbaa00;
    font-size: 0.75em;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    padding: 18px 12px;
    user-select: none;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s, color 0.2s;
    width: 44px;
    flex-shrink: 0;
}

.hero-panel:hover .hero-panel-tab {
    background: #dbaa00;
    color: #0f2d52;
}

.hero-panel-point {
    flex-shrink: 0;
    width: 24px;
    align-self: stretch;
    position: relative;
    overflow: hidden;
}

.hero-panel-point::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: #0f2d52;
    clip-path: polygon(0 0, 0 100%, 100% 50%);
    transition: background 0.2s;
}

.hero-panel:hover .hero-panel-point::before {
    background: #dbaa00;
}

.hero-panel-content {
    background: #0f2d52;
    color: #ffffff;
    max-width: 0;
    max-height: 0;
    min-height: 100%;
    white-space: normal;
    width: 260px;
    overflow: hidden;
    transition: max-width 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                padding 0.35s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0;
    box-sizing: border-box;
    white-space: nowrap;
    position: absolute;
    left: 100%;
    top: 0;
    z-index: 1;
    border-radius: 0 8px 8px 0;
    left: calc(100% - 24px);
    align-self: stretch;
    visibility: hidden;
    opacity: 0;
    transition: max-width 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                padding 0.35s ease,
                visibility 0s linear 0.35s,
                opacity 0.2s ease;
}

.hero-panel:hover .hero-panel-content {
    max-width: 284px;
    max-height: 200px;    /* add this — set high enough to fit your content */
    padding: 14px 18px 14px 30px;
    visibility: visible;
    opacity: 1;
    transition: max-width 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                padding 0.35s ease,
                visibility 0s linear 0s,
                opacity 0.2s ease 0.1s;
}

.hero-panel-content p {
    font-size: 0.88em;
    line-height: 1.55;
    color: rgba(255,255,255,0.85);
    margin: 0 0 10px;
    white-space: normal;
    max-width: 220px;
}

.hero-panel-content a {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.78em;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: #dbaa00 !important;
    text-decoration: none;
    border-bottom: 1px solid rgba(219,170,0,0.4);
    padding-bottom: 2px;
    width: fit-content;
    transition: color 0.2s;
}

.hero-panel-content a:hover { color: #fff; }

.fade {
    animation-name: fade;
    animation-duration: 1.5s;
    animation-fill-mode: forwards;
}

@keyframes fade {
    from { opacity: 0.4 }
    to { opacity: 1 }
}

.text {
    color: #ffffff;
    font-size: 18px;
    font-weight: 700;
    padding: 15px 20px;
    position: absolute;
    bottom: 0;
    width: 100%;
    text-align: center;
    background-color: rgba(15, 45, 82, 0.75);
    box-sizing: border-box;
}

/* General Page Styles */
body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
    color: #0f2d52;
}

/* Mission/Intro Bar */
.intro-container {
    max-width: 1200px;
    margin: 30px 30px 30px auto;
    padding: 0 20px;
    border-top: 4px solid #dbaa00;
    border-bottom: 4px solid #dbaa00;
    min-height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.intro-container p {
    font-size: 18px;
    line-height: 1.5;
    color: #333;
    margin: 0;
    padding: 15px 0;
    text-align: left;
}

/* Carousel Section */
.carousel-section {
    background-color: #ffffff;
    padding: 60px 0 20px;
    margin-top: 10px;
}

.carousel-outer {
    position: relative;
    max-width: 1200px;
    margin: 0 30px 0 auto;
    padding: 0 54px;
    box-sizing: border-box;
}

.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: #ffffff;
    border: 2px solid #0f2d52;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.1em;
    color: #0f2d52;
    z-index: 10;
    transition: background-color 0.2s ease, color 0.2s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.carousel-btn:hover {
    background-color: #0f2d52;
    color: #ffffff;
}

#prevBtn { left: 0; }
#nextBtn { right: 0; }

.carousel-clip {
    overflow: hidden;
    padding-bottom: 30px;
    margin-bottom: -30px;
    padding-left: 8px;
    padding-right: 8px;
    margin-left: -8px;
    margin-right: -8px;
}

.carousel-wrapper {
    position: relative;
}

.carousel-track {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    will-change: transform;
}

.exp-card {
    flex: 0 0 33.333%;
    padding: 0 12px;
    box-sizing: border-box;
    display: flex;
}

.exp-card-inner {
    background-color: #ffffff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.exp-card-inner:hover {
    box-shadow: 0 8px 28px rgba(219, 170, 0, 0.35);
}

.exp-card-inner img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}

.exp-card-body {
    padding: 28px 24px 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    justify-content: space-between;
    flex-grow: 1;
}

.exp-card-body h3 {
    font-size: 1.35em;
    font-weight: 700;
    color: #0f2d52;
    margin: 0 0 14px;
    letter-spacing: 0.2px;
}

.exp-card-body p {
    font-size: 0.97em;
    line-height: 1.65;
    color: #444;
    margin: 0;
}

.exp-card-link,
.exp-card-link:link,
.exp-card-link:visited,
.exp-card-link:hover,
.exp-card-link:active {
    display: inline-block;
    text-align: center;
    position: relative;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #0f2d52;
    text-decoration: none !important;
    margin-top: auto;
    padding-bottom: 2px;
}

.exp-card-link:hover { color: #dbaa00; }

.exp-card-link .link-text {
    display: inline-block;
    border-bottom: 2px solid #dbaa00;
    padding-bottom: 2px;
}

.exp-card-link .arrow {
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    transition: transform 0.2s ease;
}

.exp-card-link:hover .arrow {
    transform: translateY(-50%) translateX(4px);
}

/* Student Stories Banner */
.stories-banner {
    max-width: 1200px;
    margin: 0 30px 20px auto;
    background: #0f2d52;
    border-radius: 16px;
    border-left: 8px solid #dbaa00;
    padding: 32px 44px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.stories-banner-text {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.stories-banner-eyebrow {
    font-size: 0.75em;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #dbaa00;
}

.stories-banner-heading {
    font-size: 1.35em;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
    line-height: 1.25;
}

.stories-banner-link,
.stories-banner-link:link,
.stories-banner-link:visited,
.stories-banner-link:hover,
.stories-banner-link:active {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #dbaa00;
    color: #0f2d52;
    font-size: 0.85em;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 13px 26px;
    border-radius: 999px;
    text-decoration: none !important;
    white-space: nowrap;
    flex-shrink: 0;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stories-banner-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(219, 170, 0, 0.4);
}

.stories-banner-link .arrow {
    transition: transform 0.2s ease;
}

.stories-banner-link:hover .arrow {
    transform: translateX(4px);
}

@media (max-width: 768px) {
    .hero-panels {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        gap: 8px;
    }
    .stories-banner {
        flex-direction: column;
        align-items: flex-start;
        margin: 0 20px 40px 0;
        padding: 24px 22px;
    }
    .slideshow-container {
        margin: 0 20px 0 0;
        height: 350px;
    }
    .exp-card {
        flex: 0 0 100%;
        padding: 0 56px;
    }
    .carousel-outer {
        margin: 0 20px 0 0;
        padding: 0;
    }
    #prevBtn { left: 0; }
    #nextBtn { right: 0; }
    .intro-container {
        margin: 20px 20px 20px 0;
        padding: 0 15px;
    }
    .intro-container p { font-size: 16px; }
}

#main-menu ul.sf-menu {
    display: flex;
    align-items: stretch;
    height: 34px;
}
#main-menu .sf-menu > li {
    display: flex;
    align-items: center;
}
#main-menu .sf-menu > li > a {
    display: flex !important;
    align-items: center;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    height: 100%;
}

footer {
    text-align: center;
    padding: 10px 0;
    background-color: #0f2d52;
    color: white;
}
footer p { margin: 0; font-size: 0.9em; }
footer a { color: #dbaa00; text-decoration: none; margin: 0 10px; font-weight: bold; }
footer a:hover { text-decoration: underline; }
</style>
<!-- Slideshow Container -->
<div class="slideshow-container" style="position: relative;"><img alt="Welcome to Experiential Learning at UC Merced" src="/sites/success.ucmerced.edu/files/page/images/dsc03572.jpg" />
	<div class="hero-fog">&nbsp;</div>

	<div class="hero-panels">
		<div class="hero-panel">
			<div class="hero-panel-bookmark">
				<div class="hero-panel-tab">Request Form</div>

				<div class="hero-panel-point">&nbsp;</div>
			</div>

			<div class="hero-panel-content">
				<p>Ready to submit an Experiential Learning Recognition request?</p>
				<a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_6s4Yl0YHxvJJdJQ">Click Here &rarr;</a></div>
		</div>

		<div class="hero-panel">
			<div class="hero-panel-bookmark">
				<div class="hero-panel-tab">Student Stories</div>

				<div class="hero-panel-point">&nbsp;</div>
			</div>

			<div class="hero-panel-content">
				<p>Want to hear some real stories from students?</p>
				<a href="https://success.ucmerced.edu/Student-Stories-With-EL">Click Here &rarr;</a></div>
		</div>
	</div>
</div>
<script>
    let slideIndex = 0;
    showSlides();
    function showSlides() {
        let slides = document.getElementsByClassName("mySlides");
        for (let i = 0; i < slides.length; i++) slides[i].style.display = "none";
        slideIndex++;
        if (slideIndex > slides.length) slideIndex = 1;
        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 6000);
    }
</script><!-- Intro Description Bar -->

<div class="intro-container">
	<p><strong>Experiential learning is a hands-on approach where students gain knowledge and transferable skills by engaging directly in real-world tasks and reflecting on their experiences. This approach enriches academic learning by fostering personal growth, critical thinking, cultural awareness, and professional development.</strong></p>
</div>
<!-- Experience Cards Carousel -->

<div class="carousel-section">
	<div class="carousel-outer"><button aria-label="Previous" class="carousel-btn" id="prevBtn">&larr;</button><button aria-label="Next" class="carousel-btn" id="nextBtn">&rarr;</button>

		<div class="carousel-clip">
			<div class="carousel-wrapper">
				<div class="carousel-track" id="carouselTrack">
					<div class="exp-card">
						<div class="exp-card-inner"><img alt="Study Abroad" src="/sites/success.ucmerced.edu/files/page/images/124138campuslife140225.jpg" />
							<div class="exp-card-body">
								<h3>Study Abroad</h3>

								<p>Studying abroad offers students the chance to pursue their education through an international perspective, providing an immersive experience in different cultural and academic environments.</p>
								<a class="exp-card-link" href="https://studyabroad.ucmerced.edu/"><span class="link-text">Learn More</span> <span class="arrow">&rarr;</span></a></div>
						</div>
					</div>

					<div class="exp-card">
						<div class="exp-card-inner"><img alt="Community Service" src="/sites/success.ucmerced.edu/files/page/images/ucm_day1-177_1.jpg" />
							<div class="exp-card-body">
								<h3>Community Service</h3>

								<p>Community Service allows students to contribute time and effort to benefit others, impact the community, and cultivate skills and personal growth through various avenues.</p>
								<a class="exp-card-link" href="https://cec.ucmerced.edu/"><span class="link-text">Learn More</span> <span class="arrow">&rarr;</span></a></div>
						</div>
					</div>

					<div class="exp-card">
						<div class="exp-card-inner"><img alt="Undergraduate Research" src="/sites/success.ucmerced.edu/files/page/images/054zhukovacampus.jpg" />
							<div class="exp-card-body">
								<h3>Undergraduate Research</h3>

								<p>Undergraduate research offers students the chance to engage in hands-on research experiences across various disciplines, participating in summer research programs, and more.</p>
								<a class="exp-card-link" href="https://uroc.ucmerced.edu/"><span class="link-text">Learn More</span> <span class="arrow">&rarr;</span></a></div>
						</div>
					</div>

					<div class="exp-card">
						<div class="exp-card-inner"><img alt="Leadership" src="/sites/success.ucmerced.edu/files/page/images/dsc_0556_1_1.jpg" />
							<div class="exp-card-body">
								<h3>Leadership</h3>

								<p>Leadership involves engaging in activities that guide, inspire, and influence others toward achieving common goals. UC Merced students can take on leadership positions in student clubs and organizations.</p>
								<a class="exp-card-link" href="https://studentleadership.ucmerced.edu/leadership"><span class="link-text">Learn More</span> <span class="arrow">&rarr;</span></a></div>
						</div>
					</div>

					<div class="exp-card">
						<div class="exp-card-inner"><img alt="Internships" src="/sites/success.ucmerced.edu/files/page/images/machineshop_04_2014_1.jpg" />
							<div class="exp-card-body">
								<h3>Internships</h3>

								<p>An internship is a structured work experience, whether paid or unpaid, that takes students&#39; knowledge beyond the classroom to industry while building their network.</p>
								<a class="exp-card-link" href="https://hire.ucmerced.edu/students/jobs-internships"><span class="link-text">Learn More</span> <span class="arrow">&rarr;</span></a></div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<script>
    (function () {
        const track = document.getElementById('carouselTrack');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');

        const realCards = Array.from(track.querySelectorAll('.exp-card'));
        const realCount = realCards.length;
        const vis = window.innerWidth <= 768 ? 1 : 3;

        realCards.slice(0, vis).forEach(c => track.appendChild(c.cloneNode(true)));
        realCards.slice(-vis).forEach(c => track.insertBefore(c.cloneNode(true), track.firstChild));

        let current = vis;
        let autoTimer;
        let isTransitioning = false;

        function getCardWidth() {
            return track.querySelectorAll('.exp-card')[0].getBoundingClientRect().width;
        }
        function jumpTo(index) {
            track.style.transition = 'none';
            current = index;
            track.style.transform = 'translateX(-' + (current * getCardWidth()) + 'px)';
        }
        function slideTo(index) {
            if (isTransitioning) return;
            isTransitioning = true;
            current = index;
            track.style.transition = 'transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            track.style.transform = 'translateX(-' + (current * getCardWidth()) + 'px)';
        }

        track.addEventListener('transitionend', () => {
            isTransitioning = false;
            if (current >= realCount + vis) jumpTo(vis);
            if (current < vis) jumpTo(realCount);
        });

        prevBtn.addEventListener('click', () => { slideTo(current - 1); resetAuto(); });
        nextBtn.addEventListener('click', () => { slideTo(current + 1); resetAuto(); });
        track.addEventListener('mouseenter', () => clearInterval(autoTimer));
        track.addEventListener('mouseleave', () => startAuto());

        function advance() { slideTo(current + 1); }
        function startAuto() { autoTimer = setInterval(advance, 4500); }
        function resetAuto() { clearInterval(autoTimer); startAuto(); }

        jumpTo(vis);
        startAuto();
        window.addEventListener('resize', () => jumpTo(current));
    })();
</script><!-- Student Stories Banner -->

<div class="stories-banner">
	<div class="stories-banner-text"><span class="stories-banner-eyebrow">Student Voices</span>

		<h2 class="stories-banner-heading">Want to hear real experiences with EL?<br />
			Browse our student stories.</h2>
	</div>
	<a class="stories-banner-link" href="https://success.ucmerced.edu/Student-Stories-With-EL">Read Student Stories <span class="arrow">&rarr;</span></a></div>
<!-- Experiential Learning Pin Section -->

<div class="pin-section">
	<div class="pin-container">
		<div class="pin-header">
			<h2 class="pin-title">Experiential Learning Recognition Pin</h2>

			<p class="pin-subtitle">For Graduating Undergraduate Students</p>
		</div>

		<div class="pin-body">
			<div class="pin-description">
				<p><em><strong>Graduating undergraduate students</strong></em> who have participated in study abroad, community service, leadership, internship and/or undergraduate research experience will be eligible to receive an&nbsp;Experiential Learning pin(s). You can apply for one or more recognitions by completing the Experiential Learning Recognition Request Form. Note that you can complete one form for multiple recognitions.</p>

				<p>You must complete this form no later than <b>Friday, April 3rd</b>&nbsp;to be eligible to receive your pin(s) during the Spring 2026 Grad Fair happening on April 8 &amp; 9 at the UC Merced Lakireddy Ballroom. If you complete the survey after April 3rd, you will still be eligible to receive your pin(s)&nbsp;but your pickup location and time&nbsp;will change.</p>
				<a class="pin-cta" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_6s4Yl0YHxvJJdJQ" target="_blank">Experiential Learning Recognition Request Form <span class="pin-cta-arrow">&rarr;</span></a></div>

			<div class="pin-right">
				<h3 class="pin-criteria-heading">Pin Criteria</h3>

				<div class="pin-accordions">
					<div class="pin-accordion"><button aria-expanded="false" class="pin-accordion-btn"><span>Study Abroad</span> <span class="pin-chevron">+</span></button>

						<div class="pin-accordion-body">
							<p>Participant receiving academic credit for one of the following:</p>

							<ul>
								<li>UC Education Abroad Program (UCEAP)</li>
								<li>Experience through a UC Merced course</li>
								<li>Experience through another UC campus</li>
								<li>Experience through another study abroad provider or US institution</li>
							</ul>

							<p>The form will ask you to identify the following for each experience:</p>

							<ul>
								<li>Location of experience</li>
								<li>When you completed the experience and duration</li>
								<li>Whether or not you received UC credit</li>
							</ul>

							<p class="pin-contact">For questions, contact <a href="mailto:charmelin@ucmerced.edu">Craig Harmelin</a></p>
						</div>
					</div>

					<div class="pin-accordion"><button aria-expanded="false" class="pin-accordion-btn"><span>Community Service</span> <span class="pin-chevron">+</span></button>

						<div class="pin-accordion-body">
							<p>Participation in one of the following:</p>

							<ul>
								<li>Community Engagement Center-related activity</li>
								<li>Student club or organization related service project</li>
								<li>Course-related service or service-learning</li>
								<li>Experience UC Merced</li>
								<li>Self-directed independent service (i.e. project of your choice and making)</li>
								<li>Other -- the form will ask you to describe your experience</li>
							</ul>

							<p class="pin-contact">For questions, contact <a href="mailto:pricillacardenas@ucmerced.edu">Pricilla Cardenas</a></p>
						</div>
					</div>

					<div class="pin-accordion"><button aria-expanded="false" class="pin-accordion-btn"><span>Leadership</span> <span class="pin-chevron">+</span></button>

						<div class="pin-accordion-body">
							<p>Participation in one of the following:</p>

							<ul>
								<li>Yosemite Leadership Program</li>
								<li>Bobcat Leadership Seminar</li>
								<li>Experience UC Merced</li>
								<li>Associated Students of UC Merced (ASUCM)</li>
								<li>Campus Activities Board (CAB)</li>
								<li>Registered Student Club or Organization Officer or Leadership Position</li>
								<li>Other -- the form will ask you to describe your experience</li>
							</ul>

							<p class="pin-contact">For questions, contact <a href="mailto:sbarrera7@ucmerced.edu">Stephany Barrera</a></p>
						</div>
					</div>

					<div class="pin-accordion"><button aria-expanded="false" class="pin-accordion-btn"><span>Internship</span> <span class="pin-chevron">+</span></button>

						<div class="pin-accordion-body">
							<p>Participation in a paid or unpaid internship. The form will ask you to identify the following for each internship:</p>

							<ul>
								<li>Modality (in-person, remote, hybrid)</li>
								<li>Location of internship (on-campus or off-campus; US or international)</li>
								<li>Employer name</li>
								<li>Internship job title</li>
							</ul>

							<p class="pin-contact">For questions, contact <a href="mailto:rgoodman@ucmerced.edu">Robert Goodman</a></p>
						</div>
					</div>

					<div class="pin-accordion"><button aria-expanded="false" class="pin-accordion-btn"><span>Undergraduate Research</span> <span class="pin-chevron">+</span></button>

						<div class="pin-accordion-body">
							<p>Participation in a research or creative project(s) outside of regular course requirements. The form will ask you to identify the following for each experience:</p>

							<ul>
								<li>When you completed the experience(s) and the approximate number of hours</li>
								<li>Faculty mentor</li>
							</ul>

							<p class="pin-contact">For questions, contact <a href="mailto:patriciasotobecerr@ucmerced.edu">Patricia Soto Becerra</a></p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
<style type="text/css">.pin-section {
    padding: 0px 0 10px;
    margin-top: 0;
}
.pin-container {
    max-width: 1200px;
    margin: 0 30px 0 auto;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.09);
    border-top: 6px solid #dbaa00;
    overflow: hidden;
    padding: 50px 60px 60px;
}
.pin-header {
    text-align: center;
    margin-bottom: 36px;
    padding-bottom: 32px;
    border-bottom: 1px solid #e8e8e8;
}
.pin-title {
    font-size: 2em;
    font-weight: 700;
    color: #0f2d52;
    margin: 0 0 10px;
}
.pin-subtitle {
    font-size: 1.05em;
    color: #666;
    margin: 0;
    font-style: italic;
}
.pin-body {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: start;
}
.pin-description p {
    font-size: 1em;
    line-height: 1.75;
    color: #333;
    margin: 0 0 16px;
}
.pin-description p:last-of-type { margin-bottom: 24px; }
.pin-cta,
.pin-cta:link,
.pin-cta:visited,
.pin-cta:hover,
.pin-cta:active {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    font-size: 0.88em;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #0f2d52;
    text-decoration: none !important;
    border-bottom: 2px solid #dbaa00;
    padding-bottom: 3px;
    transition: color 0.2s ease;
}
.pin-cta:hover { color: #dbaa00; }
.pin-cta-arrow { transition: transform 0.2s ease; }
.pin-cta:hover .pin-cta-arrow { transform: translateX(4px); }
.pin-right { display: flex; flex-direction: column; }
.pin-criteria-heading {
    font-size: 0.78em;
    font-weight: 700;
    color: #0f2d52;
    margin: 0 0 14px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.pin-accordions { display: flex; flex-direction: column; gap: 8px; }
.pin-accordion {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #e5e5e5;
    background-color: #ffffff;
    transition: box-shadow 0.2s ease;
}
.pin-accordion:hover { box-shadow: 0 4px 14px rgba(219, 170, 0, 0.18); }
.pin-accordion-btn {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 18px;
    background-color: #ffffff;
    border: none;
    cursor: pointer;
    font-size: 0.98em;
    font-weight: 700;
    color: #0f2d52;
    text-align: left;
    transition: background-color 0.2s ease, color 0.2s ease;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
.pin-accordion-btn:hover { background-color: #f5f8fb; }
.pin-accordion-btn[aria-expanded="true"] { background-color: #0f2d52; color: #ffffff; }
.pin-accordion-btn[aria-expanded="true"] .pin-chevron { color: #dbaa00; transform: rotate(45deg); }
.pin-chevron {
    font-size: 1.4em;
    font-weight: 300;
    line-height: 1;
    color: #dbaa00;
    transition: transform 0.25s ease;
    flex-shrink: 0;
}
.pin-accordion-body {
    display: none;
    padding: 18px 18px 20px;
    border-top: 2px solid #dbaa00;
    background-color: #fafafa;
}
.pin-accordion-body p { font-size: 0.93em; line-height: 1.6; color: #333; margin: 0 0 8px; }
.pin-accordion-body ul { margin: 0 0 12px 16px; padding: 0; }
.pin-accordion-body ul li { font-size: 0.93em; line-height: 1.6; color: #333; margin-bottom: 3px; }
.pin-contact {
    margin-top: 12px !important;
    font-size: 0.9em !important;
    color: #666 !important;
    padding-top: 12px;
    border-top: 1px solid #eee;
}
.pin-contact a,
.pin-contact a:link,
.pin-contact a:visited { color: #0f2d52; font-weight: 700; text-decoration: none; border-bottom: 1px solid #dbaa00; padding-bottom: 1px; }
.pin-contact a:hover { color: #dbaa00; }
@media (max-width: 900px) { .pin-body { grid-template-columns: 1fr; gap: 36px; } }
@media (max-width: 768px) {
    .pin-container { margin: 0 20px 0 0; padding: 30px 24px 40px; border-radius: 16px; }
    .pin-title { font-size: 1.5em; }
}
</style>
<script>
    document.querySelectorAll('.pin-accordion-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const expanded = btn.getAttribute('aria-expanded') === 'true';
            const body = btn.nextElementSibling;
            document.querySelectorAll('.pin-accordion-btn').forEach(b => {
                b.setAttribute('aria-expanded', 'false');
                b.nextElementSibling.style.display = 'none';
            });
            if (!expanded) {
                btn.setAttribute('aria-expanded', 'true');
                body.style.display = 'block';
            }
        });
    });
</script>