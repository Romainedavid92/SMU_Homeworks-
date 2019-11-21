#Imports
from bs4 import BeautifulSoup
from splinter import Browser
import re
import pandas as pd 

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=True)


def scrape():
    browser = init_browser()

    # Create a dictionary for all of the scraped data
    mars_data = {}

    # Visit the Mars news page. 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
 

    # Search for news
    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find the latest Mars news.
    newsTitle = soup.find("div", {"class" : "content_title"})
    titleLink = newsTitle.find("a")
    newsTitleText = titleLink.text
    link = titleLink["href"]
    frontBit = "https://mars.nasa.gov"
    fullLink_news = frontBit + link
  
    # Add title to the dictionary
    
    mars_data["newsTitleText"] = newsTitleText
    


    # ## JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Scrape the browser into soup and use soup to find the full resolution image of mars
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    featImage = soup.find("article", {"class": "carousel_item"})
    link = featImage["style"].split("(")[1].replace(");", "").replace("'", "")
    frontBit = "https://www.jpl.nasa.gov"
    fullLink_featImage = frontBit + link
    
    # Add the featured image url to the dictionary
    mars_data["fullLink_featImage"] = fullLink_featImage


    # ## Mars Weather 
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    tweet = soup.find('p', {"class": "tweet-text"})
    weather = tweet.text
    
    # Add the weather to the dictionary
    mars_data["weather"] = weather

    # Visit the USGS Astogeology site and scrape pictures of the hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.find_by_css("a.itemLink h3")[0].click()
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    imageTitle = soup.find("h2", {"class" : "title"}).text
    imageLink_panda = soup.find("img", {"class": "wide-image"})["src"]
    frontBit = "https://astrogeology.usgs.gov"
    imageLink_panda1 = frontBit + imageLink_panda
    
    hemi_data = []

    for i in range(4):
        hemi_dict = {}
    
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        browser.find_by_css("a.itemLink h3")[i].click()
    
    #Soupify
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')
    
        imageTitle = soup.find("h2", {"class" : "title"}).text
        imageLink_panda = soup.find("img", {"class": "wide-image"})["src"]
    
        frontBit = "https://astrogeology.usgs.gov"
        imageLink_panda1 = frontBit + imageLink_panda
    
        hemi_dict["title"] = imageTitle
        hemi_dict["link"] = imageLink_panda1
    
        hemi_data.append(hemi_dict)
    mars_data['hemi_data'] = hemi_data

    # Mars Fact
    list_dfs = pd.read_html("https://space-facts.com/mars/")
    marsFacts = list_dfs[0]
    marsFacts.columns = ["Name", "Measure"]

    marsFactsHTML = marsFacts.to_html()
    marsFactsHTML = marsFactsHTML.replace('\n', ' ')
    # Add the Mars facts table to the dictionary
    mars_data["mars_table"] = marsFactsHTML

    # Return the dictionary
    return mars_data