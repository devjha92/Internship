#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a python program to display all the header tags from wikipedia.org and make data frame.


# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


import pandas as pd


# In[9]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[81]:


page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[82]:


soup=BeautifulSoup(page.content)
soup


# In[96]:


from urllib.request import urlopen
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print('ALL HEADER TAGS ::', *titles, sep='\n')

     


# In[98]:


df=pd.DataFrame({'Header Tags':titles})
df


# In[ ]:


# Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release) 
and make data frame


# In[15]:


page=requests.get("https://www.imdb.com/list/ls055386972/")
page


# In[16]:


soup=BeautifulSoup(page.content)
soup


# In[17]:


movie_names = [i.text.split('\n')[2] 
     for i in soup.find_all(class_="lister-item-header")]
movie_names


# In[22]:


rating=[i.text.strip() 
    for i in soup.find_all(class_="ipl-rating-star small")]
rating


# In[27]:


release_year = []
for i in soup.find_all(class_="lister-item-year text-muted unbold"):
    release_year.append(i.text)
release_year  


# In[28]:



df=pd.DataFrame({'Movies':movie_names,'Ratings':rating,'Release_Year':release_year})

df


# In[ ]:


# Write a python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of 
release) and make data frame.


# In[46]:


page=requests.get("https://www.imdb.com/list/ls023325613/")
page


# In[47]:


soup= BeautifulSoup(page.content)
soup


# In[62]:


movies_names=[i.text.split('\n')[2] 
   for i in soup.find_all(class_="lister-item-header")]
movies_names


# In[60]:


rating_movies=[i.text.strip() 
    for i in soup.find_all(class_="ipl-rating-star small")]
rating_movies


# In[59]:


movies_release_year = []
for i in soup.find_all(class_="lister-item-year text-muted unbold"):
    movies_release_year.append(i.text)
movies_release_year  


# In[63]:


df=pd.DataFrame({'Movies':movies_names,'Ratings':rating_movies,'Release_Year':movies_release_year})

df


# In[ ]:


#Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) 
#from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[6]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[7]:


soup=BeautifulSoup(page.content)
soup


# In[20]:


Name=soup.find('div',class_='presidentListing')
Name


# In[24]:


Name.text.split('\n')[1]


# In[29]:


Term=soup.find('div',class_='presidentListing')
Term
Term.text.split('\n')[2]


# In[43]:


title = []
for i in soup.find_all('div',class_='presidentListing'):
    title.append(i.text.split('\n')[1])
title


# In[45]:


term = []
for i in soup.find_all('div',class_='presidentListing'):
    term.append(i.text.split('\n') [2])
term


# In[46]:


df=pd.DataFrame({'Names':title,'Term':term})
df


# In[ ]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


# In[6]:


#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[7]:


soup=BeautifulSoup(page.content)
soup


# In[13]:


Title=[]
for i in soup.find_all('td',class_='table-body__cell u-center-text'):
     Title.append(i.text.replace('\n',''))
Title


# In[42]:


Titles_1=Title[0::2]
Titles_1


# In[44]:


Titles_Final=Titles_1[0:10]
Titles_Final


# In[37]:


Position=Title[1::2]
Position


# In[39]:


Positions=Position[0:10]
Positions


# In[124]:


Match=soup.find('td',class_='table-body__cell u-center-text')
Match
Match.text.split('|')


# In[90]:


Point=soup.find('td',class_="rankings-block__banner--points")
Point
Point.text


# In[92]:


point=[]
for i in soup.find_all('td',class_="rankings-block__banner--points"):
      point.append(i.text)
point


# In[107]:


Rating= soup.find('td',class_='table-body__cell u-text-right rating')
Rating


# In[46]:


rating=[]
for i in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
rating


# In[47]:


Rating=rating[0:10]
Rating


# In[20]:


Country=soup.find('span',class_='u-hide-phablet')
Country


# In[19]:


country=[]
for i in soup.find_all('span',class_='u-hide-phablet'):
      country.append(i.text)
country


# In[27]:


countrys=country[0:10]
countrys


# In[49]:


print(len(Titles_Final),len(Positions),len(Rating),len(countrys))


# In[53]:


df=pd.DataFrame({'Teams':countrys,'Rating':Rating,'Points':Positions,'Matches':Titles_Final})
df


# In[ ]:


#Top 10 ODI Batsmen along with the records of their team and rating.


# In[54]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[188]:


soup=BeautifulSoup(page.content)
soup


# In[211]:


batsman=soup.find('div',class_='rankings-block__banner--name-large')
batsman.text


# In[223]:


Players=[]
for i in soup.find_all('div',class_='rankings-block__banner--name-large'):
    Players.append(i.text)
Players

for i in soup.find_all('td', class_='table-body__cell rankings-table__name name'):
      for j in i.find_all('a'):
        Players.append(j.text)  
        
