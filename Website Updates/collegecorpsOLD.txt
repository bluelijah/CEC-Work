<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Corps - UC Merced</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        .cc-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 0 20px;
        }
        
        /* Hero Section */
        .cc-hero {
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .cc-hero img {
            width: 100%;
            height: auto;
            display: block;
        }
        
        /* Divider Line */
        .cc-divider {
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #002856 0%, #FFBF3C 50%, #002856 100%);
            margin: 60px 0;
        }
        
        /* Section Styles */
        .cc-section {
            padding: 60px 20px;
            background: white;
        }
        
        .cc-section-alt {
            background: #f8f9fa;
        }
        
        .cc-section-title {
            font-size: 2.5em;
            color: #002856;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 700;
        }
        
        .cc-section-text {
            font-size: 1.1em;
            line-height: 1.8;
            color: #555;
            max-width: 900px;
            margin: 0 auto 30px;
            text-align: center;
        }
        
        .cc-section-text strong {
            color: #002856;
            font-weight: 700;
        }
        
        /* Video Container */
        .cc-video-container {
            text-align: center;
            margin: 40px 0;
        }
        
        .cc-video-container iframe {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        
        /* Focus Areas */
        .cc-focus-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0;
            margin-top: 40px;
            max-width: 1100px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .cc-focus-card {
            background: transparent;
            padding: 20px 15px;
            border-radius: 0;
            box-shadow: none;
            text-align: center;
            transition: none;
            border-top: 0;
            border-right: 3px solid #FFBF3C;
            position: relative;
        }
        
        .cc-focus-card:last-child {
            border-right: none;
        }
        
        .cc-focus-card:hover {
            transform: none;
            box-shadow: none;
        }
        
        .cc-focus-card h3 {
            color: #002856;
            font-size: 1.2em;
            margin-bottom: 0;
            font-weight: 700;
            line-height: 1.3;
        }
        
        /* Goals Section */
        .cc-goals-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            margin-top: 50px;
        }
        
        .cc-goal-card {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .cc-goal-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }
        
        .cc-goal-number {
            font-size: 2em;
            color: #FFBF3C;
            font-weight: 700;
            margin-bottom: 15px;
        }
        
        .cc-goal-image {
            width: 100%;
            height: 200px;
            background-size: cover;
            background-position: center;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .cc-goal-text {
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
        }
        
        /* Accordion Styles */
        .cc-accordion-item {
            margin-bottom: 15px;
        }
        
        .cc-accordion-header {
            width: 100%;
            background-color: #002856;
            color: white;
            padding: 20px;
            text-align: left;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .cc-accordion-header:hover {
            background-color: #0f2d52;
        }
        
        .cc-accordion-header.active {
            background-color: #FFBF3C;
            color: #000;
        }
        
        .cc-accordion-icon {
            transition: transform 0.3s ease;
        }
        
        .cc-accordion-header.active .cc-accordion-icon {
            transform: rotate(180deg);
        }
        
        .cc-accordion-content {
            display: none;
            padding: 25px;
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 0 0 8px 8px;
            margin-top: -5px;
        }
        
        .cc-accordion-content h3 {
            color: #002856;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        
        .cc-accordion-content ul {
            margin-left: 30px;
            margin-bottom: 15px;
        }
        
        .cc-accordion-content li {
            margin-bottom: 10px;
            line-height: 1.6;
        }
        
        /* Cohort Selector */
        .cc-cohort-selector-container {
            max-width: 800px;
            margin: 40px auto;
            text-align: center;
        }
        
        .cc-cohort-selector-label {
            font-size: 1.3em;
            color: #002856;
            font-weight: 700;
            margin-bottom: 15px;
            display: block;
        }
        
        .cc-cohort-select {
            width: 100%;
            max-width: 400px;
            padding: 15px 20px;
            font-size: 1.1em;
            border: 3px solid #002856;
            border-radius: 8px;
            background: white;
            color: #002856;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .cc-cohort-select:hover {
            border-color: #FFBF3C;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .cc-cohort-select:focus {
            outline: none;
            border-color: #FFBF3C;
            box-shadow: 0 0 0 3px rgba(255, 191, 60, 0.2);
        }
        
        .cc-cohort-content {
            display: none;
            margin-top: 40px;
            padding: 40px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            animation: fadeIn 0.5s ease-in-out;
        }
        
        .cc-cohort-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .cc-cohort-title {
            font-size: 2em;
            color: #002856;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 700;
        }
        
        .cc-cohort-stats {
            margin: 30px 0;
        }
        
        .cc-cohort-stats ul {
            list-style: none;
            padding: 0;
        }
        
        .cc-cohort-stats li {
            padding: 15px;
            margin-bottom: 10px;
            background: #f8f9fa;
            border-left: 5px solid #FFBF3C;
            border-radius: 5px;
            font-size: 1.1em;
        }
        
        .cc-cohort-stats ul ul {
            margin-top: 10px;
            margin-left: 20px;
        }
        
        .cc-cohort-stats ul ul li {
            font-size: 1em;
            background: white;
            border-left-color: #002856;
        }
        
        /* Button Styles */
        .cc-btn {
            display: inline-block;
            padding: 15px 40px;
            background: #FFBF3C;
            color: #002856;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 1.1em;
            transition: all 0.3s ease;
            border: 3px solid #FFBF3C;
            cursor: pointer;
            margin: 10px;
        }
        
        .cc-btn:hover {
            background: #002856;
            color: white;
            border-color: #002856;
            transform: scale(1.05);
        }
        
        .cc-btn-secondary {
            background: white;
            color: #002856;
            border: 3px solid #002856;
        }
        
        .cc-btn-secondary:hover {
            background: #002856;
            color: white;
        }
        
        .cc-map-container {
            text-align: center;
            margin: 30px 0;
        }
        
        .cc-map-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        
        /* Footer Section */
        .cc-footer {
            background: #002856;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        
        .cc-footer a {
            color: #FFBF3C;
            text-decoration: none;
            font-weight: 600;
        }
        
        .cc-footer a:hover {
            color: #ffd666;
            text-decoration: underline;
        }
        
        /* Mobile Responsive */
        @media (max-width: 768px) {
            .cc-container {
                padding: 0 15px;
            }
            
            .cc-hero img {
                width: 100%;
                height: auto;
            }
            
            .cc-section {
                padding: 40px 15px;
            }
            
            .cc-section-title {
                font-size: 2em;
            }
            
            .cc-focus-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .cc-focus-card {
                border-right: none;
                border-bottom: 2px solid #FFBF3C;
                padding: 15px 10px;
            }
            
            .cc-focus-card:nth-child(2),
            .cc-focus-card:nth-child(4) {
                border-right: none;
            }
            
            .cc-focus-card h3 {
                font-size: 1em;
            }
            
            .cc-goals-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .cc-goal-card {
                padding: 25px;
            }
            
            .cc-cohort-content {
                padding: 20px;
            }
            
            .cc-video-container iframe {
                width: 100%;
                height: 250px;
            }
        }
    </style>
</head>
<body>

    <!-- Hero Section -->
    <div class="cc-hero">
        <img src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/college_corps_main_page.png" alt="College Corps">
    </div>

    <!-- What is College Corps Section -->
    <div class="cc-section">
        <div class="cc-container">
            <h2 class="cc-section-title">What is College Corps?</h2>
            
            <p class="cc-section-text">
                <strong>The #CaliforniansForAll College Corps will help create debt-free pathways to college while engaging students across the state in solving problems in their communities.</strong>
            </p>
            
            <p class="cc-section-text">
                #CaliforniansForAll College Corps is part of Governor Gavin Newsom's initiative to promote community service. Managed by California Volunteers, Office of the Governor, and partnered with colleges, it helps diverse students graduate on time with less debt. The program develops future civic leaders by engaging students in community service, building leadership skills, and reducing college costs. Fellows work with organizations focused on K-12 & Community Education, Food Security, Climate Action, and Public Health. As an AmeriCorps program, it follows AmeriCorps guidelines where applicable.
            </p>
            
            <div class="cc-video-container">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/jRgHjsgR4iQ?si=UjJS6j5ulTTv1uGH" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
    </div>

    <div class="cc-divider"></div>

    <!-- Focus Areas Section -->
    <div class="cc-section cc-section-alt">
        <div class="cc-container">
            <h2 class="cc-section-title">Focus Areas</h2>
            
            <p class="cc-section-text">
                Communities will benefit from the support of College Corps Fellows in tackling California's most pressing challenges. Fellows will serve in nonprofit and governmental organizations in four primary focus areas identified by California Volunteers:
            </p>
            
            <div class="cc-focus-grid">
                <div class="cc-focus-card">
                    <h3>Climate Action</h3>
                </div>
                
                <div class="cc-focus-card">
                    <h3>K-12 & Community Education</h3>
                </div>
                
                <div class="cc-focus-card">
                    <h3>Food Security</h3>
                </div>
                
                <div class="cc-focus-card">
                    <h3>Public Health</h3>
                </div>
            </div>
        </div>
    </div>

    <div class="cc-divider"></div>

    <!-- Goals Section -->
    <div class="cc-section">
        <div class="cc-container">
            <h2 class="cc-section-title">College Corps Goals</h2>
            
            <div class="cc-goals-grid">
                <div class="cc-goal-card">
                    <div class="cc-goal-number">Goal 1</div>
                    <div class="cc-goal-image" style="background-image: url('https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/1.png');"></div>
                    <p class="cc-goal-text">Develop a generation of socially conscious leaders capable of bridging divides and addressing challenges.</p>
                </div>
                
                <div class="cc-goal-card">
                    <div class="cc-goal-number">Goal 2</div>
                    <div class="cc-goal-image" style="background-image: url('https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/2.png');"></div>
                    <p class="cc-goal-text">Support low- to moderate-income students in graduating from college on time and with reduced debt.</p>
                </div>
                
                <div class="cc-goal-card">
                    <div class="cc-goal-number">Goal 3</div>
                    <div class="cc-goal-image" style="background-image: url('https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/3.png');"></div>
                    <p class="cc-goal-text">Tackle social issues and contribute to the creation of more equitable communities throughout California.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="cc-divider"></div>

    <!-- College Corps at UC Merced Section -->
    <div class="cc-section cc-section-alt">
        <div class="cc-container">
            <h2 class="cc-section-title">College Corps at UC Merced</h2>
            
            <!-- Benefits Accordion -->
            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Benefits</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <h3><strong>UC Merced Cohort Experience</strong></h3>
                    
                    <p>All Fellows who complete their 450-hour term of service will receive a total maximum financial benefit of $10,000 paid in the form of a living allowance during service, plus an educational award upon completion of required service hours.</p>
                    
                    <p>Ensuring that Fellows from the UC Merced Cohort feel a shared sense of identity and a common sense of purpose is a priority for the College Corps Program. It aims to promote the following priority outcomes through the Cohort experience.</p>
                    
                    <p>To advance these outcomes, UC Merced College Corps Program will offer Fellows the opportunity to participate in the following activities and events:</p>
                    
                    <ul>
                        <li><u>Lunch & Learn Lesson Workshops</u> are designed to enhance skills and share knowledge in an informal setting, fostering networking and collaboration. Held during lunch hours, these workshops fit easily into busy schedules, offering an engaging, interactive learning experience that's less formal than traditional training. They also provide a beneficial break from routine, promoting overall well-being, while keeping participants updated on relevant topics. Additionally, they are a cost-effective and low-disruption way to support continuous learning and growth.</li>
                        <li><u>PODS (Peers of Development & Support)</u> are designed to facilitate mutual growth and support among individuals within the program. It provides a structured environment where peers can share experiences, offer feedback, and support each other's development. The primary goals include fostering a collaborative learning culture, enhancing personal and professional growth through peer interactions, and building a supportive network that helps individuals navigate challenges and achieve their goals. By promoting open communication and collective problem-solving, PODS contribute to a more engaged and cohesive community.</li>
                        <li><u>A Personal Learning Plan:</u> One of California Volunteers initiative goals consist of the following: strives to create a generation of civic-minded leaders with the ability to bridge divides and solve. In pursuit of this goal, UC Merced College Corps has implemented a Personal Learning Plan for fellows to create goals with their community host site supervisor. The intent being that with guidance and mentorship, fellows will develop skills, knowledge and values necessary for creating community change work and strengthening civic leadership. Community Host Site Partners may use the personal learning plan as a resource tool for regular check ins.</li>
                        <li><u>Participating in National Days of Service Events</u> enhances civic engagement by encouraging fellows to actively contribute to community service and address pressing social issues. These events offer hands-on experience, improve understanding of community needs, and develop skills like teamwork, leadership, and problem-solving. They also help fellows build connections with other community members and organizations, strengthening their network and impact. Overall, this requirement aligns with the program's mission to promote active citizenship and personal growth, ensuring that fellows make meaningful contributions to their communities while gaining enriching experiences.</li>
                    </ul>
                    
                    <div class="cc-divider" style="margin: 30px 0;"></div>
                    
                    <h3><strong>Statewide Cohort Experience</strong></h3>
                    
                    <p>Ensuring that Fellows from across the state feel a shared sense of identity and a common purpose is a priority for the College Corps Program. This Program aims to promote the following priority outcomes through the Statewide Cohort Experience:</p>
                    
                    <ul>
                        <li><strong>Solidarity:</strong> Fellows feel connected to each other across diverse backgrounds and geographies and connected to California Volunteers.</li>
                        <li><strong>Bridging:</strong> Fellows learn leadership and cross-cultural collaboration skills that help them bridge divides and navigate differences to solve problems.</li>
                        <li><strong>Inspiration:</strong> Fellows are inspired to pursue a lifetime of service through connections with a network of state and local leaders.</li>
                    </ul>
                    
                    <p>To advance these outcomes, California Volunteers will offer Fellows the opportunity to participate in the following activities and events:</p>
                    
                    <ul>
                        <li><u>Statewide Launch & Swearing-In Celebration</u> brings together all California Service Corps members, from across the state for an energetic kick-off to their service experience.</li>
                        <li><u>Fellow Ambassador Program</u> will engage at least two Fellows from each partner campus to receive additional training that will help them serve as spokesperson for College Corps on their campus and beyond.</li>
                        <li><u>Mid-Year Leadership Workshops</u> bring regional cohorts of Fellows together, in-person to build relationships, learn new skills, and share what they are learning through their own service experience.</li>
                        <li><u>California Service Corps Regional Service Days</u> will offer College Corps Fellows the opportunity to gain service hours serving side by side with other California Service Corps members.</li>
                        <li><u>End-of-Year Ceremony</u> will celebrate the end of a transformative year and recognize California Service Corps members statewide for their accomplishments.</li>
                    </ul>
                </div>
            </div>

            <!-- Service Areas Accordion -->
            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Service Areas</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <h3><strong>Introduction to Our Service and Community Impact</strong></h3>
                    
                    <p>UC Merced College Corps is devoted to creating meaningful connections with our community through partnerships with nonprofit and governmental organizations. Our fellows play a vital role in addressing California's most pressing challenges, contributing to initiatives that uplift both students and their communities. By fostering responsible civic engagement, we strive to meet critical needs in four primary focus areas identified by California Volunteers:</p>
                    
                    <ul>
                        <li>K-12 & Community Education</li>
                        <li>Food Security</li>
                        <li>Climate Action</li>
                        <li>Public Health</li>
                    </ul>
                    
                    <p>Explore the Cohort 4 Community Host Partners page to learn about the exciting host sites where Fellows serve within the Merced community!</p>
                    
                    <div class="cc-divider" style="margin: 30px 0;"></div>
                    
                    <h3><strong>Service Placement Guidelines</strong></h3>
                    
                    <p>Community Host Partners play an important role in mentoring Fellows, ensuring they are doing meaningful work, and gaining practical job skills. California Volunteers shared the following guidelines with Partner Campuses and Community Host Partners.</p>
                    
                    <p>College Corps Fellows must:</p>
                    
                    <ul>
                        <li>Serve primarily with one Community Host Partner throughout their term of service</li>
                        <li>Spend the majority of service hours engaging directly with beneficiaries in the community, not conducting desk research or performing administrative tasks</li>
                        <li>Conduct service directly aligned with their program's stated focus area(s) and performance measures</li>
                        <li>Accurately log service and training hours in America Learns (an online timesheet system) on a daily or weekly basis</li>
                    </ul>
                </div>
            </div>

            <!-- Eligibility Accordion -->
            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Eligibility</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <h3><strong>General Eligibility</strong></h3>
                    
                    <p>To apply, students should meet the following minimum eligibility criteria:</p>
                    
                    <ul>
                        <li>Full-time, enrolled undergraduate student at a College Corps partner campus</li>
                        <li>Has a high school diploma or its equivalent by start of program</li>
                        <li>Must currently be and remain in good academic standing</li>
                        <li>Ability to commit to the program for the full academic year</li>
                    </ul>
                    
                    <div class="cc-divider" style="margin: 30px 0;"></div>
                    
                    <h3><strong>Requirements</strong></h3>
                    
                    <p><strong>To apply, students must be a US Citizen, US National, legal permanent resident or AB 540 CA Dream Act Student</strong></p>
                    
                    <p>Please consult with our Program staff for more details</p>
                    
                    <div class="cc-divider" style="margin: 30px 0;"></div>
                    
                    <h3><strong>Financial Need</strong></h3>
                    
                    <p>Eligible students should meet at least one of the following four criteria:</p>
                    
                    <ul>
                        <li>Qualifies for a Federal Pell Grant</li>
                        <li>Qualifies for State Cal Grant</li>
                        <li>Qualifies for Middle Class Scholarship</li>
                        <li>Student needs to work part or full time to meet educational costs and borrow loans</li>
                    </ul>
                </div>
            </div>

            <!-- Expectations & Required Program Aspects Accordion -->
            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Expectations & Required Program Aspects</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <h3><strong>Expected Criteria for Fellows</strong></h3>
                    
                    <p>College Corps has a competitive selection process. To be selected, students must demonstrate a willingness to fully commit to the program, complete the required number of service hours, and fully engage in all program activities throughout the entire academic year. In addition, successful applicants should demonstrate:</p>
                    
                    <ul>
                        <li>Passion for working in partnership with communities to make positive change.</li>
                        <li>Flexibility to work in different areas and adapt to changing circumstances.</li>
                        <li>Growth mindset and eagerness to try new things.</li>
                        <li>Interest in connecting with and learning from other students and partners across the state.</li>
                        <li>Willingness to be an ambassador for the Fellowship on campus and beyond.</li>
                    </ul>
                    
                    <p>To remain eligible for College Corps, Fellows are expected to maintain full-time enrollment and remain in good academic standing for the entire academic year.</p>
                    
                    <div class="cc-divider" style="margin: 30px 0;"></div>
                    
                    <h3><strong>Required College Corps Aspects</strong></h3>
                    
                    <p>As a College Corps Fellow, there are several requirements that will be needed to be fulfilled throughout their year of service. These include:</p>
                    
                    <ul>
                        <li>Serving 450 hours through an in-person direct community service placement from August through June.</li>
                        <li>Serving an average of 12-15 hours/week throughout the academic year</li>
                        <li>Being enrolled in a designated Undergraduate Studies (USTU) course in the Fall 2025 and Spring 2026 semester. The USTU course is a 1-unit course.</li>
                        <li>Attend workshops such as Pre-Service Orientation, attend two six-hour Saturday Seminars in the Fall and Spring Semesters, and Lunch & Learn Lessons to enhance professional development and personal growth.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="cc-divider"></div>

    <!-- Cohort Information Section -->
    <div class="cc-section">
        <div class="cc-container">
            <h2 class="cc-section-title">Cohort Information</h2>
            
            <div class="cc-cohort-selector-container">
                <label class="cc-cohort-selector-label" for="cohortSelect">Select a Cohort to Learn More:</label>
                <select id="cohortSelect" class="cc-cohort-select">
                    <option value="">-- Choose a Cohort --</option>
                    <option value="cohort2">Cohort 2 (2023-2024)</option>
                    <option value="cohort3">Cohort 3 (2024-2025)</option>
                    <option value="cohort4">Cohort 4 (2025-2026)</option>
                    <option value="cohort5">Cohort 5 (2026-2027)</option>
                </select>
            </div>

            <!-- Cohort 2 Content -->
            <div id="cohort2" class="cc-cohort-content">
                <h3 class="cc-cohort-title">Cohort 2 (2023-2024)</h3>
                <h4 style="text-align: center; color: #FFBF3C; margin-bottom: 30px;">College Corps Impact in Merced County!</h4>
                
                <div class="cc-cohort-stats">
                    <ul>
                        <li><strong>111 Fellows Enrolled</strong>
                            <ul>
                                <li>10 Fellows Completed with 300+ hours</li>
                                <li>87 Fellows Completed with 450+ hours</li>
                            </ul>
                        </li>
                        <li><strong>26 Community Host Sites</strong></li>
                        <li><strong>14,322 Students Mentored and/or Tutored</strong></li>
                        <li><strong>1,293 Community Members Served</strong></li>
                        <li><strong>163,805 Pounds of Food Distributed</strong></li>
                    </ul>
                </div>
            </div>

            <!-- Cohort 3 Content -->
            <div id="cohort3" class="cc-cohort-content">
                <h3 class="cc-cohort-title">Cohort 3 (2024-2025)</h3>
                <h4 style="text-align: center; color: #FFBF3C; margin-bottom: 30px;">Current Cohort</h4>
                
                <div class="cc-cohort-stats">
                    <ul>
                        <li><strong>132 Fellows Enrolled</strong></li>
                        <li><strong>29 Community Host Sites</strong></li>
                        <li><strong>New Focus Area: Public Health</strong></li>
                    </ul>
                </div>
            </div>

            <!-- Cohort 4 Content -->
            <div id="cohort4" class="cc-cohort-content">
                <h3 class="cc-cohort-title">Cohort 4 (2025-2026)</h3>
                
                <p style="text-align: center; font-size: 1.1em; margin-bottom: 30px;">Information coming soon!</p>
                
                <h4 style="text-align: center; color: #002856; margin-top: 40px; margin-bottom: 20px;"><strong>Where do Fellows Serve?</strong></h4>
                
                <p style="text-align: center; margin-bottom: 30px;">Explore the map showcasing all the host sites that UC Merced College Corps has partnered with for the 2025-2026 academic year, marking Cohort 4. This map highlights the various locations where our students will be making a positive impact in their communities. Discover our partnerships and see where our efforts are taking place!</p>
                
                <div class="cc-map-container">
                    <img src="https://cec.ucmerced.edu/sites/cec.ucmerced.edu/files/page/images/map_ss_0.png" alt="Cohort 4 Host Sites Map">
                    <a href="https://www.google.com/maps/d/edit?mid=13OMlFhUbYOvoUY6LaD38tyz01H2trJY&usp=sharing" class="cc-btn" target="_blank">VIEW INTERACTIVE MAP</a>
                </div>
            </div>

            <!-- Cohort 5 Content -->
            <div id="cohort5" class="cc-cohort-content">
                <h3 class="cc-cohort-title">Cohort 5 (2026-2027)</h3>
                <h4 style="text-align: center; color: #FFBF3C; margin-bottom: 20px;"><strong>2026-27 Cohort 5 Interest Form</strong></h4>
                
                <p style="text-align: center; font-size: 1.1em; margin-bottom: 30px;">Are you interested in joining College Corps at UC Merced? Complete the interest form below to receive information once our next recruitment cycle opens!</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="https://ucmerced.az1.qualtrics.com/jfe/form/SV_87Xjan3yma6oXzw" class="cc-btn" target="_blank">SUBMIT STUDENT INTEREST FORM</a>
                </div>
                
                <div class="cc-divider" style="margin: 40px 0;"></div>
                
                <h4 style="text-align: center; color: #002856; margin-bottom: 20px;"><strong>Questions?</strong></h4>
                
                <p style="text-align: center; margin-bottom: 15px;">In this page you will find answers to some frequently asked questions about the College Corps Program.</p>
                
                <p style="text-align: center; margin-bottom: 15px;">Please feel free to check out our Instagram <a href="https://www.instagram.com/ucmcollegecorps/?igsh=enh5eWVxaGtleGRj&utm_source=qr#" target="_blank" style="color: #002856; font-weight: bold;">@ucmcollegecorps</a>, as well as our partnering office <a href="https://www.instagram.com/ucmercedcec/?igsh=NTc4MTIwNjQ2YQ%3D%3D#" target="_blank" style="color: #002856; font-weight: bold;">@ucmercedcec</a>, where information and updates on current Fellows progress and any upcoming service opportunities will continuously be posted!</p>
                
                <p style="text-align: center;">If you are on campus, please feel free to visit us in <strong>KL 172</strong> or send us an email at <a href="mailto:collegecorps@ucmerced.edu" style="color: #002856; font-weight: bold;">collegecorps@ucmerced.edu</a></p>
            </div>
        </div>
    </div>

    <div class="cc-divider"></div>

    <!-- FAQ Section -->
    <div class="cc-section cc-section-alt">
        <div class="cc-container">
            <h2 class="cc-section-title">Frequently Asked Questions</h2>
            
            <!-- FAQ Accordion Items -->
            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>What is the College Corps Program?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>The College Corps Program is a statewide initiative aimed at engaging college students in community service while addressing critical issues such as K-12 & Community Education, Climate Action, Food Security, and Public Health. It helps students gain professional experience, contribute to meaningful causes, and reduce financial burdens.</p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Who is eligible to participate in the Program?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Eligibility requirements typically include:</p>
                    <ul>
                        <li>Enrollment as a full-time undergraduate student at a participating California College or University</li>
                        <li>A commitment to completing the program's service hour requirements</li>
                        <li>Being in good academic standing at your institution</li>
                    </ul>
                    <p>Each participating campus may have additional eligibility criteria, so it's good to check directly with them.</p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>What types of service opportunities are available?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Service opportunities are designed around four main focus areas:</p>
                    <ul>
                        <li><strong>K-12 & Community Education:</strong> Tutoring, mentoring, or supporting students in under-resourced schools</li>
                        <li><strong>Climate Action:</strong> Working on environmental sustainability projects, conservation, and community resilience</li>
                        <li><strong>Food Security:</strong> Assisting in food distribution programs or supporting organizations tackling hunger issues</li>
                        <li><strong>Public Health:</strong> Supporting health education, outreach, and initiatives to promote wellness and address health disparities in the community</li>
                    </ul>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>How many hours do Fellows need to complete?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Fellows complete a total of 450 hours, which include all direct service hours and training hours acquired through required professional development workshops and USTU seminars.</p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>What kind of benefits do Fellows receive?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Participants receive several benefits, including:</p>
                    <ul>
                        <li>A $10,000 stipend, distributed in installments over the academic year
                            <ul>
                                <li>A monthly stipend distributed in equal installments by the Financial Aid Office</li>
                                <li>An additional education award upon completion of ALL program requirements, which can be used for tuition, student loans, or other education-related expenses</li>
                            </ul>
                        </li>
                        <li>Hands-on experience in public service and professional development opportunities</li>
                        <li>The chance to build networks and gain valuable skills for future careers</li>
                    </ul>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>How do I apply for the Program?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>We will have our 2026-27 Cohort 5 interest form that will be at the top of this page available later this year if you are interested in applying for the College Corps Program!</p>
                    <p>We do require students to attend Info Sessions as well as meet with our College Corps team during the Spring semester as a pre-requisite to applying!</p>
                    <p>To stay informed on current updates please continue to visit our College Corps website and follow us on Instagram <a href="https://www.instagram.com/ucmcollegecorps/?igsh=enh5eWVxaGtleGRj&utm_source=qr#" target="_blank" style="color: #002856; font-weight: bold;">@ucmcollegecorps!</a></p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>What training or support is provided to Fellows?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Fellows in the College Corps Program typically receive:</p>
                    <ul>
                        <li><u>Pre-Service Training:</u> This may include workshops on community engagement, cultural competency, and leadership development</li>
                        <li><u>Ongoing Support:</u> Site supervisors, program coordinators, and peer mentors are available to guide Fellows throughout their service</li>
                        <li><u>Professional Development Opportunities:</u> Some programs offer skill-building seminars or access to career networks to help participants grow personally and professionally</li>
                    </ul>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>What kinds of organizations partner with the Program?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Partner organizations are typically nonprofits, schools, or government agencies focused on addressing community needs. Common areas include:</p>
                    <ul>
                        <li><u>K-12 & Community Education:</u> Supporting youth through tutoring, mentoring, or enrichment programs</li>
                        <li><u>Food Security:</u> Working with food banks, pantries, or meal delivery programs</li>
                        <li><u>Climate Action:</u> Partnering with environmental groups on sustainability and conservation projects</li>
                        <li><u>Public Health:</u> Collaborating with health organizations to provide education, outreach, or services that promote community well-being</li>
                    </ul>
                    <p>Each campus may have partnerships that align with its region's unique priorities.</p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Can I participate if I have a part-time job or other commitments?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Yes, many Fellows balance the program with part-time jobs, classes, or other responsibilities. However:</p>
                    <ul>
                        <li>You must commit to completing the 450 service hours over the program year</li>
                        <li>Some flexibility is required, as service hours often depend on the needs of your assigned partner organization</li>
                    </ul>
                    <p>Be sure to discuss your schedule with program coordinators to ensure you can manage the commitment.</p>
                </div>
            </div>

            <div class="cc-accordion-item">
                <button class="cc-accordion-header">
                    <span>Is transportation assistance provided?</span>
                    <span class="cc-accordion-icon">▼</span>
                </button>
                <div class="cc-accordion-content">
                    <p>Fellows can carpool with other Fellows either with an individually owned vehicle or a UC Merced reserved vehicle through TAPS.</p>
                    <p>There are different transportation options available for Fellows to get to their sites:</p>
                    <ul>
                        <li><u>Preferred Option:</u> College Corps Van system with regular routes and drivers</li>
                        <li><u>Second Option:</u> If for some reason the Van ride system does not work for a Fellows schedule, and they have access to their own vehicle, they can drive themselves, or carpool with other Fellows.</li>
                        <li><u>Third Option:</u> Public Transportation (Cat Tracks) is the final, but least encouraged option, due to lack of availability in Merced County</li>
                    </ul>
                    <p>Fellows can carpool with other Fellows either with an individually owned vehicle or a UC Merced reserved vehicle through TAPS.</p>
                    <p><strong>Uber and Lyft cannot be directly reimbursed, therefore is not encouraged as a transportation option.</strong></p>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="cc-footer">
        <div class="cc-container">
            <p><strong>Questions?</strong> Visit us at the Community Engagement Center - KL 172</p>
            <p>Monday - Friday, 9:00 AM - 5:00 PM</p>
            <p><a href="mailto:collegecorps@ucmerced.edu">collegecorps@ucmerced.edu</a></p>
            <p style="margin-top: 20px;">Follow us on Instagram: <a href="https://www.instagram.com/ucmcollegecorps/" target="_blank">@ucmcollegecorps</a> | <a href="https://www.instagram.com/ucmercedcec/" target="_blank">@ucmercedcec</a></p>
            <p style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">&copy; 2025 UC Merced | Community Engagement Center</p>
        </div>
    </div>

    <!-- JavaScript -->
    <script>
        // Accordion functionality
        document.querySelectorAll('.cc-accordion-header').forEach(button => {
            button.addEventListener('click', () => {
                button.classList.toggle('active');
                const content = button.nextElementSibling;
                
                if (content.style.display === 'block') {
                    content.style.display = 'none';
                } else {
                    content.style.display = 'block';
                }
            });
        });

        // Cohort selector functionality
        const cohortSelect = document.getElementById('cohortSelect');
        const cohortContents = document.querySelectorAll('.cc-cohort-content');

        cohortSelect.addEventListener('change', function() {
            // Hide all cohort content
            cohortContents.forEach(content => {
                content.classList.remove('active');
            });

            // Show selected cohort content
            const selectedCohort = this.value;
            if (selectedCohort) {
                const selectedContent = document.getElementById(selectedCohort);
                if (selectedContent) {
                    selectedContent.classList.add('active');
                    // Smooth scroll to the content
                    selectedContent.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
            }
        });
    </script>

</body>
</html>