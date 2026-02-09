<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Awards</title>
    <style>
        .awards-page-wrapper {
            font-family: Arial, sans-serif;
            margin: 0;
            color: #333;
        }

        .awards-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .awards-main-title {
            color: #0f2d52;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        .awards-intro-text {
            text-align: center;
            max-width: 1200px;
            margin: 0 auto 40px;
            line-height: 1.6;
            color: #666;
            padding: 0 20px;
        }

        /* grid holds cards */
        .awards-grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 40px;
            align-items: stretch;
        }

        /* single card */
        .award-card-link {
            display: flex;
            padding: 30px;
            flex-direction: column;
            justify-content: flex-start;
            background: linear-gradient(135deg, #4A90E2 0%, #0f2d52 100%);
            border-radius: 12px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            position: relative;
            overflow: hidden;
            min-height: 320px;
            border: 3px solid #dbaa00;
        }

        .award-card-overlay {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(180deg, #dbaa00 0%, rgba(255,255,255,0) 20%);
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
            z-index: 1;
        }

        .award-card-link:hover .award-card-overlay {
            opacity: 20;
        }

        .award-card-link:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 25px #dbaa00;
            border-color: #dbaa00;
        }

        .award-trophy-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 15px;
            position: relative;
            z-index: 2;
        }

        .award-trophy-icon img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            filter: brightness(0) saturate(100%) invert(84%) sepia(26%) saturate(1426%) hue-rotate(1deg) brightness(104%) contrast(101%);
            position: relative;
            z-index: 2;
        }

        .award-card-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 15px;
            position: relative;
            z-index: 2;
        }

        .award-card-description {
            font-size: 0.95rem;
            line-height: 1.5;
            opacity: 0.9;
            position: relative;
            z-index: 2;
            text-align: center;
            margin-bottom: auto; /* push Learn More to bottom */
        }

        .award-card-cta {
            margin-top: 20px;
            padding: 10px 20px;
            background: rgba(255,215,0,0.3);
            border: 2px solid #dbaa00;
            border-radius: 6px;
            display: inline-block;
            font-weight: bold;
            transition: all 0.3s ease;
            position: relative;
            z-index: 2;
            color: white;
            text-decoration: none;
        }

        .award-card-cta:hover {
            background: #dbaa00;
            color: #003262;
        }

        @media (max-width: 768px) {
            .awards-page-wrapper {
                margin-right: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="awards-page-wrapper">
        <div class="awards-container">
            <p class="awards-intro-text">The Community Engagement Center is proud to recognize students who demonstrate exceptional commitment to service, leadership, and community impact. Explore our awards below to find the recognition that matches your dedication and achievements.</p>

            <div class="awards-grid-container">
                <!-- Card 1 -->
                <div class="award-card-link">
                    <div class="award-card-overlay">&nbsp;</div>

                    <div class="award-trophy-icon"><img alt="Trophy" src="/sites/cec.ucmerced.edu/files/images/greytrophy.png" /></div>

                    <div class="award-card-title">Community Service Graduation Pin</div>

                    <div class="award-card-description">Recognizes students who have demonstrated exceptional dedication to supporting and empowering the local Merced community through sustained service.</div>
                    <a class="award-card-cta" href="https://cec.ucmerced.edu/Graduation/Pin">Learn More &rarr;</a>
                </div>

                <!-- Card 2 -->
                <div class="award-card-link">
                    <div class="award-card-overlay">&nbsp;</div>

                    <div class="award-trophy-icon"><img alt="Trophy" src="/sites/cec.ucmerced.edu/files/images/greytrophy.png" /></div>

                    <div class="award-card-title">Public Service & Leadership Certificate</div>

                    <div class="award-card-description">For students who have shown outstanding commitment to learning about, and practicing community engagement.</div>
                    <a class="award-card-cta" href="https://cec.ucmerced.edu/psl-certificate">Learn More &rarr;</a>
                </div>

                <!-- Card 3 -->
                <div class="award-card-link">
                    <div class="award-card-overlay">&nbsp;</div>

                    <div class="award-trophy-icon"><img alt="Trophy" src="/sites/cec.ucmerced.edu/files/images/greytrophy.png" /></div>

                    <div class="award-card-title">UFC Service Organization Award</div>

                    <div class="award-card-description">This award recognizes a student club or organization for exemplary service in the community surrounding UC Merced. The University Friends Circle will present the recipient with a $1,000 award to support continued community service efforts.</div>
                    <a class="award-card-cta" href="https://cec.ucmerced.edu/UFC_Award">Learn More &rarr;</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>