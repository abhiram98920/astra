import json
import re

log_path = r'C:\Users\Abhiram P M\.gemini\antigravity\brain\1a270961-5c6b-4378-98eb-dcbe67c2428b\.system_generated\logs\transcript.jsonl'
with open(log_path, encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    if 'view_file' in line and 'index.html' in line and 'Total Lines:' in line:
        try:
            data = json.loads(line)
            content = data.get('content', '')
            if content:
                # The content usually contains line numbers like "1: <!DOCTYPE html>"
                # We can strip them.
                clean_lines = []
                for cl in content.split('\n'):
                    match = re.match(r'^\d+:\s(.*)', cl)
                    if match:
                        clean_lines.append(match.group(1))
                if clean_lines:
                    with open('recovered_index.html', 'w', encoding='utf-8') as out:
                        out.write('\n'.join(clean_lines))
                    print("Recovered!")
                    break
        except Exception as e:
            pass
