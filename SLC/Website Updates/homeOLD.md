<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">/* Leadership Event Slider */
.leadership-slider-wrapper {
    position: relative;
    width: 100%;
    overflow: hidden;
}

.leadership-slider-track {
    display: flex;
    gap: 15px;
    width: fit-content;
}

.leadership-slide {
    flex-shrink: 0;
    background-size: contain; /* keep full image */
    background-position: center;
    background-repeat: no-repeat;
    background-color: transparent; /* FIX: removed black */
    cursor: pointer;
    transition: transform 0.10s ease, box-shadow 0.10s ease;
    border-radius: 10px;
    position: relative;
}

.leadership-slide:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

.leadership-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(0, 40, 86, 0.9), transparent);
    color: white;
    padding: 20px;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.leadership-slide:hover .leadership-overlay {
    opacity: 1;
}

.leadership-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0;
}

@media (max-width: 768px) {
    .leadership-title {
        font-size: 1.2rem;
    }
}
</style>
<div class="leadership-slider-wrapper">
	<div class="leadership-slider-track" id="leadershipTrack"><!-- Welcome -->
		<div class="leadership-slide" data-image="https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/page/images/leadership_pano_slides_4_1.png" data-link="https://studentleadership.ucmerced.edu/home">
			<div class="leadership-overlay">
				<h3 class="leadership-title">Welcome</h3>
			</div>
		</div>
		<!-- Bobcat Day -->

		<div class="leadership-slide" data-image="https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/page/images/3_12_2.png" data-link="https://studentleadership.ucmerced.edu/bobactday2026">
			<div class="leadership-overlay">
				<h3 class="leadership-title">Bobcat Day Schedule</h3>
			</div>
		</div>
		<!-- Mailing List -->

		<div class="leadership-slide" data-image="https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/page/images/2_14.png" data-link="https://studentleadership.ucmerced.edu/mailing-list">
			<div class="leadership-overlay">
				<h3 class="leadership-title">Join Our Mailing List</h3>
			</div>
		</div>
		<!-- YLP -->

		<div class="leadership-slide" data-image="https://studentleadership.ucmerced.edu/sites/g/files/ufvvjh1756/f/page/images/1_13_1.png" data-link="https://studentleadership.ucmerced.edu/YLPSI">
			<div class="leadership-overlay">
				<h3 class="leadership-title">YLP</h3>
			</div>
		</div>
	</div>
</div>
<script>
(function () {
    const track = document.getElementById('leadershipTrack');
    const wrapper = document.querySelector('.leadership-slider-wrapper');
    const slides = document.querySelectorAll('.leadership-slide');

    const isMobile = window.innerWidth <= 768;
    const targetHeight = isMobile ? 200 : 300;
    const timePerSlide = 30;

    wrapper.style.height = targetHeight + 'px';

    let totalWidth = 0;

    slides.forEach(slide => {
        const imageSrc = slide.getAttribute('data-image');
        const link = slide.getAttribute('data-link');

        slide.style.backgroundImage = `url('${imageSrc}')`;
        slide.style.height = targetHeight + 'px';

        const width = isMobile ? targetHeight * 1.6 : targetHeight * 1.8;
        slide.style.width = width + 'px';

        totalWidth += width;

        slide.onclick = function () {
            window.location.href = link;
        };
    });

    totalWidth += (slides.length - 1) * 15;

    slides.forEach(slide => {
        const clone = slide.cloneNode(true);
        track.appendChild(clone);
    });

    const animationDuration = slides.length * timePerSlide;

    const style = document.createElement('style');
    style.textContent = `
        @keyframes leadership-scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-${totalWidth}px); }
        }
    `;
    document.head.appendChild(style);

    track.style.animation = `leadership-scroll ${animationDuration}s linear infinite`;

    wrapper.addEventListener('mouseenter', () => {
        track.style.animationPlayState = 'paused';
    });

    wrapper.addEventListener('mouseleave', () => {
        track.style.animationPlayState = 'running';
    });
})();
</script>

<h3 style="text-align: center;"><strong><em>Our Mission: The Margo F. Souza Student Leadership Center aims to develop leadership skills, knowledge, capacity, and self-efficacy while also empowering students to thrive as life-long learners and leaders in the 21st century. </em></strong></h3>

<p style="text-align: center;"><img alt="" src="/sites/studentleadership.ucmerced.edu/files/documents/ccpa_line.png" style="width: 100%; height: 100%;" /></p>

<h3 style="text-align: center;">Explore our featured leadership programs &amp; opportunities.</h3>

<p style="text-align: center;">Sign up using our <a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_0pMBHiT8pEBGyUe">interest form</a> to be one of the first to be notified when leadership programs open!</p>
