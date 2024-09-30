from bs4 import BeautifulSoup
import requests

def scrape_apt_activity():
    url = 'https://example-threat-intel-site.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse the website content to find APT-related activity
    activities = []
    for item in soup.find_all('div', class_='apt-entry'):
        activity = {
            'title': item.find('h2').text,
            'description': item.find('p').text,
            'link': item.find('a')['href']
        }
        activities.append(activity)

    return activities
