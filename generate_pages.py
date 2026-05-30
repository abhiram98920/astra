import os

header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- TRANSPARENT MAIN HEADER -->
        <header class="main-header">
            <div class="header-logo">
                <a href="index.html">
                    <img src="content doc/images/logo.avif" alt="Astra Health">
                </a>
            </div>
            
            <div class="header-right">
                <!-- TOP CONTACTS -->
                <div class="top-contacts">
                    <a href="tel:01233631555"><i class="fas fa-phone-alt" style="color: #A9DDFB;"></i> 01233 631 555</a>
                    <a href="mailto:admin@astrahealth.uk"><i class="fas fa-envelope" style="color: #A9DDFB;"></i> admin@astrahealth.uk</a>
                    <span style="display: flex; align-items: center; gap: 5px;"><i class="fas fa-shield-alt" style="color: #A9DDFB;"></i> Trusted Partner</span>
                    <div class="lang-switch">
                        <img src="https://flagcdn.com/w20/gb.png" alt="English">
                        <span style="font-weight: 500;">EN</span>
                        <span style="opacity: 0.6;">AR</span>
                    </div>
                </div>

                <!-- MAIN NAV -->
                <nav class="main-nav-links">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About</a>
                
                <!-- Services Mega Menu -->
                <div class="nav-item-mega">
                    <a href="services.html" class="nav-link">Services <i class="fas fa-chevron-down" style="font-size: 10px;"></i></a>
                    <div class="mega-menu">
                        <div class="mega-srv-grid">
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/hero2.png" alt="MSK">
                                <span>MSK Assessment</span>
                            </a>
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/pillar-experienced.png" alt="Joint">
                                <span>Joint Injections</span>
                            </a>
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/service_shockwave_1778168510104.png" alt="Shockwave">
                                <span>Shockwave Therapy</span>
                            </a>
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/service_acupuncture.png" alt="Acupuncture">
                                <span>Acupuncture</span>
                            </a>
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/service_manual_therapy.png" alt="Manual">
                                <span>Manual Therapy</span>
                            </a>
                            <a href="services.html" class="mega-srv-item">
                                <img src="content doc/images/pillar-caring.png" alt="Urogynecology">
                                <span>Urogynecology</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Doctors Mega Menu -->
                <div class="nav-item-mega">
                    <a href="team.html" class="nav-link">Doctors <i class="fas fa-chevron-down" style="font-size: 10px;"></i></a>
                    <div class="mega-menu">
                        <div class="mega-doc-card">
                            <img src="content doc/images/team-sumin.avif" alt="Sumin Moses">
                            <h4>Sumin Moses</h4>
                            <p>Specialist MSK Physio</p>
                        </div>
                        <div class="mega-doc-card">
                            <img src="content doc/images/team-ruth.avif" onerror="this.src='content doc/images/pillar-friendly.png'" alt="Ruth Jayakaran">
                            <h4>Ruth Jayakaran</h4>
                            <p>Director & Senior Physio</p>
                        </div>
                        <div style="display: flex; align-items: center; justify-content: center; padding: 0 20px;">
                            <a href="team.html" class="btn-appointment" style="background: var(--primary);"><i class="fas fa-user-md"></i> View All Doctors</a>
                        </div>
                    </div>
                </div>

                <a href="contact.html" class="nav-link">Contact</a>
                <a href="contact.html" class="btn-appointment"><i class="fas fa-calendar-plus"></i> Book Appointment</a>
            </nav>
            </div>
        </header>

    <!-- INNER PAGE HERO -->
    <section class="hero-section" style="height: 400px; padding-top: 150px; text-align: center; justify-content: center; background: linear-gradient(rgba(18,43,75,0.8), rgba(18,43,75,0.8)), url('content doc/images/hero2.png') center/cover;">
        <div class="hero-content" style="max-width: 800px; margin: 0 auto; color: #fff;">
            <h1 style="font-size: 50px; margin-bottom: 20px;">{hero_heading}</h1>
            <p style="font-size: 18px; opacity: 0.9;">{hero_sub}</p>
        </div>
    </section>
"""

footer = """
    <!-- FOOTER -->
    <footer class="main-footer">
        <div class="footer-top">
            <div class="ft-logo">
                <img src="content doc/images/logo.avif" alt="Logo">
                <p style="font-family: 'Libre Franklin'; font-size: 14px; opacity: 0.8; line-height: 1.6;">
                    Defining the gold standard in physical healthcare and patient-centric clinical excellence in Ashford, Kent.
                </p>
            </div>
            <div class="footer-links">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="team.html">Our Team</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h4>Clinic Hours</h4>
                <ul>
                    <li style="color: rgba(255,255,255,0.8);">Mon — Fri: 08:00 - 20:00</li>
                    <li style="color: rgba(255,255,255,0.8);">Sat: 09:00 - 14:00</li>
                    <li style="color: rgba(255,255,255,0.8);">Sun: Closed</li>
                </ul>
            </div>
            <div class="footer-links">
                <h4>Contact Us</h4>
                <ul>
                    <li><i class="fas fa-map-marker-alt" style="margin-right: 10px;"></i> 11 Repton Avenue, Ashford, Kent</li>
                    <li><i class="fas fa-phone-alt" style="margin-right: 10px;"></i> 01233 631 555</li>
                    <li><i class="fas fa-envelope" style="margin-right: 10px;"></i> admin@astrahealth.uk</li>
                </ul>
            </div>
        </div>
        <div class="footer-copy">
            &copy; 2026 Astra Health. Designed By Bten.in
        </div>
    </footer>
    <script src="main.js"></script>
