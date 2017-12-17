#! /usr/bin/env python3
#This program takes an argument, the Amazon url to scrape for price
#It will return the price of the item on that page
import bs4, requests, sys

url = 'https://www.amazon.com/Timex-Unisex-TWG012800-Weekender-Leather/dp/B01GI8SU5O/'
PRICE_ELEMENT_NAME = '#priceblock_ourprice'

#If a url is passed, use it, otherwise use demo url
if len(sys.argv) > 1:
    url = sys.argv[1]

#Get the product price on the provided url
def getAmazonPrice(productUrl):
    res = requests.get(url)
    res.raise_for_status()

    #parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(PRICE_ELEMENT_NAME)

    return elems[0].text

price = getAmazonPrice(url)
print('The price is ' + price)
