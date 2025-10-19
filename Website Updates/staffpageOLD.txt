<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<style type="text/css">.staff {
            border-bottom: 2px solid #ffbf3c;
        }
        .card-container {
            display: grid;
            grid-template-columns: repeat(2, 325px);
            gap: 20px;
            padding: 20px;
            justify-content: center;
        }
        .flip-card {
            background-color: transparent;
            width: 325px;
            height: 434px;
            perspective: 1000px;
        }
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
        }
        .flip-card-front {
            background-color: #bbb;
            color: black;
        }
        .flip-card-back {
            background-color:#E5E5E5;
            color:#0F2D52;
            transform: rotateY(180deg);
        }
        .flip-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        #searchBar {
            width: 100%;
            max-width: 400px;
            padding: 10px;
            margin: 20px auto;
            display: block;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .filter-buttons {
            text-align: center;
            margin-bottom: 20px;
        }
        .filter-buttons button {
            margin: 5px;
            padding: 10px;
            border: none;
            cursor: pointer;
            background-color: #ffbf3c;
            color: white;
            border-radius: 5px;
        }
</style>
<!-- Centered Buttons -->
<div class="button-container"><button class="modal-btn" onclick="openModal('https://cec.ucmerced.edu/about-us')">About Us</button><button class="modal-btn" onclick="openModal('https://cec.ucmerced.edu/hours-and-location')">Hours &amp; Location</button></div>
<!-- Modal Structure -->

<div class="modal" id="pageModal">
	<div class="modal-content"><span class="close" onclick="closeModal()">&times;</span><iframe height="500px" id="modalFrame" src="" style="border: none;" width="100%"></iframe></div>
</div>
<!-- CSS for Button Styling & Centering -->
<style type="text/css">.button-container {
        display: flex;
        justify-content: center;
        gap: 15px; /* Space between buttons */
        margin-top: 20px;
    }

    .modal-btn {
        background-color: #ffbf3c; /* Gold color */
        color: black;
        font-size: 16px;
        font-weight: bold;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        min-width: 180px; /* Ensures both buttons have the same width */
        text-align: center;
    }

    .modal-btn:hover {
        background-color: #e6a700; /* Darker gold on hover */
        transform: scale(1.05);
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Modal Styles */
    .modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
    }

    .modal-content {
        background-color: white;
        margin: 10% auto;
        padding: 20px;
        width: 80%;
        max-width: 800px;
        border-radius: 10px;
    }

    .close {
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }
</style>
<!-- JavaScript for Modal --><script>
    function openModal(url) {
        document.getElementById("modalFrame").src = url;
        document.getElementById("pageModal").style.display = "block";
    }
    function closeModal() {
        document.getElementById("pageModal").style.display = "none";
        document.getElementById("modalFrame").src = "";
    }
</script>
<p><input id="searchBar" placeholder="Search by name, title, or email..." type="text" /></p>

<div class="filter-buttons"><button onclick="filterStaff('all')">All</button><button onclick="filterStaff('professional')">Professional Staff</button><button onclick="filterStaff('student')">CEC Student Staff</button><button onclick="filterStaff('driver')">Bright Sparks Student Staff</button></div>

<h3 class="staff" style="text-align: center;">Professional Staff</h3>

