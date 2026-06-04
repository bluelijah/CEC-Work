<!-- Thank you to https://supfort.com/pure-css-accordion-without-javascript --><!--
<style type="text/css">
  .accordion [type=radio], .accordion [type=checkbox] {
      display:none;
  }

  input {
    display: none;
  }

  .accordion label {
      display: block;
      font-size:25px;
      font-weight:700;
      padding: 8px 22px;
      margin: 0 0 1px 0;
      cursor: pointer;
      background: #002856;
      border-radius: 3px;
      color: #FFF;
      transition: ease .5s;
      text-transform:uppercase;
  }

  label:hover {
      background: #FFBF3C;
  }

  .acc_content {
      /* background: #E2E5F6; */
      padding: 10px 25px;
      border: 1px solid #A7A7A7;
      margin: 0 0 1px 0;
      border-radius: 3px;
  }

  input + label + .acc_content {
  	opacity: 0;
  	height: 0;
  	font-size: 0;
  	padding: 0 25px;
  	transition: ease .5s;
  }

  input:checked + label + .acc_content {
  	opacity: 1;
  	height: 200px;
  	font-size: 14px;
  	padding: 10px 25px;
  }

</style>

<div class="accordion vertical">

<input type="checkbox" name="checkbox-accordion" id="title1" />
<label for="title1">Community-Engaged Learning and Research</label>
  <div class="acc_content">
    <h4>Connecting coursework and academic research to community-identified concerns to enrich knowledge and inform action on social issues.</h4>
      <ul class="examples">
        <li>Partner with local agencies to survey or interview residents on the effects of recent local legislation that has passed.</li>
        <li>Enroll in a program that combines coursework with field experience in community organizing around an issue you feel passionate about.</li>
        <li>Review the literature on best practices regarding the election of local officials to create a position paper for an organization.</li>
        <li>Evaluate the effectiveness of a program in your community that was created to address a local need.</li>
        <li>Career option: Working as a researcher for your local college or university to explore the possible effects of large-scale access to post-secondary education on a local community.</li>
      </ul>
  </div>

<input type="checkbox" id="title2" />
<label for="title2">Philanthropy</label>
  <div class="acc_content">
    <h4>Involving, educating, and mobilizing individual or collective action to influence or persuade others.</h4>
      <ul class="examples">
        <li>Collaborate on a campaign event (knocking on doors, phone calls, tabling, etc.) to raise awareness about an issue you are passionate about.</li>
        <li>Join a coalition to promote comprehensive sex education.</li>
        <li>Organize your peers through social media to promote a campaign for an issue you are passionate about.</li>
        <li>Join a coalition to promote community activism.</li>
        <li>Organize your peers through social media to promote a local community political campaign.</li>
        <li>Create a petition for an issue you care about and work to get others to sign it.</li>
        <li>Career option: Working as an organizer for a city parks and recreation board or other civic organizations to educate and mobilize people about how to create new parks in your community.</li>
      </ul>
  </div>

<input type="checkbox" id="title3" />
<label for="title3">Community Organizing and Activism</label>
  <div class="acc_content">
    <h4>Working to address the immediate needs of individuals or a community, often involving contact with the people or places being served.</h4>
      <ul class="examples">
        <li>Participate in a service year program (e.g., AmeriCorps, City Year, etc.) addressing inequity in education access.</li>
        <li>Work with food banks to provide community programming and nutrition education.</li>
        <li>Volunteer on a community garden project.</li>
        <li>Participate in a service year program (e.g., AmeriCorps, City Year, etc.) addressing inequity in access to community resources and funding.</li>
        <li>Work with local government to organize block parties and community events.</li>
        <li>Volunteer to share your skills and train people in something you are good at.</li>
        <li>Career options: Working with Habitat for Humanity or other agencies to help organize home-building for low-income families in your neighborhood.</li>
        <li>Career options: Working with Boys and Girls Clubs or other agencies to mentor and tutor youth.</li>
      </ul>
  </div>

