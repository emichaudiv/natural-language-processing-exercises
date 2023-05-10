#!/usr/bin/env python
# coding: utf-8

# In[70]:


from bs4 import BeautifulSoup
headers = {'User-Agent': 'Codeup Data Science'} 
import requests
from requests import get
import os
import re


# In[23]:


url = 'https://codeup.com/blog/'


# In[27]:


headers = {'User-Agent': 'Codeup Data Science'} 
response = requests.get(url,headers=headers)
response


# In[88]:


soup = BeautifulSoup(response.content,'html.parser')


# In[79]:


soup.find_all('a',class_='more-link')[0]['href']


# In[81]:


links = [link['href']for link in soup.select('.more-link')]
links


# In[55]:


article = soup.find_all("div", class_="post-content")


# In[58]:


article


# In[63]:


for element in article:
    print(element.text)


# In[99]:


inshorts='https://inshorts.com/en/read'


# In[100]:


headers = {'User-Agent': 'Codeup Data Science'} 
responses = requests.get(inshorts,headers=headers)
responses


# In[101]:


soup = BeautifulSoup(response.content,'html.parser')


# In[102]:


soup.find_all("span", itemprop="headline")


# In[103]:


soup.find_all("div", itemprop="articleBody")


# In[104]:


soup.select('li')


# In[105]:


[li.text.lower()for li in soup.select('li')]


# In[106]:


catagories = [li.text.lower()for li in soup.select('li')]
catagories [0] = 'national'
catagories


# In[114]:


catagories = [li.text.lower()for li in soup.select('li')]
catagories [0] = 'national'
inshort = []
for catagory in catagories:
    url = 'https://inshorts.com/en/read' +'/' +catagory
    response = get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    titles = [span.text for span in soup.find_all("span", itemprop="headline")]
    content = [div.text for div in soup.find_all("div", itemprop="articleBody")]
    for i in range(len(titles)):
        article = {
            'title': titles[i],
            'content': content[i],
            'category': catagory
        }
        inshort.append(article)


# In[119]:


inshort


# In[ ]:




