import urllib.request
import re

urls = [
    'https://www.koppert.in/disease-control/powdery-mildew',
    'https://www.koppert.in/disease-control/downy-mildew-of-cucurbits',
    'https://www.koppert.in/disease-control/fusarium-wilt',
    'https://www.koppert.in/disease-control/bacterial-canker-of-tomato'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Extract title
        title_m = re.search(r'<title>(.*?)</title>', html)
        title = title_m.group(1) if title_m else ''
        
        # Extract h1, h2
        h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
        h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
        
        # Clean text
        h1_clean = [re.sub(r'<[^>]+>', '', x).strip() for x in h1]
        h2_clean = [re.sub(r'<[^>]+>', '', x).strip() for x in h2]
        
        print(f"=== {url} ===")
        print(f"Title: {title}")
        print(f"H1: {h1_clean}")
        print(f"H2: {h2_clean}")
        
        # Look for solutions / products on the page
        products = re.findall(r'<a[^>]*href=["\']/products/[^"\']+["\'][^>]*>(.*?)</a>', html, re.DOTALL)
        clean_prods = list(set([' '.join(re.sub(r'<[^>]+>', ' ', p).split()) for p in products if p.strip()]))
        print(f"Products / Solutions: {clean_prods[:8]}\n")
    except Exception as e:
        print(f"Error fetching {url}: {e}\n")