<div class="card-container" id="professional">
	<div class="flip-card" data-email="vdoty@ucmerced.edu" data-name="Vernette Doty" data-role="Director">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Vernette Doty" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/people/doty_vernette_f21_3.jpg" /></div>

			<div class="flip-card-back">
				<h1>Vernette Doty</h1>

				<p><strong>Director</strong></p>

				<p>vdoty@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths: Developer, Responsibility, Empathy, Harmony, Input</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="atafolla@ucmerced.edu" data-name="Andrea Tafolla" data-role="Associate Director">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Andrea Tafolla" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/people/tafolla_andrea_f21_2.jpg" /></div>

			<div class="flip-card-back">
				<h1>Andrea Tafolla</h1>

				<p><strong>Associate Director</strong></p>

				<p>atafolla@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths: Connectedness, Relator, Arranger, Individualization, Learner</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="colingage@ucmerced.edu" data-name="Colin Gage" data-role="Bright Spark Scholars Coordinator">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Colin Gage" src="/sites/cec.ucmerced.edu/files/documents/colin_gage_photo.jpg" /></div>

			<div class="flip-card-back">
				<h1>Colin Gage</h1>

				<p><strong>Bright Spark Scholars Coordinator</strong></p>

				<p>colingage@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>I work with student tutors, staff, and drivers to help provide tutoring to local Merced-area kids.</p>

				<div class="quote-strengths">
					<p>Strengths: Achiever, Learner, Arranger, Belief,&nbsp;Responsibility</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="pricillacardenas@ucmerced.edu" data-name="Pricilla Cardenas" data-role="Community Engagement Coordinator">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Pricilla Cardenas" src="/sites/cec.ucmerced.edu/files/documents/pricilla_headshot.jpg" /></div>

			<div class="flip-card-back">
				<h1>Pricilla Cardenas</h1>

				<p><strong>Community Engagement Coordinator</strong></p>

				<p>pricillacardenas@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths: Adaptability, Relator, Restorative, Positivity, Connectedness</p>
				</div>
			</div>
		</div>
	</div>
</div>

<h3 class="staff" style="text-align: center;">Community Engagement Center Student Staff</h3>

<div class="card-container" id="student">
	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Jason Avalos" data-role="Student Lead">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Jason Avalos" src="/sites/cec.ucmerced.edu/files/people/jason_resized.png" /></div>

			<div class="flip-card-back">
				<h1>Jason Avalos</h1>

				<p><strong>Student Lead</strong></p>

				<p>4th Year, Biology</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>Student Staff lead and long-term programs and operation student coordinator!</p>

				<div class="quote-strengths">
					<p>Strengths: Connectedness, Relator, Arranger, Individualization, Learner</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Veronica Diaz Fletes" data-role="Student Driver and Weekend Lead">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Veronica Diaz Fletes" src="/sites/cec.ucmerced.edu/files/people/veronica_resized.png" /></div>

			<div class="flip-card-back">
				<h1>Veronica Diaz Fletes</h1>

				<p><strong>Student Driver and Weekend Lead</strong></p>

				<p>3rd Year, Global Arts Studies Program</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>I am the Weekend Lead &amp; Driver, and help lead in weekend service events and provide transportation to students. I also work in the office helping with flyers, and Qualtrics forms!</p>

				<div class="quote-strengths">
					<p>Strengths:Coming soon!</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Stephanie Medina" data-role="Social Media &amp; Outreach">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Stephanie Medina" src="/sites/cec.ucmerced.edu/files/people/stephanie-medina.png" /></div>

			<div class="flip-card-back">
				<h1>Stephanie Medina</h1>

				<p><strong>Social Media &amp; Outreach</strong></p>

				<p>4th Year, Psychology</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths: Connectedness, Relator, Arranger, Individualization, Learner</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Michelle Clark" data-role="Service and Leadership Programs Student Assistant">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Michelle Clark" src="/sites/cec.ucmerced.edu/files/people/michelle.clark-s24.png" /></div>

			<div class="flip-card-back">
				<h1>Michelle Clark</h1>

				<p><strong>Service and Leadership Programs Student Assistant</strong></p>

				<p>2nd Year, Environmental System Sciences</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>I work in one- time service!&nbsp;That means&nbsp;I create and sometimes delegate to ensure all of our registration and promotion is ready to enable student volunteers.</p>

				<div class="quote-strengths">
					<p>Strengths:&nbsp;Communication, Context, Responsibility, Discipline, Strategic</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Leonardo Aleman Medina