<input type="checkbox" id="title4" />
<label for="title4">Community-Engaged Learning and Research</label>
  <div class="acc_content">
    <h4>Donating or using private funds or charitable contributions from individuals or institutions to contribute to the public good.</h4>
      <ul class="examples">
        <li>Donate to local domestic violence shelters.</li>
        <li>Donate to your local mutual aid fund.</li>
        <li>Commit to donate a percentage of your salary to youth mentoring organizations.</li>
        <li>Donate your extra produce to Merced&rsquo;s People&rsquo;s Fridge.</li>
        <li>Donate to a charity drive that benefits low-income families in your neighborhood.</li>
        <li>Plan a crowd-funding campaign to provide backpacks for youth in foster care.</li>
        <li>Organize an auction or raffle to raise money for a cause you care about.</li>
        <li>Commit to donate a percentage of your salary to fundraising efforts for community events via your local government.</li>
        <li>Career option: Working as a program manager at a corporate business&#39;s foundation or other foundation and making grants to local arts organizations.</li>
      </ul>
  </div>

<input type="checkbox" id="title5" />
<label for="title5">Policy and Governance</label>
  <div class="acc_content">
    <h4>Participating in political processes, policymaking, and public governance.</h4>
      <ul class="examples">
        <li>Attend or organize a political debate, forum, or town hall to discuss issues affecting your local community.</li>
        <li>Visit with your elected representative to discuss building community centers and spaces.</li>
        <li>Draft legislation related to a personal cause or passion.</li>
        <li>Career option: Working as a city manager, elected official, legislative staff member, or in public works.</li>
      </ul>
  </div>

<input type="checkbox" id="title6" />
<label for="title6">Social Entrepreneurship and Corporate Social Responsibility</label>
  <div class="acc_content">
    <h4>Using ethical business or private sector approaches to create or expand market-oriented responses to social or environmental problems. </h4>
      <ul class="examples">
        <li>Participate in a class with a student-managed investment fund to invest in organizations that support public works like parks, libraries, and schools.</li>
        <li>Work for a business to develop a product or technology that supports your community&#39;s small business owners.</li>
        <li>Develop a lending project to help people in your community start small businesses.</li>
        <li>Career option: Working with a nonprofit team that generates funds to support your local community and its needs.</li>
      </ul>
  </div>

</div>
--><!-- Thank you to https://mraffaele.com/posts/2011/10/25/css-accordion-no-javascript/ -->
<p>The pathways show all the different ways we can make a positive impact and support the common good. They often connect and overlap, reminding us that real change happens through collaboration and community. There isn&rsquo;t just one right way to get involved&mdash;people explore different paths at different times in their lives.</p>

<p>Ready to discover your path? Take the <strong>Pathways to Public Service Assessment</strong> by clicking the link below. If you want to talk about your results or find new ways to get involved, we&rsquo;d love to hear from you! Just send us a message at <a href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a>.</p>

<h2 style="text-align: center;"><a href="https://stanforduniversity.qualtrics.com/jfe/form/SV_2sO52GgyYDCVUkm" target="_blank"><strong><em>Pathways to Public Service Survey&nbsp;</em></strong></a></h2>

