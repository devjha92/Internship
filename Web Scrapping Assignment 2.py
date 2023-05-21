#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[79]:


import selenium 
import pandas as pd
from selenium import webdriver 
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. This task will be done in following steps:
# 
# First get the webpage https://www.naukri.com/
# Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# Then click the searchbutton.
# Then scrape the data for the first 10 jobs results you get.
# Finally create a dataframe of the scraped data.

# In[84]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[85]:


driver.get('https://www.naukri.com/')


# In[86]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[87]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[88]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[89]:


job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[:10]:
    title=i.text
    job_title.append(title)


# In[90]:


job_location=[]
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[:10]:
    location=i.text
    job_location.append(location)


# In[92]:


company=[]
company_name=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_name[:10]:
    companies=i.text
    company.append(companies)


# In[95]:


experience_required=[]
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[:10]:
    Experience=i.text
    experience_required.append(exp)


# In[65]:


print(len(job_title), len(job_title), len(company),len(experience_required))


# In[96]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company,'Experience':experience_required})
df


# Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the 
# location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results youget.
# 5. Finally create a dataframe of the scraped data.

# In[115]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[116]:


driver.get('https://www.naukri.com/')


# In[117]:


position=driver.find_element(By.CLASS_NAME,"suggestor-input ")
position.send_keys('Data Scientist')


# In[118]:


Location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Bangalore')


# In[119]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[120]:


job_position=[]
titles=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in titles[:10]:
    job=i.text
    job_position.append(job)


# In[121]:


job_location=[]
Locations=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in Locations[:10]:
    job_1=i.text
    job_location.append(job_1)


# In[123]:


company_job=[]
Company=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in Company[:10]:
    company_1=i.text
    company_job.append(company_1)


# In[124]:


df=pd.DataFrame({'Position':job_position, 'Location':job_location, 'Company':company_job})
df


# Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# ASSIGNMENT 2
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results. 
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get thewebpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.Search
# 3. Then click the searchbutton.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results youget.
# 6. Finally create a dataframe of the scraped data

# In[ ]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[126]:


driver.get(' https://www.naukri.com/')


# In[128]:


Job=driver.find_element(By.CLASS_NAME,"suggestor-input")
Job.send_keys('Data Scientist')


# In[129]:


Search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
Search.click()


# In[141]:


job_ds=[]
jobs=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in jobs[:10]:
    job_ds.append(i.text)


# In[155]:


job_location=[]
job_loc=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in job_loc[:10]:
    job_location.append(i.text) 


# In[138]:


Company_N=[]
company_name=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_name[:10]:
        Company_N.append(i.text)


# In[136]:


exp=[]
Experience=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in Experience[:10]:
    exp.append(i.text)


# In[154]:


df=pd.DataFrame({'Job Title':job_ds, 'Location':job_location, 'Company_Name':Company_N, 'Experience':exp })
df


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. ProductDescription
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and 
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the 
# required data asusual.
# 

# In[3]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[4]:


driver.get('https://www.flipkart.com/')


# In[10]:


glass=driver.find_element(By.CLASS_NAME,"_3704LK")
glass.send_keys('sunglasses')


# In[12]:


search=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
search.click()


# In[30]:


Brand=[]
start=0
end=3
for page in range(start,end):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand[:100]:
        Brand.append(i.text) 
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)
                          


# In[31]:


print(len(Brand))


# In[42]:


PD=[]
start=0
end=3
for i in range(start,end):
    Product=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in Product[:100]:
        PD.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[33]:


print(len(PD))


# In[44]:


Price=[]
start=0
end=3
for i in range(start,end):
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price[:100]:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[37]:


print(len(Price))


# In[36]:


Discount=[]
start=0
end=3
for i in range(start,end):
    discount=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in discount[:100]:
        Discount.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[38]:


print(len(Discount))


# In[45]:


df=pd.DataFrame({'Brand':Brand[:100], 'PD':PD[:100], 'Price':Price[:100], 'Discount':Discount[:100]})
df


# Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[3]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[4]:


driver.get('https://www.flipkart.com/')


# In[7]:


product=driver.find_element(By.CLASS_NAME,'_3704LK')
product.send_keys('sneakers')


# In[10]:


Search=driver.find_element(By.CLASS_NAME,'_34RNph')
Search.click()


# In[35]:


brand=[]
start=0
end=3
for page in range(start,end):
    Brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand:
        brand.append(i.text) 
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)
                     


# In[36]:


print(len(brand))


# In[37]:


p_description=[]
start=0
end=3
for page in range(start,end):
    product_d=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_d:
        p_description.append(i.text) 
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)


# In[38]:


print(len(p_description))


# In[51]:


Price_list=[]
start=0
end=3
for i in range(start,end):
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price[:100]:
        Price_list.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(4)


