import os
import re

dir_path = r"c:\Users\Abhiram P M\Desktop\BT\astranew"

faq_partners_html = """
    <!-- FAQ SECTION -->
    <section class="faq-section" style="background-color:#0A4DA2; color: #fff; padding: 80px 0 20px;">
        <div class="container" style="max-width: 900px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 40px;">
                <p style="font-size: 14px; font-weight: 300; margin-bottom: 5px;">Frequently Asked Questions</p>
                <h2 class="section-title" style="font-size: 36px; font-weight: 600; margin: 0; color: #fff;">Need To Know?</h2>
            </div>
            
            <div class="faq-list">
                <div class="faq-item">
                    <button class="faq-question">What services does Astra Health offer? <span class="faq-icon"><i class="fas fa-plus"></i></span></button>
                    <div class="faq-answer">
                        <p>We offer a comprehensive range of services including Physiotherapy, MSK Assessment, Joint Injections, Acupuncture, Women's Health, and Private GP services.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">How do I book an appointment? <span class="faq-icon"><i class="fas fa-plus"></i></span></button>
                    <div class="faq-answer">
                        <p>You can book an appointment online through our website, or by calling our appointment line at 01233 631 555.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What should I bring to my appointment? <span class="faq-icon"><i class="fas fa-plus"></i></span></button>
                    <div class="faq-answer">
                        <p>Please bring any relevant medical records, a list of current medications, and wear comfortable clothing if you are attending a physiotherapy session.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What are the visiting hours at Astra Health? <span class="faq-icon"><i class="fas fa-plus"></i></span></button>
                    <div class="faq-answer">
                        <p>Our clinics are generally open from 8:00 AM to 6:00 PM on weekdays. For specific department timings, please check our services page or contact us.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Does Astra Health offer home healthcare services? <span class="faq-icon"><i class="fas fa-plus"></i></span></button>
                    <div class="faq-answer">
                        <p>Yes, we do offer specialized home visits for patients who are unable to travel. Please contact us directly to arrange a home consultation.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PARTNERS -->
    <section class="section-padding partners-section" style="background-color:#0A4DA2; padding-bottom:120px;">
        <div class="container" style="max-width: 1200px; margin: 0 auto;">
            <h2 class="section-title" style="margin-bottom: 10px; font-size: 32px; color: #fff;">Professional Partners</h2>
            <div class="partners-grid">
                <span class="partner-logo">WPA</span>
                <span class="partner-logo">PruHealth</span>
                <span class="partner-logo">Cigna</span>
                <span class="partner-logo">AVIVA</span>
                <span class="partner-logo">Simplyhealth</span>
                <span class="partner-logo">NHS</span>
            </div>
        </div>
    </section>
"""

# Append CSS to style.css
css_to_add = """
/* FAQ SECTION */
.faq-section {
    font-family: 'Poppins', sans-serif;
}
.faq-list {
    border-top: 1px solid rgba(255,255,255,0.1);
}
.faq-item {
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.faq-question {
    width: 100%;
    text-align: left;
    background: none;
    border: none;
    color: #fff;
    font-size: 16px;
    font-weight: 500;
    padding: 20px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    font-family: inherit;
}
.faq-icon {
    background-color: #2196f3;
    color: #fff;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-size: 12px;
    transition: transform 0.3s ease;
}
.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}
.faq-answer p {
    color: #A9DDFB;
    padding-bottom: 20px;
    margin: 0;
    font-size: 14px;
    font-weight: 300;
}
"""

style_path = os.path.join(dir_path, "style.css")
with open(style_path, 'r', encoding='utf-8') as f:
    style_content = f.read()

if "/* FAQ SECTION */" not in style_content:
    with open(style_path, 'a', encoding='utf-8') as f:
        f.write("\n" + css_to_add)
    print("Added CSS to style.css")

# Append JS to main.js
js_to_add = """
// FAQ Accordion
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.faq-question').forEach(button => {
        button.addEventListener('click', () => {
            const faqItem = button.parentElement;
            const isActive = faqItem.classList.contains('active');
            
            // Close all other faqs
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
"""

js_path = os.path.join(dir_path, "main.js")
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

if "// FAQ Accordion" not in js_content:
    with open(js_path, 'a', encoding='utf-8') as f:
        f.write("\n" + js_to_add)
    print("Added JS to main.js")

# Modify all HTML files
for filename in os.listdir(dir_path):
    if filename.endswith(".html") and filename not in ["new_footer.html", "original_index.html"]:
        filepath = os.path.join(dir_path, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            continue
            
        original_content = content
        
        # Remove existing PARTNERS section if present
        content = re.sub(r'<!-- PARTNERS -->\s*<section class=".*?partners-section".*?</section>', '', content, flags=re.DOTALL)
        
        # Remove existing FAQ section if present
        content = re.sub(r'<!-- FAQ SECTION -->\s*<section class="faq-section".*?</section>', '', content, flags=re.DOTALL)
        
        # Inject FAQ_PARTNERS_HTML before <footer
        # some files have <footer class="...">, some have <footer>
        content = re.sub(r'(<footer\b[^>]*>)', lambda m: faq_partners_html + "\n" + m.group(1), content, count=1)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected FAQ + Partners into {filename}")
