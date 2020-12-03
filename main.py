#!/usr/bin/env python3

import json
import time
import requests
import bot
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

def update_data():
    with open('data.json', "w") as outfile:
        data = {}
        data['active_jobs'] = get_listings()
        json.dump(data, outfile, indent=2) 

# Updates data.json when bot is started, so it doesn't spam if if has been off for a while
update_data()

print("Bot is running...")

while True:
    data_file = open('data.json')

    old_listings = json.load(data_file)['active_jobs']
    new_listings = get_listings()

    if (old_listings != new_listings):
        new_jobs = [item for item in new_listings if item not in old_listings]
        for job in new_jobs:

            job_title = job['job_title']
            company = job['company']
            link_to_job = job['link_to_job']

            message = f"Hello there, *{company}* is searching for *{job_title}*. Read more from here... \n\n{link_to_job}"
            bot.send_message(message)
        
        # After sending messages, update data.json
        update_data()

    time.sleep(10)
