<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.playhouse-page * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .playhouse-page {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
            background-image: url('/sites/g/files/ufvvjh561/f/images/logos/mercedplayhouselogo.png');
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            background-size: 40%;
            position: relative;
        }

        .playhouse-page::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.95);
            z-index: -1;
        }

        .playhouse-container {
            width: 100%;
            margin: 0 auto;
            padding: 0;
            position: relative;
            z-index: 1;
        }

        .playhouse-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
            color: white;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
        }

        .playhouse-header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: white;
        }

        .playhouse-header p {
            color: white;
            font-size: 1.1rem;
        }

        .playhouse-content-box {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
        }

        .playhouse-content-box h2 {
            color: #0f2d52;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }

        .playhouse-content-box h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        .playhouse-content-box h4 {
            color: #0f2d52;
            font-size: 1.2rem;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        .playhouse-content-box p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.2rem;
        }

        .playhouse-content-box ul {
            margin-left: 2rem;
            margin-bottom: 1.5rem;
        }

        .playhouse-content-box li {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 0.5rem;
        }

        .playhouse-content-box strong {
            color: #0f2d52;
        }

        .playhouse-highlight-box {
            background: linear-gradient(135deg, #fffbf0 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #dbaa00;
            margin-bottom: 1.5rem;
        }

        .playhouse-highlight-box p {
            margin-bottom: 1rem;
        }

        .playhouse-highlight-box p:last-child {
            margin-bottom: 0;
        }

        .playhouse-opportunity-card {
            background: #f9f9f9;
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            border-left: 4px solid #dbaa00;
        }

        .playhouse-opportunity-card h4 {
            color: #0f2d52;
            font-size: 1.3rem;
            margin-top: 0;
            margin-bottom: 0.8rem;
        }

        .playhouse-opportunity-card p {
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }

        .playhouse-contact-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
            margin-top: 2rem;
            text-align: center;
        }

        .playhouse-contact-section h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }

        .playhouse-contact-section p {
            color: #555;
            margin-bottom: 1.5rem;
        }

        .playhouse-contact-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }

        .playhouse-contact-item {
            text-align: center;
        }

        .playhouse-contact-item strong {
            display: block;
            color: #0f2d52;
            margin-bottom: 0.5rem;
        }

        .playhouse-button {
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

        .playhouse-button:hover {
            background: #dbaa00;
            color: #0f2d52 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(219, 170, 0, 0.5);
        }

        .playhouse-button-center {
            text-align: center;
            margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
            .playhouse-button-center {
                display: flex;
                flex-direction: column;
                gap: 1rem;
            }

            .playhouse-page {
                margin-right: 40px;
                background-size: 70%;
            }

            .playhouse-header h1 {
                font-size: 1.8rem;
            }

            .playhouse-content-box {
                padding: 1.5rem;
            }

            .playhouse-contact-info {
                flex-direction: column;
                gap: 1rem;
            }

            .playhouse-opportunity-card {
                padding: 1.5rem;
            }
        }
</style>
<div class="playhouse-page">
	<div class="playhouse-container">
		<div class="playhouse-header">
			<h1>Playhouse Merced</h1>

			<p>Center for the Performing Arts - Volunteer Opportunities</p>
		</div>

		<div class="playhouse-content-box">
			<h2>Join the Playhouse Merced Community</h2>

			<p>Playhouse Merced - Center for the Performing Arts offers exciting volunteer opportunities for students interested in theater, performing arts, costume design, stage management, and more. Get hands-on experience while earning volunteer hours and contributing to community theater.</p>

			<div class="playhouse-highlight-box">
				<p><strong>Get involved in theater!</strong> From behind-the-scenes technical work to social media and promotions, Playhouse Merced provides opportunities to develop skills in the performing arts while contributing to community productions.</p>
			</div>
		</div>

		<div class="playhouse-content-box">
			<h2>Volunteer Intern Positions</h2>

			<p>Playhouse Merced offers intern positions that provide valuable behind-the-scenes theater experience. All volunteer positions count toward high school community service and college volunteer requirements.</p>

			<div class="playhouse-opportunity-card">
				<h4>Social Media &amp; Promotions Intern</h4>

				<p>Do you dream about becoming an influencer? Or maybe a photographer or marketing agent? This is the job for you! Help reach the community by making fun social media posts and posters!</p>
			</div>

			<div class="playhouse-opportunity-card">
				<h4>Stage Manager Intern</h4>

				<p>Are you a natural leader and organized individual? Want to learn the ins &amp; outs of a theater behind-the-scenes? Come work with us and get more experience in learning to manage a show!</p>
			</div>

			<div class="playhouse-opportunity-card">
				<h4>Prop Master Intern</h4>

				<p>Props are a vital part of a performance, so come help us and get experience in making, gathering, and organizing props for a show!</p>
			</div>

			<div class="playhouse-highlight-box">
				<p><strong>Playhouse Merced is also hiring for paid positions.</strong> If you&#39;re interested in paid opportunities such as costume design, conservatory assistant, or directing positions, please reach out directly via email at playhousemercedED@gmail.com or call 209-725-8587.</p>
			</div>
		</div>

		<div class="playhouse-contact-section">
			<h3>Get Involved</h3>

			<p>Interested in volunteering with Playhouse Merced? Sign up below or contact us to learn more about available positions!</p>

			<div class="playhouse-contact-info">
				<div class="playhouse-contact-item"><strong>Phone</strong>

					<p>209-725-8587</p>
				</div>

				<div class="playhouse-contact-item"><strong>Email</strong>

					<p>playhousemercedED@gmail.com</p>
				</div>

				<div class="playhouse-contact-item"><strong>Website</strong>

					<p><a href="https://hisawyer.com/playhouse-merced-center-for-the-performing-arts" style="color: #0f2d52; font-weight: bold;">hisawyer.com</a></p>
				</div>
			</div>

			<p>Follow Playhouse Merced on Facebook for more information about upcoming shows and opportunities!</p>

			<div class="playhouse-button-center"><a class="playhouse-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_ahsggABGp0H0AcK">Sign Up Now</a></div>
		</div>
	</div>
</div>
