from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import bs4
import pandas as pd
import requests
from pprint import pprint
import urllib3
import time

def init_browser():
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def mars_news():
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    article= soup.select_one("ul.item_list li.slide")
    article.find('div', class_='content_title')
    title = article.find('div', class_='content_title').get_text()
    teaser = article.find('div', class_='article_teaser_body').get_text()
    return mars_news

def init_browser():
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path)

def mars_image():
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs4.BeautifulSoup(html, 'html.parser')
    new_image= soup.select_one("ul.articles li.slide")
    new_image.find('a', class_='fancybox')
    feature_img_url = f"https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA24073_hires.jpg"
#print(feature_img_url)
    return mars_image

def init_browser():
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path)

def mars_facts():
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(3)
    mars_earth_facts_df=pd.read_html(url)[1]
#fact_table[1]
    mars_earth_facts_df.columns=["Mars/Earth Comparison Description", "Mars Values", "Earth Values"]
    mars_earth_facts_df
    mars_earth_facts_html="mars_facts.html"
    mars_earth_facts_df.to_html(mars_earth_facts_html)
    return mars_facts

def init_browser():
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path)

def mars_hemisphere_img():
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(3)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    images_to_find = soup.find_all('div', class_='item')
    mars_hemisphere_image_urls = []
    head_url = 'https://astrogeology.usgs.gov'
#loop for images @ stack overflow and my mastering python/pandas book
    for itf in images_to_find:
        title = itf.find('h3').text
        mars_partial_img_url = itf.find('a', class_='itemLink product-item')['href']
        browser.visit(head_url + mars_partial_img_url)
        mars_partial_img_html = browser.html
        soup = BeautifulSoup(mars_partial_img_html, 'html.parser')
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        mars_hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        #mars_hemisphere_image_urls
    return mars_hemisphere_img
