<style type="text/css">.cec-event-slider-wrapper {
            position: relative;
            width: 100%;
            overflow: hidden;
            border-radius: 0;
            box-shadow: none;
            margin: 0;
            border-left: 5px solid #dbaa00;
            border-right: 5px solid #dbaa00;
        }

        .cec-event-slider-track {
            display: flex;
            gap: 15px;
            width: fit-content;
            will-change: transform;
        }

        .cec-event-slide {
            flex-shrink: 0;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            cursor: pointer;
            border-radius: 10px;
            position: relative;
            transition: box-shadow 0.3s ease;
        }

        .cec-event-slide:hover,
        .cec-event-slide:focus {
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            outline: 3px solid #dbaa00;
            outline-offset: 3px;
        }

        .cec-event-slide:focus .cec-event-overlay {
            opacity: 1;
        }

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

        .cec-slider-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 8px 0 0;
        }

        .cec-ctrl-btn {
            background: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 50%;
            width: 44px;
            height: 44px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #002856;
            transition: background 0.15s;
        }

        .cec-ctrl-btn:hover {
            background: #f0f0f0;
        }

        .cec-ctrl-btn:focus-visible {
            outline: 3px solid #dbaa00;
            outline-offset: 2px;
        }

        .cec-ctrl-btn svg {
            width: 16px;
            height: 16px;
            fill: currentColor;
        }

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

        .demo-container {
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
</style>

<div class="demo-container">
    <div aria-label="Event image slider" aria-roledescription="carousel" class="cec-event-slider-wrapper" id="cecSliderWrapper" role="region">
        <div aria-live="off" class="cec-event-slider-track" id="cecEventTrack">
            <!-- Event 1 -->
            <div class="cec-event-slide cec-original-slide"
                 data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/maxsize.png"
                 data-link="https://cec.ucmerced.edu/event1"
                 role="link"
                 tabindex="0"
                 aria-label="Welcome to the Community Service Center — view event"
                 onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href=this.getAttribute('data-link')">
                <div class="cec-event-overlay">
                    <h3 class="cec-event-title">Welcome to the Community Service Center</h3>
                    <p class="cec-event-date">&nbsp;</p>
                </div>
            </div>
            <!-- Event 2 -->
            <div class="cec-event-slide cec-original-slide"
                 data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/studentcollab.png"
                 data-link="https://cec.ucmerced.edu/event2"
                 role="link"
                 tabindex="0"
                 aria-label="Student Collaborations — view event"
                 onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href=this.getAttribute('data-link')">
                <div class="cec-event-overlay">
                    <h3 class="cec-event-title">Student Collaborations</h3>
                    <p class="cec-event-date">&nbsp;</p>
                </div>
            </div>
            <!-- Event 3 -->
            <div class="cec-event-slide cec-original-slide"
                 data-image="/sites/g/files/ufvvjh561/f/images/panoSlider/earth_week_pano_banner1.png"
                 data-link="https://cec.ucmerced.edu/earth-week-2026"
                 role="link"
                 tabindex="0"
                 aria-label="Earth Week Events, April 11th to 24th — view event"
                 onkeydown="if(event.key==='Enter'||event.key===' ')window.location.href=this.getAttribute('data-link')">
                <div class="cec-event-overlay">
                    <h3 class="cec-event-title">Earth Week Events</h3>
                    <p class="cec-event-date">April 11th-24th</p>
                </div>
            </div>
        </div>
    </div>

    <div aria-label="Slider controls" class="cec-slider-controls" role="group">
        <button aria-label="Previous slide" class="cec-ctrl-btn" id="cecPrev">
            <svg aria-hidden="true" viewbox="0 0 16 16"><path d="M11 2 L5 8 L11 14" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
        </button>
        <button aria-label="Pause animation" aria-pressed="false" class="cec-ctrl-btn" id="cecPausePlay">
            <svg aria-hidden="true" id="cecPauseIcon" viewbox="0 0 16 16"><rect height="12" rx="1" width="4" x="3" y="2"></rect><rect height="12" rx="1" width="4" x="9" y="2"></rect></svg>
            <svg aria-hidden="true" id="cecPlayIcon" style="display:none" viewbox="0 0 16 16"><path d="M4 2 L13 8 L4 14 Z"></path></svg>
        </button>
        <button aria-label="Next slide" class="cec-ctrl-btn" id="cecNext">
            <svg aria-hidden="true" viewbox="0 0 16 16"><path d="M5 2 L11 8 L5 14" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
        </button>
    </div>

    <script>
        (function () {
            const track = document.getElementById('cecEventTrack');
            const wrapper = document.getElementById('cecSliderWrapper');
            const pausePlayBtn = document.getElementById('cecPausePlay');
            const prevBtn = document.getElementById('cecPrev');
            const nextBtn = document.getElementById('cecNext');
            const pauseIcon = document.getElementById('cecPauseIcon');
            const playIcon = document.getElementById('cecPlayIcon');

            const originalSlides = document.querySelectorAll('.cec-original-slide');
            const isMobile = window.innerWidth <= 768;
            const timePerSlide = 8;
            const GAP = 15;

            let userPaused = false;
            let hoverPaused = false;
            let currentOffset = 0;
            let totalWidth = 0;
            let slideWidths = [];
            let rafId = null;
            let lastTimestamp = null;
            let pixelsPerSecond = 0;

            let imagesLoaded = 0;
            const imageData = [];

            originalSlides.forEach((slide, index) => {
                const img = new Image();
                const imageSrc = slide.getAttribute('data-image');

                img.onload = function () {
                    imageData[index] = { aspectRatio: img.width / img.height };
                    imagesLoaded++;
                    if (imagesLoaded === originalSlides.length) setupSlider();
                };

                img.onerror = function () {
                    imageData[index] = { aspectRatio: 16 / 9 };
                    imagesLoaded++;
                    if (imagesLoaded === originalSlides.length) setupSlider();
                };

                img.src = imageSrc;
            });

            function setupSlider() {
                const targetHeight = isMobile ? 200 : 300;
                wrapper.style.height = targetHeight + 'px';

                totalWidth = 0;
                slideWidths = [];

                originalSlides.forEach((slide, index) => {
                    const data = imageData[index];
                    const imageSrc = slide.getAttribute('data-image');

                    slide.style.backgroundImage = `url('${imageSrc}')`;
                    slide.style.backgroundSize = 'cover';
                    slide.style.backgroundPosition = 'center';

                    const width = Math.round(targetHeight * data.aspectRatio);
                    slide.style.height = targetHeight + 'px';
                    slide.style.width = width + 'px';
                    slideWidths.push(width);
                    totalWidth += width;
                });

                totalWidth += (originalSlides.length - 1) * GAP;
                pixelsPerSecond = totalWidth / (originalSlides.length * timePerSlide);

                originalSlides.forEach(slide => {
                    const clone = slide.cloneNode(true);
                    clone.classList.remove('cec-original-slide');
                    clone.setAttribute('aria-hidden', 'true');
                    clone.removeAttribute('tabindex');
                    clone.removeAttribute('role');

                    const link = slide.getAttribute('data-link');
                    clone.onclick = function () { window.location.href = link; };
                    track.appendChild(clone);
                });

                originalSlides.forEach(slide => {
                    const link = slide.getAttribute('data-link');
                    slide.onclick = function () { window.location.href = link; };
                });

                // Pause when a slide receives keyboard focus
                originalSlides.forEach(slide => {
                    slide.addEventListener('focus', () => {
                        hoverPaused = true;
                        applyState();
                    });
                    slide.addEventListener('blur', () => {
                        hoverPaused = false;
                        applyState();
                    });
                });

                startRAF();

                wrapper.addEventListener('mouseenter', () => { hoverPaused = true; applyState(); });
                wrapper.addEventListener('mouseleave', () => { hoverPaused = false; applyState(); });
            }

            function tick(timestamp) {
                if (!lastTimestamp) lastTimestamp = timestamp;
                const delta = timestamp - lastTimestamp;
                lastTimestamp = timestamp;

                currentOffset += pixelsPerSecond * (delta / 1000);
                if (currentOffset >= totalWidth) currentOffset -= totalWidth;

                track.style.transform = `translateX(-${currentOffset}px)`;
                rafId = requestAnimationFrame(tick);
            }

            function startRAF() {
                if (rafId) return;
                lastTimestamp = null;
                rafId = requestAnimationFrame(tick);
            }

            function stopRAF() {
                if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
            }

            function applyState() {
                if (!userPaused && !hoverPaused) startRAF();
                else stopRAF();
            }

            function setPauseUI(paused) {
                pausePlayBtn.setAttribute('aria-label', paused ? 'Play animation' : 'Pause animation');
                pausePlayBtn.setAttribute('aria-pressed', paused ? 'true' : 'false');
                pauseIcon.style.display = paused ? 'none' : '';
                playIcon.style.display = paused ? '' : 'none';
            }

            pausePlayBtn.addEventListener('click', () => {
                userPaused = !userPaused;
                setPauseUI(userPaused);
                applyState();
            });

            function snapToSlide(direction) {
                if (!userPaused) { userPaused = true; setPauseUI(true); }
                stopRAF();

                let accumulated = 0;
                let currentSlideIndex = 0;
                for (let i = 0; i < slideWidths.length; i++) {
                    const mid = accumulated + slideWidths[i] / 2;
                    if (currentOffset <= mid) { currentSlideIndex = i; break; }
                    accumulated += slideWidths[i] + GAP;
                    currentSlideIndex = i;
                }

                let targetIndex = currentSlideIndex + direction;
                if (targetIndex < 0) targetIndex = slideWidths.length - 1;
                if (targetIndex >= slideWidths.length) targetIndex = 0;

                let targetOffset = 0;
                for (let i = 0; i < targetIndex; i++) targetOffset += slideWidths[i] + GAP;

                currentOffset = targetOffset;
                track.style.transition = 'transform 0.4s ease';
                track.style.transform = `translateX(-${targetOffset}px)`;

                track.addEventListener('transitionend', function onDone() {
                    track.style.transition = 'none';
                    track.removeEventListener('transitionend', onDone);
                }, { once: true });
            }

            prevBtn.addEventListener('click', () => snapToSlide(-1));
            nextBtn.addEventListener('click', () => snapToSlide(1));
        })();
    </script>
</div>