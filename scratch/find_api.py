import urllib.request
import re

url = 'https://www.farmlytai.in/assets/index-BsJrNQlh.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Search for pT definition
match = re.search(r'pT=.*?function.*?(?=function|\n|;var)', content)
if not match:
    match = re.search(r'(async function pT|const pT=|var pT=|let pT=)[^;]+', content)
if match:
    print('pT match:', match.group(0)[:500])
else:
    # Search for pT around occurrences
    for m in re.finditer(r'pT\b', content):
        start = max(0, m.start() - 100)
        end = min(len(content), m.end() + 200)
        print('pT context:', content[start:end])
        print('---')
