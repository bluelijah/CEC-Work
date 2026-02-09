<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">/* Event Slider Styles */
        .cec-event-slider-wrapper {
            position: relative;
            width: 100%;
            overflow: hidden;
            border-radius: 0;
            box-shadow: none;
            margin: 0;
        }

        .cec-event-slider-track {
            display: flex;
            gap: 15px;
            width: fit-content;
        }

        .cec-event-slide {
            flex-shrink: 0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 10px;
            position: relative;
        }

        .cec-event-slide:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }

        /* Overlay for event titles (optional) */
        .cec-event-overlay {
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

        .cec-event-slide:hover .cec-event-overlay {
            opacity: 1;
        }

        .cec-event-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0;
        }

        .cec-event-date {
            font-size: 1rem;
            margin: 5px 0 0 0;
        }

        @keyframes cec-event-slide {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-50%);
            }
        }

        /* Mobile Responsiveness - use original image sizes below 768px */
        @media (max-width: 768px) {
            .cec-event-slider-wrapper {
                border-radius: 0;
            }
            
            .cec-event-title {
                font-size: 1.2rem;
            }
            
            .cec-event-date {
                font-size: 0.9rem;
            }
        }

        /* Demo container - remove this in production */
        .demo-container {
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
</style>
<div class="demo-container"><!-- Event Slider -->
	<div class="cec-event-slider-wrapper">
		<div class="cec-event-slider-track" id="cecEventTrack"><!-- Event 1 -->
			<div class="cec-event-slide cec-original-slide" data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/maxsize.png" data-link="https://cec.ucmerced.edu/event1">
				<div class="cec-event-overlay">
					<h3 class="cec-event-title">Welcome to the Community Service Center</h3>

					<p class="cec-event-date">&nbsp;</p>
				</div>
			</div>
			<!-- Event 2 -->

			<div class="cec-event-slide cec-original-slide" data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/studentcollab.png" data-link="https://cec.ucmerced.edu/event2">
				<div class="cec-event-overlay">
					<h3 class="cec-event-title">Student Collaborations</h3>

					<p class="cec-event-date">&nbsp;</p>
				</div>
			</div>
			<!-- Event 3 -->

			<div class="cec-event-slide cec-original-slide" data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/bybfsessionspano.png" data-link="https://cec.ucmerced.edu/calendar/long-term-service/best-you-best-future-program">
				<div class="cec-event-overlay">
					<h3 class="cec-event-title">Upcoming BYBF Training and Info Sessions</h3>

					<p class="cec-event-date">&nbsp;</p>
				</div>
			</div>
			<!-- Event 4 -->

			<div class="cec-event-slide cec-original-slide" data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/lwylsessionspano.png" data-link="https://cec.ucmerced.edu/lift-while-you-lead">
				<div class="cec-event-overlay">
					<h3 class="cec-event-title">Upcoming BYBF Training and Info Sessions</h3>

					<p class="cec-event-date">&nbsp;</p>
				</div>
			</div>
			<!-- Event 5 -->

			<div class="cec-event-slide cec-original-slide" data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/speech_and_debate_judging_banner.png" data-link="https://cec.ucmerced.edu/events/judging-yosemite-forensic-league">
				<div class="cec-event-overlay">
					<h3 class="cec-event-title">Upcoming BYBF Training and Info Sessions</h3>

					<p class="cec-event-date">&nbsp;</p>
				</div>
			</div>
		</div>
	</div>
</div>
<script>
        (function() {
            const track = document.getElementById('cecEventTrack');
            const wrapper = document.querySelector('.cec-event-slider-wrapper');
            const originalSlides = document.querySelectorAll('.cec-original-slide');
            const isMobile = window.innerWidth <= 768;
            const timePerSlide = 8; // seconds per slide (increased from 5)
            
            let imagesLoaded = 0;
            let minHeight = Infinity;
            const imageData = [];

            // Load all images and find minimum height
            originalSlides.forEach((slide, index) => {
                const img = new Image();
                const imageSrc = slide.getAttribute('data-image');
                
                img.onload = function() {
                    const aspectRatio = img.width / img.height;
                    imageData[index] = {
                        aspectRatio: aspectRatio,
                        naturalWidth: img.width,
                        naturalHeight: img.height
                    };
                    
                    // Calculate what height this image would be if fit to viewport
                    // For desktop, we'll use a max width calculation
                    if (!isMobile) {
                        const calculatedHeight = img.height;
                        if (calculatedHeight < minHeight) {
                            minHeight = calculatedHeight;
                        }
                    }
                    
                    imagesLoaded++;
                    
                    if (imagesLoaded === originalSlides.length) {
                        setupSlider();
                    }
                };
                
                img.src = imageSrc;
            });

            function setupSlider() {
                // Set wrapper height - reduced to show multiple slides at once
                const targetHeight = isMobile ? 200 : 300; // Reduced from minHeight calculation
                
                wrapper.style.height = targetHeight + 'px';

                // Calculate total width needed for all original slides
                let totalWidth = 0;

                // Set each slide's dimensions and background
                originalSlides.forEach((slide, index) => {
                    const data = imageData[index];
                    const imageSrc = slide.getAttribute('data-image');
                    
                    slide.style.backgroundImage = `url('${imageSrc}')`;
                    slide.style.backgroundSize = 'cover';
                    slide.style.backgroundPosition = 'center';
                    
                    // Calculate width based on aspect ratio and target height
                    const width = Math.round(targetHeight * data.aspectRatio);
                    slide.style.height = targetHeight + 'px';
                    slide.style.width = width + 'px';
                    totalWidth += width;
                });

                // Add gap widths to total (15px gap between each slide)
                totalWidth += (originalSlides.length - 1) * 15;

                // Duplicate slides for seamless loop
                originalSlides.forEach(slide => {
                    const clone = slide.cloneNode(true);
                    clone.classList.remove('cec-original-slide');
                    clone.style.backgroundSize = 'cover';
                    clone.style.backgroundPosition = 'center';
                    
                    // Add click handler to clone
                    const link = slide.getAttribute('data-link');
                    clone.onclick = function() {
                        window.location.href = link;
                    };
                    
                    track.appendChild(clone);
                });

                // Add click handlers to original slides
                originalSlides.forEach(slide => {
                    const link = slide.getAttribute('data-link');
                    slide.onclick = function() {
                        window.location.href = link;
                    };
                });

                // Calculate animation duration based on slide count
                const slideCount = originalSlides.length;
                const animationDuration = slideCount * timePerSlide;
                
                // Set animation with calculated duration
                track.style.animation = `cec-event-slide ${animationDuration}s linear infinite`;
                
                // Calculate the translation distance (exactly 50% since we duplicated)
                // This ensures all slides are fully visible before loop
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes cec-event-slide {
                        0% {
                            transform: translateX(0);
                        }
                        100% {
                            transform: translateX(-${totalWidth + 15}px);
                        }
                    }
                `;
                document.head.appendChild(style);
                
                // Add pause on hover event listeners to all slides
                const allSlides = document.querySelectorAll('.cec-event-slide');
                allSlides.forEach(slide => {
                    slide.addEventListener('mouseenter', function() {
                        track.style.animationPlayState = 'paused';
                    });
                    slide.addEventListener('mouseleave', function() {
                        track.style.animationPlayState = 'running';
                    });
                });
                
                // Also add to wrapper
                wrapper.addEventListener('mouseenter', function() {
                    track.style.animationPlayState = 'paused';
                });
                wrapper.addEventListener('mouseleave', function() {
                    track.style.animationPlayState = 'running';
                });
            }
        })();
    </script>