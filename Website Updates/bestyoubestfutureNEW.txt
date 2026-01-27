<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* --- Infinite Scroller --- */
.infinite-slider {
  overflow: hidden;
  width: 100%;
  padding: 0;
  background: transparent;
  margin-bottom: 2rem;
}

.infinite-slider .track {
  display: flex;
  width: max-content;
  gap: 8px;
  animation: scroll-left 35s linear infinite;
  will-change: transform;
}

/* One "card" */
.infinite-slider .slide {
  flex: 0 0 auto;
  width: clamp(220px, 28vw, 360px);
  height: clamp(140px, 18vw, 220px);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,.12);
}

.infinite-slider img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .35s ease;
  transform: scale(1.06);
}

.infinite-slider .slide:hover img {
  transform: scale(1.15);
}

.infinite-slider .slide:nth-child(2) img,
.infinite-slider .slide:nth-child(7) img {
  object-position: center 25%;
}

@keyframes scroll-left {
  to { transform: translateX(-50%); }
}

/* accessibility: respect users who prefer less motion */
@media (prefers-reduced-motion: reduce) {
  .infinite-slider .track { animation: none; }
}

.bybf-page * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.bybf-page {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: #333;
    padding-right: 30px;
}

.bybf-container {
    width: 100%;
    margin: 0 auto;
    padding: 0;
}

.bybf-content-box {
    background: white;
    padding: 2.5rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
}

.bybf-content-box h2 {
    color: #0f2d52;
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
}

.bybf-content-box h3 {
    color: #0f2d52;
    font-size: 1.4rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.bybf-content-box p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-bottom: 1.2rem;
}

.bybf-content-box ul {
    margin-left: 2rem;
    margin-bottom: 1.5rem;
}

.bybf-content-box li {
    font-size: 1.1rem;
    line-height: 1.8;
    color: #555;
    margin-bottom: 0.5rem;
}

.bybf-content-box strong {
    color: #0f2d52;
}