</body>
</html>
"""

# ABOUT PAGE
about_html = header.format(
    title="About Us - Astra Health",
    hero_heading="About Us",
    hero_sub="Learn everything there is to know about our local clinic, our friendly team and our top-of-the-line equipment."
) + """
    <section class="section-padding">
        <div class="container philosophy-grid" style="max-width: 1200px; margin: 0 auto;">
            <div>
                <h2 class="section-title dark">Our Story</h2>
                <div class="divider"></div>
                <p style="color: #666; font-size: 16px; line-height: 1.8; margin-bottom: 20px;">
                    Founded in 2014 by Sumin Moses and Ruth Jayakaran, Astra Health has become one of the county's most trusted clinical practices. With a 4.8/5 rating on Google, our team of 8 specialists practises across Kent, delivering exceptional care.
                </p>
                <p style="color: #666; font-size: 16px; line-height: 1.8;">
                    We are proud recipients of the Excellent Customer Care Award (KCHT NHS Trust) in 2014.
                </p>
            </div>
            <div class="philosophy-image-container">
                <img src="content doc/images/pillar-experienced.png" alt="Our Founders" class="philosophy-img-main" style="height: 400px;">
            </div>
        </div>
    </section>

    <section class="section-padding" style="background: var(--bg-light);">
        <div class="container philosophy-grid" style="max-width: 1200px; margin: 0 auto;">
            <div class="philosophy-image-container">
                <img src="content doc/images/pillar-caring.png" alt="Our Mission" class="philosophy-img-main" style="height: 400px;">
            </div>
            <div>
                <h2 class="section-title dark">Our Mission</h2>
                <div class="divider"></div>
                <p style="color: #666; font-size: 16px; line-height: 1.8; margin-bottom: 20px;">
                    Our goal is to help our patients live a healthy, pain-free life and strive to provide the highest quality of care, guidance and support. We provide late evening, early morning, and weekend appointments, with urgent appointments available within 24 hours.
                </p>
                <p style="color: #666; font-size: 16px; line-height: 1.8;">
                    We guarantee a safe and comfortable environment while creating an atmosphere of trust and respect.
                </p>
            </div>
        </div>
    </section>
""" + footer

# SERVICES PAGE
services_html = header.format(
    title="Services - Astra Health",
    hero_heading="Our Services",
    hero_sub="Comprehensive medical care and specialist physiotherapy tailored to your unique needs."
) + """
    <section class="section-padding" style="background: #fff;">
        <div class="container" style="max-width: 1200px; margin: 0 auto;">
            <div class="services-row" style="flex-wrap: wrap; justify-content: center; gap: 30px;">
                
                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-bone"></i></div>
                    <div class="s-card-text">
                        <h3>MSK Assessment</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Treating conditions affecting muscles, joints, bones, and soft tissues.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-syringe"></i></div>
                    <div class="s-card-text">
                        <h3>Joint Injections</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Relieve pain and inflammation for osteoarthritis and tendinitis.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-bolt"></i></div>
                    <div class="s-card-text">
                        <h3>Shockwave Therapy</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Non-invasive treatment using sound waves to stimulate healing.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-magic"></i></div>
                    <div class="s-card-text">
                        <h3>Acupuncture</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Traditional Chinese medicine to balance energy flow.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-hands-helping"></i></div>
                    <div class="s-card-text">
                        <h3>Manual Therapy</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Hands-on assessment and treatment of joint mobility and function.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-female"></i></div>
                    <div class="s-card-text">
                        <h3>Urogynecological</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Treating pelvic floor dysfunction, bladder, bowel and sexual health.</p>
                    </div>
                </div>
                
                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-baby-carriage"></i></div>
                    <div class="s-card-text">
                        <h3>Pregnancy Care</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Managing physical changes and challenges throughout pregnancy.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-stethoscope"></i></div>
                    <div class="s-card-text">
                        <h3>Post-natal checks</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Checkups to ensure mother and baby are recovering well.</p>
                    </div>
                </div>

                <div class="s-card" style="flex: 0 0 calc(33.333% - 30px); min-width: 300px;">
                    <div class="s-card-icon"><i class="fas fa-male"></i></div>
                    <div class="s-card-text">
                        <h3>Men's Health</h3>
                        <p style="font-size: 13px; color: #666; margin-top: 10px;">Tailored treatments for pelvic pain and wellness concerns.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>
