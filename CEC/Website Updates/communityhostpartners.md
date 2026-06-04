<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>College Corps Community Host Partners</title>
<style type="text/css">/* Modern styling inspired by Pathways page */
body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0 auto;
}

.host-partners-container {
    margin: 0 auto;
    padding: 0 20px;
}

.host-partners-intro {
    text-align: center;
    margin: 2rem 0;
    padding: 2rem;
    background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 100%);
    border-radius: 12px;
    border: 2px solid #0077cc;
    line-height: 1.6;
    color: #555;
}

.host-partners-intro p {
    margin-bottom: 1.5rem;
}

.host-partners-intro p:last-child {
    margin-bottom: 0;
}

.host-partners-intro a {
    color: #0077cc;
    font-weight: bold;
    text-decoration: underline;
    transition: all 0.3s ease;
}

.host-partners-intro a:hover {
    color: #005a99;
    text-decoration: none;
}

.section-headline {
    border-bottom: 2px solid #ffbf3c;
    padding-bottom: 8px;
    margin: 32px 0 24px;
    font-size: 1.4rem;
    color: #002856;
    text-align: center;
}

.divider-line {
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #002856 0%, #ffbf3c 50%, #002856 100%);
    margin: 2rem 0;
    border-radius: 2px;
}

/* Accordion container */
.accordion {
    margin: 0 auto;
    width: 100%;
}

.accordion ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.accordion li {
    margin: 16px 0 0 0;
    padding: 0;
}

/* Accordion toggle buttons */
.acc-toggle {
    display: block;
    width: 100%;
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
    text-align: left;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 40, 86, 0.2);
    font-family: Arial, Helvetica, sans-serif;
}

.acc-toggle:hover,
.acc-toggle[aria-expanded="true"] {
    background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
    border-color: #ffbf3c;
    color: #002856;
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
}

.acc-toggle:focus {
    outline: 3px solid #ffbf3c;
    outline-offset: 2px;
}

/* Carousel and card styles */
.carousel {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 1.5rem 0;
}

.carousel-content {
    display: flex;
    overflow-x: auto;
    scroll-behavior: smooth;
    gap: 1rem;
    padding: 1rem 0;
    flex: 1;
}

.carousel-content::-webkit-scrollbar {
    height: 8px;
}

.carousel-content::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

.carousel-content::-webkit-scrollbar-thumb {
    background: #0077cc;
    border-radius: 10px;
}

.card {
    min-width: 280px;
    max-width: 280px;
    background: #fff;
    border: 3px solid #0077cc;
    border-radius: 8px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 119, 204, 0.1);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 119, 204, 0.3);
    border-color: #002856;
}

.card p {
    margin: 0 0 1rem 0;
    color: #002856;
    font-weight: 600;
    font-size: 1rem;
}

.card-image {
    width: 100%;
    height: auto;
    max-height: 150px;
    object-fit: contain;
    margin-bottom: 1rem;
}

.learn-more-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: 0.6em 1.5em;
    background: linear-gradient(135deg, #0077cc 0%, #005a99 100%);
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 6px;
    font-size: 0.95rem;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 119, 204, 0.3);
    font-family: Arial, Helvetica, sans-serif;
}

.learn-more-btn:hover {
    background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 191, 60, 0.4);
}

.learn-more-btn:focus {
    outline: 3px solid #002856;
    outline-offset: 2px;
}

