import urllib.request
import re

url = 'https://www.farmlytai.in/assets/index-BsJrNQlh.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Search for dT and uT
for var_name in ['dT', 'uT', 'fT']:
    for m in re.finditer(rf'\b{var_name}\s*=', content):
        start = max(0, m.start() - 50)
        end = min(len(content), m.end() + 200)
        print(f'{var_name} definition:', content[start:end])
        print('---')