""" + footer

# TEAM PAGE
team_html = header.format(
    title="Our Team - Astra Health",
    hero_heading="Meet our Team",
    hero_sub="Our team of highly trained experts is dedicated to your wellbeing."
) + """
    <section class="section-padding team-section-new">
        <div class="container" style="max-width: 1200px; margin: 0 auto;">
            <div class="team-cards-row" style="max-width: 1200px; grid-template-columns: repeat(3, 1fr);">
                
                <!-- Sumin -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/team-sumin.avif" alt="Sumin Moses"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Sumin Moses</h3>
                        <p class="expert-specialty"><i class="fas fa-user-md" style="color: var(--primary);"></i> Specialist MSK Physio</p>
                        <p class="expert-creds">Highly experienced and compassionate.</p>
                    </div>
                </div>

                <!-- Ruth -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/team-ruth.avif" onerror="this.src='content doc/images/pillar-friendly.png'" alt="Ruth Jayakaran"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Ruth Jayakaran</h3>
                        <p class="expert-specialty"><i class="fas fa-user-md" style="color: var(--primary);"></i> Director & Senior Physio</p>
                        <p class="expert-creds">15+ years exp., Women's health focus.</p>
                    </div>
                </div>

                <!-- Litto -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/hero-card.avif" alt="Litto Thomas"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Litto Thomas</h3>
                        <p class="expert-specialty"><i class="fas fa-user-md" style="color: var(--primary);"></i> Physiotherapist</p>
                        <p class="expert-creds">10+ years helping patients recover.</p>
                    </div>
                </div>

                <!-- Hirna -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/pillar-experienced.png" alt="Hirna Raje"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Hirna Raje</h3>
                        <p class="expert-specialty"><i class="fas fa-user-md" style="color: var(--primary);"></i> Physiotherapist</p>
                        <p class="expert-creds">10+ years experience, Masters Degree.</p>
                    </div>
                </div>

                <!-- Haripriya -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/pillar-caring.png" alt="Haripriya"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Haripriya K.</h3>
                        <p class="expert-specialty"><i class="fas fa-user-md" style="color: var(--primary);"></i> Physiotherapist</p>
                        <p class="expert-creds">Master's from Univ. of Nottingham.</p>
                    </div>
                </div>

                <!-- Fizzah -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/logo.avif" style="object-fit: contain;" alt="Fizzah"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Fizzah Lutufullah</h3>
                        <p class="expert-specialty"><i class="fas fa-clipboard" style="color: var(--primary);"></i> Senior Administrator</p>
                        <p class="expert-creds">Dedicated to smooth clinic operations.</p>
                    </div>
                </div>

                <!-- Tincy -->
                <div class="expert-card">
                    <div class="expert-img-wrapper"><img src="content doc/images/logo.avif" style="object-fit: contain;" alt="Tincy"></div>
                    <div class="expert-info-box">
                        <h3 class="expert-name">Tincy Mookkanolil</h3>
                        <p class="expert-specialty"><i class="fas fa-clipboard" style="color: var(--primary);"></i> Administrator</p>
                        <p class="expert-creds">MBA qualified administrator.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>
""" + footer

# CONTACT PAGE
contact_html = header.format(
    title="Contact Us - Astra Health",
    hero_heading="Get in Touch",
    hero_sub="We are here to help. Reach out to our Ashford clinic today to book an appointment."
) + """
    <section class="section-padding" style="background: #fff;">
        <div class="container philosophy-grid" style="max-width: 1200px; margin: 0 auto;">
            <div>
                <h2 class="section-title dark">Contact Details</h2>
                <div class="divider"></div>
                <ul style="list-style: none; padding: 0; font-size: 18px; color: #555; line-height: 2;">
                    <li><i class="fas fa-map-marker-alt" style="color: var(--primary); width: 30px;"></i> 11 Repton Avenue, Ashford, Kent, TN23 3RX</li>
                    <li><i class="fas fa-phone" style="color: var(--primary); width: 30px;"></i> <a href="tel:01233631555" style="color: inherit; text-decoration: none;">01233 631 555</a></li>
                    <li><i class="fas fa-envelope" style="color: var(--primary); width: 30px;"></i> <a href="mailto:admin@astrahealth.uk" style="color: inherit; text-decoration: none;">admin@astrahealth.uk</a></li>
                    <li><i class="fas fa-envelope" style="color: var(--primary); width: 30px;"></i> <a href="mailto:astraprivategp@gmail.com" style="color: inherit; text-decoration: none;">astraprivategp@gmail.com</a> (Private GPs)</li>
                </ul>
            </div>
            <div class="philosophy-image-container">
                <div style="background: #eee; height: 400px; border-radius: 20px; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <i class="fas fa-map-marked-alt" style="font-size: 60px; color: #ccc;"></i>
                    <p style="margin-top: 20px; color: #999;">Map embedded here</p>
                </div>
            </div>
        </div>
    </section>
""" + footer


import os
base_dir = r"c:\Users\Abhiram P M\Desktop\BT\astranew"

with open(os.path.join(base_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

with open(os.path.join(base_dir, "services.html"), "w", encoding="utf-8") as f:
    f.write(services_html)

with open(os.path.join(base_dir, "team.html"), "w", encoding="utf-8") as f:
    f.write(team_html)

with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

print("Inner pages generated successfully!")
