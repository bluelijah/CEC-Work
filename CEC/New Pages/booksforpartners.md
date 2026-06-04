<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">.pb-wrap { font-family: 'Open Sans', sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; }

.pb-header { background: linear-gradient(135deg, #0f2d52 0%, #1a4a7a 100%); color: white; padding: 40px; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: left; }
.pb-header h1 { font-size: 2.2em; color: white !important; margin-bottom: 12px; }
.pb-header p { font-size: 1.05em; opacity: 0.95; max-width: 700px; margin: 0; line-height: 1.8; }

.pb-info { background: white; border-left: 5px solid #dbaa00; border-radius: 12px; padding: 25px 35px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); color: #555; font-size: 1.02em; }
.pb-info strong { color: #0f2d52; }
.pb-info a { color: #dbaa00; font-weight: 600; text-decoration: none; }
.pb-info a:hover { text-decoration: underline; }

.pb-carousel { background: white; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); padding: 40px 60px; margin-bottom: 30px; position: relative; }
.pb-track-wrapper { overflow: hidden; width: 100%; }
.pb-track { display: flex; transition: transform 0.5s ease; }

.pb-card { flex-shrink: 0; display: flex; flex-direction: column; align-items: center; padding: 10px 20px 20px; text-align: center; box-sizing: border-box; }
.pb-card-inner { display: flex; flex-direction: column; align-items: center; width: 500px; max-width: 100%; margin: 0 auto; }
.pb-cover { width: 200px; height: 290px; object-fit: cover; border-radius: 6px; box-shadow: 0 8px 25px rgba(0,0,0,0.2); margin-bottom: 25px; }
.pb-cover-placeholder { width: 200px; height: 290px; border-radius: 6px; box-shadow: 0 8px 25px rgba(0,0,0,0.2); margin-bottom: 25px; background: linear-gradient(135deg, #0f2d52, #1a4a7a); display: flex; align-items: center; justify-content: center; color: white; font-size: 0.85em; padding: 20px; text-align: center; }
.pb-title { font-size: 1.5em; font-weight: 700; color: #0f2d52; margin-bottom: 6px; }
.pb-author { font-size: 1.05em; color: #777; margin-bottom: 25px; }
.pb-btns { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; width: 100%; }

.pb-btn { display: inline-flex; align-items: center; justify-content: center; background: #dbaa00; color: #0f2d52 !important; padding: 12px 22px; text-decoration: none; border-radius: 6px; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.1); font-size: 0.98em; border: 2px solid #dbaa00; text-shadow: none; -webkit-font-smoothing: antialiased; }
.pb-btn:hover { background: #0f2d52; color: #dbaa00 !important; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); border-color: #0f2d52; }
.pb-btn:focus { outline: 3px solid #0f2d52; outline-offset: 2px; }

.pb-arrow { position: absolute; top: 50%; transform: translateY(-50%); background: #0f2d52; color: white; border: none; width: 44px; height: 44px; border-radius: 50%; font-size: 1.2em; cursor: pointer; transition: background 0.3s ease; display: flex; align-items: center; justify-content: center; z-index: 10; }
.pb-arrow:hover { background: #dbaa00; color: #0f2d52; }
.pb-arrow:focus { outline: 3px solid #dbaa00; outline-offset: 2px; }
.pb-arrow-prev { left: 12px; }
.pb-arrow-next { right: 12px; }

.pb-dots { display: flex; justify-content: center; gap: 8px; margin-top: 20px; }
.pb-dot { width: 10px; height: 10px; border-radius: 50%; background: #ccc; cursor: pointer; transition: background 0.3s; border: none; padding: 0; }
.pb-dot.pb-dot-active { background: #0f2d52; }
.pb-dot:focus { outline: 3px solid #0f2d52; outline-offset: 2px; }

.pb-counter { text-align: center; margin-top: 12px; color: #999; font-size: 0.9em; }

@media (max-width: 768px) {
  .pb-header { padding: 25px; margin: 0 15px 25px; }
  .pb-info { padding: 20px; margin: 0 15px 25px; }
  .pb-carousel { margin: 0 15px 25px; padding: 30px 40px; }
  .pb-card { padding: 10px 10px 20px; }
  .pb-btns { grid-template-columns: 1fr; }
  .pb-btn { width: 100%; }
}
</style>
<div class="pb-wrap">
	<div class="pb-header">
		<h1>Recommended Books for Community Partners</h1>

		<p>These books have been curated by the UC Merced Center for Community Engagement to support your work as a community partner. We hope they inspire and inform your continued impact.</p>
	</div>

	<div class="pb-info"><strong>How to access these books:</strong> Many of these titles are available to rent through the CEC. If you&#39;d prefer to purchase your own copy, we encourage you to buy through <a href="https://www.betterworldbooks.com" target="_blank">Better World Books (opens in new tab)</a> &mdash; a sustainable, socially conscious bookseller that donates a book for every one sold. Purchase links are included on each book below.</div>

	<div class="pb-carousel" role="region" aria-label="Book carousel"><button aria-label="Previous book" class="pb-arrow pb-arrow-prev" onclick="pbMove(-1)">&larr;</button><button aria-label="Next book" class="pb-arrow pb-arrow-next" onclick="pbMove(1)">&rarr;</button>

		<div class="pb-track-wrapper">
			<div class="pb-track" id="pbTrack"><!-- Book 1: Soul of a Citizen -->
				<div class="pb-card">
					<div class="pb-card-inner"><img alt="Soul of a Citizen cover" class="pb-cover" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" src="/sites/g/files/ufvvjh561/f/images/books/soul-of-a-citizen.png" />
						<div class="pb-cover-placeholder" style="display:none;">Cover Image</div>

						<div class="pb-title">Soul of a Citizen</div>

						<div class="pb-author">Paul Rogat Loeb</div>

						<div class="pb-btns"><a class="pb-btn" href="https://www.betterworldbooks.com/search/results?q=Soul%20of%20a%20Citizen" target="_blank">Purchase on Better World Books (opens in new tab)</a> <a class="pb-btn" href="mailto:communityservice@ucmerced.edu">Rent Through the CEC (opens email)</a></div>
					</div>
				</div>
				<!-- Book 2: Pathways of Social Impact -->

				<div class="pb-card">
					<div class="pb-card-inner"><img alt="Pathways of Social Impact cover" class="pb-cover" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" src="/sites/g/files/ufvvjh561/f/images/books/pathways-of-social-impact.png" />
						<div class="pb-cover-placeholder" style="display:none;">Cover Image</div>

						<div class="pb-title">Pathways of Social Impact</div>

						<div class="pb-author">Sean P. Crossland</div>

						<div class="pb-btns"><a class="pb-btn" href="https://www.betterworldbooks.com/search/results?q=Pathways%20of%20Social%20Impact" target="_blank">Purchase on Better World Books (opens in new tab)</a> <a class="pb-btn" href="mailto:communityservice@ucmerced.edu">Rent Through the CEC (opens email)</a></div>
					</div>
				</div>
			</div>
		</div>

		<div class="pb-dots" id="pbDots">&nbsp;</div>

		<div aria-live="polite" class="pb-counter" id="pbCounter">&nbsp;</div>
	</div>
</div>
<script>
(function() {
  var pbCurrent = 0;
  var pbTrack = document.getElementById('pbTrack');
  var pbWrapper = pbTrack.parentElement;
  var pbCards = pbTrack.querySelectorAll('.pb-card');
  var pbTotal = pbCards.length;
  var pbDotsEl = document.getElementById('pbDots');
  var pbCounterEl = document.getElementById('pbCounter');

  function pbSetWidths() {
    var w = pbWrapper.offsetWidth;
    pbCards.forEach(function(c) { c.style.width = w + 'px'; });
  }

  pbSetWidths();
  window.addEventListener('resize', pbSetWidths);

  for (var i = 0; i < pbTotal; i++) {
    var d = document.createElement('button');
    d.className = 'pb-dot' + (i === 0 ? ' pb-dot-active' : '');
    d.setAttribute('type', 'button');
    d.setAttribute('data-i', i);
    d.setAttribute('aria-label', 'Go to book ' + (i + 1) + ' of ' + pbTotal);
    d.setAttribute('aria-current', i === 0 ? 'true' : 'false');
    d.onclick = function() { pbGoTo(parseInt(this.getAttribute('data-i'))); };
    pbDotsEl.appendChild(d);
  }

  function pbUpdateUI() {
    pbTrack.style.transform = 'translateX(-' + (pbCurrent * pbWrapper.offsetWidth) + 'px)';
    pbDotsEl.querySelectorAll('.pb-dot').forEach(function(d, i) {
      d.classList.toggle('pb-dot-active', i === pbCurrent);
      d.setAttribute('aria-current', i === pbCurrent ? 'true' : 'false');
    });
    pbCounterEl.textContent = (pbCurrent + 1) + ' of ' + pbTotal;
  }

  function pbGoTo(index) {
    pbCurrent = (index + pbTotal) % pbTotal;
    pbUpdateUI();
  }

  window.pbMove = function(dir) { pbGoTo(pbCurrent + dir); };

  pbUpdateUI();
})();
</script>