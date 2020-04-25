import ast
import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as Soup
import urllib.request
'''
import zipfile
with zipfile.ZipFile('chromedriver_win32.zip') as zip_file:
    zip_file.extractall()
'''

#unzipping the chrome driver
#my chrome version is 81 , you should download the drvier accroding to your version

def make_folder():
    global folder_path
    if os.path.exists('downloads')==False:
        os.mkdir('downloads')
    else:
        folder_path = 'downloads/'+keyword+'/'
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)

def download_iamges():

    make_folder()
    file_name = keyword
    for i in range(len(link_list)):
        file_path = folder_path + file_name + str(i) + '.jpg'
        urllib.request.urlretrieve(link_list[i], file_path)



driver = webdriver.Chrome('chromedriver.exe')

keyword = input('Enter the keyword:')
if ' ' in keyword:
    keyword = keyword.replace(' ','+')
#print(keyword)
# google images of the keyword
url = 'https://www.google.com/search?q='+keyword+'&source=lnms&tbm=isch'
#folder = input('Name of the folder:')

req = driver.get(url)
#print(req)
print()
#req_requests = requests.get(url).text
res = driver.execute_script('return document.documentElement.outerHTML')
#wait = input('Wait a while')
driver.quit()
soup = Soup(res,'lxml')
#print(soup.prettify())
print('Go to the browser and scroll it down')
def scrap_image_address():
    global match
    match = soup.find_all('img')
    print(len(match))
    #urls = []
    count = 0
    for i in match:
        print(i)
want_to = input('Want to scrap the URLs ? ')
if want_to == 'yes':
    scrap_image_address()
else:
    print('Alright bro ')

import re
link_list = []
for i in match:
    text = i
    #print(type(text))
    link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(text))  #finding strings of the type url
    #print("Original string: ", text)
    #print(link)
    if len(link) != 0:   #appending non empty lists
        link_list.append(link[0])
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
#print(link_list)
#print(len(link_list))

download_iamges()