<p>The UC Merced Community Engagement Center hopes to guide any interested students working on community service projects to incorporates these pathways. Please see below for more information.</p>
<style type="text/css">.accordion {
      /* font-family:Arial, Helvetica, sans-serif; */
      margin:0 auto;
      font-size:14px;
      /* border:1px solid #002856; */
      /* border-radius:10px; */
      width:100%;
      /* padding:10px; */
      background:#fff;
  }
  .accordion ol {
      /* list-style:none; */
      margin:0;
      padding:0;
  }
  .accordion li {
      margin:0;
      padding:0;
  }
  .accordion [type=radio], .accordion [type=checkbox] {
      display:none;
  }
  .accordion label {
      display:block;
      font-size:23px; /* of each title per accordion band */
      line-height:35px; /* of each accordion band */
      background:	#002856;
      border:1px solid #542437;
      color:	#FFF;
      text-shadow:1px 1px 1px rgba(255,255,255,0.3);
      font-weight:700; /* thickness */
      cursor:pointer;
      text-transform:uppercase;
      -webkit-transition: all .2s ease-out;
      -moz-transition: all .2s ease-out;
      border-radius: 3px;
  }
  .accordion ol li label:hover, .accordion [type=radio]:checked ~ label, .accordion [type=checkbox]:checked ~ label {
      background: #FFBF3C;
      /* color:#002856; */
      text-shadow:1px 1px 1px rgba(0,0,0,0.5)
  }
  .accordion .acc_content {
      padding:0 10px;
      overflow:hidden;
      border:1px solid #FFF; /* Make the border match the background so it fades in nicely */
      -webkit-transition: all .5s ease-out;
      -moz-transition: all .5s ease-out;
      border-radius: 3px;
  }
  .accordion p {
      /* color:#002856; */
      /* margin:0 0 10px; */
  }
  .accordion h4 {
      /* color:#002856; */
      padding:0;
      /* margin:10px 0;*/
  }

  /* Vertical */
  /* .vertical ul li {
      overflow:hidden;
      margin:0 0 1px;
  }*/
  .vertical ol li label {
      padding:10px;
  }
  .vertical [type=radio]:checked ~ label, .vertical [type=checkbox]:checked ~ label {
      border-bottom:0;
  }
  .vertical ol li label:hover {
      border:1px solid #002856; /* We don't want the border to disappear on hover */
  }
  .vertical ol li .acc_content {
      height:0px;
      border-top:0;
  }
  .vertical [type=radio]:checked ~ label ~ .acc_content, .vertical [type=checkbox]:checked ~ label ~ .acc_content {
      height:100%;
      border:1px solid #542437;
  }
  ul.examples {
    margin: 5px;
    padding: 5px;
  }
  ul.examples li {
    display: list-item;
    list-style-type: square;
    /* margin: 5px; */
    padding: 5px;
    font-size: 16px;
  }
  .accordion [type=radio], .accordion [type=checkbox] {
      display:none;
  }
</style>
<style type="text/css">.side1{
    float: left;
    padding: 10px;
    margin-left: 75px;
  }
  .side2{
    float: right;
    clear: right;
    padding: 10px;
    margin-right: 150px;
  }
  .vst {
    background-color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    font-weight: 550;
    text-transform: uppercase !important;
    border-style: solid;
    border-color:	#002856;
    padding: 10px;
    margin-bottom: 10px;
  }
  .vst:hover {
    border-style: solid;
    border-color:	#FFBF3C;
  }
  .vst a {
    color: #002856 !important;
    text-decoration: none !important;
  }
</style>
<style type="text/css">.button-row {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-bottom: 10px;
  }
  .volunteer {
    background-color: white;
    padding: 10px 32px 5px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    font-weight: 550;
    text-transform: uppercase !important;
    margin-left: 10px;
    margin-right: 10px;
    border: 2px solid	#FFBF3C;
  }
  .volunteer:hover {
    border-color:	#002856;
  }
  .volunteer h4 {
    text-color: #002856 !important;
  }
  .volunteer a {
    text-decoration: none !important;
  }
