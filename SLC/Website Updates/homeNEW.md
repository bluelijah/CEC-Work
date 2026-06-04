<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.slc-mission-container {
    max-width: 1200px;
    margin: 0 20px 0 0;
    padding: 0 20px;
    border-top: 4px solid #dbaa00;
    border-bottom: 4px solid #dbaa00;
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.slc-mission-statement {
    font-size: 18px;
    line-height: 1.5;
    color: #333;
    margin: 0;
    padding: 0;
    text-align: left;
}

.slc-mission-label {
    font-weight: 700;
    color: #003262;
    font-size: 20px;
    font-style: italic;
    line-height: 1.5;
}

.slc-title-line {
    border-bottom: 2px solid #E5E5E5;
    text-align: center;
    padding-bottom: 15px;
    margin-bottom: 40px;
    color: #0f2d52;
}

.slc-block-subtext {
    font-size: 13px;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.85);
    margin: 0;
    letter-spacing: 0.3px;
}

.slc-blocks-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    padding: 20px 0 20px 20px;
    max-width: 1200px;
    margin: 0 0 0 auto;
    margin-right: 30px;
}

.slc-identity-block {
    display: block;
    border-radius: 16px;
    padding: 60px 30px;
    text-align: center;
    color: white;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
    background-size: cover;
    background-position: center;
    text-decoration: none;
}

.slc-identity-block::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(15, 45, 82, 0.65);
    z-index: 0;
    transition: background 0.3s ease;
}

.slc-identity-block::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, #dbaa00 0%, #f0c930 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 1;
}

.slc-identity-block:hover::before,
.slc-identity-block:focus::before {
    opacity: 0.85;
}

.slc-identity-block:hover,
.slc-identity-block:focus {
    transform: translateY(-8px);
    box-shadow: 0 12px 24px rgba(219, 170, 0, 0.3);
    outline: 3px solid #dbaa00;
    outline-offset: 3px;
    cursor: pointer;
}

.slc-programs-block {
    background-image: url('https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/images/programs_background.jpg');
    background-size: 110%;
    background-position: left center;
}

.slc-incentives-block {
    background-image: url('https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/images/incentives_background.jpg');
}

.slc-conferences-block {
    background-image: url('https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/images/conferences_background.jpg');
}

.slc-block-content {
    position: relative;
    z-index: 2;
}

.slc-block-title {
    font-size: 18px;
    font-weight: 400;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
    color: white;
}

.slc-block-subtitle {
    font-size: 32px;
    opacity: 1;
    font-weight: 700;
    color: white;
    margin: 0;
}

@media (max-width: 768px) {
    .slc-blocks-container {
        grid-template-columns: 1fr;
        gap: 20px;
        padding: 20px 20px 10px 10px;
        margin: 0 0 0 auto;
    }

    .slc-identity-block {
        padding: 50px 25px;
    }

    .slc-block-title {
        font-size: 16px;
    }

    .slc-block-subtitle {
        font-size: 28px;
    }

    .slc-title-line {
        font-size: 24px;
        margin-bottom: 30px;
    }

    .slc-mission-container {
        padding: 0 15px;
        height: auto;
        min-height: 120px;
        margin: 0 20px 0 auto;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .slc-mission-statement {
        font-size: 16px;
    }

    .slc-mission-label {
        font-size: 18px;
    }
}

@media (max-width: 480px) {
    .slc-identity-block {
        padding: 40px 20px;
    }

    .slc-block-subtitle {
        font-size: 24px;
    }
}
</style>
<div class="slc-mission-container">
	<p class="slc-mission-statement"><span class="slc-mission-label">Our Mission:</span> The Margo F. Souza Student Leadership Center aims to develop leadership skills, knowledge, capacity, and self-efficacy while also empowering students to thrive as life-long learners and leaders in the 21st century.</p>
</div>

<div class="slc-blocks-container">
	<div aria-label="Programs — go to the Programs page" class="slc-identity-block slc-programs-block" onclick="window.location.href='https://studentleadership.ucmerced.edu/'" onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href='https://studentleadership.ucmerced.edu/'" role="link" tabindex="0"><!-- REPLACE THIS FILEPATH -->
		<div class="slc-block-content">
			<p class="slc-block-title">Explore our</p>

			<p class="slc-block-subtitle">Programs</p>
		</div>
	</div>

	<div aria-label="Incentives — go to the Incentives page" class="slc-identity-block slc-incentives-block" onclick="window.location.href='https://studentleadership.ucmerced.edu/'" onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href='https://studentleadership.ucmerced.edu/'" role="link" tabindex="0"><!-- REPLACE THIS FILEPATH -->
		<div class="slc-block-content">
			<p class="slc-block-title">Explore our</p>

			<p class="slc-block-subtitle">Incentives</p>
		</div>
	</div>

	<div aria-label="Conferences — go to the Conferences page" class="slc-identity-block slc-conferences-block" onclick="window.location.href='https://studentleadership.ucmerced.edu/'" onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href='https://studentleadership.ucmerced.edu/'" role="link" tabindex="0"><!-- REPLACE THIS FILEPATH -->
		<div class="slc-block-content">
			<p class="slc-block-title">Explore our</p>

			<p class="slc-block-subtitle">Conferences</p>
		</div>
	</div>
</div>
