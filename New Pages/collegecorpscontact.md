<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.staff {
            border-bottom: 2px solid #dbaa00;
        }
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
            justify-content: center;
        }
        .card-container:has(.flip-card:nth-child(1):nth-last-child(-n+3)) {
            grid-template-columns: repeat(auto-fit, minmax(250px, 325px));
        }
        .flip-card {
            background-color: transparent;
            width: 100%;
            max-width: 325px;
            height: 434px;
            perspective: 1000px;
            cursor: default;
        }
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            border-radius: 15px;
        }

        /* Hover mode (default) */
        body.mode-hover .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }

        /* Click mode */
        body.mode-click .flip-card {
            cursor: pointer;
        }
        body.mode-click .flip-card.flipped .flip-card-inner {
            transform: rotateY(180deg);
        }

        /* Keyboard focus flip */
        .flip-card:focus .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-card-front, .flip-card-back {
            border-radius: 15px;
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            overflow: hidden;
        }
        .flip-card-front {
            background-color: #fff;
        }
        .flip-card-back {
            background: linear-gradient(300deg, #a6beea, #f4cd2a);
            color: #0F2D52;
            transform: rotateY(180deg);
            box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
            padding: 20px;
            box-sizing: border-box;
            font-size: 0.9rem;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: rgba(15, 45, 82, 0.5) transparent;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .flip-card-back::-webkit-scrollbar { width: 6px; }
        .flip-card-back::-webkit-scrollbar-track { background: rgba(255,255,255,0.1); border-radius: 3px; }
        .flip-card-back::-webkit-scrollbar-thumb { background: rgba(15,45,82,0.5); border-radius: 3px; }
        .flip-card-back::-webkit-scrollbar-thumb:hover { background: rgba(15,45,82,0.7); }
        .flip-card-back h1 {
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 10px;
            flex-shrink: 0;
        }
        .flip-card-back p {
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: #0F2D52;
        }
        .flip-card-back a {
            color: #0f2d52;
            font-weight: 600;
            text-decoration: none;
        }
        .flip-card-back a:hover { text-decoration: underline; }
        .flip-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            transform: scale(1.05);
        }
        .section-title {
            text-align: center;
            color: #0f2d52;
            border-bottom: 3px solid #dbaa00;
            padding-bottom: 10px;
            margin: 30px 20px 0 20px;
            font-size: 1.4em;
        }
        .contact-footer {
            background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%);
            color: white;
            padding: 35px 40px;
            border-radius: 12px;
            margin: 0 0 30px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .contact-footer p {
            margin-bottom: 12px;
            font-size: 1.05em;
            line-height: 1.6;
            opacity: 0.95;
            color: white;
        }
        .contact-footer strong { color: #dbaa00; }
        .contact-footer a,
        .contact-footer a:link,
        .contact-footer a:visited {
            color: white !important;
            text-decoration: none;
            font-weight: 600;
        }
        .contact-footer a:hover { text-decoration: underline; }

        /* Flip mode toggle buttons */
        .flip-mode-buttons {
            text-align: center;
            margin-bottom: 20px;
        }
        .flip-mode-buttons button {
            margin: 5px;
            padding: 10px 16px;
            min-height: 44px;
            border: 2px solid #003366;
            cursor: pointer;
            background-color: #003366;
            color: white;
            border-radius: 5px;
            transition: all 0.3s ease-in-out;
            font-size: 0.9rem;
        }
        .flip-mode-buttons button:hover {
            background-color: #00509e;
            border-color: #00509e;
            transform: scale(1.05);
        }
        .flip-mode-buttons button.active {
            background-color: #ffffff;
            color: #003366;
            border-color: #003366;
        }
        .flip-mode-buttons button.active:hover {
            background-color: #e8eef5;
            transform: scale(1.05);
        }
</style>

<div class="contact-footer">
    <p><strong>Visit us:</strong><br />
        Community Engagement Center - KL 172<br />
        Monday - Friday, 9:00 AM - 5:00 PM</p>
    <p><strong>Email us:</strong><br />
        <a href="mailto:collegecorps@ucmerced.edu">collegecorps@ucmerced.edu</a></p>
    <p><strong>Follow us on Instagram:</strong><br />
        <a href="https://www.instagram.com/ucmcollegecorps/" target="_blank">@ucmcollegecorps (opens in new tab)</a> | <a href="https://www.instagram.com/ucmercedcec/" target="_blank">@ucmercedcec (opens in new tab)</a></p>
</div>

<div class="flip-mode-buttons">
    <button id="btn-hover" class="active" onclick="setFlipMode('hover')">Hover to flip</button>
    <button id="btn-click" onclick="setFlipMode('click')">Click to flip</button>
</div>

<h3 class="section-title">Program Coordinators</h3>

<div class="card-container" id="coordinator">
    <div class="flip-card"
         role="button"
         tabindex="0"
         aria-label="Eliza Sanchez, Fellow Program Coordinator — hover or press Enter to see details"
         data-email="esanchez@ucmerced.edu"
         data-name="Eliza Sanchez"
         data-role="Fellow Program Coordinator"
         onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.classList.toggle('flipped');}">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img alt="Eliza Sanchez, Fellow Program Coordinator" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/image_9-26-24_2.35.09_pm.jpg" /></div>
            <div class="flip-card-back">
                <h1>Eliza Sanchez</h1>
                <p><strong>Fellow Program Coordinator</strong></p>
                <p>Eliza is your main contact for AmericaLearns, additional service opportunities, training, and service back home.</p>
                <p><a href="https://outlook.office.com/bookwithme/user/64ade8c431a44fbfacd81e578fd32366%40ucmerced.edu/meetingtype/060f98a8-05a9-471a-b92e-803cc89370dc?anonymous" target="_blank">Book a Meeting (opens in new tab)</a></p>
                <p><a href="mailto:esanchez@ucmerced.edu">esanchez@ucmerced.edu</a></p>
            </div>
        </div>
    </div>

    <div class="flip-card"
         role="button"
         tabindex="0"
         aria-label="Alondra Franco Hernandez, Program Manager — hover or press Enter to see details"
         data-email="afrancohernandez@ucmerced.edu"
         data-name="Alondra Franco Hernandez"
         data-role="Program Manager"
         onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.classList.toggle('flipped');}">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img alt="Alondra Franco Hernandez, Program Manager" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/alondra.jpg" /></div>
            <div class="flip-card-back">
                <h1>Alondra Franco Hernandez</h1>
                <p><strong>Program Manager</strong></p>
                <p>Alondra assists with general questions about the program and any issues or questions about transportation.</p>
                <p><a href="https://outlook-sdf.office.com/bookwithme/user/95b08b725e044511b35161d0daf9dab4@ucmerced.edu?anonymous&ep=pcard" target="_blank">Book a Meeting (opens in new tab)</a></p>
                <p><a href="mailto:afrancohernandez@ucmerced.edu">afrancohernandez@ucmerced.edu</a></p>
            </div>
        </div>
    </div>
