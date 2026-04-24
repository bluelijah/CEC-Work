<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>College Corps Staff Directory – UC Merced</title>
  <style>
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0,0,0,0);
      white-space: nowrap;
      border: 0;
    }
    .skip-link {
      position: absolute;
      top: -40px;
      left: 0;
      background: #003366;
      color: white;
      padding: 8px 16px;
      text-decoration: none;
      font-weight: 600;
      z-index: 1000;
      border-radius: 0 0 4px 0;
    }
    .skip-link:focus {
      top: 0;
    }
    .staff {
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
    body.mode-hover .flip-card:hover .flip-card-inner {
      transform: rotateY(180deg);
    }
    body.mode-click .flip-card {
      cursor: pointer;
    }
    body.mode-click .flip-card.flipped .flip-card-inner {
      transform: rotateY(180deg);
    }
    .flip-card:focus .flip-card-inner {
      transform: rotateY(180deg);
    }
    .flip-card:focus {
      outline: 3px solid #dbaa00;
      outline-offset: 3px;
      border-radius: 15px;
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
    .flip-card-back h3 {
      font-size: 1.4rem;
      font-weight: bold;
      margin-bottom: 10px;
      flex-shrink: 0;
      color: #0F2D52;
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
    .flip-mode-buttons {
      text-align: center;
      margin-bottom: 20px;
    }
    .flip-mode-buttons button {
      margin: 5px;
      padding: 10px 16px;
      min-height: 44px;
      min-width: 44px;
      border: 2px solid #003366;
      cursor: pointer;
      background-color: #003366;
      color: white;
      border-radius: 5px;
      transition: all 0.3s ease-in-out;
      font-size: 0.9rem;
      font-family: Arial, Helvetica, sans-serif;
    }
    .flip-mode-buttons button:hover {
      background-color: #00509e;
      border-color: #00509e;
      transform: scale(1.05);
    }
    .flip-mode-buttons button:focus {
      outline: 3px solid #dbaa00;
      outline-offset: 2px;
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
    #card-announcer {
      position: absolute;
      width: 1px;
      height: 1px;
      overflow: hidden;
      clip: rect(0,0,0,0);
      white-space: nowrap;
    }
  </style>
</head>
<body>

<!-- FIX 1: Skip link for keyboard users to bypass nav/repeated content -->
<a class="skip-link" href="#main-content">Skip to main content</a>

<!-- FIX 2: Page-level h1 (required; only one per page) -->
<h1 class="sr-only">College Corps Staff Directory</h1>

<!-- FIX 3: aria-live region announces flipped card content to screen readers -->
<div id="card-announcer" aria-live="polite" aria-atomic="true"></div>

<main id="main-content">

  <div class="contact-footer">
    <p><strong>Visit us:</strong><br>
      Community Engagement Center - KL 172<br>
      Monday – Friday, 9:00 AM – 5:00 PM</p>

    <p><strong>Email us:</strong><br>
      <a href="mailto:collegecorps@ucmerced.edu">collegecorps@ucmerced.edu</a></p>

    <p><strong>Follow us on Instagram:</strong><br>
      <!-- These already had "(opens in new tab)" — kept as-is, added rel for security -->
      <a href="https://www.instagram.com/ucmcollegecorps/" target="_blank" rel="noopener noreferrer">@ucmcollegecorps (opens in new tab)</a>
      |
      <a href="https://www.instagram.com/ucmercedcec/" target="_blank" rel="noopener noreferrer">@ucmercedcec (opens in new tab)</a></p>
  </div>

  <!-- FIX 4: role="group" + aria-label groups the buttons semantically -->
  <!-- FIX 5: aria-pressed conveys toggle state to screen readers -->
  <div class="flip-mode-buttons" role="group" aria-label="Card flip interaction mode">
    <button class="active" id="btn-hover" onclick="setFlipMode('hover')" aria-pressed="true">Hover to flip</button>
    <button id="btn-click" onclick="setFlipMode('click')" aria-pressed="false">Click to flip</button>
  </div>

  <!-- FIX 6: h2 section headings are correct here since h1 is declared above -->
  <h2 class="section-title">Program Coordinators</h2>

  <div class="card-container" id="coordinator">

    <!-- FIX 7: aria-expanded reflects flip state; onclick uses shared toggleCard() -->
    <!-- FIX 8: flip-card-back gets aria-hidden toggled by JS so screen readers skip it when closed -->
    <div
      aria-label="Aurora Hernandez, Fellow Program Coordinator"
      aria-expanded="false"
      class="flip-card"
      onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();toggleCard(this);}"
      onclick="if(document.body.classList.contains('mode-click')){toggleCard(this);}"
      role="button"
      tabindex="0"
    >
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img alt="Aurora Hernandez, Fellow Program Coordinator" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/aurora2.png">
        </div>
        <div class="flip-card-back" aria-hidden="true">
          <h3>Aurora Hernandez</h3>
          <p><strong>Fellow Program Coordinator</strong></p>
          <p>Aurora is your main contact for AmericaLearns, additional service opportunities, training, and service back home.</p>
          <p><a href="mailto:avargascontreras@ucmerced.edu">avargascontreras@ucmerced.edu</a></p>
        </div>
      </div>
    </div>

    <div
      aria-label="Alondra Franco Hernandez, Program Manager"
      aria-expanded="false"
      class="flip-card"
      onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();toggleCard(this);}"
      onclick="if(document.body.classList.contains('mode-click')){toggleCard(this);}"
      role="button"
      tabindex="0"
    >
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img alt="Alondra Franco Hernandez, Program Manager" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/alondra.jpg">
        </div>
        <div class="flip-card-back" aria-hidden="true">
          <h3>Alondra Franco Hernandez</h3>
          <p><strong>Program Manager</strong></p>
          <p>Alondra assists with general questions about the program and any issues or questions about transportation.</p>
          <!-- FIX 9: Added "(opens in new tab)" to booking links that were missing it -->
          <p><a href="https://outlook-sdf.office.com/bookwithme/user/95b08b725e044511b35161d0daf9dab4@ucmerced.edu?anonymous&amp;ep=pcard" target="_blank" rel="noopener noreferrer">Book a Meeting (opens in new tab)</a></p>
          <p><a href="mailto:afrancohernandez@ucmerced.edu">afrancohernandez@ucmerced.edu</a></p>
        </div>
      </div>
    </div>

  </div>

  <h2 class="section-title">Operations &amp; Finance</h2>

  <div class="card-container" id="operations">

    <div
      aria-label="Kyla Perez, Program Data Specialist"
      aria-expanded="false"
      class="flip-card"
      onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();toggleCard(this);}"
      onclick="if(document.body.classList.contains('mode-click')){toggleCard(this);}"
      role="button"
      tabindex="0"
    >
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img alt="Kyla Perez, Program Data Specialist" src="/sites/g/files/ufvvjh561/f/people/portraits/k.perez_cc_headshot.png">
        </div>
        <div class="flip-card-back" aria-hidden="true">
          <h3>Kyla Perez</h3>
          <p><strong>Program Data Specialist</strong></p>
          <p>Kyla assists with questions regarding DSIG Payment Request Forms and Mileage Reimbursement.</p>
          <p><a href="https://outlook-sdf.office.com/bookwithme/user/fce3fc4acd984cacab383a701968b6a5%40ucmerced.edu/meetingtype/11d6251b-820c-4501-ad90-cb958e75f02c?anonymous" target="_blank" rel="noopener noreferrer">Book a Meeting (opens in new tab)</a></p>
          <p><a href="mailto:kperez@ucmerced.edu">kperez@ucmerced.edu</a></p>
        </div>
      </div>
    </div>

    <div
      aria-label="Debra Fitzgerald, Grant Administrative Officer"
      aria-expanded="false"
      class="flip-card"
      onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();toggleCard(this);}"
      onclick="if(document.body.classList.contains('mode-click')){toggleCard(this);}"
      role="button"
      tabindex="0"
    >
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img alt="Debra Fitzgerald, Grant Administrative Officer" src="/sites/g/files/ufvvjh561/f/people/portraits/d.fitzgerald_cc_headshot.png">
        </div>
        <div class="flip-card-back" aria-hidden="true">
          <h3>Debra Fitzgerald</h3>
          <p><strong>Grant Administrative Officer</strong></p>
          <p>Debi provides direction and oversight of administrative operations, including grant writing and day-to-day administration of budgets and recordkeeping systems.</p>
          <p><a href="mailto:dfitzgerald@ucmerced.edu">dfitzgerald@ucmerced.edu</a></p>
        </div>
      </div>
    </div>

    <div
      aria-label="Lisa Silveira, Financial Aid Advisor"
      aria-expanded="false"
      class="flip-card"
      onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();toggleCard(this);}"
      onclick="if(document.body.classList.contains('mode-click')){toggleCard(this);}"
      role="button"
      tabindex="0"
    >
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img alt="Lisa Silveira, Financial Aid Advisor" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/lisa_-_photo_1.png">
        </div>
        <div class="flip-card-back" aria-hidden="true">
          <h3>Lisa Silveira</h3>
          <p><strong>Financial Aid Advisor</strong></p>
          <p>Lisa assists with any inquiries regarding financial aid or living disbursements.</p>
          <p><a href="mailto:lsilveira@ucmerced.edu">lsilveira@ucmerced.edu</a></p>
        </div>
      </div>
    </div>

  </div>

