$filePath = "about.html"
$content = Get-Content $filePath -Raw -Encoding UTF8

$oldSection = @"
    <!-- Our Mission Section -->
    <section style="padding: 100px 0; background: #f8f9fa;">
        <div class="container">
            <div class="section-title reveal" style="text-align: center; margin-bottom: 60px;">
                <span>Our Philosophy</span>
                <h2>Our Mission &amp; Vision</h2>
            </div>
            <div style="max-width: 900px; margin: 0 auto; text-align: center;" class="reveal">
                <div style="margin-bottom: 40px; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 15px 40px rgba(0,0,0,0.05); position: relative;">
                    <i class="fas fa-quote-left" style="position: absolute; top: 30px; left: 30px; font-size: 40px; color: rgba(204,163,82,0.1);"></i>
                    <p style="font-size: 18px; line-height: 1.8; color: var(--secondary); font-weight: 500; font-style: italic;">
                        "Our mission is to help our patients live a healthy, pain-free life and we strive to provide the highest quality of care, guidance and support. We offer late evening, early morning and weekend appointments to suit your needs. Most urgent appointments are made within 24 hours so you can be sure to get a sound working diagnosis on your first visit."
                    </p>
                    <p style="font-size: 18px; line-height: 1.8; color: var(--secondary); font-weight: 500; font-style: italic; margin-top: 20px;">
                        "Our goal is to offer personalized treatments tailored to each individual's needs and goals. We are committed to providing a safe and comfortable environment while creating an atmosphere of trust and respect."
                    </p>
                </div>
            </div>
        </div>
    </section>
"@

$newSection = @"
    <!-- Mission & Vision Section -->
    <section class="mission-vision-section">
        <div class="mv-dots mv-dots-tl"></div>
        <div class="mv-dots mv-dots-br"></div>
        <div class="container">
            <div class="section-title reveal" style="text-align:center; margin-bottom: 60px;">
                <span>Our Foundation</span>
                <h2 style="color:#fff;">Mission &amp; Vision</h2>
            </div>
            <div class="mv-grid">
                <div class="mv-block reveal">
                    <div class="mv-icon"><i class="fas fa-bullseye"></i></div>
                    <h3 class="mv-heading">Our Mission</h3>
                    <div class="mv-divider"></div>
                    <p class="mv-text">Our mission is to help our patients live a healthy, pain-free life. We strive to provide the highest quality of care, guidance and support with urgent appointments available within 24 hours.</p>
                    <ul class="mv-list">
                        <li><i class="fas fa-check"></i> Urgent appointments within 24 hours</li>
                        <li><i class="fas fa-check"></i> Evidence-based clinical practices</li>
                        <li><i class="fas fa-check"></i> Compassionate, patient-first care</li>
                    </ul>
                </div>
                <div class="mv-sep reveal"><span>AND</span></div>
                <div class="mv-block reveal">
                    <div class="mv-icon mv-icon-accent"><i class="fas fa-eye"></i></div>
                    <h3 class="mv-heading">Our Vision</h3>
                    <div class="mv-divider mv-divider-accent"></div>
                    <p class="mv-text">To offer personalised treatments tailored to each individual's needs, in a safe, comfortable environment built on trust, respect and clinical excellence.</p>
                    <ul class="mv-list">
                        <li><i class="fas fa-check"></i> Regional leader in MSK &amp; Physio care</li>
                        <li><i class="fas fa-check"></i> Trusted by thousands of patients</li>
                        <li><i class="fas fa-check"></i> Expanding specialist services every year</li>
                    </ul>
                </div>
            </div>
            <div class="mv-stats reveal">
                <div class="mv-stat"><span class="stat-number" data-target="4.8">0</span><span class="stat-label">Google Rating</span></div>
                <div class="mv-stat"><span class="stat-number" data-target="8">0</span><span class="stat-label">Specialists</span></div>
                <div class="mv-stat"><span class="stat-number" data-target="20">0</span><span class="stat-label">Years Experience</span></div>
                <div class="mv-stat"><span class="stat-number" data-target="2014">0</span><span class="stat-label">Est. Year</span></div>
            </div>
        </div>
    </section>
"@

if ($content.Contains("Our Mission Section")) {
    $newContent = $content.Replace($oldSection, $newSection)
    if ($newContent -ne $content) {
        Set-Content $filePath -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "SUCCESS: Mission section replaced."
    } else {
        Write-Host "WARN: String not matched exactly. Trying line-normalised replace..."
        # Try with CRLF normalization
        $oldNorm = $oldSection -replace "`r`n", "`n"
        $contentNorm = $content -replace "`r`n", "`n"
        $newNorm = $contentNorm.Replace($oldNorm, $newSection)
        if ($newNorm -ne $contentNorm) {
            Set-Content $filePath -Value $newNorm -Encoding UTF8 -NoNewline
            Write-Host "SUCCESS via CRLF normalization."
        } else {
            Write-Host "FAIL: Could not match section."
        }
    }
} else {
    Write-Host "FAIL: Marker 'Our Mission Section' not found in file."
}
