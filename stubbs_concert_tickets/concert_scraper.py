#! /usr/bin/env python3
# This program searches the stubbs website for concerts
# json reference: https://stackoverflow.com/questions/1389738/how-to-save-data-with-python#1389792
import bs4, requests, pprint, re

URL = 'https://www.stubbsaustin.com/concert-listings'
SHOW_DETAILS_CLASS_NAME = 'frontgateFeedSummary'
CONCERT_TITLE_CLASS_NAME = 'contentTitle'

#Get the shows on the website
def getConcerts():
    titles = []
    res = requests.get(URL)
    res.raise_for_status()

    #parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #find all of the concert container elements
    concert_containers = soup.find_all(class_=SHOW_DETAILS_CLASS_NAME)

    #loop through all of the show containers and grab the titles
    for concert in concert_containers:
        titles.append(concert.find(class_=CONCERT_TITLE_CLASS_NAME).text)

    return titles

concerts = getConcerts()
pprint.pprint(concerts)
