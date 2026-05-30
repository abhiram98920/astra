import os
import re

dir_path = r"c:\Users\Abhiram P M\Desktop\BT\astranew"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='utf-16') as f:
                content = f.read()
        except:
            print(f"Skipping {filepath} due to encoding issues.")
            return

    original_content = content
    
    # 1. Update Address (make sure it has TN23 3RX exactly once)
    # Match "11 Repton Avenue, Ashford, Kent" optionally followed by ", TN23 3RX"
    content = re.sub(r"11 Repton Avenue, Ashford, Kent(?:,\s*TN23 3RX)?", "11 Repton Avenue, Ashford, Kent, TN23 3RX", content)
    
    # Also handle multiline:
    content = re.sub(r"11 Repton Avenue, Ashford,<br>\s*Kent, UK\.?", "11 Repton Avenue, Ashford,<br>Kent, TN23 3RX.", content)
    
    # 2. Update Email appointments@astrahealth.uk to admin@astrahealth.uk
    content = content.replace("appointments@astrahealth.uk", "admin@astrahealth.uk")
    
    if content != original_content:
        # Save back with same encoding
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass
        print(f"Updated {filepath}")

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        process_file(filepath)