Players=Players[:10]
Players


# In[224]:



Team_Name=soup.find('div',class_='rankings-block__banner--nationality')
Team_Name


# In[231]:


Team_Name=[]

for i in soup.find_all('div',class_='rankings-block__banner--nationality'):
    Team_Name.append(i.text.replace("\n",""))
    
for j in soup.find_all('span', class_='table-body__logo-text'):
    Team_Name.append(j.text)
Team_Name


Team_Name=Team_Name[:10]
Team_Name


# In[238]:


Rating=[]
for i in soup.find_all('div',class_='rankings-block__banner--rating'):
    Rating.append(i.text)
Rating
for j in soup.find_all('td',class_='table-body__cell rating'):
    Rating.append(j.text)
Rating=Rating[:10]
Rating


# In[264]:


Records=[]
for i in  soup.find_all('span',class_='rankings-block__career-best-text'):
    Records.append(i.text.split())
Records
    
for j in soup.find_all('td',class_='table-body__cell u-text-right u-hide-phablet'):
    Records.append(j.text.split())
Records=Records[:10]
Records


# In[265]:


df=pd.DataFrame({'Batsman':Players, 'Team':Team_Name, 'Rating': Rating, 'Records':Records })
df


# In[ ]:


# c) Top 10 ODI bowlers along with the records of their team andrating


# In[6]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page


# In[13]:


soup=BeautifulSoup(page.content)
soup


# In[14]:


Player=[]
for i in soup.find_all('div', class_='rankings-block__banner--name-large'):
    Player.append(i.text)
Player
for j in soup.find_all('td', class_='table-body__cell rankings-table__name name'):
        Player.append(j.text.split())
Player=Player[0:10]
Player


# In[15]:


Team_Name=[]

for i in soup.find_all('div',class_='rankings-block__banner--nationality'):
    Team_Name.append(i.text.replace("\n",""))
    
for j in soup.find_all('span', class_='table-body__logo-text'):
    Team_Name.append(j.text)
Team_Name


Team_Name_1=Team_Name[:10]
Team_Name_1


# In[16]:


Rating=[]
for i in soup.find_all('div',class_='rankings-block__banner--rating'):
    Rating.append(i.text)
Rating
for j in soup.find_all('td',class_='table-body__cell rating'):
    Rating.append(j.text)
Rating=Rating[0:10]
Rating


# In[17]:


Records=[]
for i in  soup.find_all('span',class_='rankings-block__career-best-text'):
    Records.append(i.text.split())
Records
    
for j in soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet"):
    Records.append(j.text.split())
Records=Records[0:10]
Records


# In[18]:


df=pd.DataFrame({'Players':Player, 'Team':Team_Name_1, 'Rating': Rating, 'Record':Records})
df


# In[ ]:


#) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.


# In[19]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[20]:


soup=BeautifulSoup(page.content)
soup


# In[21]:


Team_Name=[]
for i in soup.find_all('span', class_="u-hide-phablet"):
    Team_Name.append(i.text)
Team_Name
for j in soup.find_all('span',class_="u-hide-phablet"):
        Team_Name.append(j.text.split())
Team_Name_1=Team_Name[0:10]
Team_Name_1


# In[23]:


Rating=[]
for i in soup.find_all('td',class_='rankings-block__banner--rating u-text-right'):
    Rating.append(i.text.split())
Rating
for j in soup.find_all('td',class_='table-body__cell u-text-right rating'):
    Rating.append(j.text)
Rating=Rating[0:10]
Rating


# In[24]:


Points=[]

for j in soup.find_all('td',class_='table-body__cell u-center-text'):
        Points.append(j.text)
Points


# In[25]:


Points=Points[0::2]
Points


# In[26]:


Points=Points[0:10]
Points


# In[27]:


Matches=[]

for j in soup.find_all('td',class_='table-body__cell u-center-text'):
        Matches.append(j.text)
Matches

Matches=Matches[1::2]
Matches
Matches=Matches[0:10]
Matches


# In[28]:



df=pd.DataFrame({'Team':Team_Name_1,'Rating':Rating,'Point':Points,'Match':Matches})
df


# In[ ]:


#b) Top 10 women’s ODI Batting players along with the records of their team and rating.


# In[31]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page


# In[32]:


soup=BeautifulSoup(page.content)
soup


# In[33]:


batting=soup.find('div',class_="rankings-block__banner--name-large")
batting.text


# In[34]:


Players=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    Players.append(i.text)

for j in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    Players.append(j.text.split())
    
Players
Players=Players[0::10]
Players


# In[35]:


Team_Name=[]

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    Team_Name.append(i.text.replace("\n",""))
    
for j in soup.find_all('span', class_="table-body__logo-text"):
    Team_Name.append(j.text)
Team_Name


Team_Name=Team_Name[:10]
Team_Name


# In[36]:


