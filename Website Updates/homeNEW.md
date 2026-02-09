<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.cec-mission-container {
            max-width: 1200px;
            margin: 0 20px 0 auto;
            padding: 0 20px;
            border-top: 4px solid #dbaa00;
            border-bottom: 4px solid #dbaa00;
            height: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .cec-mission-statement {
            font-size: 18px;
            line-height: 1.5;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: left;
        }

        .cec-mission-label {
            font-weight: 700;
            color: #003262;
            font-size: 20px;
            font-style: italic;
            line-height: 1.5;
        }
        
        .cec-title-line {
            border-bottom: 2px solid #E5E5E5;
            text-align: center;
            padding-bottom: 15px;
            margin-bottom: 40px;
            color: #0f2d52;
        }

        .cec-blocks-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            padding: 20px 0 20px 20px;
            max-width: 1200px;
            margin: 0 0 0 auto;
            margin-right: 30px;
        }

        .cec-identity-block {
            border-radius: 16px;
            padding: 60px 30px;
            text-align: center;
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
            cursor: pointer;
            background-size: cover;
            background-position: center;
        }

        .cec-identity-block::after {
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

        .cec-identity-block::before {
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

        .cec-identity-block:hover::before {
            opacity: 0.85;
        }

        .cec-identity-block:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(219, 170, 0, 0.3);
        }

        .cec-student-block {
            background-image: url('/sites/g/files/ufvvjh561/f/images/studentsmain.jpg');
        }

        .cec-corps-block {
            background-image: url('/sites/g/files/ufvvjh561/f/images/collegecorpsmain.jpg');
        }

        .cec-partner-block {
            background-image: url('/sites/g/files/ufvvjh561/f/images/jamboreemain.jpg');
        }

        .cec-block-content {
            position: relative;
            z-index: 2;
        }

        .cec-block-title {
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
            color: white;
        }

        .cec-block-subtitle {
            font-size: 32px;
            opacity: 1;
            font-weight: 700;
            color: white;
            margin: 0;
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .cec-blocks-container {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 20px 10px 10px;
                margin: 0 0 0 auto;
            }
            
            .cec-identity-block {
                padding: 50px 25px;
            }
            
            .cec-block-title {
                font-size: 16px;
            }
            
            .cec-block-subtitle {
                font-size: 28px;
            }
            
            .cec-title-line {
                font-size: 24px;
                margin-bottom: 30px;
            }
            
            .cec-mission-container {
                padding: 0 15px;
                height: auto;
                min-height: 120px;
                margin: 0 20px 0 auto;
                padding-top: 10px;
                padding-bottom: 10px;
            }
            
            .cec-mission-statement {
                font-size: 16px;
            }
            
            .cec-mission-label {
                font-size: 18px;
            }
        }

        @media (max-width: 480px) {
            .cec-identity-block {
                padding: 40px 20px;
            }
            
            .cec-block-subtitle {
                font-size: 24px;
            }
        }
</style>
<div class="cec-mission-container">
	<p class="cec-mission-statement"><span class="cec-mission-label">Our Mission:</span> The Community Engagement Center brings together UC Merced students, staff, faculty, and community members with local agencies and organizations. Together, we create reciprocal partnerships that generate student learning, build capacity, and solve problems through service, scholarship, and leadership. From local to global, these actions contribute to building a healthy and sustainable community, creating positive, direct change.</p>
</div>

<div class="cec-blocks-container">
	<div class="cec-identity-block cec-student-block" onclick="window.location.href='https://cec.ucmerced.edu/students'">
		<div class="cec-block-content">
			<h3 class="cec-block-title">I am a</h3>

			<p class="cec-block-subtitle">Student</p>
		</div>
	</div>

	<div class="cec-identity-block cec-corps-block" onclick="window.location.href='https://cec.ucmerced.edu/college-corps-directory'">
		<div class="cec-block-content">
			<h3 class="cec-block-title">I am</h3>

			<p class="cec-block-subtitle">College Corps</p>
		</div>
	</div>

	<div class="cec-identity-block cec-partner-block" onclick="window.location.href='https://cec.ucmerced.edu/community-partners'">
		<div class="cec-block-content">
			<h3 class="cec-block-title">I am a</h3>

			<p class="cec-block-subtitle">Community Partner</p>
		</div>
	</div>
</div>
