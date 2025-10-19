<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Required Service Forms</title>
    <style>
        .ots-events-grid {
            display: grid;
            gap: 1.5rem;
            grid-template-columns: 1fr;
        }
        @media (min-width: 600px) {
            .ots-events-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (min-width: 900px) {
            .ots-events-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        .ots-event-card-gold a {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 4.5em;
            padding: 1em 1.5em;
            border: 2px solid #ffbf3c;
            border-radius: 8px;
            color: #d4851e;
            font-weight: bold;
            text-decoration: none;
            background: linear-gradient(135deg, #fffbf0 0%, #fff4e6 100%);
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(255, 191, 60, 0.1);
        }
        .ots-event-card-gold a:hover {
            background: linear-gradient(135deg, #ffbf3c 0%, #e6a829 100%);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(255, 191, 60, 0.4);
        }
        /* Optional: matches the look of other pages */
        .ots-section-headline {
            border-bottom: 2px solid #ffbf3c;
            font-size: 1.25rem;
            color: #333;
            text-align: center;
        }
        .ots-intro-text {
            line-height: 1.5;
            color: #555;
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .forms-page-container {
                margin-right: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="forms-page-container">
        <p class="ots-intro-text">Welcome! Before you sign our waivers, please visit our <strong>"Record Your Service Hours"</strong> section under our <strong>"Students"</strong> tab to get more information about community engagement and recording your hours.</p>
        <p class="ots-intro-text">The following webforms are <strong>mandatory</strong> for all students participating in community engagement. All web forms must be completed and submitted <strong>before</strong> students can begin volunteering off-campus.</p>
        <h3 class="ots-section-headline">Mandatory Forms</h3>
        <div class="ots-events-grid">
            <div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/form/community-engagement-responsibility-agreement-and-waiver-liability">Responsibility Agreement & Waiver </a></div>
            <div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/form/confidentiality-agreement">Confidentiality Agreement </a></div>
            <div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/form/canra">CANRA </a></div>
            <div class="ots-event-card-gold"><a href="https://cec.ucmerced.edu/release-form">Photo/Video/Audio Release Form </a></div>
        </div>
    </div>
</body>
</html>