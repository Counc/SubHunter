import socket
import threading
from queue import Queue
import os
from colorama import init, Fore, Style

# Colorama'yı başlat
init(autoreset=True)

# Socket zaman aşımı (donmaları önlemek için)
socket.setdefaulttimeout(2.0)

def banner():
    print(f"""{Fore.CYAN}{Style.BRIGHT}
   ____        _     _                  _            
  / ___| _   _| |__ | |__  _   _ _ __  | |_ ___ _ __ 
  \___ \| | | | '_ \| '_ \| | | | '_ \ | __/ _ \ '__|
   ___) | |_| | |_) | |_) | |_| | | | || ||  __/ |   
  |____/ \__,_|_.__/|_.__/ \__,_|_| |_| \__\___|_|   
    {Style.RESET_ALL}
    {Fore.GREEN}>> GitHub: Counc{Style.RESET_ALL}
    """)

# Varsayılan temel wordlist
DEFAULT_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "web", "server",
    "ns2", "firewall", "admin", "portal", "ns", "dns", "imap", "proxy", "ns3", "blog",
    "test", "shop", "cpanel", "whm", "autodiscover", "exchange", "secure",
    "vpn", "api", "dev", "staging", "panel", "login", "cloud", "s3", "db", "database",
    "support", "help", "status", "dashboard", "git", "gitlab", "jenkins", "ssh"
]

results_lock = threading.Lock()
active_subdomains = []

def check_subdomain(domain, sub):
    target = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        with results_lock:
            print(f"{Fore.GREEN}[+] Aktif Bulundu: {Style.BRIGHT}{target}{Style.RESET_ALL} ({ip})")
            active_subdomains.append(target)
    except (socket.gaierror, socket.timeout):
        pass
    except Exception:
        pass

def worker(domain, q):
    while not q.empty():
        sub = q.get()
        check_subdomain(domain, sub)
        q.task_done()

def main():
    banner()
    
    # Kullanıcıdan domaini interaktif olarak istiyoruz
    raw_domain = input(f"{Style.BRIGHT}[?] Taranacak hedef domaini girin (örn: google.com): {Style.RESET_ALL}").strip()
    
    if not raw_domain:
        print(f"{Fore.RED}[!] Geçerli bir domain girmelisiniz!{Style.RESET_ALL}")
        return

    # Eğer kullanıcı https:// veya sonuna / eklediyse temizleyelim
    if "://" in raw_domain:
        raw_domain = raw_domain.split("://")[1]
    domain = raw_domain.split("/")[0]

    # İsteğe bağlı özel wordlist sorma
    wordlist_file = input(f"{Style.BRIGHT}[?] Özel wordlist dosyan varsa adını yaz (Yoksa direkt Enter'a bas): {Style.RESET_ALL}").strip()
    
    subdomains = []
    if wordlist_file:
        if os.path.exists(wordlist_file):
            print(f"[*] Wordlist yükleniyor: {Fore.CYAN}{wordlist_file}{Style.RESET_ALL}")
            with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
                subdomains = [line.strip() for line in f if line.strip()]
        else:
            print(f"{Fore.RED}[!] Dosya bulunamadı, varsayılan liste kullanılıyor.{Style.RESET_ALL}")
            subdomains = DEFAULT_SUBDOMAINS
    else:
        subdomains = DEFAULT_SUBDOMAINS

    print(f"\n[*] Hedef Taranıyor: {Fore.CYAN}{domain}{Style.RESET_ALL}")
    print(f"[*] Toplam {len(subdomains)} kelime taranacak.\n")
    
    q = Queue()
    for sub in subdomains:
        q.put(sub)
        
    threads = []
    for _ in range(20):
        t = threading.Thread(target=worker, args=(domain, q))
        t.daemon = True
        t.start()
        threads.append(t)
        
    try:
        q.join()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Tarama durduruldu.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}[*] Tarama Tamamlandı! Toplam {len(active_subdomains)} aktif alt alan adı bulundu.{Style.RESET_ALL}")
    
    if active_subdomains:
        save = input(f"{Style.BRIGHT}[?] Sonuçlar kaydedilsin mi? (E/H): {Style.RESET_ALL}").strip().lower()
        if save in ['e', 'y']:
            filename = f"{domain}_subdomains.txt"
            with open(filename, "w", encoding="utf-8") as f:
                for sub in active_subdomains:
                    f.write(f"{sub}\n")
            print(f"{Fore.GREEN}[+] Kaydedildi: {filename}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
<<<<<<< HEAD

=======
  
>>>>>>> 45facbeb4684d1d5f7e1610deefdf0bdb2d3014f