Rating=[]
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    Rating.append(i.text)
Rating
for j in soup.find_all('td',class_="table-body__cell rating"):
    Rating.append(j.text)
Rating=Rating[:10]
Rating


# In[37]:


Records=[]
for i in  soup.find_all('span',class_="rankings-block__career-best-text"):
    Records.append(i.text.split())
Records
    
for j in soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet"):
    Records.append(j.text.split())
Records=Records[:10]
Records


# In[38]:


df=pd.DataFrame({'Player':Players,'Team':Team_Name,'Rating':Rating, 'Record':Records})
df


# In[ ]:


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[65]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[66]:


soup=BeautifulSoup(page.content)
soup


# In[71]:


Player_Name=[]
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    Player_Name.append(i.text)
    
for j in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    Player_Name.append(j.text.split())

    
Player_Name
Player_Name=Player_Name[:10]
Player_Name


# In[73]:


Team_Name=[]

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    Team_Name.append(i.text.replace("\n",""))
    
for j in soup.find_all('span', class_="table-body__logo-text"):
    Team_Name.append(j.text)
Team_Name
Team_Name=Team_Name[:10]
Team_Name


# In[74]:


Rating=[]
for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    Rating.append(i.text)

for j in soup.find_all('td',class_="table-body__cell rating"):
    Rating.append(j.text)
Rating=Rating[:10]
Rating


# In[79]:


Records=[]
for i in  soup.find_all('span',class_="rankings-block__career-best-text"):
    Records.append(i.text.split())

for j in soup.find_all('td',class_="table-body__cell u-text-right u-hide-phablet"):
    Records.append(j.text.split())
Records=Records[:10]
Records


# In[80]:


df=pd.DataFrame({'Player':Player_Name, 'Teams':Team_Name, 'Ratings':Rating, 'Records':Records})
df


# In[ ]:


#7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and 
make data framei) Headline
ii) Time
iii) News Link


# In[39]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[40]:


soup=BeautifulSoup(page.content, 'html.parser')
soup


# In[41]:


Headline=soup.find('a',class_="LatestNews-headline")
Headline.text


# In[42]:


Headline=[]

for i in soup.find_all('a',class_="LatestNews-headline"):
        Headline.append(i.text)
Headline
Head_line=Headline[0:10]
Head_line


# In[43]:


Time=soup.find('span',class_="LatestNews-wrapper")
Time.text


# In[44]:


Time=[]
for i in soup.find_all('span',class_="LatestNews-wrapper"):
    Time.append(i.text)
Time
Time=Time[:10]
Time
        


# In[45]:


News_Link=[]
for i in soup.find_all('a', class_='LatestNews-headline'):
    News_Link.append(i['href'])
News_Link=News_Link[:10]
News_Link


# In[46]:


df=pd.DataFrame({'HeadLine':Head_line, 'Times':Time, 'Newslink':News_Link })
df


# In[ ]:


Write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data framei) Paper Title
ii) Authors
iii) Published Date
iv) Paper URL


# In[47]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[48]:


soup=BeautifulSoup(page.content)
soup


# In[49]:


paper_title=soup.find('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
paper_title.text


# In[50]:


paper_title=[]
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
paper_title


# In[51]:


Author=[]
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Author.append(i.text)
Author


# In[52]:


Date=[]
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    Date.append(i.text)
Date


# In[53]:


URL=[]
for i in soup.find_all('a', class_="sc-5smygv-0 fIXTHm"):
     URL.append(i['href'])
URL


# In[54]:


df=pd.DataFrame({'Paper_Title':paper_title, 'Author':Author, 'Date':Date, 'URL':URL})
df


# In[ ]:


#Write a python program to scrape mentioned details from dineout.co.in and make data framei) Restaurant name
ii) Cuisine
iii) Location
iv) Ratings
v) Image URL


# In[56]:


page=requests.get('https://www.dineout.co.in/pune-restaurants/welcome-back')
page


# In[57]:


soup=BeautifulSoup(page.content)
soup


# In[58]:


Restaurant_Name=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    Restaurant_Name.append(i.text)
Restaurant_Name=Restaurant_Name[:10]
Restaurant_Name


# In[59]:


Cuisine=[]
for i in soup.find_all('div',class_="detail-info"):
    Cuisine.append(i.text.split('|')[1])
Cuisine=Cuisine[:10]
Cuisine


# In[60]:


Location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    Location.append(i.text)
Location=Location[:10]
Location


# In[61]:


Image_URL=[]
for i in soup.find_all('img',class_="no-img"):
    Image_URL.append(i.get('data-src'))
Image_URL=Image_URL[:10]
Image_URL


# In[62]:


df=pd.DataFrame({'Restaurant_Name':Restaurant_Name, 'Cuisine':Cuisine, 'Location':Location, 'Image_URL':Image_URL,})
df


# In[ ]:




