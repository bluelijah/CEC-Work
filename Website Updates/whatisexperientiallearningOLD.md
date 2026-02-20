<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">/* Slideshow Styles */
        .slideshow-container {
            position: relative;
            max-width: 1200px;
            height: 500px; /* Increased height for a bigger rectangle */
            margin: 20px auto;
            background-color: #f2c300;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border: 4px solid #00274d;
        }

        .mySlides {
            display: none;
            position: relative;
            height: 100%; /* Ensures the images fill the container vertically */
        }

        .mySlides img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* Ensures images maintain their aspect ratio and cover the area */
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
            color: #00274d;
            font-size: 20px;
            font-weight: bold;
            padding: 15px;
            position: absolute;
            bottom: 0;
            width: 100%;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.8);
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.3);
        }

        /* General Page Styles */
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
            color: #00274d;
        }

        .container {
            width: 85%;
            max-width: 1200px;
            margin: 20px auto;
            padding: 15px 5px;
        }

        header {
            margin-bottom: 15px;
        }

        header p {
            color: #333;
            line-height: 1.5;
            font-size: 1.2em;
            margin: 0;
        }

        .experiences {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 10px;
            justify-content: center;
        }

        .experience {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            margin: 0;
            border: 2px solid #00274d;
        }

        .experience img {
            width: 100%;
            height: 230px;
            object-fit: cover;
            border-bottom: 4px solid #00274d;
        }

        .experience-content {
            padding: 8px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .experience-content h3 {
            margin-top: 0;
            margin-bottom: 8px;
            color: #00274d;
            font-size: 1.2em;
        }

        .experience-content p {
            flex-grow: 1;
            margin: 8px 0;
            font-size: 1em;
            line-height: 1.4;
            color: #333;
        }

        .experience-content a {
            display: inline-block;
            padding: 6px 10px;
            background-color: #f2c300;
            color: #00274d;
            text-decoration: none;
            font-weight: bold;
            border-radius: 4px;
            text-align: center;
            border: 2px solid #00274d;
            transition: background-color 0.3s ease, color 0.3s ease;
            margin-top: 8px;
        }

        .experience-content a:hover {
            background-color: #00274d;
            color: #ffffff;
        }

        .experience:hover {
            transform: translateY(-3px);
        }

        footer {
            text-align: center;
            margin-top: 15px;
            padding: 10px 0;
            background-color: #00274d;
            color: white;
        }

        footer p {
            margin: 0;
            font-size: 0.9em;
        }

        footer a {
            color: #f2c300;
            text-decoration: none;
            margin: 0 10px;
            font-weight: bold;
        }

        footer a:hover {
            text-decoration: underline;
        }
</style>
<!-- Slideshow Container -->
<div class="slideshow-container">
	<div class="mySlides fade"><img alt="Welcome Slide" src="/sites/success.ucmerced.edu/files/page/images/bridge_crossing_170822-12_edit.jpg" />
		<div class="text">Welcome Bobcats to Experiential Learning at UC Merced!</div>
	</div>

	<div class="mySlides fade"><img alt="Opportunities Slide" src="/sites/success.ucmerced.edu/files/page/images/little_lake_20220817-2_1-compressed.jpg" />
		<div class="text">Your one-stop shop for: Internships, Study Abroad, Leadership, and more!</div>
	</div>

	<div class="mySlides fade"><img alt="Community Engagement Slide" src="/sites/success.ucmerced.edu/files/page/images/screenshot_2024-11-15_at_2.07.46_pm.jpg" />
		<div class="text">Learn more about how to get a Graduation Pin!</div>
	</div>
</div>
<script>
    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides");

        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1 }

        slides[slideIndex - 1].style.display = "block";
        setTimeout(showSlides, 6000); // Change image every 6 seconds
    }
</script>

<div class="container">
	<header>
		<p><strong>Experiential learning is a hands-on approach where students gain knowledge and transferable skills by engaging directly in real-world tasks and reflecting on their experiences. This approach enriches academic learning by fostering personal growth, critical thinking, cultural awareness, and professional development.</strong></p>
	</header>

	<div class="experiences">
		<div class="experience"><img alt="Study Abroad" src="/sites/success.ucmerced.edu/files/page/images/124138campuslife140225.jpg" />
			<div class="experience-content">
				<h3>Study Abroad</h3>

				<p>Studying abroad offers students the chance to pursue their education through an international perspective, providing an immersive experience in different cultural and academic environments.</p>
				<a href="https://studyabroad.ucmerced.edu/">Learn More</a></div>
		</div>

		<div class="experience"><img alt="Leadership" src="/sites/success.ucmerced.edu/files/page/images/dsc_0556_1_1.jpg" />
			<div class="experience-content">
				<h3>Leadership</h3>

				<p>Leadership involves engaging in activities that guide, inspire, and influence others toward achieving common goals. UC Merced students can take on leadership positions in student clubs and organizations.</p>
				<a href="https://studentleadership.ucmerced.edu/leadership">Learn More</a></div>
		</div>

		<div class="experience"><img alt="Community Service" src="/sites/success.ucmerced.edu/files/page/images/ucm_day1-177_1.jpg" />
			<div class="experience-content">
				<h3>Community Service</h3>

				<p>Community Service allows students to contribute time and effort to benefit others, impact the community, and cultivate skills and personal growth through various avenues.</p>
				<a href="https://cec.ucmerced.edu/">Learn More</a></div>
		</div>

		<div class="experience"><img alt="Undergraduate Research" src="/sites/success.ucmerced.edu/files/page/images/054zhukovacampus.jpg" />
			<div class="experience-content">
				<h3>Undergraduate Research</h3>

				<p>Undergraduate research offers students the chance to engage in hands-on research experiences across various disciplines, participating in summer research programs, and more.</p>
				<a href="https://uroc.ucmerced.edu/">Learn More</a></div>
		</div>

		<div class="experience"><img alt="Internships" src="/sites/success.ucmerced.edu/files/page/images/machineshop_04_2014_1.jpg" />
			<div class="experience-content">
				<h3>Internships</h3>

				<p>An internship is a structured work experience, whether paid or unpaid, that takes students&#39; knowledge beyond the classroom to industry while building their network.</p>
				<a href="https://hire.ucmerced.edu/students/jobs-internships">Learn More</a></div>
		</div>
	</div>
</div>

<footer>
	<p>UC Merced Experiential Learning &copy; 2024</p>
</footer>
