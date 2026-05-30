import os
import re

dir_path = r"c:\Users\Abhiram P M\Desktop\BT\astranew"

for filename in os.listdir(dir_path):
    if filename.endswith(".html") and filename not in ["new_footer.html", "original_index.html"]:
        filepath = os.path.join(dir_path, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            continue
            
        original_content = content
        
        # 1. Inject responsive.css after style.css
        if "responsive.css" not in content:
            content = re.sub(r'(<link rel="stylesheet" href="style\.css">)', r'\1\n    <link rel="stylesheet" href="responsive.css">', content)
            
        # 2. Inject hamburger menu inside main-header
        # Look for <header class="main-header">
        if "hamburger-menu" not in content:
            hamburger_html = '\n            <!-- Mobile Menu Toggle -->\n            <div class="hamburger-menu" id="mobile-menu-btn" style="display:none;"><i class="fas fa-bars"></i></div>\n'
            # Insert after the closing </div> of header-logo
            content = re.sub(r'(<div class="header-logo">.*?</div>)', r'\1' + hamburger_html, content, flags=re.DOTALL)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected responsive tags into {filename}")

# 3. Add JS toggle logic to main.js
js_path = os.path.join(dir_path, "main.js")
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

toggle_js = """
// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.querySelector('.main-nav-links');
    
    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileBtn.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Toggle mega menu on mobile
    const megaToggles = document.querySelectorAll('.nav-item-mega > a');
    megaToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 1024) {
                e.preventDefault();
                toggle.parentElement.classList.toggle('open');
            }
        });
    });
});
"""

if "// Mobile Menu Toggle" not in js_content:
    with open(js_path, 'a', encoding='utf-8') as f:
        f.write("\n" + toggle_js)
    print("Added Mobile Menu logic to main.js")

