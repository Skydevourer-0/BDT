import requests
#import json
from bs4 import BeautifulSoup

url='http://www.cnad.com/guanggaoyu/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
response=requests.get(url,headers=headers)


strhtml=requests.get(url)
strml=strhtml.text.encode('iso-8859-1').decode('gbk')
soup=BeautifulSoup(strml,'lxml')
data=soup.select('#news_content > p')
data.decode('utf-8','strict')
        

for item in data:
   result={
           'content':item.string,
           'link':item.get('href')
   }
   print(result)
