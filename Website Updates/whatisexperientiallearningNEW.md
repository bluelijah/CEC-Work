<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">
        /* Slideshow Styles */
        .slideshow-container {
            position: relative;
            max-width: 1200px;
            height: 500px;
            margin: 0 30px 0 auto;
            background-color: #dbaa00;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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
            padding: 60px 0 90px;
            margin-top: 10px;
        }

        /* Outer container: provides space for the side arrows */
        .carousel-outer {
            position: relative;
            max-width: 1200px;
            margin: 0 30px 0 auto;
            padding: 0 54px;
            box-sizing: border-box;
        }

        /* Side arrow buttons */
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

        /* Clip wrapper: hides cards outside viewport, allows bottom shadow */
        .carousel-clip {
            overflow: hidden;
            padding-bottom: 30px;
            margin-bottom: -30px;
            /* Extra side padding so box-shadow isn't clipped on mobile */
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

        /* Cards: exactly 1/3 of the track */
        .exp-card {
            flex: 0 0 33.333%;
            padding: 0 12px;
            box-sizing: border-box;
            display: flex;
        }

        @media (max-width: 768px) {
            .exp-card {
                flex: 0 0 100%;
                padding: 0 56px;
            }

            /* On mobile arrows sit beside the card */
            .carousel-outer {
                margin: 0 20px 0 0;
                padding: 0;
            }

            #prevBtn { left: 0; }
            #nextBtn { right: 0; }
        }

        .exp-card-inner {
            background-color: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            display: flex;
            flex-direction: column;
            width: 100%;
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
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.88em;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #0f2d52;
            text-decoration: none !important;
            transition: color 0.2s ease;
            margin-top: auto;
            padding-top: 22px;
        }

        .exp-card-link:hover {
            color: #dbaa00;
        }

        .exp-card-link .link-text {
            border-bottom: 2px solid #dbaa00;
            padding-bottom: 2px;
        }

        .exp-card-link .arrow {
            font-size: 1.1em;
            transition: transform 0.2s ease;
        }

        .exp-card-link:hover .arrow {
            transform: translateX(4px);
        }

        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #0f2d52;
            color: white;
        }

        footer p {
            margin: 0;
            font-size: 0.9em;
        }

        footer a {
            color: #dbaa00;
            text-decoration: none;
            margin: 0 10px;
            font-weight: bold;
        }

        footer a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .slideshow-container {
                margin: 0 20px 0 0;
                height: 350px;
            }

            .intro-container {
                margin: 20px 20px 20px 0;
                padding: 0 15px;
            }

            .intro-container p {
                font-size: 16px;
            }
        }
</style>

<!-- Slideshow Container -->
<div class="slideshow-container">
    <div class="mySlides fade">
        <img alt="Welcome Slide" src="/sites/success.ucmerced.edu/files/page/images/bridge_crossing_170822-12_edit.jpg" />
        <div class="text">Welcome Bobcats to Experiential Learning at UC Merced!</div>
    </div>
    <div class="mySlides fade">
        <img alt="Opportunities Slide" src="/sites/success.ucmerced.edu/files/page/images/little_lake_20220817-2_1-compressed.jpg" />
        <div class="text">Your one-stop shop for: Internships, Study Abroad, Leadership, and more!</div>
    </div>
    <div class="mySlides fade">
        <img alt="Community Engagement Slide" src="/sites/success.ucmerced.edu/files/page/images/screenshot_2024-11-15_at_2.07.46_pm.jpg" />
        <div class="text">Learn more about how to get a Graduation Pin!</div>
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
</script>

<!-- Intro Description Bar -->
<div class="intro-container">
    <p><strong>Experiential learning is a hands-on approach where students gain knowledge and transferable skills by engaging directly in real-world tasks and reflecting on their experiences. This approach enriches academic learning by fostering personal growth, critical thinking, cultural awareness, and professional development.</strong></p>
</div>

