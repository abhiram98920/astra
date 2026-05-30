import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all cards and their icons
cards = re.findall(r'(<div class="coe-card.*?">.*?<div class="coe-card-top">\s*<i class="fas (fa-.*?)"></i>)', content, re.DOTALL)

for card_html, icon_class in cards:
    # insert watermark just before the coe-card-top
    watermark = f'<i class="fas {icon_class} watermark"></i>\n                        '
    new_card_html = card_html.replace('<div class="coe-card-top">', watermark + '<div class="coe-card-top">')
    content = content.replace(card_html, new_card_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
