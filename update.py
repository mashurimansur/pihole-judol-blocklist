import urllib.request
import re
import os

SOURCES = {
    "uun-aja_1": "https://raw.githubusercontent.com/uun-aja/judol-blocklist/main/judol-list.txt",
    "uun-aja_2": "https://raw.githubusercontent.com/uun-aja/judol-blocklist/main/judol-list02_bersih.txt",
    "arfshl": "https://raw.githubusercontent.com/arfshl/anti-gambling-domains/main/domains.txt",
    "mwhd96": "https://raw.githubusercontent.com/mwhd96/BlockListJudol/main/blockjudol.txt",
    "acma_australia": "https://raw.githubusercontent.com/elliotwutingfeng/ACMA-blocked-gambling-websites/main/urls-pihole.txt",
    "adguard_gambling": "https://raw.githubusercontent.com/RA-Apps/AdGuard-Gambling-List/main/blocklist.txt",
    "hosts_vn_gambling": "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/gambling/domain.txt",
    "hosts_vn_gambling_local": "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/gambling/domain-VN.txt"
}

def clean_domain(domain):
    domain = domain.strip().lower()
    # Remove Adblock Plus syntax like ||domain.com^
    domain = re.sub(r'^\|\|', '', domain)
    domain = re.sub(r'\^$', '', domain)
    # Remove hosts syntax
    domain = re.sub(r'^(127\.0\.0\.1|0\.0\.0\.0)\s+', '', domain)
    # Remove protocol
    domain = re.sub(r'^https?://', '', domain)
    # Remove paths
    domain = domain.split('/')[0]
    # Remove port
    domain = domain.split(':')[0]
    # Remove comments
    domain = domain.split('#')[0].strip()
    
    # Validate domain shape
    if not domain:
        return None
    if re.match(r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,50}$', domain):
        return domain
    return None

def main():
    unique_domains = set()
    for name, url in SOURCES.items():
        print(f"Fetching {name} from {url}...")
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode('utf-8')
                count = 0
                for line in content.splitlines():
                    domain = clean_domain(line)
                    if domain:
                        unique_domains.add(domain)
                        count += 1
                print(f"  Loaded {count} domains.")
        except Exception as e:
            print(f"  Error fetching {name}: {e}")

    output_path = "domains.txt"
    with open(output_path, "w") as f:
        for domain in sorted(unique_domains):
            f.write(f"{domain}\n")
            
    print(f"Total unique domains: {len(unique_domains)}")

if __name__ == "__main__":
    main()