<!-- Experience Cards Carousel -->
<div class="carousel-section">
    <div class="carousel-outer">
        <button class="carousel-btn" id="prevBtn" aria-label="Previous">&#8592;</button>
        <button class="carousel-btn" id="nextBtn" aria-label="Next">&#8594;</button>

        <div class="carousel-clip">
            <div class="carousel-wrapper">
                <div class="carousel-track" id="carouselTrack">

            <div class="exp-card">
                <div class="exp-card-inner">
                    <img alt="Study Abroad" src="/sites/success.ucmerced.edu/files/page/images/124138campuslife140225.jpg" />
                    <div class="exp-card-body">
                        <h3>Study Abroad</h3>
                        <p>Studying abroad offers students the chance to pursue their education through an international perspective, providing an immersive experience in different cultural and academic environments.</p>
                        <a href="https://studyabroad.ucmerced.edu/" class="exp-card-link"><span class="link-text">Learn More</span> <span class="arrow">&#8594;</span></a>
                    </div>
                </div>
            </div>

            <div class="exp-card">
                <div class="exp-card-inner">
                    <img alt="Community Service" src="/sites/success.ucmerced.edu/files/page/images/ucm_day1-177_1.jpg" />
                    <div class="exp-card-body">
                        <h3>Community Service</h3>
                        <p>Community Service allows students to contribute time and effort to benefit others, impact the community, and cultivate skills and personal growth through various avenues.</p>
                        <a href="https://cec.ucmerced.edu/" class="exp-card-link"><span class="link-text">Learn More</span> <span class="arrow">&#8594;</span></a>
                    </div>
                </div>
            </div>

            <div class="exp-card">
                <div class="exp-card-inner">
                    <img alt="Undergraduate Research" src="/sites/success.ucmerced.edu/files/page/images/054zhukovacampus.jpg" />
                    <div class="exp-card-body">
                        <h3>Undergraduate Research</h3>
                        <p>Undergraduate research offers students the chance to engage in hands-on research experiences across various disciplines, participating in summer research programs, and more.</p>
                        <a href="https://uroc.ucmerced.edu/" class="exp-card-link"><span class="link-text">Learn More</span> <span class="arrow">&#8594;</span></a>
                    </div>
                </div>
            </div>

            <div class="exp-card">
                <div class="exp-card-inner">
                    <img alt="Leadership" src="/sites/success.ucmerced.edu/files/page/images/dsc_0556_1_1.jpg" />
                    <div class="exp-card-body">
                        <h3>Leadership</h3>
                        <p>Leadership involves engaging in activities that guide, inspire, and influence others toward achieving common goals. UC Merced students can take on leadership positions in student clubs and organizations.</p>
                        <a href="https://studentleadership.ucmerced.edu/leadership" class="exp-card-link"><span class="link-text">Learn More</span> <span class="arrow">&#8594;</span></a>
                    </div>
                </div>
            </div>

            <div class="exp-card">
                <div class="exp-card-inner">
                    <img alt="Internships" src="/sites/success.ucmerced.edu/files/page/images/machineshop_04_2014_1.jpg" />
                    <div class="exp-card-body">
                        <h3>Internships</h3>
                        <p>An internship is a structured work experience, whether paid or unpaid, that takes students&#39; knowledge beyond the classroom to industry while building their network.</p>
                        <a href="https://hire.ucmerced.edu/students/jobs-internships" class="exp-card-link"><span class="link-text">Learn More</span> <span class="arrow">&#8594;</span></a>
                    </div>
                </div>
            </div>

        </div>
    </div><!-- end wrapper -->
    </div><!-- end clip -->
    </div><!-- end outer -->
</div><!-- end carousel-section -->

