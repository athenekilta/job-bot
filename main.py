import json
import time
import requests
from bs4 import BeautifulSoup

page = requests.get("https://athene.fi/jobs/")

soup = BeautifulSoup(page.content, 'html.parser')

def get_listings():
    listings = []
    job_listings = soup.find('ul', {'class': 'job_listings'})

    for job_listing in job_listings.find_all('li', {'class': 'job_listing'}):

        listing_data = {
            'job_title': job_listing.find('h3').text,
            'company': job_listing.find('div', {'class': 'company'}).strong.text,
            'link_to_job': job_listing.find('a')['href']
        }

        listings.append(listing_data)

    return listings

data = {}
data["active_jobs"] = get_listings()

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)

