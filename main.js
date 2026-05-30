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

/* ---- MOBILE MENU ---- */
const mBtn = document.getElementById('mobileBtn');
const nav  = document.getElementById('navInner');
if (mBtn && nav) {
    mBtn.addEventListener('click', () => {
        const isOpen = nav.style.display === 'flex';
        nav.style.cssText = isOpen
            ? ''
            : 'display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:var(--navy2);padding:20px 28px;gap:12px;z-index:999;';
        mBtn.innerHTML = isOpen ? '<i class="fas fa-bars"></i>' : '<i class="fas fa-times"></i>';
    });
}

/* ---- HERO BG CYCLING ---- */
const heroBgs = [
    "content doc/images/hero.png",
    "content doc/images/hero2.png",
    "content doc/images/hero3.png"
];
const heroSlides = [
    { title: "Your #1 Healthcare<br>Partners in Kent.", desc: "Defining the gold standard in physical healthcare and patient-centric clinical excellence in Ashford, Kent." },
    { title: "Advanced Physiotherapy<br>Specialists.", desc: "Expert MSK assessments and specialist treatments for a faster, safer recovery journey." },
    { title: "Women's Health<br>&amp; Wellbeing.", desc: "Expert women's health treatments and pelvic health clinical strategy tailored for you." }
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
    // Start exit animations
    if (heroImg) heroImg.classList.add('hero-img-anim-exit');
    if (heroTitle) heroTitle.classList.add('hero-content-anim-exit');

    setTimeout(() => {
        // Change content
        if (heroImg) {
            heroImg.src = heroBgs[hIdx];
            heroImg.classList.remove('hero-img-anim-exit');
            heroImg.classList.remove('hero-img-anim');
            void heroImg.offsetWidth; // trigger reflow
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

// Initial entrance animation
if (heroImg) heroImg.classList.add('hero-img-anim');
if (heroTitle) heroTitle.classList.add('hero-content-anim');

// Auto-cycle every 5s
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
    
    // Add glassmorphism when scrolled down
    if (scrollTop > 50) {
        header.classList.add('header-scrolled');
    } else {
        header.classList.remove('header-scrolled');
    }

    // Hide/show logic
    if (scrollTop > lastScrollTop && scrollTop > 150) {
        // Scrolling down
        header.classList.add('header-hidden');
    } else {
        // Scrolling up
        header.classList.remove('header-hidden');
    }
    
    lastScrollTop = scrollTop;
});