# In[52]:


print(len(Price_list))


# In[53]:


import pandas as pd
df=pd.DataFrame({'Brand':brand[:100],'Product Description':p_description[:100], 'Price':Price_list[:100]})
df


# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
# set CPU Type filter to “Intel Core i7” as shown in the below image
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price
# 

# In[77]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[78]:


driver.get('https://www.amazon.in')


# In[79]:


find=driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
find.send_keys('Laptop')


# In[80]:


Search=driver.find_element(By.XPATH,'//div[@class="nav-right"]')
Search.click()


# In[81]:


Filter=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[12]/li/span/a/span')
Filter.click()


# In[20]:


Title=[]
title=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title[:10]:
    Title.append(i.text)


# In[21]:


print(len(Title))


# In[86]:


Rating=[]
rating=driver.find_elements(By.XPATH,'//div[@class="a-row a-size-small"]')
for i in rating[:10]:
    Rating.append(i.text)


# In[87]:


print(len(Rating))


# In[25]:


price=[]
Price=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in Price[:10]:
    price.append(i.text)


# In[26]:


print(len(price))


# In[38]:


df=pd.DataFrame({'Title':Title, 'Rating':Rating, 'Price':price})
df


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the web pagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[84]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")
driver


# In[85]:


driver.get('https://www.azquotes.com')


# In[86]:


title=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
title.click()


# In[90]:


print(len(Quote))


# In[89]:


Quote=[]
start=0
end=10
for page in range(start,end):
    quote=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote:
        Quote.append(i.text)
   


# In[91]:


AU=[]
start=0
end=10
for page in range(start,end):
    au=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in au:
            AU.append(i.text)
    


# In[92]:


print(len(AU))


# In[96]:


Type_of_Quote=[]
start=0
end=10
for page in range(start,end):
    toq=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in toq:
        Type_of_Quote.append(i.text)
    


# In[97]:


print(len(Type_of_Quote))


# In[98]:


df=pd.DataFrame({'Author':AU, 'Quote':Quote, 'Type of Quote':Type_of_Quote})
df


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# 

# In[2]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")


# In[16]:


driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[29]:


Rating=[]
start=0
end=10
for page in range(start,end):
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating[:100]:
        Rating.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)


# In[22]:


print(len(Rating))


# In[24]:


Summary=[]
start=0
end=10
for page in range(start,end):
    summary=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in summary[:100]:
        Summary.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)


# In[25]:


print(len(Summary))


# In[26]:


Full_review=[]
start=0
end=10
for page in range(start,end):
    review=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in review[:100]:
        Full_review.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(4)


# In[27]:


print(len(Full_review))


# In[30]:


df=pd.DataFrame({'Rating':Rating, 'Summary':Summary, 'Full_review':Full_review})
df


# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.
# 

# In[99]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")


# In[100]:


driver.get('https://www.jagranjosh.com/')


# In[101]:


Gk=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[3]/ul/li[3]/a')
Gk.click()


# In[102]:


list=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')
list.click()


# In[109]:


PM=[]
names = driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[2]/p')

for name in names:

    PM.append(name.text)
PM


# In[106]:


Born_Dead=[]
names = driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[3]/p')

for name in names:

    Born_Dead.append(name.text)
Born_Dead


# In[111]:


Term_of_office=[]
names = driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[4]')

for name in names:

    Term_of_office.append(name.text)
Term_of_office


# In[108]:


Remarks=[]
names = driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[5]/p')

for name in names:

    Remarks.append(name.text)
Remarks


# In[112]:


print(len(PM))
print(len(Born_Dead))
print(len(Term_of_office))
print(len(Remarks))


# In[113]:


df=pd.DataFrame({'Priminster Name':PM, 'Born_dead':Born_Dead,  'Term of Office':Term_of_office, 'Remarks':Remarks})
df


# Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpagehttps://www.motor1.com/
# 2. Then You have to click on the List option from Dropdown menu on leftside.
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe    

# In[3]:


driver=webdriver.Chrome(r"C:\Users\admin\Downloads\chromedriver_win32.exe")


# In[112]:


driver.get('https://www.motor1.com/')


# In[113]:


list=driver.find_element(By.CLASS_NAME,'m1-hamburger-button')
list.click()


# In[117]:


dropdown=driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[3]/ul/li[7]/a')
dropdown.click()


# In[123]:


Expensive=[]
EXP=driver.find_elements(By.XPATH,'//div[@class="make-item"]')
for i in EXP[:50]:
     Expensive.append(i.text)


# In[124]:


print(len(Expensive))


# In[125]:


df=pd.DataFrame({'CARS':Expensive})
df


# In[ ]:




