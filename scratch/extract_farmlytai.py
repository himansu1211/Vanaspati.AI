import urllib.request
import re

url = 'https://www.farmlytai.in/assets/index-BsJrNQlh.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Search for any js filenames
js_files = set(re.findall(r'["\']([a-zA-Z0-9_\-\./]+\.js)["\']', content))
print(f'Found {len(js_files)} JS files:')
for j in list(js_files)[:30]:
    print(' ', j)

# Search for blog
blog_matches = set(re.findall(r'["\']([^"\']*blog[^"\']*)["\']', content, re.IGNORECASE))
print(f'\nFound {len(blog_matches)} blog matches:')
for b in list(blog_matches)[:30]:
    print(' ', b)

# Search for plant
plant_matches = set(re.findall(r'["\']([^"\']*plant[^"\']*)["\']', content, re.IGNORECASE))
print(f'\nFound {len(plant_matches)} plant matches:')
for p in list(plant_matches)[:30]:
    print(' ', p)