.arrow-btn {
    cursor: pointer;
    font-size: 2.5em;
    color: #0077cc;
    user-select: none;
    padding: 0 1rem;
    transition: all 0.3s ease;
    background: none;
    border: none;
    font-family: Arial, Helvetica, sans-serif;
    min-height: 44px;
    min-width: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.arrow-btn:hover {
    color: #ffbf3c;
    transform: scale(1.2);
}

.arrow-btn:focus {
    outline: 3px solid #0077cc;
    outline-offset: 2px;
}

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

.acc_content.is-open {
    max-height: 3000px;
    opacity: 1;
    padding: 1.5em;
    margin-top: 8px;
    border-color: #e0e0e0;
    background: linear-gradient(135deg, #fffbf0 0%, #fff 100%);
}

/* Modal */
.expanded-card {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.expanded-card-content {
    background: #fff;
    color: #000;
    padding: 2rem;
    border-radius: 12px;
    position: relative;
    width: 90%;
    max-width: 600px;
    max-height: 80vh;
    overflow-y: auto;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.close-btn {
    position: absolute;
    top: 15px;
    right: 20px;
    cursor: pointer;
    font-size: 1.5rem;
    color: #002856;
    font-weight: bold;
    transition: all 0.3s ease;
    background: none;
    border: none;
    font-family: Arial, Helvetica, sans-serif;
    min-height: 44px;
    min-width: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 4px;
}

.close-btn:hover {
    color: #ffbf3c;
    transform: scale(1.2);
}

.close-btn:focus {
    outline: 3px solid #002856;
    outline-offset: 2px;
}

.expanded-card-content h2 {
    color: #002856;
    margin-top: 0;
    padding-right: 3rem;
}

.expanded-card-content p {
    line-height: 1.6;
    color: #555;
}

.expanded-card-content a {
    color: #0077cc;
    font-weight: bold;
}

.expanded-card-content a:hover {
    color: #ffbf3c;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .host-partners-container {
        margin-right: 20px;
    }

    .card {
        min-width: 250px;
        max-width: 250px;
    }

    .arrow-btn {
        font-size: 2em;
        padding: 0 0.5rem;
    }
}
</style>

<div class="host-partners-container">
    <div class="host-partners-intro" role="note">
        <p>As UC Merced CollegeCorps, we are committed to community outreach and engagement. Our fellows work with organizations and agencies in reciprocal partnerships that strengthen our students and their communities. Our goal is to address community needs and demonstrate responsible community participation. By focusing on K-12 Education, Climate Action, Food Disparities, and Public Health, we are building a community of change agents one fellow at a time.</p>
    </div>

    <div class="divider-line" aria-hidden="true"></div>

    <h2 class="section-headline">Explore Our Community Partners</h2>

    <p style="text-align: center; color: #555; margin-bottom: 2rem;">Browse our partner organizations by focus area and learn how they're making an impact in the community.</p>

    <!-- Modal -->
    <div
        class="expanded-card"
        id="expanded-card"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-heading"
        style="display:none;"
    >
        <div class="expanded-card-content">
            <button class="close-btn" aria-label="Close partner details" onclick="closeCard()" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();closeCard();}">&#x2715;</button>
            <div id="expanded-card-text">&nbsp;</div>
        </div>
    </div>

    <div class="accordion vertical">
        <ul class="acc_list">

            <!-- K-12 & Community Education Accordion -->
            <li>
                <button
                    class="acc-toggle"
                    id="acc-btn-1"
                    aria-expanded="false"
                    aria-controls="acc-content-1"
                    onclick="toggleAcc(this)"
                    onkeydown="handleAccKey(event, this)"
                >K-12 &amp; Community Education</button>
                <div class="acc_content" id="acc-content-1" role="region" aria-labelledby="acc-btn-1">
                    <div class="carousel" id="carousel-1">
                        <button class="arrow-btn" aria-label="Scroll K-12 partners left" onclick="rotateCarousel(-1, 'carousel-1')">&#9664;</button>
                        <div class="carousel-content" id="carousel-content-1">

                            <div class="card">
                                <p>Boys and Girls Club of Merced County</p>
                                <img alt="Boys and Girls Club of Merced County logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/boys_and_girls_club.png" />
                                <button class="learn-more-btn" onclick="expandCard('Boys and Girls Club of Merced County')" aria-label="Learn more about Boys and Girls Club of Merced County">Learn More</button>
                            </div>

                            <div class="card">
                                <p>CalTeach, University of California Merced</p>
                                <img alt="CalTeach Learning Lab logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/calteach_learning_lab.jpeg" />
                                <button class="learn-more-btn" onclick="expandCard('CalTeach, University of California Merced')" aria-label="Learn more about CalTeach, University of California Merced">Learn More</button>
                            </div>

                            <div class="card">
                                <p>City of Atwater Recreation</p>
                                <img alt="City of Atwater Recreation logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/city_of_water_recreation.png" />
                                <button class="learn-more-btn" onclick="expandCard('City of Atwater Recreation')" aria-label="Learn more about City of Atwater Recreation">Learn More</button>
                            </div>

                            <div class="card">
                                <p>City of Merced Parks and Community Services</p>
                                <img alt="City of Merced Parks and Community Services logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/city_of_merced_parks_and_community_services.jpeg" />
                                <button class="learn-more-btn" onclick="expandCard('City of Merced Parks and Community Services')" aria-label="Learn more about City of Merced Parks and Community Services">Learn More</button>
                            </div>

                            <div class="card">
                                <p>El Nido Elementary School District</p>
                                <img alt="El Nido Elementary School District logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/el_nido_elementary.png" />
                                <button class="learn-more-btn" onclick="expandCard('El Nido Elementary School District')" aria-label="Learn more about El Nido Elementary School District">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Fossil Discovery Center of Madera County/San Joaquin Valley Paleontology Foundation</p>
                                <img alt="Fossil Discovery Center logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/fossil_discovery_center.jpeg" />
                                <button class="learn-more-btn" onclick="expandCard('Fossil Discovery Center of Madera County/San Joaquin Valley Paleontology Foundation')" aria-label="Learn more about Fossil Discovery Center of Madera County">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Harvest Park Educational Center (HPEC)</p>
                                <img alt="Harvest Park Educational Center logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/hpec_0.png" />
                                <button class="learn-more-btn" onclick="expandCard('Harvest Park Educational Center (HPEC)')" aria-label="Learn more about Harvest Park Educational Center">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Kids Discovery Station</p>
                                <img alt="Kids Discovery Station logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/kids_discovery_station.png" />
                                <button class="learn-more-btn" onclick="expandCard('Kids Discovery Station')" aria-label="Learn more about Kids Discovery Station">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Lifeline CDC</p>
                                <img alt="Lifeline CDC logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/lifeline_cdc.jpeg" />
                                <button class="learn-more-btn" onclick="expandCard('Lifeline CDC')" aria-label="Learn more about Lifeline CDC">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Merced County Community Action - Agency Early Learning Preschool Programs</p>
                                <img alt="MCCA Early Learning Preschool Programs logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/merced_county_community_action_agency_-_early_learning_preschool_programs.png" />
                                <button class="learn-more-btn" onclick="expandCard('Merced County Community Action - Agency Early Learning Preschool Programs')" aria-label="Learn more about Merced County Community Action Agency Early Learning Preschool Programs">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Merced County Library</p>
                                <img alt="Merced County Library logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/merced_county_library.png" />
                                <button class="learn-more-btn" onclick="expandCard('Merced County Library')" aria-label="Learn more about Merced County Library">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Restorative Justice League</p>
                                <img alt="Restorative Justice League logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/restorative_justice_league_0.jpeg" />
                                <button class="learn-more-btn" onclick="expandCard('Restorative Justice League')" aria-label="Learn more about Restorative Justice League">Learn More</button>
                            </div>

                            <div class="card">
                                <p>STEAM Center, Merced City School District</p>
                                <img alt="STEAM Center Merced City School District logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/steam_center.png" />
                                <button class="learn-more-btn" onclick="expandCard('STEAM Center, Merced City School District')" aria-label="Learn more about STEAM Center, Merced City School District">Learn More</button>
                            </div>

                            <div class="card">
                                <p>United Way of Merced County: 2-1-1 Mountain Valley</p>
                                <img alt="United Way of Merced County 2-1-1 logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/united_way_of_merced_county.png" />
                                <button class="learn-more-btn" onclick="expandCard('United Way of Merced County: 2-1-1 Mountain Valley')" aria-label="Learn more about United Way of Merced County 2-1-1 Mountain Valley">Learn More</button>
                            </div>

                            <div class="card">
                                <p>United Way of Merced County VITA</p>
                                <img alt="United Way of Merced County VITA logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/united_way_vita_merced_county.png" />
                                <button class="learn-more-btn" onclick="expandCard('United Way of Merced County VITA')" aria-label="Learn more about United Way of Merced County VITA">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Walking by Faith Ministries International dba/SERENITY</p>
                                <img alt="Walking by Faith Ministries International SERENITY logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/walking_by_faith_ministris_international_dba_-_serenity.png" />
                                <button class="learn-more-btn" onclick="expandCard('Walking by Faith Ministries International dba/SERENITY')" aria-label="Learn more about Walking by Faith Ministries International SERENITY">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Weaver Union School District</p>
                                <img alt="Weaver Union School District logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/weaver_middle_school_0.png" />
                                <button class="learn-more-btn" onclick="expandCard('Weaver Union School District')" aria-label="Learn more about Weaver Union School District">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Buhach Colony High School AVID</p>
                                <img alt="Buhach Colony High School AVID logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/buhach_avid.png" />
                                <button class="learn-more-btn" onclick="expandCard('Buhach Colony High School AVID')" aria-label="Learn more about Buhach Colony High School AVID">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Improve Your Tomorrow</p>
                                <img alt="Improve Your Tomorrow logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/iyt.jpg" />
                                <button class="learn-more-btn" onclick="expandCard('Improve Your Tomorrow')" aria-label="Learn more about Improve Your Tomorrow">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Merced Applegate Zoo</p>
                                <img alt="Merced Applegate Zoo logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/applegate_zoo.jpg" />
                                <button class="learn-more-btn" onclick="expandCard('Merced Applegate Zoo')" aria-label="Learn more about Merced Applegate Zoo">Learn More</button>
                            </div>

                            <div class="card">
                                <p>El Capitan High School AVID</p>
                                <img alt="El Capitan High School AVID logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/el_capitan_.png" />
                                <button class="learn-more-btn" onclick="expandCard('El Capitan High School AVID')" aria-label="Learn more about El Capitan High School AVID">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Merced County Probation</p>
                                <img alt="Merced County Probation logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/merced_probation.jpg" />
                                <button class="learn-more-btn" onclick="expandCard('Merced County Probation')" aria-label="Learn more about Merced County Probation">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Golden Valley High School AVID</p>
                                <img alt="Golden Valley High School AVID logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/gv_cougar.jpg" />
                                <button class="learn-more-btn" onclick="expandCard('Golden Valley High School AVID')" aria-label="Learn more about Golden Valley High School AVID">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Love.Faith.Hope</p>
                                <img alt="Love Faith Hope logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/love.faith_.hope_.jpg" />
                                <button class="learn-more-btn" onclick="expandCard('Love.Faith.Hope')" aria-label="Learn more about Love.Faith.Hope">Learn More</button>
                            </div>

                        </div>
                        <button class="arrow-btn" aria-label="Scroll K-12 partners right" onclick="rotateCarousel(1, 'carousel-1')">&#9654;</button>
                    </div>
                </div>
            </li>

            <!-- Climate Action Accordion -->
            <li>
                <button
                    class="acc-toggle"
                    id="acc-btn-2"
                    aria-expanded="false"
                    aria-controls="acc-content-2"
                    onclick="toggleAcc(this)"
                    onkeydown="handleAccKey(event, this)"
                >Climate Action</button>
                <div class="acc_content" id="acc-content-2" role="region" aria-labelledby="acc-btn-2">
                    <div class="carousel" id="carousel-2">
                        <button class="arrow-btn" aria-label="Scroll Climate Action partners left" onclick="rotateCarousel(-1, 'carousel-2')">&#9664;</button>
                        <div class="carousel-content" id="carousel-content-2">

                            <div class="card">
                                <p>East Merced Resource Conservation District</p>
                                <img alt="East Merced Resource Conservation District logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/east_merced_resource_conservation_district_1.png" />
                                <button class="learn-more-btn" onclick="expandCard('East Merced Resource Conservation District')" aria-label="Learn more about East Merced Resource Conservation District">Learn More</button>
                            </div>

                            <div class="card">
                                <p>Merced Irrigation District</p>
                                <img alt="Merced Irrigation District logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/merced_irrigation_district.png" />
                                <button class="learn-more-btn" onclick="expandCard('Merced Irrigation District')" aria-label="Learn more about Merced Irrigation District">Learn More</button>
                            </div>

                            <div class="card">
                                <p>UC Merced Natural Reserve System</p>
                                <img alt="UC Merced Natural Reserve System logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/documents/collegecorps/naturalreservesystem.png" />
                                <button class="learn-more-btn" onclick="expandCard('UC Merced Natural Reserve System')" aria-label="Learn more about UC Merced Natural Reserve System">Learn More</button>
                            </div>

                        </div>
                        <button class="arrow-btn" aria-label="Scroll Climate Action partners right" onclick="rotateCarousel(1, 'carousel-2')">&#9654;</button>
                    </div>
                </div>
            </li>

            <!-- Public Health Accordion -->
            <li>
                <button
                    class="acc-toggle"
                    id="acc-btn-3"
                    aria-expanded="false"
                    aria-controls="acc-content-3"
                    onclick="toggleAcc(this)"
                    onkeydown="handleAccKey(event, this)"
                >Public Health</button>
                <div class="acc_content" id="acc-content-3" role="region" aria-labelledby="acc-btn-3">
                    <div class="carousel" id="carousel-3">
                        <button class="arrow-btn" aria-label="Scroll Public Health partners left" onclick="rotateCarousel(-1, 'carousel-3')">&#9664;</button>
                        <div class="carousel-content" id="carousel-content-3">

                            <div class="card">
                                <p>Merced Community Action Agency/Public Health</p>
                                <img alt="Merced County Community Action Agency Public Health logo" class="card-image" src="https://cec.ucmerced.edu/sites/g/files/ufvvjh561/f/page/images/merced_county_community_action_agency_-_early_learning_preschool_programs.png" />
                                <button class="learn-more-btn" onclick="expandCard('Merced County Community Action Agency/Public Health')" aria-label="Learn more about Merced Community Action Agency Public Health">Learn More</button>
                            </div>

                        </div>
                        <button class="arrow-btn" aria-label="Scroll Public Health partners right" onclick="rotateCarousel(1, 'carousel-3')">&#9654;</button>
                    </div>
                </div>
            </li>

        </ul>
    </div>
</div>

<script>
    var lastFocusedBtn = null;

    function toggleAcc(btn) {
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
        var content = document.getElementById(btn.getAttribute('aria-controls'));
        content.classList.toggle('is-open', !expanded);
    }

    function handleAccKey(event, btn) {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            toggleAcc(btn);
        }
    }

    function expandCard(cardName) {
        lastFocusedBtn = document.activeElement;
        document.getElementById('expanded-card-text').innerHTML = cardDetails[cardName];
        var modal = document.getElementById('expanded-card');
        modal.style.display = 'flex';
        // Move focus to close button
        modal.querySelector('.close-btn').focus();
    }

    function closeCard() {
        document.getElementById('expanded-card').style.display = 'none';
        // Return focus to the button that opened the modal
        if (lastFocusedBtn) {
            lastFocusedBtn.focus();
        }
    }

    // Close modal on backdrop click
    document.getElementById('expanded-card').addEventListener('click', function(e) {
        if (e.target === this) closeCard();
    });

    // Close modal on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && document.getElementById('expanded-card').style.display === 'flex') {
            closeCard();
        }
    });

    function rotateCarousel(direction, carouselId) {
        var carousel = document.getElementById(carouselId);
        var carouselContent = carousel.querySelector('.carousel-content');
        var cardWidth = carouselContent.querySelector('.card').offsetWidth + 16;
        carouselContent.scrollBy({ left: direction * cardWidth, behavior: 'smooth' });
    }

    const cardDetails = {
        'Boys and Girls Club of Merced County': `
            <h2 id="modal-heading"><strong>Boys and Girls Club of Merced County</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Provide direct support with youth enrichment activities.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 615 W 15th St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.bgcmerced.org/ourpurpose" target="_blank">Boys and Girls Club (opens in new tab)</a></p>
        `,
        'CalTeach, University of California Merced': `
            <h2 id="modal-heading"><strong>CalTeach, University of California Merced</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The UC Merced CalTeach program is designed to address the shortage of science and mathematics teachers in California's K-12 schools. As part of this, a K-12 STEM Learning Lab introduces young students to the curious and wonderful world of STEM!</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 5200 Lake Rd. Merced, 95343</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://learninglab.ucmerced.edu/" target="_blank">CalTeach Learning Lab (opens in new tab)</a></p>
        `,
        'City of Atwater Recreation': `
            <h2 id="modal-heading"><strong>City of Atwater Recreation</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education, Public Health</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: They create community and quality of life through people, parks and programs.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 1.) 760 E. Bellevue Rd. Atwater, CA 95301 / 2.) 1699 County Park 3 Atwater, CA 95301 / 3.) 760 Elm Ave. Atwater, CA 95301</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.atwater.org/recreation1/" target="_blank">City of Atwater Recreation (opens in new tab)</a></p>
        `,
        'City of Merced Parks and Community Services': `
            <h2 id="modal-heading"><strong>City of Merced Parks and Community Services</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: Plan, facilitate, promote, maintain, and develop activities and facilities that enhance the quality of life in Merced.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: Main Site: 678 W. 18th St. Merced, CA / Senior Center: 715 W. 15th St.</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.cityofmerced.org/departments/parks-community-services" target="_blank">City of Merced Parks and Community Services (opens in new tab)</a></p>
        `,
        'El Nido Elementary School District': `
            <h2 id="modal-heading"><strong>El Nido Elementary School District</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: El Nido Elementary serves a student population of over 96% unduplicated English Learners and socio-economically disadvantaged in Transitional Kindergarten through grade 8, their families and the surrounding community. An incorporated community, El Nido Elementary serves as the community hub for services, support and education.</p>
            <p style="font-size: 14px; margin-top: 10px;">Note: This host site participates in food security programs and events.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 161 E. El Nido Rd. El Nido, CA 95317</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.elnidoschool.org/" target="_blank">El Nido Elementary (opens in new tab)</a></p>
        `,
        'Fossil Discovery Center of Madera County/San Joaquin Valley Paleontology Foundation': `
            <h2 id="modal-heading"><strong>Fossil Discovery Center of Madera County/San Joaquin Valley Paleontology Foundation</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: To educate the public/students on local natural and paleontological histories.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 19450 Ave. 21 1/2, Chowchilla, CA 93610</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.maderamammoths.org/" target="_blank">Fossil Discovery Center (opens in new tab)</a></p>
        `,
        'Harvest Park Educational Center (HPEC)': `
            <h2 id="modal-heading"><strong>Harvest Park Educational Center (HPEC)</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: HPEC aims to provide at-risk, disconnected, children and youth (TK-12th grade) from low-income families with supplemental education as well as behavioral/mental health training and support.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 557 W. 26th St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://hpecafterschoolk12.education/" target="_blank">HPEC (opens in new tab)</a></p>
        `,
        'Kids Discovery Station': `
            <h2 id="modal-heading"><strong>Kids Discovery Station</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: A unique environment where children can experience fun and stimulating activities that encourage imagination, creativity, and learning through the power of play.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 350 W Yosemite Ave. Merced, CA 95348</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.kidsdiscoverystation.org/" target="_blank">Kids Discovery Station (opens in new tab)</a></p>
        `,
        'Lifeline CDC': `
            <h2 id="modal-heading"><strong>Lifeline CDC</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: LifeLine CDC empowers under-resourced neighborhoods to thrive.</p>
            <p style="font-size: 14px; margin-top: 10px;">Note: This host site participates in food security programs and events.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: Rivera Elementary School: 945 Buena Vista Dr. Merced, CA 95348</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.lifelinecdc.org/" target="_blank">Lifeline CDC (opens in new tab)</a></p>
        `,
        'Merced County Community Action - Agency Early Learning Preschool Programs': `
            <h2 id="modal-heading"><strong>Merced County Community Action - Agency Early Learning Preschool Programs</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Provide comprehensive childcare and preschool services to participating children and families: one child, one family at a time.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 4140 Cook Street Le Grand, CA 95333</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.mercedcaa.com/our-programs/preschool-programs/" target="_blank">MCCA Early Learning Preschool Programs (opens in new tab)</a></p>
        `,
        'Merced County Library': `
            <h2 id="modal-heading"><strong>Merced County Library</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: We provide access to materials and technology that build bridges to discovery. We build an innovative and informed community from the littlest community members up.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 2100 O St. Merced, 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.countyofmerced.com/3876/Library" target="_blank">Merced County Library (opens in new tab)</a></p>
        `,
        'Restorative Justice League': `
            <h2 id="modal-heading"><strong>Restorative Justice League</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Provide a multi-tiered system of framework and relational approach, establishing the social culture and behavioral supports necessary for schools to be safe, caring, and provide an effective learning environment for all.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 364 W. 27th St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://restorativejusticeleague.com/" target="_blank">Restorative Justice League (opens in new tab)</a></p>
        `,
        'STEAM Center, Merced City School District': `
            <h2 id="modal-heading"><strong>STEAM Center, Merced City School District</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The STEAM Center functions as a field trip destination for MCSD students to gain hands-on experiences in science, technology, engineering, arts, and mathematics.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 2900 Green Street Merced, 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.mcsd.k12.ca.us/District/Portal/steam-center" target="_blank">STEAM Center (opens in new tab)</a></p>
        `,
        'United Way of Merced County: 2-1-1 Mountain Valley': `
            <h2 id="modal-heading"><strong>United Way of Merced County: 2-1-1 Mountain Valley</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: A comprehensive information and referral service for Merced and Mariposa Counties with a focus to place those in need in contact with needed resources.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 531 W. Main St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.unitedwaymerced.org/" target="_blank">United Way of Merced County 2-1-1 (opens in new tab)</a></p>
        `,
        'United Way of Merced County VITA': `
            <h2 id="modal-heading"><strong>United Way of Merced County VITA</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Promoting Equitable Access to Information through free tax preparation to ensure low-income residents have access to information and professional guidance they might not otherwise be able to afford. Also Empowering Financial Wellness - contributing to a community's overall financial health by equipping clients with knowledge and resources to make informed financial decisions.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 531 W. Main St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.unitedwaymerced.org/vita" target="_blank">United Way Merced County VITA (opens in new tab)</a></p>
        `,
        'Walking by Faith Ministries International dba/SERENITY': `
            <h2 id="modal-heading"><strong>Walking by Faith Ministries International dba/SERENITY</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The Strengthen, Transform, Affirm, Restore, and Support (STARS) after school program at the Serenity Youth Empowerment Center provides free after school and summer tutoring for low-incoming youth, including extracurricular activities.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 740 Canal St. Merced, CA 95341</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://wbfinternationalministries.org/" target="_blank">Walking by Faith Ministries International SERENITY (opens in new tab)</a></p>
        `,
        'Weaver Union School District': `
            <h2 id="modal-heading"><strong>Weaver Union School District</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Weaver Middle School helps build strong community engagement and accountability, increase student achievement, support all learners, and remove barriers to learning.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 3076 E Childs Ave. Merced, CA 95341</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.weaverusd.org/o/wms" target="_blank">Weaver Union School District (opens in new tab)</a></p>
        `,
        'Buhach Colony High School AVID': `
            <h2 id="modal-heading"><strong>Buhach Colony High School AVID</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The mission is to close the opportunity gap by preparing all students for college and career readiness and success in a global society.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 1800 N. Buhach Rd.</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://bchs.muhsd.org/" target="_blank">Buhach Colony High School AVID (opens in new tab)</a></p>
        `,
        'Improve Your Tomorrow': `
            <h2 id="modal-heading"><strong>Improve Your Tomorrow</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Mission of IYT is to increase the number of young men of color to attend and graduate from colleges and universities and to guide and build academic and professional relationships with our students through mentorship, service and college advising.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 205 W Olive Avenue / 945 Buena Vista Dr. Merced (Rivera Elementary) / 800 E 26th St. Merced (Hoover Intermediate) / 3076 E. Childs Ave, Merced (Weaver Middle) / Childs Ave, Merced (Golden Valley High)</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.improveyourtomorrow.org/regional/centralvalley" target="_blank">Improve Your Tomorrow (opens in new tab)</a></p>
        `,
        'Merced Applegate Zoo': `
            <h2 id="modal-heading"><strong>Merced Applegate Zoo</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The zoo is dedicated to rescuing and caring for injured, orphaned, and imprinted animals while inspiring guests to connect with the wildlife they share the world with through education and conservation.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 1045 W 25th street</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.cityofmerced.gov/parks-and-community/applegate-park-zoo" target="_blank">Merced Applegate Zoo (opens in new tab)</a></p>
        `,
        'El Capitan High School AVID': `
            <h2 id="modal-heading"><strong>El Capitan High School AVID</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The mission is to provide tutoring, mentoring and support to small groups in each class to check-in, model note-taking and time management techniques and scaffold/create support to help students complete larger tasks.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 205 W Olive Avenue</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://sites.google.com/guhsd.net/elcapavid/home" target="_blank">El Capitan High School AVID (opens in new tab)</a></p>
        `,
        'Merced County Probation': `
            <h2 id="modal-heading"><strong>Merced County Probation</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The Merced County Probation Department acts as a fair and impartial justice partner to the court, provides rehabilitative community-based supervision, and maintains a safe custodial environment for the youth and young adults in our care. We are catalysts for change to foster healthier families and safer communities.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 3080 M Street</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.countyofmerced.com/3884/Probation" target="_blank">Merced County Probation (opens in new tab)</a></p>
        `,
        'Golden Valley High School AVID': `
            <h2 id="modal-heading"><strong>Golden Valley High School AVID</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The AVID program helps students develop skills, mindset and support they need to succeed in college and beyond.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 2121 E. Childs Ave.</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.goldenvalleyhs.org/" target="_blank">Golden Valley High School AVID (opens in new tab)</a></p>
        `,
        'Love.Faith.Hope': `
            <h2 id="modal-heading"><strong>Love.Faith.Hope</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: K-12/Community Education</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: Love.Faith.Hope's purpose is to reach students K-12th grade and their families.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 2185 G Street</p>
        `,
        'East Merced Resource Conservation District': `
            <h2 id="modal-heading"><strong>East Merced Resource Conservation District</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: Climate Action</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: To serve as a local hub for conservation: connecting people with the technical, financial, and educational assistance to conserve and manage natural resources.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 2926 G Street STE102, Merced, 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.eastmercedrcd.org/" target="_blank">East Merced Resource Conservation District (opens in new tab)</a></p>
        `,
        'Merced Irrigation District': `
            <h2 id="modal-heading"><strong>Merced Irrigation District</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: Climate Action</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The mission is to provide outstanding opportunities for high-quality outdoor recreation. Fellows will be involved in all aspects of Recreation programs, offering program instructions, officiating, communicating to program participants and parents as well as program development.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: Main Site: 9090 Lake McClure Rd / 2nd Site: 3100 Barrett Cove Rd., La Grange CA 95329</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://mercedid.org/" target="_blank">Merced Irrigation District (opens in new tab)</a></p>
        `,
        'UC Merced Natural Reserve System': `
            <h2 id="modal-heading"><strong>UC Merced Natural Reserve System</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: Climate Action</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: The UC Merced Natural Reserve System connects researchers, educators, students, and the community to nature through education, research, and community engagement across diverse natural lands.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 5200 N Lake Road, SE2 120F</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://nrs.ucmerced.edu/" target="_blank">UC Merced Natural Reserve System (opens in new tab)</a></p>
        `,
        'Merced County Community Action Agency/Public Health': `
            <h2 id="modal-heading"><strong>Merced Community Action Agency/Public Health</strong></h2>
            <p style="font-size: 14px; margin-top: 10px;">Focus Area: Public Health</p>
            <p style="font-size: 14px; margin-top: 10px;">Mission: To serve, advocate, and collaborate for those in need by developing innovative strategies for self-empowerment.</p>
            <p style="font-size: 14px; margin-top: 10px;">Vision: To eliminate poverty in Merced County through individual and organizational dedication, collaboration, and innovation.</p>
            <p style="font-size: 14px; margin-top: 10px;">Physical Address: 1235 W Main St. Merced, CA 95340</p>
            <p style="font-size: 14px; margin-top: 10px;">Website: <a href="https://www.mercedcaa.com/" target="_blank">Merced Community Action Agency (opens in new tab)</a></p>
        `
    };
</script>