import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

header_start = idx_content.find('<!-- TRANSPARENT MAIN HEADER -->')
header_end = idx_content.find('</header>') + len('</header>')
new_header = idx_content[header_start:header_end]

footer_start = idx_content.find('<!-- FOOTER -->')
footer_end = idx_content.find('</footer>') + len('</footer>')
new_footer = idx_content[footer_start:footer_end]

with open('generate_pages.py', 'r', encoding='utf-8') as f:
    py_content = f.read()

# Replace header
py_content = re.sub(r'<!-- HEADER -->.*?<\/header>', new_header, py_content, flags=re.DOTALL)

# Replace footer
py_content = re.sub(r'<!-- FOOTER -->.*?<\/footer>', new_footer, py_content, flags=re.DOTALL)

with open('generate_pages.py', 'w', encoding='utf-8') as f:
    f.write(py_content)
