import urllib.request
import re

url = 'https://www.koppert.in/disease-control/powdery-mildew'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')

# Split by h2 or div
parts = re.split(r'<h[23][^>]*>', html)
print(f"Total sections: {len(parts)}")
for i, part in enumerate(parts[1:], 1):
    heading_end = part.find('</h')
    if heading_end != -1:
        h_text = re.sub(r'<[^>]+>', ' ', part[:heading_end]).strip()
        h_text = ' '.join(h_text.split())
        body = part[heading_end:]
        # Remove scripts, styles
        body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
        body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
        clean_body = re.sub(r'<[^>]+>', ' ', body).strip()
        clean_body = ' '.join(clean_body.split())
        print(f"\n--- Section {i}: {h_text} ---")
        print(clean_body[:300] + '...')
