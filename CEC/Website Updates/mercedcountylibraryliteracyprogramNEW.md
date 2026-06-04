<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.library-page * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .library-page {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
            background-image: url('/sites/g/files/ufvvjh561/f/images/library.jpg');
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            background-size: 50%;
            position: relative;
        }

        .library-page::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.9);
            z-index: -1;
        }

        .library-container {
            width: 100%;
            margin: 0 auto;
            padding: 0;
            position: relative;
            z-index: 1;
        }

        .library-header {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, #0f2d52 0%, #1a4573 100%);
            color: white;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(15, 45, 82, 0.3);
        }

        .library-header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: white;
        }

        .library-header p {
            color: white;
            font-size: 1.1rem;
        }

        .library-content-box {
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
        }

        .library-content-box h2 {
            color: #0f2d52;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }

        .library-content-box h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }

        .library-content-box p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 1.2rem;
        }

        .library-content-box ul {
            margin-left: 2rem;
            margin-bottom: 1.5rem;
        }

        .library-content-box li {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 0.5rem;
        }

        .library-content-box strong {
            color: #0f2d52;
        }

        .library-highlight-box {
            background: linear-gradient(135deg, #fffbf0 0%, #fff9e6 100%);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid #dbaa00;
            margin-bottom: 1.5rem;
        }

        .library-highlight-box p {
            margin-bottom: 1rem;
        }

        .library-highlight-box p:last-child {
            margin-bottom: 0;
        }

        .library-three-column {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .library-column {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .library-column h4 {
            color: #0f2d52;
            font-size: 1.1rem;
            margin-top: 0;
            margin-bottom: 1rem;
            text-align: center;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #dbaa00;
        }

        .library-column ul {
            margin-left: 1.5rem;
            font-size: 1rem;
        }

        .library-column li {
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }

        .library-contact-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            border-top: 4px solid #dbaa00;
            margin-top: 2rem;
            text-align: center;
        }

        .library-contact-section h3 {
            color: #0f2d52;
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }

        .library-contact-section p {
            color: #555;
            margin-bottom: 1.5rem;
        }

        .library-contact-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }

        .library-contact-item {
            text-align: center;
        }

        .library-contact-item strong {
            display: block;
            color: #0f2d52;
            margin-bottom: 0.5rem;
        }

        .library-contact-item a {
            color: #0f2d52;
            text-decoration: underline;
        }

        .library-contact-item a:hover {
            color: #1a4573;
        }

        .library-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 44px;
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

        .library-button:hover {
            background: #dbaa00;
            color: #0f2d52 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(219, 170, 0, 0.5);
        }

        .library-button-center {
            text-align: center;
            margin-top: 1.5rem;
        }

        @media (max-width: 768px) {
            .library-button-center { display: flex; flex-direction: column; gap: 1rem; }
            .library-page { margin-right: 40px; background-size: 70%; }
            .library-header h1 { font-size: 1.8rem; }
            .library-content-box { padding: 1.5rem; }
            .library-three-column { grid-template-columns: 1fr; }
            .library-contact-info { flex-direction: column; gap: 1rem; }
        }
</style>

<div class="library-page">
    <div class="library-container">
        <div class="library-content-box">
            <p>The <strong>Read &amp; Succeed Adult Literacy Program</strong> at Merced County Library provides free 1-on-1 tutoring and resources to adults who want to improve their English literacy skills. This program makes a meaningful difference in the lives of community members who are working to develop their reading and writing abilities.</p>

            <div class="library-highlight-box" role="note">
                <p><strong>Make an Impact:</strong> Are you passionate about giving back to your community and helping others in underserved communities develop their skills for success? The Read &amp; Succeed Adult Literacy Program needs volunteer tutors!</p>
            </div>

            <h3>What You&#39;ll Do</h3>
            <p>Volunteering consists of a 3-hour weekly commitment for a minimum of 3-to-6 months. You will be paired with a learner to help them work towards their personalized goals. This is a semester-long commitment where you&#39;ll work one-on-one or in small groups with adults at the Merced County Library, providing the consistent support and guidance needed to help participants grow their confidence and abilities in English.</p>

            <div class="library-three-column">
                <div class="library-column">
                    <h4>Volunteer Responsibilities</h4>
                    <ul>
                        <li>Provide one-on-one tutoring in English literacy</li>
                        <li>Work with learners on reading and writing skills</li>
                        <li>Help learners work towards personalized goals</li>
                        <li>Commit to weekly 3-hour sessions</li>
                    </ul>
                </div>
                <div class="library-column">
                    <h4>Requirements</h4>
                    <ul>
                        <li>No experience required!</li>
                        <li>Attend a 2-hour training session</li>
                        <li>3-hour weekly commitment</li>
                        <li>Minimum 3-to-6 month commitment</li>
                        <li>Flexible scheduling available</li>
                    </ul>
                </div>
                <div class="library-column">
                    <h4>What We Provide</h4>
                    <ul>
                        <li>Free training and orientation</li>
                        <li>Ongoing support and guidance</li>
                        <li>Flexible scheduling options</li>
                        <li>Rewarding and meaningful experience</li>
                    </ul>
                </div>
            </div>

            <h3>Application Process</h3>
            <ul>
                <li>Fill out and submit the application using the sign-up button below</li>
                <li>Attend a 2-hour training session</li>
                <li>Be matched with a learner and start your weekly sessions</li>
            </ul>

            <p><strong>Note:</strong> Session dates and times will be set according to your availability and occur on the same day &amp; time every week.</p>

            <div class="library-highlight-box" role="note">
                <p><strong>Community Service Graduation Pin:</strong> By participating in the Read &amp; Succeed Adult Literacy Program, you will be eligible for the Community Service Graduation Pin! Full participation must be completed for the Community Service Graduation Pin, which is a semester-long commitment.</p>
            </div>

            <p>The program offers flexibility to fit around your academic and personal commitments, ensuring you&#39;re able to participate without compromising your schedule. If you&#39;re ready to take the next step in making a positive impact, complete the registration form below! Together, we can build a stronger and more inclusive place for everyone in our local Merced Community!</p>
        </div>

        <div class="library-contact-section">
            <h3>Get Started Today</h3>
            <p>Ready to make a difference? Sign up to become a volunteer tutor with the Read &amp; Succeed Adult Literacy Program!</p>

            <div class="library-contact-info">
                <div class="library-contact-item">
                    <strong>Phone</strong>
                    <p><a href="tel:+12093857391">(209) 385-7391</a></p>
                </div>
                <div class="library-contact-item">
                    <strong>Email</strong>
                    <p><a href="mailto:readandsucceed@mercedcountylibrary.org">readandsucceed@mercedcountylibrary.org</a></p>
                </div>
            </div>

            <div class="library-button-center">
                <a class="library-button" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_6gM1XUFsAeBH4hM">Sign Up Now</a>
            </div>
        </div>
    </div>
</div>