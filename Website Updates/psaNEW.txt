<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* PSA Page Styles */
.psa-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Image Slider Styles */
.psa-slider-wrapper {
    position: relative;
    width: 100%;
    height: 300px;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0, 40, 86, 0.2);
    margin-bottom: 40px;
}

.psa-slider-track {
    display: flex;
    gap: 15px;
    animation: psa-slide 60s linear infinite;
    width: fit-content;
}

.psa-slide {
    height: 300px;
    width: 400px;
    flex-shrink: 0;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Create multiple slides - add your image names here */
.psa-slide:nth-child(1) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa1.jpg');
}

.psa-slide:nth-child(2) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa2.jpg');
}

.psa-slide:nth-child(3) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa3.jpeg');
}

.psa-slide:nth-child(4) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa4.jpeg');
}
.psa-slide:nth-child(5) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa5.jpg');
}
.psa-slide:nth-child(6) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa6.jpg');
}
.psa-slide:nth-child(7) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa7.jpg');
}
.psa-slide:nth-child(8) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa8.jpeg');
}
.psa-slide:nth-child(9) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa9.jpg');
}
.psa-slide:nth-child(10) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa10.jpg');
}
.psa-slide:nth-child(11) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa11.jpg');
}
.psa-slide:nth-child(12) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa12.jpg');
}

/* Duplicate slides for seamless loop */
.psa-slide:nth-child(13) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa1.jpg');
}
.psa-slide:nth-child(14) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa2.jpg');
}
.psa-slide:nth-child(15) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa3.jpeg');
}
.psa-slide:nth-child(16) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa4.jpeg');
}
.psa-slide:nth-child(17) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa5.jpg');
}
.psa-slide:nth-child(18) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa6.jpg');
}
.psa-slide:nth-child(19) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa7.jpg');
}
.psa-slide:nth-child(20) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa8.jpeg');
}
.psa-slide:nth-child(21) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa9.jpg');
}
.psa-slide:nth-child(22) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa10.jpg');
}
.psa-slide:nth-child(23) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa11.jpg');
}
.psa-slide:nth-child(24) {
    background-image: url('/sites/cec.ucmerced.edu/files/images/psa/psa12.jpg');
}

@keyframes psa-slide {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(-50%);
    }
}

/* Header Styles */
.psa-headline {
    text-align: center;
    border-bottom: 3px solid #ffbf3c;
    padding-bottom: 10px;
    margin: 30px 0 20px;
    font-size: 2rem;
    color: #002856;
}

/* Content Box Styles */
.psa-info-box {
    background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
    border: 3px solid #002856;
    border-radius: 15px;
    padding: 30px;
    margin: 25px 0;
    box-shadow: 0 4px 15px rgba(0, 40, 86, 0.15);
}

.psa-info-box p {
    line-height: 1.8;
    color: #333;
    font-size: 1.1rem;
    margin-bottom: 15px;
}

/* Highlighted Info */
.psa-highlight {
    background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
    color: #002856;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 1.2rem;
    font-weight: bold;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(255, 191, 60, 0.3);
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .psa-container {
        padding: 10px;
        margin-left: 0;
        margin-right: 20px;
    }
    
    .psa-slider-wrapper {
        height: 200px;
        margin-left: -10px;
        margin-right: 0;
        border-radius: 0;
    }
    
    .psa-slide {
        height: 200px;
        width: 300px;
    }
    
    .psa-headline {
        font-size: 1.5rem;
    }
    
    .psa-info-box {
        padding: 20px;
    }
}
</style>
<div class="psa-container"><!-- Continuous Image Slider -->
	<div class="psa-slider-wrapper">
		<div class="psa-slider-track">
			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>

			<div class="psa-slide">&nbsp;</div>
		</div>
	</div>
	<!-- Main Header -->

	<h2 class="psa-headline">Public Service Announcements</h2>
	<!-- Info Box -->

	<div class="psa-info-box">
		<p>Join us for our monthly Public Service Announcements! Whether you&#39;re an individual student, part of a club, or representing an organization, we&#39;re here to help you discover meaningful volunteer opportunities and stay engaged with the community.</p>

		<p>PSA sessions are your gateway to learning about upcoming one-time service events, longer-term programs, and exciting community engagement opportunities across the Central Valley. Each session includes an informational presentation followed by an engaging arts-and-crafts service project.</p>
	</div>
	<!-- Next Event Highlight -->

	<div class="psa-highlight">Next PSA: Wednesday, September 3rd at 5:00 PM<br />
		Location: COB 2 265</div>
	<!-- Additional Info -->

	<div class="psa-info-box">
		<h3 style="color: #002856; text-align: center;">Open to All UC Merced Students</h3>

		<p style="text-align: center;">Whether you&#39;re looking to fulfill service requirements, explore new interests, or make an impact in the community, PSA is the perfect place to start. No prior volunteer experience necessary!</p>
	</div>
</div>
