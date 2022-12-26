import requests

class Search_subdomain:
    def __init__(self, subdoamins_file):
        self.open = open(subdoamins_file, 'r').read().splitlines()
    
    def search(self, domain):
        subdomains = self.open

        for subdomain in subdomains:
            
            url = f"http://{subdomain}.{domain}"

            try:
                requests.get(url, timeout=1, headers={'User-Agent': 'some cool user-agent'})
            except requests.ConnectionError:
                pass
            else:
                print(url)

        print("it's all")

search_domains = Search_subdomain('subdomains-100.txt')

while True:
    domain = input('Введите домен: ')
    search_domains.search(domain)