" data-role="Service and Leadership Programs Student Assistant">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Leonardo Aleman Medina
" src="/sites/cec.ucmerced.edu/files/people/leo_fall2025.png" /></div>

			<div class="flip-card-back">
				<h1>Leonardo Aleman Medina</h1>

				<p><strong>Service and Leadership Programs Student Assistant</strong></p>

				<p>2nd year, Environmental Systems communityservice@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>I work as a student coordinator for the Public Service and Leadership Certificate program. This program is designed to get students more involved in community service and leadership!&nbsp;</p>

				<div class="quote-strengths">
					<p>Strengths:More info coming soon!</p>
				</div>
			</div>
		</div>
	</div>
</div>

<h3 class="staff" style="text-align: center;">Bright Spark Student Staff</h3>

<div class="card-container" id="driver">
	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Kasia Holland" data-role="Bright Spark Scholars Program Student Assistant">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Kasia Holland" src="/sites/cec.ucmerced.edu/files/people/kasia_fall_2025.jpeg" /></div>

			<div class="flip-card-back">
				<h1>Kasia Holland</h1>

				<p><strong>Bright Spark Scholars Program Student Assistant</strong></p>

				<p>3rd Year, Psychology</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job!</p>

				<p>I work for the long-term service project, Bright Spark Scholars Program, where I help manage some of the tutors by tracking their hours, driving them to the site, and more!</p>

				<div class="quote-strengths">
					<p>Strengths: Relator, Consistency, Futuristic, Harmony, Discipline</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Linsy De Leon" data-role="Bright Spark Scholars Program Student Assistant">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Linsy De Leon" src="/sites/cec.ucmerced.edu/files/people/person-placeholder.jpg" /></div>

			<div class="flip-card-back">
				<h1>Linsy De Leon</h1>

				<p><strong>Bright Spark Scholars Program Student Assistant</strong></p>

				<p>4th Year, Psychology</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths: Individualization, Significance, Command, Achiever, Woo</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Azelia Ibarra" data-role="Bright Spark Scholar Driver">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Azelia Ibarra" src="/sites/cec.ucmerced.edu/files/people/azelia_spring2025.jpg" /></div>

			<div class="flip-card-back">
				<h1>Azelia Ibarra</h1>

				<p><strong>Bright Spark Scholar Driver</strong></p>

				<p>More info coming soon!</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths:Futuristic, Positivity, Communication, Empathy and Focus</p>
				</div>
			</div>
		</div>
	</div>

	<div class="flip-card" data-email="communityservice@ucmerced.edu" data-name="Melina Ramirez" data-role="Bright Spark Scholar Driver">
		<div class="flip-card-inner">
			<div class="flip-card-front"><img alt="Melina Ramirez" src="/sites/cec.ucmerced.edu/files/people/melina_spring2025.jpg" /></div>

			<div class="flip-card-back">
				<h1>Melina Ramirez</h1>

				<p><strong>Bright Spark Scholar Driver</strong></p>

				<p>More info coming soon!</p>

				<p>communityservice@ucmerced.edu</p>

				<p>Get to know more about my job! Info coming soon!</p>

				<div class="quote-strengths">
					<p>Strengths:Input, Includer, Restorative, Learner, and Self-assurance</p>
				</div>
			</div>
		</div>
	</div>
</div>
<script>
        document.getElementById('searchBar').addEventListener('keyup', function () {
            let searchValue = this.value.toLowerCase();
            document.querySelectorAll('.flip-card').forEach(card => {
                let name = card.getAttribute('data-name').toLowerCase();
                let role = card.getAttribute('data-role').toLowerCase();
                let email = card.getAttribute('data-email').toLowerCase();
                if (name.includes(searchValue) || role.includes(searchValue) || email.includes(searchValue)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        function filterStaff(category) {
            document.querySelectorAll('.card-container').forEach(container => {
                container.style.display = category === 'all' || container.id === category ? 'grid' : 'none';
            });
        }
    </script>