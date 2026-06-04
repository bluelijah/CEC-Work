<style type="text/css">
  /* ── Brand tokens ───────────────────────────────────────────── */
  :root {
    --navy:   #0f2d52;
    --gold:   #dbaa00;
    --white:  #ffffff;
    --light:  #f5f8fb;
    --text:   #333333;
    --muted:  #666666;
    --border: #e5e5e5;
    --shadow: 0 4px 12px rgba(0,0,0,.08);
    --shadow-hover: 0 8px 28px rgba(219,170,0,.30);
    --radius: 16px;
    --font-body: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  }

  /* ── Reset & base ───────────────────────────────────────────── */
  .intro-container *, .filter-section *, .cards-section *, .cta-section *,
  .cards-section *::before, .cards-section *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  .card-body a { color: inherit; text-decoration: none; }

  /* ── Intro bar ──────────────────────────────────────────────── */
  .intro-container {
    max-width: 1200px;
    margin: 30px 30px 30px auto;
    padding: 0 20px;
    border-top: 4px solid var(--gold);
    border-bottom: 4px solid var(--gold);
    min-height: 80px;
    display: flex;
    align-items: center;
  }
  .intro-container p {
    font-size: 1.05em;
    line-height: 1.6;
    color: var(--text);
    padding: 18px 0;
  }
  .intro-container strong { color: var(--navy); }

  /* ── Filter bar ─────────────────────────────────────────────── */
  .filter-section {
    max-width: 1200px;
    margin: 0 30px 36px auto;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
  }
  .filter-label {
    font-size: .82em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--navy);
    margin-right: 4px;
  }
  .filter-btn {
    border: 2px solid var(--border);
    border-radius: 999px;
    padding: 7px 18px;
    font-family: var(--font-body);
    font-size: .85em;
    font-weight: 500;
    color: var(--navy);
    background: var(--white);
    cursor: pointer;
    transition: all .2s;
  }
  .filter-btn:hover { border-color: var(--gold); background: #fffbee; }
  .filter-btn.active { background: var(--navy); border-color: var(--navy); color: var(--white); }
  .filter-btn[data-tag="Community Service"].active       { background: #1a5c3a; border-color: #1a5c3a; }
  .filter-btn[data-tag="Study Abroad"].active            { background: #1a4a82; border-color: #1a4a82; }
  .filter-btn[data-tag="Leadership"].active              { background: #7a2020; border-color: #7a2020; }
  .filter-btn[data-tag="Internship"].active              { background: #5a3a00; border-color: #5a3a00; }
  .filter-btn[data-tag="Undergraduate Research"].active  { background: #3a1a60; border-color: #3a1a60; }

  /* ── Card grid ──────────────────────────────────────────────── */
  .cards-section {
    max-width: 1200px;
    margin: 0 30px 30px auto;
  }
  .cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
  }

  /* ── Individual card ────────────────────────────────────────── */
  .account-card {
    background: var(--white);
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    transition: transform .3s ease, box-shadow .3s ease;
    border: 1px solid var(--border);
    cursor: pointer;
  }
  .account-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-hover);
  }
  .account-card.hidden { display: none; }

  /* Cover photo */
  .card-cover {
    position: relative;
    height: 180px;
    overflow: hidden;
    background: #d8e4f0;
    flex-shrink: 0;
  }
  .card-cover img {
    width: 100%; height: 100%;
    object-fit: cover;
    display: block;
    transition: transform .4s ease;
  }
  .account-card:hover .card-cover img { transform: scale(1.04); }

  /* EL type badge */
  .el-badge {
    position: absolute;
    top: 12px; right: 12px;
    padding: 5px 12px;
    border-radius: 999px;
    font-size: .72em;
    font-weight: 700;
    letter-spacing: .06em;
    text-transform: uppercase;
    color: var(--white);
    backdrop-filter: blur(6px);
  }
  .el-badge.community-service        { background: rgba(26,92,58,.88); }
  .el-badge.study-abroad             { background: rgba(26,74,130,.88); }
  .el-badge.leadership               { background: rgba(122,32,32,.88); }
  .el-badge.internship               { background: rgba(90,58,0,.88); }
  .el-badge.undergraduate-research   { background: rgba(58,26,96,.88); }

  /* Card body */
  .card-body {
    padding: 22px 22px 20px;
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  .card-name {
    font-size: 1.2em;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 4px;
    line-height: 1.2;
  }
  .card-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 4px 14px;
  }
  .card-meta-item {
    font-size: .82em;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 4px;
    width: 100%;
  }

  /* Read story hint */
  .card-hint {
    margin-top: 14px;
    font-size: .8em;
    font-weight: 700;
    color: var(--gold);
    letter-spacing: .04em;
    text-transform: uppercase;
  }

  /* ── Story Modal Overlay ────────────────────────────────────── */
  .el-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(15, 45, 82, 0.65);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }
  .el-overlay.el-open { display: flex; }

  .el-modal {
    background: var(--white);
    border-radius: var(--radius);
    width: 100%;
    max-width: 600px;
    max-height: 88vh;
    overflow-y: auto;
    border: 1px solid var(--border);
    position: relative;
  }
  .el-modal::-webkit-scrollbar       { width: 6px; }
  .el-modal::-webkit-scrollbar-track { background: transparent; }
  .el-modal::-webkit-scrollbar-thumb { background: #c8d4e8; border-radius: 999px; }

  .el-modal-cover {
    width: 100%;
    height: 220px;
    overflow: hidden;
    position: relative;
    background: #d8e4f0;
    flex-shrink: 0;
  }
  .el-modal-cover img {
    width: 100%; height: 100%;
    object-fit: cover;
    display: block;
  }

  .el-modal-header {
    background: var(--navy);
    border-bottom: 4px solid var(--gold);
    padding: 20px 24px 16px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  .el-modal-header-info { flex: 1; min-width: 0; }
  .el-modal-name {
    font-size: 1.3em;
    font-weight: 700;
    color: var(--white);
    line-height: 1.2;
    margin: 0 0 4px;
  }
  .el-modal-meta {
    font-size: .85em;
    color: rgba(255,255,255,.65);
    margin: 0;
  }
  .el-modal-badge {
    display: inline-block;
    margin-top: 8px;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: .72em;
    font-weight: 700;
    letter-spacing: .06em;
    text-transform: uppercase;
    color: var(--white);
  }
  .el-modal-badge.community-service      { background: rgba(26,92,58,1); }
  .el-modal-badge.study-abroad           { background: rgba(26,74,130,1); }
  .el-modal-badge.leadership             { background: rgba(122,32,32,1); }
  .el-modal-badge.internship             { background: rgba(90,58,0,1); }
  .el-modal-badge.undergraduate-research { background: rgba(58,26,96,1); }

  .el-modal-close {
    background: rgba(255,255,255,0.12);
    border: none;
    color: var(--white);
    font-size: 18px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    padding: 0;
    line-height: 1;
    transition: background 0.15s;
    margin-left: 12px;
  }
  .el-modal-close:hover { background: rgba(255,255,255,0.25); }

  .el-modal-body {
    padding: 28px 28px 32px;
  }
  .el-modal-story-label {
    font-size: .75em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--gold);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .el-modal-story-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }
  .el-modal-story-text {
    font-size: .95em;
    line-height: 1.75;
    color: var(--text);
    font-style: italic;
    margin: 0;
    border-left: 4px solid var(--gold);
    padding-left: 18px;
    background: var(--light);
    padding: 16px 20px;
    border-radius: 0 8px 8px 0;
  }

  /* ── Video card ─────────────────────────────────────────────── */
  .video-card { cursor: default; }
  .video-card .card-cover { flex: 1; height: auto; }
  .video-card iframe { width: 100%; height: 100%; border: 0; display: block; }
  .video-badges {
    position: absolute;
    top: 10px; right: 10px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: flex-end;
  }
  .video-badges .el-badge { position: relative; font-size: .65em; padding: 4px 10px; }

  /* ── Empty state ────────────────────────────────────────────── */
  .empty-state {
    grid-column: 1 / -1;
    text-align: center;
    padding: 60px 20px;
    color: var(--muted);
    font-size: 1em;
    display: none;
  }
  .empty-state.visible { display: block; }

  /* ── Submit CTA ─────────────────────────────────────────────── */
  .cta-section {
    max-width: 1200px;
    margin: 0 30px 0 auto;
    background: var(--navy);
    padding: 30px 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
    border-top: 5px solid var(--gold);
  }
  .cta-text h2 { font-size: 1.6em; font-weight: 700; color: var(--white); margin-bottom: 8px; }
  .cta-text p  { font-size: .95em; color: rgba(255,255,255,.72); line-height: 1.6; max-width: 480px; }
  .cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: var(--gold);
    color: var(--navy);
    font-family: var(--font-body);
    font-size: .88em;
    font-weight: 700;
    letter-spacing: .07em;
    text-transform: uppercase;
    padding: 14px 28px;
    border-radius: 999px;
    border: none;
    cursor: pointer;
    transition: transform .2s, box-shadow .2s;
    white-space: nowrap;
    text-decoration: none;
  }
  .cta-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(219,170,0,.4); }
  .cta-btn .arrow { transition: transform .2s; }
  .cta-btn:hover .arrow { transform: translateX(4px); }

  /* ── Nav fix ────────────────────────────────────────────────── */
  #main-menu ul.sf-menu { display: flex; align-items: stretch; height: 34px; }
  #main-menu .sf-menu > li { display: flex; align-items: center; }
  #main-menu .sf-menu > li > a { display: flex !important; align-items: center; padding-top: 0 !important; padding-bottom: 0 !important; height: 100%; }

  /* ── Fade-in ────────────────────────────────────────────────── */
  @keyframes cardIn {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .account-card                    { animation: cardIn .5s ease both; }
  .account-card:nth-child(2)       { animation-delay: .07s; }
  .account-card:nth-child(3)       { animation-delay: .14s; }
  .account-card:nth-child(4)       { animation-delay: .21s; }
  .account-card:nth-child(5)       { animation-delay: .28s; }
  .account-card:nth-child(6)       { animation-delay: .35s; }

  /* ── Responsive ─────────────────────────────────────────────── */
  @media (max-width: 900px) {
    .cards-grid { grid-template-columns: repeat(2, 1fr); }
    .cta-section { flex-direction: column; align-items: flex-start; }
  }
  @media (max-width: 600px) {
    .intro-container { margin: 20px 20px 20px 0; }
    .filter-section, .cards-section, .cta-section { margin-right: 20px; margin-left: 0; }
    .cards-grid { grid-template-columns: 1fr; }
    .cta-section { padding: 30px 24px; }
  }
</style>

<!-- Intro bar -->
<div class="intro-container">
  <p><strong>Experiential learning looks different for every student.</strong> Browse stories from your peers, filter by EL type to find stories that resonate with your own path, or explore all five areas: Community Service, Study Abroad, Leadership, Internship, and Undergraduate Research.</p>
</div>

<!-- Filter bar -->
<div class="filter-section">
  <span class="filter-label">Filter by:</span>
  <button class="filter-btn active" data-tag="All">All</button>
  <button class="filter-btn" data-tag="Community Service">Community Service</button>
  <button class="filter-btn" data-tag="Study Abroad">Study Abroad</button>
  <button class="filter-btn" data-tag="Leadership">Leadership</button>
  <button class="filter-btn" data-tag="Internship">Internship</button>
  <button class="filter-btn" data-tag="Undergraduate Research">Undergraduate Research</button>
</div>

<!-- Cards grid -->
<div class="cards-section">
  <div class="cards-grid" id="elCardsGrid">

    <!-- Featured Video Card -->
    <div class="account-card video-card" data-tag="All">
      <div class="card-cover">
        <iframe src="https://www.youtube.com/embed/qVzpke873gM" title="Experiential Learning Story" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <div class="video-badges">
          <span class="el-badge community-service">Community Service</span>
          <span class="el-badge study-abroad">Study Abroad</span>
          <span class="el-badge leadership">Leadership</span>
          <span class="el-badge internship">Internship</span>
          <span class="el-badge undergraduate-research">Undergraduate Research</span>
        </div>
      </div>
    </div>

    <!-- Michelle Clark -->
    <div class="account-card"
      data-tag="Internship"
      data-name="Michelle Clark"
      data-meta="3rd Year · Environmental Systems Science"
      data-badge-class="internship"
      data-badge-label="Internship"
      data-img="/sites/success.ucmerced.edu/files/page/images/michelleclark.jpg"
      onclick="elOpenModal(this)">
      <div class="card-cover">
        <img src="/sites/success.ucmerced.edu/files/page/images/michelleclark.jpg" alt="Michelle Clark" />
        <span class="el-badge internship">Internship</span>
      </div>
      <div class="card-body">
        <div class="card-name">Michelle Clark</div>
        <div class="card-meta">
          <span class="card-meta-item">3rd Year</span>
          <span class="card-meta-item">Environmental Systems Science</span>
        </div>
        <div class="card-hint">Read their story →</div>
      </div>
    </div>

    <!-- Debora Alvarenga -->
    <div class="account-card"
      data-tag="Community Service"
      data-name="Debora Alvarenga"
      data-meta="2nd Year · Psychology (Health) and Minor in Sociology"
      data-badge-class="community-service"
      data-badge-label="Community Service"
      data-img="/sites/g/files/ufvvjh1776/f/images/debora-alvarenga.jpg"
      onclick="elOpenModal(this)">
      <div class="card-cover">
        <img src="/sites/g/files/ufvvjh1776/f/images/debora-alvarenga.jpg" alt="Debora Alvarenga" />
        <span class="el-badge community-service">Community Service</span>
      </div>
      <div class="card-body">
        <div class="card-name">Debora Alvarenga</div>
        <div class="card-meta">
          <span class="card-meta-item">2nd Year</span>
          <span class="card-meta-item">Psychology (Health) and Minor in Sociology</span>
        </div>
        <div class="card-hint">Read their story →</div>
      </div>
    </div>

    <!-- Alex Kuzmin -->
    <div class="account-card"
      data-tag="Study Abroad"
      data-name="Alex Kuzmin"
      data-meta="4th Year · Anthropology"
      data-badge-class="study-abroad"
      data-badge-label="Study Abroad"
      data-img="/sites/g/files/ufvvjh1776/f/images/alex-kuzmin.jpg"
      onclick="elOpenModal(this)">
      <div class="card-cover">
        <img src="/sites/g/files/ufvvjh1776/f/images/alex-kuzmin.jpg" alt="Alex Kuzmin" />
        <span class="el-badge study-abroad">Study Abroad</span>
      </div>
      <div class="card-body">
        <div class="card-name">Alex Kuzmin</div>
        <div class="card-meta">
          <span class="card-meta-item">4th Year</span>
          <span class="card-meta-item">Anthropology</span>
        </div>
        <div class="card-hint">Read their story →</div>
      </div>
    </div>

    <!-- Thomas Zhao -->
    <div class="account-card"
      data-tag="Undergraduate Research"
      data-name="Thomas Zhao"
      data-meta="4th Year · Mechanical Engineering"
      data-badge-class="undergraduate-research"
      data-badge-label="Undergraduate Research"
      data-img="/sites/g/files/ufvvjh1776/f/images/thomaszhao.jpg"
      onclick="elOpenModal(this)">
      <div class="card-cover">
        <img src="/sites/g/files/ufvvjh1776/f/images/thomaszhao.jpg" alt="Thomas Zhao" />
        <span class="el-badge undergraduate-research">Undergraduate Research</span>
      </div>
      <div class="card-body">
        <div class="card-name">Thomas Zhao</div>
        <div class="card-meta">
          <span class="card-meta-item">4th Year</span>
          <span class="card-meta-item">Mechanical Engineering</span>
        </div>
        <div class="card-hint">Read their story →</div>
      </div>
    </div>

    <!-- Empty state -->
    <div class="empty-state" id="elEmptyState">No accounts match that filter yet. Check back soon!</div>

  </div>
</div>

<!-- Story Modal Overlay -->
<div class="el-overlay" id="elOverlay">
  <div class="el-modal" id="elModal">

    <div class="el-modal-header">
      <div class="el-modal-header-info">
        <div class="el-modal-name" id="elModalName"></div>
        <div class="el-modal-meta" id="elModalMeta"></div>
        <span class="el-modal-badge" id="elModalBadge"></span>
      </div>
      <button class="el-modal-close" id="elCloseBtn">&#x2715;</button>
    </div>

    <div class="el-modal-cover" id="elModalCover">
      <img id="elModalImg" src="" alt="" />
    </div>

    <div class="el-modal-body">
      <div class="el-modal-story-label">Their Story</div>
      <p class="el-modal-story-text" id="elModalStory"></p>
    </div>

  </div>
</div>

<!-- Submit CTA -->
<div class="cta-section">
  <div class="cta-text">
    <h2>Share Your EL Story</h2>
    <p>Have you completed an experiential learning experience? Submit your account to be featured on this page and inspire the next generation of UC Merced students.</p>
  </div>
  <a class="cta-btn" href="https://docs.google.com/forms/d/e/1FAIpQLScd8BcdYejR4ZWIgXoy12C1yCDuFYFqGdWb4EKF5LXCu14-vg/viewform?usp=dialog" target="_blank">Submit Your Account <span class="arrow">&rarr;</span></a>
</div>

<script>
  var elStories = {
    'Michelle Clark': 'Most people are surprised when I tell them I am a solid B/C student. Classrooms have never really worked well for me as that learning environment made me feel anxious and even distracted. It was important to me when I got to college to find as many ways to learn and grow through other experiences beyond what my GPA could symbolize. I have done a lot of work outside of the classroom through seminars, hands on field experiences, and more to make the most of my college experience. Becoming part of the Yosemite Leadership Program Summer Internship was not only proof of how far I have come, but proof that there are other ways to learn that will bring you just as much success. No matter what you choose to do, you are going to have to put work into reaching your goals. You might as well enjoy that work! If I limited myself to working tirelessly to be perfect academically, I would have missed out on emotional, leadership, and professional growth. I now have options forward after college because of the learning and connections I made outside of the classroom.',
    'Debora Alvarenga': 'Engaging in experimental learning through community service allowed me to gain practical experience and connect with the community I currently call home while I attend UC Merced. I chose to engage beyond the classroom because I wanted to apply what I learn in a real-world setting while making a positive impact in our local community. Through my involvement with Bobcat Community Builders, I have had the opportunity to work with other students who are passionate about service and giving back. BCB has shown me the importance of listening to community needs and collaborating with others to make a positive impact. I have developed many skills such as communication, leadership, and problem solving that cannot always be learned in a classroom. This experience has helped me build confidence and a stronger sense of responsibility, and has allowed me to practice professionalism while working toward a common goal. This experience has strengthened my personal and professional values, preparing me to contribute more in my future career.',
    'Alex Kuzmin': 'I believe travel can truly make a person better: learning new perspectives, cultural traditions, and unique country histories. As an anthropology major, I am fascinated with how different cultures interact. I chose to study abroad in Barbados not only because of the gorgeous landscapes, but also to learn more about the history and everyday life of the island. After the completion of my program, I became more independent and even published a paper with the Undergraduate Research Journal at UC Merced based off my time in Barbados.',
    'Thomas Zhao': 'For me, I think I need more experience with lab work and some extra learning in a different way compared to the classroom. There is something more than class work and testing. Getting involved with research is more fun and more realistic compared to basic classroom studying. There is no dead requirement with exams but the experience and output which came out with the research is the bonus. This is way more fun compared to getting in a classroom for a semester, taking exams two or three times and getting past the class.'
  };

  function elCloseModal() {
    document.getElementById('elOverlay').classList.remove('el-open');
    document.body.style.overflow = '';
  }

  /* Use jQuery — already loaded by Drupal 7, survives onclick stripping */
  (function($) {
    $(document).ready(function() {

      /* Filter */
      $(document).on('click', '.filter-btn', function() {
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        var tag = $(this).data('tag');
        var visible = 0;
        $('#elCardsGrid .account-card').each(function() {
          var match = (tag === 'All' || $(this).data('tag') === tag);
          $(this).toggleClass('hidden', !match);
          if (match) visible++;
        });
        $('#elEmptyState').toggleClass('visible', visible === 0);
      });

      /* Card click */
      $(document).on('click', '#elCardsGrid .account-card:not(.video-card)', function() {
        var name       = $(this).data('name');
        var meta       = $(this).data('meta');
        var badgeLabel = $(this).data('badge-label');
        var badgeClass = $(this).data('badge-class');
        var img        = $(this).data('img');

        $('#elModalName').text(name);
        $('#elModalMeta').text(meta);
        $('#elModalStory').text(elStories[name] || '');
        $('#elModalBadge').text(badgeLabel).attr('class', 'el-modal-badge ' + badgeClass);
        $('#elModalImg').attr('src', img).attr('alt', name);
        $('#elModal').scrollTop(0);
        $('#elOverlay').addClass('el-open');
        $('body').css('overflow', 'hidden');
      });

      /* Close on backdrop click */
      $(document).on('click', '#elOverlay', function(e) {
        if (e.target === this) elCloseModal();
      });

      /* Close button */
      $(document).on('click', '#elCloseBtn', function() {
        elCloseModal();
      });

      /* Escape key */
      $(document).on('keydown', function(e) {
        if (e.key === 'Escape') elCloseModal();
      });

    });
  })(jQuery);
</script>