</style>
<div class="accordion vertical">
	<ol class="acc_list">
		<li><input id="checkbox-1" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-1">Direct Service</label>
			<div class="acc_content">
				<h4>Working to address the immediate needs of individuals or a community, often involving contact with the people or places being served.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/campus-garden">UC Merced Campus Garden </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/Bright-Sparks-Program">Bright Spark Scholars Program </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/usda-food-distribution">USDA Food Distributions </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/events/kind-neighbor-farmers-market-22">Kind Neighbor Farmers Market </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/direct-service">Kids Discovery Station </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/collegecorps">CollegeCorps</a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/d-street-shelter">D Street Shelter </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/remote-community-service-ideas">Virtual Service Opportunities </a></h4>
					</div>
				</div>

				<ul class="examples">
					<li>Work with food banks to provide community programming and nutrition education.</li>
					<li>Volunteer at a <strong>local food distribution</strong>.</li>
					<li>Participate in a service year program (e.g., AmeriCorps, City Year, etc.) addressing <strong>inequity in access to community resources and funding</strong>.</li>
					<!-- <li>Work with local government to organize <strong>block parties and community events</strong>.</li>
      			<li>Volunteer to <strong>share your skills and train people</strong> in something you are good at.</li>
      			<li><u>Career options</u>: Working with Habitat for Humanity or other agencies to help organize <strong>home-building for low-income families</strong> in your neighborhood.</li>
      			<li><u>Career options</u>: Working with Boys and Girls Clubs or other agencies to <strong>mentor and tutor youth</strong>.</li> -->
					<li>Volunteering remotely</li>
				</ul>
			</div>
		</li>
		<li><input id="checkbox-2" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-2">Philanthropy</label>
			<div class="acc_content">
				<h4>Donating or using private funds or charitable contributions from individuals or institutions to contribute to the public good.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://www.mercedcaa.org/donate/">Merced County Community Action Agency </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.domesticshelters.org/fundraisers/wish-lists">Domestic Shelters Wishlists </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.cpedv.org/domestic-violence-organizations-california">Search for Local Shelters </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://sustainability.ucmerced.edu/initiatives/food/peoples-fridge">People&#39;s Fridge </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://www.bgcmerced.org/">Boys &amp; Girls Club </a></h4>
					</div>
				</div>

				<ul class="examples">
					<li>Donate to local <strong>domestic violence shelters</strong>.</li>
					<li>Donate to your <strong>local mutual aid fund</strong>.</li>
					<li>Commit to donate a percentage of your salary to <strong>youth mentoring organizations</strong>.</li>
					<li>Donate your extra produce to <strong>Merced&rsquo;s People&rsquo;s Fridge</strong>.</li>
					<!-- <li>Donate to a <strong>charity drive</strong> that benefits <strong>low-income families</strong> in your neighborhood.</li>
            <li>Plan a crowd-funding campaign to provide <strong>backpacks for youth in foster care</strong>.</li>
            <li>Organize an <strong>auction or raffle</strong> to raise money for a cause you care about.</li>
            <li>Commit to donate a percentage of your salary to fundraising efforts for <strong>community events</strong> via your local government.</li>
            <li><u>Career option</u>: Working as a program manager at a corporate business&#39;s foundation or other foundation and <strong>making grants to local arts organizations</strong>.</li> --></ul>
			</div>
		</li>
		<li><input id="checkbox-3" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-3">Community Organizing and Activism</label>
			<div class="acc_content">
				<h4>Involving, educating, and mobilizing individual or collective action to influence or persuade others.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">CALPIRG Students </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">99Rootz </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">NAACP Merced County </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Valley Natives for Change </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Planned Parenthood Youth Advisory Board </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Central Valley Justice Coalition </a></h4>
					</div>
				</div>

				<div class="volunteer">
					<h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Merced County A Community Counteracting Tobacco (ACCT) Coalition </a></h4>
				</div>

				<ul class="examples">
					<li>Collaborate on a <strong>campaign event</strong> (knocking on doors, phone calls, tabling, etc.) to <strong>raise awareness</strong> about an issue you are passionate about.</li>
					<li>Join a <strong>coalition</strong> to promote community activism.</li>
					<!-- <li>Join a coalition to promote comprehensive <strong>sex education</strong>.</li> --><!-- <li>Organize your peers through <strong>social media</strong> to promote a campaign for an issue you are passionate about.</li> -->
					<li>Organize your peers through social media to promote a <strong>local community political campaign</strong>.</li>
					<li>Create a <strong>petition</strong> for an issue you care about and work to get others to sign it.</li>
					<!-- <li><u>Career option</u>: Working as an organizer for a city parks and recreation board or other <strong>civic organizations</strong> to educate and mobilize people about how to <strong>create new parks</strong> in your community.</li> --></ul>
			</div>
		</li>
		<li><input id="checkbox-4" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-4">Community-Engaged Learning and Research</label>
			<div class="acc_content">
				<h4>Connecting coursework and academic research to community-identified concerns to enrich knowledge and inform action on social issues.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://kickitca.org/tobacco-control-community">Merced County Tobacco Control Program </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://www.unidosporsalud.org/">Unidos por Salud </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://california-health-collaborative.learnworlds.com/course/cvtcp-trainings">Central Valley Tobacco Control Policy Internship </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://recces.ucmerced.edu/">The Resource Center for Community Engaged Scholarship (ReCCES) </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://ssi.ucmerced.edu/">Student Success Internships </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.countyofmerced.com/3617/Read-and-Succeed">Read and Succeed </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://www.countyofmerced.com/3617/Read-and-Succeed">Merced County Library Adult Literacy Program </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.alldadsmattermerced.org/">All Dad&#39;s Matter Resource Center </a></h4>
					</div>
				</div>

				<ul class="examples">
					<li>Partner with local agencies to <strong>survey or interview residents</strong> on the effects of recent local legislation that has passed.</li>
					<li>Enroll in a program that combines <strong>coursework with field experience</strong> in community organizing around an issue you feel passionate about.</li>
					<!-- <li>Review the literature on best practices regarding the election of local officials to <strong>create a position paper</strong> for an organization.</li> -->
					<li>Evaluate the <strong>effectiveness</strong> of a program in your community that was created to address a <strong>local need</strong>.</li>
					<!-- <li><u>Career option</u>: Working as a <strong>researcher</strong> for your local college or university to explore the possible effects of <strong>large-scale access to post-secondary education</strong> on a local community.</li> --></ul>
			</div>
		</li>
		<li><input id="checkbox-5" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-5">Policy and Governance</label>
			<div class="acc_content">
				<h4>Participating in political processes, policymaking, and public governance.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://www.countyofmerced.com/AgendaCenter">Merced County Agenda </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.countyofmerced.com/3227/Town-Hall-Meetings">Merced Student Town Halls </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://ballotpedia.org/Who_represents_me">Find Your Representatives Here </a></h4>
					</div>
				</div>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://journals.law.harvard.edu/jol/2016/10/24/a-beginners-guide-to-legislative-drafting/">Harvard: A Beginner&rsquo;s Guide to Legislative Drafting </a></h4>
					</div>
				</div>

				<ul class="examples">
					<li>Attend or organize a <strong>political debate, forum, or town hall</strong> to discuss issues affecting your local community.</li>
					<li><strong>Visit with your elected representative</strong> to discuss building community centers and spaces.</li>
					<li><strong>Draft legislation</strong> related to a personal cause or passion.</li>
					<!-- <li><u>Career option</u>: Working as a city manager, elected official, legislative staff member, or in public works.</li> --></ul>
			</div>
		</li>
		<li><input id="checkbox-6" name="checkbox-accordion" type="checkbox" /> <label for="checkbox-6">Social Entrepreneurship and Corporate Social Responsibility</label>
			<div class="acc_content">
				<h4>Using ethical business or private sector approaches to create or expand market-oriented responses to social or environmental problems.</h4>

				<div class="button-row">
					<div class="volunteer">
						<h4><a href="https://ucmercedsbdc.com/">UC Merced Small Business Development Center </a></h4>
					</div>

					<div class="volunteer">
						<h4><a href="https://www.unitedwaymerced.org/">United Way Merced </a></h4>
					</div>
				</div>

				<ul class="examples">
					<li>Participate in a class with a <strong>student-managed investment fund</strong> to invest in organizations that <strong>support public works like parks, libraries, and schools</strong>.</li>
					<li>Work for a business to develop a <strong>product or technology</strong> that supports your community&#39;s <strong>small business owners</strong>.</li>
					<li>Develop a <strong>lending project</strong> to help people in your community <strong>start small businesses</strong>.</li>
					<!-- <li><u>Career option</u>: Working with a <strong>nonprofit team that generates funds</strong> to support your local community and its needs.</li> --></ul>
			</div>
		</li>
	</ol>
</div>
<!-- <h4>If any of the above applies to you, please feel free to fill out this interest form:</h4>

<div class="sb-row">
	<div class="sb-col hb__buttons-gold span4"><a class="btn--invert-gold hb__play" href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_eXIEdStI9Miketo" style="width:50%">Pathways Interest Form</a></div>
</div> -->

<section style="text-align: center; margin: 2em 0;">
	<h2 style="margin-bottom: 0.5em;">Explore the Pathways Worksheet</h2>

	<h4 style="margin-bottom: 0.5em; text-align: left;">Learn more about different pathways to public service and civic engagement by reviewing our interactive worksheet.</h4>
	<iframe frameborder="0" height="480" scrolling="no" src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/documents/pathwaysworksheet.pdf" style="border: 1px solid #ccc; border-radius: 8px; display: block; margin: 0 auto;" title="Pathways Worksheet PDF" width="640"></iframe>

	<p style="margin-top: 2em; font-size: 0.95em;"><strong>Source:</strong> Adapted from Stanford University&rsquo;s <a href="https://haas.stanford.edu/about/our-approach/pathways-public-service-and-civic-engagement" rel="noopener noreferrer" target="_blank">Haas Center for Public Service</a>.</p>
</section>