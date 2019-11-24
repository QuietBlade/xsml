import requests
import selenium
import time
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver

user='账号'
pwd='密码'

Webdriver=webdriver.Chrome()
Webdriver.get("http://www.cqooc.com")
Webdriver.implicitly_wait(2)
Webdriver.find_element_by_partial_link_text('登录').click()
Webdriver.find_element_by_css_selector('#loginForm > ul > li:nth-child(1) > input').send_keys(user)
Webdriver.find_element_by_css_selector('#loginForm > ul > li:nth-child(2) > input').send_keys(pwd)
time.sleep(1)
Webdriver.find_element_by_css_selector('#loginBtn').click()
time.sleep(2)
Webdriver.get("http://www.cqooc.com/learn/mooc/progress?id=334566107")
time.sleep(5)
print("等待加载")
time.sleep(5)
text=Webdriver.page_source
soup=BeautifulSoup(text,'lxml')
id=soup.select('#chapters-list > li > span > span')
for i in id:
    f = open('flag.txt', 'a')
    ss =open('ss.txt','a')
    get_id_class=i.get('class')
    if(len(str(get_id_class))>27):
        res2=(get_id_class[1:2])
        res=str(res2)
        idd = (res[7:13])
        seeeid = (res[14:-2])
        print(idd,seeeid)
        idd.strip()
        seeeid.strip()
        f.write(seeeid+'\n')
        ss.write(idd+'\n')
        f.close()
        ss.close()

    else:
        continue
