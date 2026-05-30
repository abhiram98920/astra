/* =============================================
   ASTRA HEALTH — main.js
   ============================================= */

/* ---- REVEAL ON SCROLL ---- */
const revealEls = document.querySelectorAll('.reveal');
const revealObs = new IntersectionObserver((entries) => {
    entries.forEach((e, i) => {
        if (e.isIntersecting) {
            setTimeout(() => e.target.classList.add('active'), i * 90);
            revealObs.unobserve(e.target);
        }
    });
}, { threshold: 0.10 });
revealEls.forEach(el => revealObs.observe(el));

/* ---- SCROLL TO TOP ---- */
const scrollBtn = document.getElementById('scroll-to-top');
if (scrollBtn) {
    window.addEventListener('scroll', () => scrollBtn.classList.toggle('show', window.scrollY > 400));
    scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* ---- HERO BG CYCLING ---- */
const heroBgs = [
    "content doc/images/pexels-pavel-danilyuk-7653316.jpg",
    "content doc/images/pexels-yankrukov-8612918.jpg",
    "content doc/images/pexels-pavel-danilyuk-5998450.jpg"
];
const heroSlides = [
    { title: "Your #1 Healthcare<br><span class=\"hero-highlight\">Partners in Kent.</span>", desc: "Defining the gold standard in physical healthcare and patient-centric clinical excellence in Ashford, Kent." },
    { title: "Advanced Physiotherapy<br><span class=\"hero-highlight\">Specialists.</span>", desc: "Expert MSK assessments and specialist treatments for a faster, safer recovery journey." },
    { title: "Women's Health<br><span class=\"hero-highlight\">&amp; Wellbeing.</span>", desc: "Expert women's health treatments and pelvic health clinical strategy tailored for you." }
];
let hIdx = 0;
const heroImg   = document.querySelector('.hero-bg img');
const heroTitle = document.getElementById('heroTitle');
const heroPage  = document.querySelector('.hero-pagination');

function changeHeroSlide(dir) {
    hIdx = (hIdx + dir + heroBgs.length) % heroBgs.length;
    applyHeroSlide();
}
function applyHeroSlide() {
    if (heroImg) heroImg.classList.add('hero-img-anim-exit');
    if (heroTitle) heroTitle.classList.add('hero-content-anim-exit');

    setTimeout(() => {
        if (heroImg) {
            heroImg.src = heroBgs[hIdx];
            heroImg.classList.remove('hero-img-anim-exit');
            heroImg.classList.remove('hero-img-anim');
            void heroImg.offsetWidth;
            heroImg.classList.add('hero-img-anim');
        }
        if (heroTitle) {
            heroTitle.innerHTML = heroSlides[hIdx].title;
            heroTitle.classList.remove('hero-content-anim-exit');
            heroTitle.classList.remove('hero-content-anim');
            void heroTitle.offsetWidth;
            heroTitle.classList.add('hero-content-anim');
        }
        if (heroPage)  heroPage.innerHTML = `0${hIdx + 1}<span>/0${heroBgs.length}</span>`;
    }, 400);
}

if (heroImg) heroImg.classList.add('hero-img-anim');
if (heroTitle) heroTitle.classList.add('hero-content-anim');
setInterval(() => changeHeroSlide(1), 5000);

/* ---- FAQ ACCORDION ---- */
window.toggleFaq = function(qEl) {
    const item = qEl.closest('.faq-item');
    const list = item.closest('.faq-list');
    list.querySelectorAll('.faq-item.open').forEach(i => { if (i !== item) i.classList.remove('open'); });
    item.classList.toggle('open');
};

/* ---- DEDICATED TABS ---- */
const dedSets = [
    [
        { img:'content doc/images/pillar-experienced.png', title:'MSK Assessment', sub:'Musculoskeletal Care' },
        { img:'content doc/images/service_acupuncture.png', title:'Acupuncture', sub:'Holistic Therapy' },
        { img:'content doc/images/service_manual_therapy.png', title:'Manual Therapy', sub:'Hands-on Treatment' }
    ],
    [
        { img:'content doc/images/service_womens_health_1778168529217.png', title:"Women's Health", sub:'Pelvic Health Care' },
        { img:'content doc/images/service_postnatal.png', title:'Postnatal Checks', sub:'Post-natal Recovery' },
        { img:'content doc/images/hero3.png', title:'Pregnancy Care', sub:'Maternity Support' }
    ],
    [
        { img:'content doc/images/service_shockwave_1778168510104.png', title:'Shockwave Therapy', sub:'Chronic Pain Relief' },
        { img:'content doc/images/service_joint_injection.png', title:'Joint Injections', sub:'Targeted Treatment' },
        { img:'content doc/images/service_musculoskeletal_1778168487695.png', title:'MSK Treatment', sub:'Advanced Care' }
    ],
    [
        { img:'content doc/images/service_acupuncture.png', title:'Acupuncture', sub:'Pain Management' },
        { img:'content doc/images/service_manual_therapy.png', title:'Manual Therapy', sub:'Mobility Restoration' },
        { img:'content doc/images/service_mens_health.png', title:"Men's Health", sub:'Specialist Care' }
    ]
];

window.switchDed = function(tabEl, idx) {
    document.querySelectorAll('.ded-tab').forEach(t => t.classList.remove('active'));
    tabEl.classList.add('active');
    const sc = document.getElementById('servCards');
    if (!sc) return;
    sc.style.opacity = '0';
    setTimeout(() => {
        const set = dedSets[idx];
        sc.innerHTML = set.map(s => `
            <div class="serv-card">
                <img src="${s.img}" alt="${s.title}">
                <div class="serv-card-info">
                    <h5>${s.title}</h5>
                    <span>${s.sub}</span>
                </div>
            </div>
        `).join('');
        sc.style.opacity = '1';
    }, 220);
    sc.style.transition = 'opacity 0.22s ease';
};

/* ---- STICKY GLASSMORPHIC HEADER ---- */
const header = document.querySelector('.main-header') || document.querySelector('.header');
let lastScrollTop = 0;

window.addEventListener('scroll', () => {
    if (!header) return;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 50) {
        header.classList.add('header-scrolled');
    } else {
        header.classList.remove('header-scrolled');
    }

    if (scrollTop > lastScrollTop && scrollTop > 150) {
        header.classList.add('header-hidden');
    } else {
        header.classList.remove('header-hidden');
    }

    lastScrollTop = scrollTop;
});

