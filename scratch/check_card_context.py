import re

with open('koppert_raw.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see how each disease card or item is structured in HTML
matches = re.findall(r'<div[^>]*class="[^"]*card[^"]*"[^>]*>.*?</div>', content, re.DOTALL)
print(f"Cards found by class='card': {len(matches)}")

# Let's search for snippets around '/disease-control/'
for m in re.finditer(r'<a\s+[^>]*href=["\'](/disease-control/[a-z0-9-]+)["\'][^>]*>(.*?)</a>', content, re.DOTALL):
    link = m.group(1)
    text = m.group(2)
    clean_text = ' '.join(re.sub(r'<[^>]+>', ' ', text).split())
    # find parent or following text
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 300)
    surrounding = content[start:end]
    clean_surrounding = ' '.join(re.sub(r'<[^>]+>', ' ', surrounding).split())
    print(f"URL: {link} -> {clean_text}")
    print(f"   Context: {clean_surrounding[:200]}...\n")
