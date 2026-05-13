import argparse
from modules.sub_scanner import discover_subdomains
from colorama import Fore, Style, init

# Renkleri Windows terminalinde de çalışacak hale getir
init(autoreset=True)

def banner():
    print(Fore.RED + """
    #######################################
    #          REDRECON v1.0              #
    #    Target Intelligence Tool         #
    #######################################
    """ + Style.RESET_ALL)

def main():
    banner()
    
    # Terminal argümanlarını ayarla
    parser = argparse.ArgumentParser(description="Basit bir keşif aracı.")
    parser.add_argument("-d", "--domain", help="Hedef domain (örn: hedef.com)", required=True)
    parser.add_argument("-o", "--output", help="Sonuçları dosyaya kaydet", action="store_true")
    
    args = parser.parse_args()
    target = args.domain

    print(f"{Fore.YELLOW}[*] {target} için keşif başlatıldı...")
    
    results = discover_subdomains(target)
    
    if results:
        print(f"{Fore.GREEN}[+] {len(results)} adet alt alan adı bulundu:\n")
        for sub in results:
            print(f"{Fore.CYAN}- {sub}")
            
        if args.output:
            with open(f"{target}_results.txt", "w") as f:
                for sub in results:
                    f.write(sub + "\n")
            print(f"\n{Fore.GREEN}[!] Sonuçlar {target}_results.txt dosyasına kaydedildi.")
    else:
        print(Fore.RED + "[!] Hiç sonuç bulunamadı.")

if __name__ == "__main__":
    main()