/* ---- MOBILE MENU OVERLAY ---- */
const overlay = document.createElement('div');
overlay.className = 'mobile-overlay';
overlay.style.cssText = 'display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:999;opacity:0;transition:opacity 0.35s ease;';
document.body.appendChild(overlay);

function showOverlay(show) {
    overlay.style.display = show ? 'block' : 'none';
    setTimeout(() => { overlay.style.opacity = show ? '1' : '0'; }, 10);
    if (!show) {
        setTimeout(() => { if (overlay.style.opacity === '0') overlay.style.display = 'none'; }, 350);
    }
}

overlay.addEventListener('click', closeAllMobileMenus);

/* ---- MOBILE MENU SYSTEM ---- */
function closeAllMobileMenus() {
    document.querySelectorAll('.main-nav-links.active, .nav-inner.active, .nav-links.active').forEach(el => {
        el.classList.remove('active');
    });
    document.querySelectorAll('.hamburger-menu i, .mobile-btn i, .mobile-menu-btn i').forEach(icon => {
        icon.className = icon.className.replace('fa-times', 'fa-bars');
    });
    document.body.classList.remove('menu-open');
    showOverlay(false);
}

function toggleMobileMenu(btn, menu) {
    if (!btn || !menu) return;
    const isOpen = menu.classList.contains('active');
    menu.classList.toggle('active');
    const icon = btn.querySelector('i');
    if (icon) {
        icon.className = isOpen ? (icon.className.replace('fa-times', 'fa-bars')) : (icon.className.replace('fa-bars', 'fa-times'));
    }
    document.body.classList.toggle('menu-open', !isOpen);
    showOverlay(!isOpen);
}

document.addEventListener('DOMContentLoaded', () => {
    // System 1: #mobile-menu-btn + .main-nav-links (index, about, services, team, contact)
    const mainBtn = document.getElementById('mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav-links');
    if (mainBtn && mainNav) {
        mainBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMobileMenu(mainBtn, mainNav);
        });
    }

    // System 2: #mobileBtn + #navInner (service-details)
    const srvBtn = document.getElementById('mobileBtn');
    const srvNav = document.getElementById('navInner');
    if (srvBtn && srvNav) {
        srvBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMobileMenu(srvBtn, srvNav);
        });
    }

    // System 3: (legacy) .mobile-menu-btn (privacy, terms, 404 - now use system 2)

    // Close menu when clicking a link (all systems)
    document.querySelectorAll('.main-nav-links a, .nav-inner a, .nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            closeAllMobileMenus();
        });
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.main-nav-links, .nav-inner, .nav-links, .hamburger-menu, .mobile-btn, .mobile-menu-btn')) {
            closeAllMobileMenus();
        }
    });

    // Bottom tab: hide when footer is visible
    const sideWidgets = document.querySelector('.side-widgets');
    const footerEl = document.querySelector('.new-footer') || document.querySelector('footer');
    if (sideWidgets && footerEl) {
        const footerObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                sideWidgets.classList.toggle('hidden', entry.isIntersecting);
            });
        }, { threshold: 0.05 });
        footerObs.observe(footerEl);
    }
});

// FAQ Accordion
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.faq-question').forEach(button => {
        button.addEventListener('click', () => {
            const faqItem = button.parentElement;
            const isActive = faqItem.classList.contains('active');

            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
                item.querySelector('.faq-answer').style.maxHeight = null;
                const icon = item.querySelector('.faq-icon i');
                if(icon) {
                    icon.classList.remove('fa-minus');
                    icon.classList.add('fa-plus');
                }
            });

            if (!isActive) {
                faqItem.classList.add('active');
                const answer = faqItem.querySelector('.faq-answer');
                answer.style.maxHeight = answer.scrollHeight + "px";
                const icon = button.querySelector('.faq-icon i');
                if(icon) {
                    icon.classList.remove('fa-plus');
                    icon.classList.add('fa-minus');
                }
            }
        });
    });
});
