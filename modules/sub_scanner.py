import requests
from bs4 import BeautifulSoup
import re

def discover_subdomains(domain):
    """crt.sh üzerinden subdomain taraması yapar."""
    url = f"https://crt.sh/?q={domain}"
    found_subs = set()
    
    try:
        # User-agent ekleyerek gerçek bir tarayıcı gibi davranalım
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Sayfadaki tüm tablo hücrelerini (td) tara
            tds = soup.find_all('td')
            for td in tds:
                content = td.text.strip()
                # Eğer içerik hedef domaini barındırıyorsa ve bir domain yapısındaysa al
                if domain in content:
                    # Bazen birden fazla domain aynı hücrede alt alta olabilir
                    lines = content.split('<br>')
                    for line in lines:
                        # Gereksiz karakterleri temizle (wildcard *, vs.)
                        clean_sub = line.replace('*.', '').strip()
                        if clean_sub.endswith(domain):
                            found_subs.add(clean_sub)
                            
        return list(found_subs)
    except Exception as e:
        print(f"Hata detayı: {e}")
        return []