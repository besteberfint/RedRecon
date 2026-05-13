import requests
from bs4 import BeautifulSoup
import re

def discover_subdomains(domain):
    """crt.sh üzerinden daha dayanıklı bir şekilde subdomain taraması yapar."""
    # crt.sh bazen JSON formatında da yanıt verebilir, bu çok daha garantidir!
    url = f"https://crt.sh/?q={domain}&output=json"
    found_subs = set()
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        print(f"[*] Veri kaynağına bağlanılıyor: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # JSON yanıtını işle (HTML parsing'den çok daha sağlıklıdır)
            data = response.json()
            for entry in data:
                # 'name_value' alanı subdomain bilgisini içerir
                sub = entry['name_value'].lower()
                # Birden fazla subdomain varsa (satır sonu karakteriyle ayrılmış)
                for s in sub.split('\n'):
                    clean_sub = s.replace('*.', '').strip()
                    if clean_sub.endswith(domain):
                        found_subs.add(clean_sub)
        else:
            print(f"[!] Sunucu hatası: {response.status_code}")
            
        return sorted(list(found_subs))

    except Exception as e:
        print(f"[!] Hata: {e}")
        # Eğer JSON hatası alırsak (bazen site HTML döner), eski usul aramayı yedek olarak deneyelim
        return []