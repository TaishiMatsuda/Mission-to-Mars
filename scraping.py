# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the resulting html with soup
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
# Use the parent element to find the paragraph text
slide_elem = news_soup.select_one('ul.item_list li.slide')
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
news_p

# Visit the mars image nasa search site
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()
# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# Read Profile of Mars from Mars Facts
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df.to_html()

# Close the chrome browser
browser.quit()