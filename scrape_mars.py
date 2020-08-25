from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    #from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': "chromedriver.exe"}
    return Browser('chrome', **executable_path, headless=False)

def mars():
    browser = init_browser()
#def mars_news():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    time.sleep(5)
    
    html = browser.html
    news_soup = bs(html, 'html.parser')
    
    #article= soup.select_one("ul.item_list li.slide")
    #article.find('div', class_='content_title')
    title = news_soup.find('div', class_='content_title').text()
    teaser = news_soup.find('div', class_='article_teaser_body').text()
    teaser_title = {
        "title": title, 
        "teaser": teaser
        }
    return teaser_title

def mars_image():
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser = init_browser()
    browser.visit(url)
    
    time.sleep(5)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    new_image= soup.select_one("ul.articles li.slide")
    new_image.find('a', class_='fancybox')
    feature_img_url = f"https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA24073_hires.jpg"
#print(feature_img_url)
    return feature_img_url

def mars_facts():
    url = "https://space-facts.com/mars/"
    browser = init_browser()
    browser.visit(url)
    
    time.sleep(5)
    
    mars_earth_facts_df=pd.read_html(url)[1]
#fact_table[1]
    mars_earth_facts_df.columns=["Mars/Earth Comparison Description", "Mars Values", "Earth Values"]
    mars_earth_facts_html="mars_facts.html"
    mars_earth_facts_df.to_html(mars_earth_facts_html)
    return mars_earth_facts_html

def mars_hemisphere_img():
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = init_browser()
    browser.visit(url)
    
    time.sleep(5)
    
    html=browser.html
    soup = bs(html, 'html.parser')
    images_to_find = soup.find_all('div', class_='item')
    mars_hemisphere_image_urls = []
    head_url = 'https://astrogeology.usgs.gov'
#loop for images @ stack overflow and my mastering python/pandas book
    for itf in images_to_find:
        title = itf.find('h3').text
        mars_partial_img_url = itf.find('a', class_='itemLink product-item')['href']
        browser.visit(head_url + mars_partial_img_url)
        mars_partial_img_html = browser.html
        soup = bs(mars_partial_img_html, 'html.parser')
        img_url = head_url + soup.find('img', class_='wide-image')['src']
        mars_hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        #mars_hemisphere_image_urls
    return mars_hemisphere_image_urls


#def scrape_info():
#    mars_data = {
 #       "teaser_title": teaser_title, 
 #       "sfeature_img_url": feature_img_url,
 #       "mars_earth_facts_df": mars_earth_facts_html,
 #       "mars_hemisphere_image_urls": mars_hemisphere_image_urls
 #   }

    # Close the browser after scraping
    #browser.quit()

    #Return results
 #   return mars

   