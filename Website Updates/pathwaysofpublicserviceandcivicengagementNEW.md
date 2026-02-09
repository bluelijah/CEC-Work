<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pathways to Public Service</title>
    <style>
        /* Modern styling inspired by OTS page */
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0 auto;
        }

        .pathways-intro {
            margin-bottom: 2rem;
            line-height: 1.6;
            color: #555;
            text-align: center;
        }

        .pathways-cta {
            text-align: center;
            margin: 2rem 0;
            padding: 2rem;
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
            border-radius: 12px;
            border: 2px solid #0077cc;
        }

        .pathways-cta h2 {
            color: #002856;
            margin-bottom: 1rem;
        }

        .pathways-cta a {
            display: inline-block;
            padding: 1em 2em;
            background: linear-gradient(135deg, #0077cc 0%, #005a99 100%);
            color: #fff;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 119, 204, 0.3);
        }

        .pathways-cta a:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 119, 204, 0.4);
        }

        .pathways-cta a.plain-email {
            all: unset;
            color: #0077cc;
            cursor: pointer;
            font-weight: normal;
            display: inline;
            text-decoration: underline;
        }

        .pathways-cta a.plain-email:hover {
            text-decoration: none;
            color: #005a99;
        }

        .section-headline {
            border-bottom: 2px solid #ffbf3c;
            padding-bottom: 8px;
            margin: 32px 0 24px;
            font-size: 1.4rem;
            color: #002856;
            text-align: center;
        }

        /* Accordion container */
        .accordion {
            margin: 0 auto;
            width: 100%;
        }

        .accordion ol {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .accordion li {
            margin: 16px 0 0 0;
            padding: 0;
        }

        /* Hide checkbox inputs */
        .accordion [type=checkbox] {
            display: none;
        }

        /* Accordion labels (headers) */
        .accordion label {
            display: block;
            font-size: 1.3rem;
            line-height: 1.4;
            padding: 1em 1.5em;
            margin: 0;
            cursor: pointer;
            background: linear-gradient(135deg, #002856 0%, #003d7a 100%);
            border: 2px solid #002856;
            border-radius: 8px;
            color: #FFF;
            font-weight: 700;
            text-transform: uppercase;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 40, 86, 0.2);
        }

        .accordion label:hover {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            border-color: #ffbf3c;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }

        .accordion [type=checkbox]:checked ~ label {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            border-color: #ffbf3c;
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }

        /* Accordion content */
        .acc_content {
            max-height: 0;
            overflow: hidden;
            padding: 0 1.5em;
            background: #fff;
            border: 2px solid transparent;
            border-radius: 8px;
            transition: all 0.4s ease;
            opacity: 0;
        }

        .accordion [type=checkbox]:checked ~ .acc_content {
            max-height: 2000px;
            opacity: 1;
            padding: 1.5em;
            margin-top: 8px;
            border-color: #e0e0e0;
            background: linear-gradient(135deg, #fffbf0 0%, #fff 100%);
        }

        .acc_content h4 {
            color: #002856;
            margin: 0 0 1.5rem 0;
            font-size: 1.1rem;
            line-height: 1.5;
        }

        /* Button grid for programs */
        .button-row {
            display: grid;
            gap: 1rem;
            grid-template-columns: 1fr;
            margin-bottom: 1.5rem;
        }

        @media (min-width: 600px) {
            .button-row {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (min-width: 900px) {
            .button-row {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        .volunteer {
            background: #fff;
            border: 2px solid #0077cc;
            border-radius: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 119, 204, 0.1);
        }

        .volunteer:hover {
            background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
            border-color: #002856;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 119, 204, 0.3);
        }

        .volunteer h4 {
            margin: 0;
            padding: 0;
        }

        .volunteer a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 3.5em;
            padding: 0.75em 1em;
            color: #0077cc;
            font-weight: 600;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .volunteer:hover a {
            color: #002856;
        }

        /* Examples list */
        ul.examples {
            margin: 1.5rem 0 0 0;
            padding: 0 0 0 1.5rem;
        }

        ul.examples li {
            display: list-item;
            list-style-type: square;
            padding: 0.5rem 0;
            font-size: 1rem;
            color: #555;
            line-height: 1.6;
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .pathways-page-container {
                margin-right: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="pathways-page-container">
        <div class="pathways-intro">
            <p>The pathways show all the different ways we can make a positive impact and support the common good. They often connect and overlap, reminding us that real change happens through collaboration and community. There isn't just one right way to get involved—people explore different paths at different times in their lives.</p>
        </div>

        <div class="pathways-cta">
            <p>Ready to discover your path? Take the <strong>Pathways to Public Service Assessment</strong> by clicking the link below. If you want to talk about your results or find new ways to get involved, we'd love to hear from you! Just send us a message at <a class="plain-email" href="mailto:communityservice@ucmerced.edu">communityservice@ucmerced.edu</a>.</p>
            <a href="https://stanforduniversity.qualtrics.com/jfe/form/SV_2sO52GgyYDCVUkm" target="_blank">Take the Pathways Survey</a>
        </div>

        <h2 class="section-headline">Explore the Pathways</h2>

        <p style="text-align: center; color: #555; margin-bottom: 2rem;">The UC Merced Community Engagement Center hopes to guide any interested students working on community service projects to incorporate these pathways. Please see below for more information.</p>

        <div class="accordion vertical">
            <ol class="acc_list">
                <li><input id="checkbox-1" type="checkbox" /> <label for="checkbox-1">Direct Service</label>
                    <div class="acc_content">
                        <h4>Working to address the immediate needs of individuals or a community, often involving contact with the people or places being served.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/campus-garden">UC Merced Campus Garden</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/Bright-Sparks-Program">Bright Spark Scholars Program</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/usda-food-distribution">USDA Food Distributions</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/events/kind-neighbor-farmers-market-22">Kind Neighbor Farmers Market</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/direct-service">Kids Discovery Station</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/collegecorps">CollegeCorps</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/d-street-shelter">D Street Shelter</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/remote-community-service-ideas">Virtual Service Opportunities</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Work with food banks to provide community programming and nutrition education.</li>
                            <li>Volunteer at a <strong>local food distribution</strong>.</li>
                            <li>Participate in a service year program (e.g., AmeriCorps, City Year, etc.) addressing <strong>inequity in access to community resources and funding</strong>.</li>
                            <li>Volunteering remotely</li>
                        </ul>
                    </div>
                </li>
                <li><input id="checkbox-2" type="checkbox" /> <label for="checkbox-2">Philanthropy</label>
                    <div class="acc_content">
                        <h4>Donating or using private funds or charitable contributions from individuals or institutions to contribute to the public good.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://www.mercedcaa.org/donate/">Merced County Community Action Agency</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.domesticshelters.org/fundraisers/wish-lists">Domestic Shelters Wishlists</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.cpedv.org/domestic-violence-organizations-california">Search for Local Shelters</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://sustainability.ucmerced.edu/initiatives/food/peoples-fridge">People's Fridge</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.bgcmerced.org/">Boys & Girls Club</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Donate to local <strong>domestic violence shelters</strong>.</li>
                            <li>Donate to your <strong>local mutual aid fund</strong>.</li>
                            <li>Commit to donate a percentage of your salary to <strong>youth mentoring organizations</strong>.</li>
                            <li>Donate your extra produce to <strong>Merced's People's Fridge</strong>.</li>
                        </ul>
                    </div>
                </li>
                <li><input id="checkbox-3" type="checkbox" /> <label for="checkbox-3">Community Organizing and Activism</label>
                    <div class="acc_content">
                        <h4>Involving, educating, and mobilizing individual or collective action to influence or persuade others.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">CALPIRG Students</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">99Rootz</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">NAACP Merced County</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Valley Natives for Change</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Planned Parenthood Youth Advisory Board</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Central Valley Justice Coalition</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://cec.ucmerced.edu/pathways/organizing-activism">Merced County ACCT Coalition</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Collaborate on a <strong>campaign event</strong> (knocking on doors, phone calls, tabling, etc.) to <strong>raise awareness</strong> about an issue you are passionate about.</li>
                            <li>Join a <strong>coalition</strong> to promote community activism.</li>
                            <li>Organize your peers through social media to promote a <strong>local community political campaign</strong>.</li>
                            <li>Create a <strong>petition</strong> for an issue you care about and work to get others to sign it.</li>
                        </ul>
                    </div>
                </li>
                <li><input id="checkbox-4" type="checkbox" /> <label for="checkbox-4">Community-Engaged Learning and Research</label>
                    <div class="acc_content">
                        <h4>Connecting coursework and academic research to community-identified concerns to enrich knowledge and inform action on social issues.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://kickitca.org/tobacco-control-community">Merced County Tobacco Control Program</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.unidosporsalud.org/">Unidos por Salud</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://california-health-collaborative.learnworlds.com/course/cvtcp-trainings">Central Valley Tobacco Control Policy Internship</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://recces.ucmerced.edu/">ReCCES</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://ssi.ucmerced.edu/">Student Success Internships</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.countyofmerced.com/3617/Read-and-Succeed">Read and Succeed</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://www.countyofmerced.com/3617/Read-and-Succeed">Merced County Library Adult Literacy Program</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.alldadsmattermerced.org/">All Dad's Matter Resource Center</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Partner with local agencies to <strong>survey or interview residents</strong> on the effects of recent local legislation that has passed.</li>
                            <li>Enroll in a program that combines <strong>coursework with field experience</strong> in community organizing around an issue you feel passionate about.</li>
                            <li>Evaluate the <strong>effectiveness</strong> of a program in your community that was created to address a <strong>local need</strong>.</li>
                        </ul>
                    </div>
                </li>
                <li><input id="checkbox-5" type="checkbox" /> <label for="checkbox-5">Policy and Governance</label>
                    <div class="acc_content">
                        <h4>Participating in political processes, policymaking, and public governance.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://www.countyofmerced.com/AgendaCenter">Merced County Agenda</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.countyofmerced.com/3227/Town-Hall-Meetings">Merced Student Town Halls</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://ballotpedia.org/Who_represents_me">Find Your Representatives Here</a></h4>
                            </div>
                        </div>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://journals.law.harvard.edu/jol/2016/10/24/a-beginners-guide-to-legislative-drafting/">Harvard: A Beginner's Guide to Legislative Drafting</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Attend or organize a <strong>political debate, forum, or town hall</strong> to discuss issues affecting your local community.</li>
                            <li><strong>Visit with your elected representative</strong> to discuss building community centers and spaces.</li>
                            <li><strong>Draft legislation</strong> related to a personal cause or passion.</li>
                        </ul>
                    </div>
                </li>
                <li><input id="checkbox-6" type="checkbox" /> <label for="checkbox-6">Social Entrepreneurship and Corporate Social Responsibility</label>
                    <div class="acc_content">
                        <h4>Using ethical business or private sector approaches to create or expand market-oriented responses to social or environmental problems.</h4>

                        <div class="button-row">
                            <div class="volunteer">
                                <h4><a href="https://ucmercedsbdc.com/">UC Merced Small Business Development Center</a></h4>
                            </div>

                            <div class="volunteer">
                                <h4><a href="https://www.unitedwaymerced.org/">United Way Merced</a></h4>
                            </div>
                        </div>

                        <ul class="examples">
                            <li>Participate in a class with a <strong>student-managed investment fund</strong> to invest in organizations that <strong>support public works like parks, libraries, and schools</strong>.</li>
                            <li>Work for a business to develop a <strong>product or technology</strong> that supports your community's <strong>small business owners</strong>.</li>
                            <li>Develop a <strong>lending project</strong> to help people in your community <strong>start small businesses</strong>.</li>
                        </ul>
                    </div>
                </li>
            </ol>
        </div>

        <p><strong>Source:</strong> Adapted from Stanford University's <a href="https://haas.stanford.edu/about/our-approach/pathways-public-service-and-civic-engagement" rel="noopener noreferrer" target="_blank">Haas Center for Public Service</a>.</p>
    </div>
</body>
</html>