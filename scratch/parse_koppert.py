import re
from html.parser import HTMLParser

with open('koppert_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all links and headings
print("--- HEADINGS ---")
for h in re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL):
    clean_h = re.sub(r'<[^>]+>', ' ', h).strip()
    clean_h = ' '.join(clean_h.split())
    if clean_h:
        print(clean_h)

print("\n--- DISEASE LINKS / CARDS ---")
found_links = set()
for m in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content, re.DOTALL):
    href = m.group(1)
    inner = m.group(2)
    clean_text = ' '.join(re.sub(r'<[^>]+>', ' ', inner).split())
    if any(k in href for k in ['disease', 'powdery', 'downy', 'botrytis', 'fusarium', 'pythium', 'rhizoctonia', 'phytophthora', 'canker', 'blight', 'mildew', 'nematode']):
        if href not in found_links and clean_text:
            found_links.add(href)
            print(f"{href} -> {clean_text}")