.bybf-highlight-box {
    background: linear-gradient(135deg, #fffbf0 0%, #fff9e6 100%);
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #dbaa00;
    margin-bottom: 1.5rem;
}

.bybf-highlight-box p {
    margin-bottom: 1rem;
}

.bybf-highlight-box p:last-child {
    margin-bottom: 0;
}

.bybf-dropdown {
    margin-bottom: 2rem;
}

.bybf-dropdown-header {
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
}

.bybf-dropdown-subtitle {
    font-size: 0.85rem;
    font-weight: normal;
    text-transform: none;
    margin-top: 0.3rem;
    opacity: 0.9;
}

.bybf-dropdown-header:hover {
    background: linear-gradient(135deg, #dbaa00 0%, #c99a00 100%);
    box-shadow: 0 4px 15px rgba(219, 170, 0, 0.4);
}

.bybf-dropdown-header::after {
    content: ' ▼';
    font-size: 1rem;
    transition: transform 0.3s ease;
    display: inline-block;
    margin-left: 1rem;
}

.bybf-dropdown-header.bybf-active::after {
    transform: rotate(180deg);
}

.bybf-dropdown-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease;
    background: white;
    border: 2px solid #e0e0e0;
    border-top: none;
    border-radius: 0 0 8px 8px;
}

.bybf-dropdown-content.bybf-active {
    max-height: 2000px;
    padding: 1.5rem;
    margin-top: -8px;
    overflow-y: auto;
}

.bybf-session-item {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 8px;
    background: #f9f9f9;
    border-left: 3px solid #dbaa00;
}

.bybf-session-date {
    min-width: 80px;
    text-align: center;
    background: #0f2d52;
    color: white;
    padding: 0.5rem;
    border-radius: 8px;
}

.bybf-session-month {
    font-size: 0.9rem;
    text-transform: uppercase;
}

.bybf-session-day {
    font-size: 1.5rem;
    font-weight: bold;
}

.bybf-session-details h4 {
    color: #0f2d52;
    margin-bottom: 0.5rem;
}

.bybf-session-details p {
    margin: 0;
    font-size: 1rem;
    margin-bottom: 0.3rem;
}

.bybf-session-details a {
    color: #dbaa00;
    font-weight: bold;
    text-decoration: none;
}

.bybf-session-details a:hover {
    color: #0f2d52;
    text-decoration: underline;
}

.bybf-forms-section {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    border-top: 4px solid #dbaa00;
    margin-top: 2rem;
}

.bybf-forms-section h3 {
    color: #0f2d52;
    font-size: 1.4rem;
    margin-bottom: 1rem;
    text-align: center;
}

.bybf-forms-section p {
    color: #555;
    margin-bottom: 1.5rem;
    text-align: center;
}

.bybf-button {
    display: inline-block;
    padding: 1rem 2.5rem;
    background: #0f2d52;
    color: white !important;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.1rem;
    text-transform: uppercase;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(15, 45, 82, 0.4);
    text-align: center;
}

.bybf-button:hover {
    background: #dbaa00;
    color: #0f2d52 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(219, 170, 0, 0.5);
}

.bybf-button-center {
    text-align: center;
    margin-bottom: 1.5rem;
}

@media (max-width: 768px) {
    .bybf-page {
        padding-right: 30px;
    }

    .bybf-content-box {
        padding: 1.5rem;
    }

    .bybf-session-item {
        flex-direction: column;
    }

    .bybf-session-date {
        min-width: auto;
    }
    
    .bybf-button-center {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    .bybf-button {
        margin-left: 0 !important;
    }
}
</style>
<div class="bybf-page">
	<div class="bybf-container"><!-- Image Slider at Top -->
		<div class="infinite-slider">
			<div class="track"><!-- SET A -->
				<div class="slide"><img alt="BYBF 1" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img1.jpeg" /></div>

				<div class="slide"><img alt="BYBF 2" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img2.jpeg" /></div>

				<div class="slide"><img alt="BYBF 3" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img3.jpeg" /></div>

				<div class="slide"><img alt="BYBF 4" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img4.jpeg" /></div>
				<!-- SET B (duplicate for seamless loop) -->

				<div class="slide"><img alt="BYBF 1" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img1.jpeg" /></div>

				<div class="slide"><img alt="BYBF 2" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img2.jpeg" /></div>

				<div class="slide"><img alt="BYBF 3" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img3.jpeg" /></div>

				<div class="slide"><img alt="BYBF 4" src="/sites/g/files/ufvvjh561/f/images/bestyoubestfuture/img4.jpeg" /></div>
			</div>
		</div>

		<div class="bybf-content-box">
			<p>Are you looking for a service opportunity that will allow you to gain experience working with youth while empowering them? If so, Best You, Best Future (BYBF) is the perfect opportunity for you! The Community Engagement Center has partnered with 4 local school districts: Livingston, Weaver, Merced River &amp; Planada to bring their 7th grade students to UC Merced for a personalized tour, lunch and an empowering workshop! The Campus Visits will take place in March and April during a weekday (Monday - Friday) for two and a half hours, volunteers will be able to select which campus visits they can attend once they have completed the BYBF volunteer training.</p>

			<p>We are looking for volunteers who want to make a positive impact in our local youth. Volunteers must attend a training in order to become a BYBF Mentor.</p>

			<div class="bybf-highlight-box">
				<p><strong>By participating in the Best You, Best Future program, you will be eligible for our Community Service Graduation Pin!</strong> Full participation must be completed for the Community Service Graduation Pin, which is a semester-long commitment.</p>
			</div>
		</div>

		<div class="bybf-content-box">
			<div class="bybf-dropdown">
				<div class="bybf-dropdown-header" onclick="toggleBybfDropdown()">Upcoming Info Sessions and Training</div>
				<!-- INFO SESSION 1 -->

				<div class="bybf-dropdown-content" id="bybfSessionsDropdown">
					<div class="bybf-session-item">
						<div class="bybf-session-date">
							<div class="bybf-session-month">January</div>

							<div class="bybf-session-day">30th</div>
						</div>

						<div class="bybf-session-details">
							<h4>Info Session - Friday</h4>

							<p>11:00 AM via Zoom</p>

							<p>Zoom ID: 931 494 5028</p>
						</div>
					</div>
				</div>
				<!-- INFO SESSION 2 -->

				<div class="bybf-dropdown-content" id="bybfSessionsDropdown">
					<div class="bybf-session-item">
						<div class="bybf-session-date">
							<div class="bybf-session-month">January</div>

							<div class="bybf-session-day">30</div>
						</div>

						<div class="bybf-session-details">
							<h4>Info Session - Friday</h4>

							<p>12:00 PM via Zoom</p>

							<p>Zoom ID: 931 494 5028</p>
						</div>
					</div>
				</div>
				<!-- TRAINING SESSION 1 -->

				<div class="bybf-dropdown-content" id="bybfSessionsDropdown">
					<div class="bybf-session-item">
						<div class="bybf-session-date">
							<div class="bybf-session-month">February</div>

							<div class="bybf-session-day">6</div>
						</div>

						<div class="bybf-session-details">
							<h4>Training Session - Friday</h4>

							<p>11:00 AM InPerson</p>

							<p>Location: Granite Pass 115</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="bybf-forms-section">
		<h3>Required Service Forms and Registration</h3>

		<p>You must complete these required service forms to participate in the program, and register below.</p>

		<div class="bybf-button-center"><a class="bybf-button" href="https://cec.ucmerced.edu/required-service-forms">Complete Forms</a> <a class="bybf-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_9FCg5RH6AJOQ3f8" style="margin-left: 1rem;">Register</a></div>
	</div>
</div>
<script>
function toggleBybfDropdown() {
    const header = document.querySelector('.bybf-dropdown-header');
    const dropdowns = document.querySelectorAll('.bybf-dropdown-content');
    header.classList.toggle('bybf-active');
    dropdowns.forEach(dropdown => {
        dropdown.classList.toggle('bybf-active');
    });
}
</script>