</main>

<script>
  document.body.classList.add('mode-hover');

  function setFlipMode(mode) {
    document.querySelectorAll('.flip-card').forEach(card => {
      card.classList.remove('flipped');
      card.setAttribute('aria-expanded', 'false');
      card.querySelector('.flip-card-back').setAttribute('aria-hidden', 'true');
    });
    document.body.classList.remove('mode-hover', 'mode-click');
    document.body.classList.add('mode-' + mode);

    const hoverBtn = document.getElementById('btn-hover');
    const clickBtn = document.getElementById('btn-click');
    hoverBtn.classList.toggle('active', mode === 'hover');
    clickBtn.classList.toggle('active', mode === 'click');
    // FIX 5 (JS side): Keep aria-pressed in sync with active state
    hoverBtn.setAttribute('aria-pressed', mode === 'hover' ? 'true' : 'false');
    clickBtn.setAttribute('aria-pressed', mode === 'click' ? 'true' : 'false');
  }

  function toggleCard(card) {
    const isExpanded = card.classList.toggle('flipped');
    const back = card.querySelector('.flip-card-back');

    // FIX 7 (JS side): Update aria-expanded and aria-hidden on flip
    card.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
    back.setAttribute('aria-hidden', isExpanded ? 'false' : 'true');

    // FIX 3 (JS side): Push card content into the live region when opened
    if (isExpanded) {
      const name = back.querySelector('h3')?.textContent || '';
      const role = back.querySelector('strong')?.textContent || '';
      const desc = back.querySelectorAll('p')[1]?.textContent || '';
      document.getElementById('card-announcer').textContent =
        name + ', ' + role + '. ' + desc;
    } else {
      document.getElementById('card-announcer').textContent = '';
    }
  }
</script>
</body>
</html>