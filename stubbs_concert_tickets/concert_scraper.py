#! /usr/bin/env python3
# This program searches the stubbs website for concerts
# json reference: https://stackoverflow.com/questions/1389738/how-to-save-data-with-python#1389792
import bs4, requests, pprint, re

URL = 'https://www.stubbsaustin.com/concert-listings'
CONCERT_CONTAINER_CLASS = 'frontgateFeedSummary'
CONCERT_TITLE_CLASS = 'contentTitle'
CONCERT_WEEKDAY_CLASS = 'eventWeekday'
CONCERT_MONTH_CLASS = 'eventMonth'
CONVERT_DAY_CLASS = 'eventDay'
CONCERT_DETAILS_CLASS = 'frontgateFeedShowDetails'

#Get the shows on the website
def getConcerts():
    titles = {}
    res = requests.get(URL)
    res.raise_for_status()

    #parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #find all of the concert container elements
    concert_containers = soup.find_all(class_=CONCERT_CONTAINER_CLASS)

    #loop through all of the show containers and grab the titles
    for concert in concert_containers:
        new_concert = {}
        new_concert['title'] = concert.find(class_=CONCERT_TITLE_CLASS).text
        new_concert['weekday'] = concert.find(class_=CONCERT_WEEKDAY_CLASS).text
        new_concert['month'] = concert.find(class_=CONCERT_MONTH_CLASS).text
        new_concert['details'] = concert.find(class_=CONCERT_DETAILS_CLASS).text
        titles[new_concert['title']] = new_concert

    return titles

concerts = getConcerts()
pprint.pprint(concerts)
