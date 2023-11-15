import requests
from bs4 import BeautifulSoup

def get_web_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

def scrape_and_rewrite(url):
    html_content = get_web_page(url)

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        # links = soup.find_all('a')  # Adjust based on the HTML structure of the website
        links = soup.find_all('a', href=lambda href: href and href.startswith('https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d='))

        for link in links:
            print (link.text)

            # print (link.text)

# Replace 'YOUR_URL' with the URL of the website you want to scrape
url = 'https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat'

scrape_and_rewrite(url)