</div>

<h3 class="section-title">Operations &amp; Finance</h3>

<div class="card-container" id="operations">
    <div class="flip-card"
         role="button"
         tabindex="0"
         aria-label="Kyla Perez, Program Data Specialist — hover or press Enter to see details"
         data-email="kperez@ucmerced.edu"
         data-name="Kyla Perez"
         data-role="Program Data Specialist"
         onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.classList.toggle('flipped');}">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img alt="Kyla Perez, Program Data Specialist" src="/sites/g/files/ufvvjh561/f/people/portraits/k.perez_cc_headshot.png" /></div>
            <div class="flip-card-back">
                <h1>Kyla Perez</h1>
                <p><strong>Program Data Specialist</strong></p>
                <p>Kyla assists with questions regarding DSIG Payment Request Forms and Mileage Reimbursement.</p>
                <p><a href="https://outlook-sdf.office.com/bookwithme/user/fce3fc4acd984cacab383a701968b6a5%40ucmerced.edu/meetingtype/11d6251b-820c-4501-ad90-cb958e75f02c?anonymous" target="_blank">Book a Meeting (opens in new tab)</a></p>
                <p><a href="mailto:kperez@ucmerced.edu">kperez@ucmerced.edu</a></p>
            </div>
        </div>
    </div>

    <div class="flip-card"
         role="button"
         tabindex="0"
         aria-label="Debra Fitzgerald, Grant Administrative Officer — hover or press Enter to see details"
         data-email="dfitzgerald@ucmerced.edu"
         data-name="Debra Fitzgerald"
         data-role="Grant Administrative Officer"
         onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.classList.toggle('flipped');}">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img alt="Debra Fitzgerald, Grant Administrative Officer" src="/sites/g/files/ufvvjh561/f/people/portraits/d.fitzgerald_cc_headshot.png" /></div>
            <div class="flip-card-back">
                <h1>Debra Fitzgerald</h1>
                <p><strong>Grant Administrative Officer</strong></p>
                <p>Debi provides direction and oversight of administrative operations, including grant writing and day-to-day administration of budgets and recordkeeping systems.</p>
                <p><a href="mailto:dfitzgerald@ucmerced.edu">dfitzgerald@ucmerced.edu</a></p>
            </div>
        </div>
    </div>

    <div class="flip-card"
         role="button"
         tabindex="0"
         aria-label="Lisa Silveira, Financial Aid Advisor — hover or press Enter to see details"
         data-email="lsilveira@ucmerced.edu"
         data-name="Lisa Silveira"
         data-role="Financial Aid Advisor"
         onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.classList.toggle('flipped');}">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img alt="Lisa Silveira, Financial Aid Advisor" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/lisa_-_photo_1.png" /></div>
            <div class="flip-card-back">
                <h1>Lisa Silveira</h1>
                <p><strong>Financial Aid Advisor</strong></p>
                <p>Lisa assists with any inquiries regarding financial aid or living disbursements.</p>
                <p><a href="mailto:lsilveira@ucmerced.edu">lsilveira@ucmerced.edu</a></p>
            </div>
        </div>
    </div>
</div>

<script>
    document.body.classList.add('mode-hover');

    function setFlipMode(mode) {
        document.querySelectorAll('.flip-card').forEach(card => card.classList.remove('flipped'));
        document.body.classList.remove('mode-hover', 'mode-click');
        document.body.classList.add('mode-' + mode);
        document.getElementById('btn-hover').classList.toggle('active', mode === 'hover');
        document.getElementById('btn-click').classList.toggle('active', mode === 'click');
    }

    document.querySelectorAll('.flip-card').forEach(card => {
        card.addEventListener('click', function () {
            if (document.body.classList.contains('mode-click')) {
                this.classList.toggle('flipped');
            }
        });
    });
</script>