<script>
    (function () {
        const track = document.getElementById('carouselTrack');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');

        const realCards = Array.from(track.querySelectorAll('.exp-card'));
        const realCount = realCards.length;

        const vis = window.innerWidth <= 768 ? 1 : 3;

        // Clone for infinite loop
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
</script>


<!-- Experiential Learning Pin Section -->
<div class="pin-section">
    <div class="pin-container">

        <div class="pin-header">
            <h2 class="pin-title">Experiential Learning Recognition Pin</h2>
            <p class="pin-subtitle">For Graduating Undergraduate Students</p>
        </div>

        <div class="pin-body">
            <div class="pin-description">
                <p>Graduating undergraduate students who have participated in study abroad, community service, leadership, internship and/or undergraduate research experience will be eligible for an Experiential Learning pin. You can apply for one or more recognitions by completing the Experiential Learning Recognition Request Form. Note that you can complete one form for multiple recognitions.</p>
                <p>You must complete this form no later than <strong>December 1, 2025</strong> to be eligible to receive your pin during allotted pick up times prior to commencement. Pickup locations and times will be emailed once students are approved for a pin.</p>
                <a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_6s4Yl0YHxvJJdJQ" class="pin-cta" target="_blank">
                    Experiential Learning Recognition Request Form <span class="pin-cta-arrow">&#8594;</span>
                </a>
            </div>

            <div class="pin-right">
                <h3 class="pin-criteria-heading">Pin Criteria</h3>
                <div class="pin-accordions">

            <!-- Study Abroad -->
            <div class="pin-accordion">
                <button class="pin-accordion-btn" aria-expanded="false">
                    <span>Study Abroad</span>
                    <span class="pin-chevron">&#43;</span>
                </button>
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

            <!-- Community Service -->
            <div class="pin-accordion">
                <button class="pin-accordion-btn" aria-expanded="false">
                    <span>Community Service</span>
                    <span class="pin-chevron">&#43;</span>
                </button>
                <div class="pin-accordion-body">
                    <p>Participation in one of the following:</p>
                    <ul>
                        <li>Community Engagement Center-related activity</li>
                        <li>Student club or organization related service project</li>
                        <li>Course-related service or service-learning</li>
                        <li>Self-directed independent service (i.e. project of your choice and making)</li>
                        <li>Other -- the form will ask you to describe your experience</li>
                    </ul>
                    <p class="pin-contact">For questions, contact <a href="mailto:pricillacardenas@ucmerced.edu">Pricilla Cardenas</a></p>
                </div>
            </div>

            <!-- Leadership -->
            <div class="pin-accordion">
                <button class="pin-accordion-btn" aria-expanded="false">
                    <span>Leadership</span>
                    <span class="pin-chevron">&#43;</span>
                </button>
                <div class="pin-accordion-body">
                    <p>Participation in one of the following:</p>
                    <ul>
                        <li>Yosemite Leadership Program</li>
                        <li>Bobcat Leadership Seminar</li>
                        <li>Associated Students of UC Merced (ASUCM)</li>
                        <li>Campus Activities Board (CAB)</li>
                        <li>Registered Student Club or Organization Officer or Leadership Position</li>
                        <li>Other -- the form will ask you to describe your experience</li>
                    </ul>
                    <p class="pin-contact">For questions, contact <a href="mailto:sbarrera7@ucmerced.edu">Stephany Barrera</a></p>
                </div>
            </div>

            <!-- Internship -->
            <div class="pin-accordion">
                <button class="pin-accordion-btn" aria-expanded="false">
                    <span>Internship</span>
                    <span class="pin-chevron">&#43;</span>
                </button>
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

            <!-- Undergraduate Research -->
            <div class="pin-accordion">
                <button class="pin-accordion-btn" aria-expanded="false">
                    <span>Undergraduate Research</span>
                    <span class="pin-chevron">&#43;</span>
                </button>
                <div class="pin-accordion-body">
                    <p>Participation in a research or creative project(s) outside of regular course requirements. The form will ask you to identify the following for each experience:</p>
                    <ul>
                        <li>When you completed the experience(s) and the approximate number of hours</li>
                        <li>Faculty mentor</li>
                    </ul>
                    <p class="pin-contact">For questions, contact <a href="mailto:patriciasotobecerr@ucmerced.edu">Patricia Soto Becerra</a></p>
                </div>
            </div>

        </div><!-- end accordions -->
            </div><!-- end pin-right -->
        </div><!-- end pin-body -->
    </div><!-- end container -->
</div><!-- end pin section -->

<style>
    .pin-section {
        padding: 50px 0 70px;
        margin-top: 10px;
    }

    /* The decorated card container */
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

    /* Centered header */
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

    /* Two-column layout: description left, accordions right */
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

    .pin-description p:last-of-type {
        margin-bottom: 24px;
    }

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

    .pin-cta-arrow {
        transition: transform 0.2s ease;
    }

    .pin-cta:hover .pin-cta-arrow {
        transform: translateX(4px);
    }

    /* Right column: criteria heading + accordions */
    .pin-right {
        display: flex;
        flex-direction: column;
    }

    .pin-criteria-heading {
        font-size: 0.78em;
        font-weight: 700;
        color: #0f2d52;
        margin: 0 0 14px;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* Accordions */
    .pin-accordions {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .pin-accordion {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e5e5e5;
        background-color: #ffffff;
        transition: box-shadow 0.2s ease;
    }

    .pin-accordion:hover {
        box-shadow: 0 4px 14px rgba(219, 170, 0, 0.18);
    }

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

    .pin-accordion-btn:hover {
        background-color: #f5f8fb;
    }

    .pin-accordion-btn[aria-expanded="true"] {
        background-color: #0f2d52;
        color: #ffffff;
    }

    .pin-accordion-btn[aria-expanded="true"] .pin-chevron {
        color: #dbaa00;
        transform: rotate(45deg);
    }

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

    .pin-accordion-body p {
        font-size: 0.93em;
        line-height: 1.6;
        color: #333;
        margin: 0 0 8px;
    }

    .pin-accordion-body ul {
        margin: 0 0 12px 16px;
        padding: 0;
    }

    .pin-accordion-body ul li {
        font-size: 0.93em;
        line-height: 1.6;
        color: #333;
        margin-bottom: 3px;
    }

    .pin-contact {
        margin-top: 12px !important;
        font-size: 0.9em !important;
        color: #666 !important;
        padding-top: 12px;
        border-top: 1px solid #eee;
    }

    .pin-contact a,
    .pin-contact a:link,
    .pin-contact a:visited {
        color: #0f2d52;
        font-weight: 700;
        text-decoration: none;
        border-bottom: 1px solid #dbaa00;
        padding-bottom: 1px;
    }

    .pin-contact a:hover { color: #dbaa00; }

    @media (max-width: 900px) {
        .pin-body {
            grid-template-columns: 1fr;
            gap: 36px;
        }
    }

    @media (max-width: 768px) {
        .pin-container {
            margin: 0 20px 0 0;
            padding: 30px 24px 40px;
            border-radius: 16px;
        }

        .pin-title {
            font-size: 1.5em;
        }
    }
</style>

<script>
    document.querySelectorAll('.pin-accordion-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const expanded = btn.getAttribute('aria-expanded') === 'true';
            const body = btn.nextElementSibling;

            // Close all others
            document.querySelectorAll('.pin-accordion-btn').forEach(b => {
                b.setAttribute('aria-expanded', 'false');
                b.nextElementSibling.style.display = 'none';
            });

            // Toggle this one
            if (!expanded) {
                btn.setAttribute('aria-expanded', 'true');
                body.style.display = 'block';
            }
        });
    });
</script>

<footer>
    <p>UC Merced Experiential Learning &copy; 2024</p>
</footer>