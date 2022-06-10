#!/usr/bin/env python
# coding: utf-8

# # 10.3.3 Scrape Mars Data: The News

# In[18]:


# import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[19]:


# Set executable Path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[20]:


# Visit the mars NASA news site 
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page 
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[21]:


# Set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[22]:


# Begin scraping 
slide_elem.find('div', class_='content_title')


# In[23]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[24]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # 10.3.4 Scrape Mars Data: Featrued Image

# In[25]:


url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[26]:


# Find and click the full image button 
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[28]:


# Find the relative image url 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[29]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # 10.3.5: Scrape Mars Data: Facts

# In[30]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[31]:


df.to_html()


# In[32]:


# Quitting the browser
#browser.quit()


# # Mission to Mars Challenge

# In[33]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[34]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[35]:


slide_elem.find('div', class_='content_title')


# In[36]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[37]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[38]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[39]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[40]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[41]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[42]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[43]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[44]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[45]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[46]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


# In[47]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    elem = browser.find_link_by_text('Sample').first
    img_url = elem['href']
    title = browser.find_by_css('h2.title').text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[49]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[50]:


# 5. Quit the browser
browser.quit()


# In[ ]:




