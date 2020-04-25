from tkinter import *
from PIL import Image
from tkinter import filedialog
import os
from selenium import webdriver
import requests
import re
from bs4 import BeautifulSoup as Soup
import urllib.request

def browse():
    global folder_path,file_name
    file_name = filedialog.askdirectory()
    folder_path.set(file_name)

def make_folder():
    global folder_path
    if os.path.exists('downloads')==False:
        os.mkdir('downloads')
    else:
        folder_path = 'downloads/'+keyword+'/'
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)

def download_iamges():
    global link_list
    link_list = []
    scrap_image_address()
    make_folder()
    file_name = keyword
    for i in range(len(link_list)):
        file_path = folder_path + file_name + str(i) + '.jpg'
        urllib.request.urlretrieve(link_list[i], file_path)

def scrap_image_address():
    global match,keyword,link_list
    keyword = entry2.get()
    if ' ' in keyword:
        keyword = keyword.replace(' ', '+')

    driver = webdriver.Chrome('chromedriver.exe')
    url = 'https://www.google.com/search?q=' + keyword + '&source=lnms&tbm=isch'
    req = driver.get(url)
    res = driver.execute_script('return document.documentElement.outerHTML')
    # wait = input('Wait a while')

    driver.quit()
    soup = Soup(res, 'lxml')
    match = soup.find_all('img')
    link_list = []

    for i in match:
        text = i
        # print(type(text))
        link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(text))  # finding strings of the type url
        # print("Original string: ", text)
        # print(link)
        if len(link) != 0:  # appending non empty lists
            link_list.append(link[0])


    print(len(match))
    #urls = []
    #count = 0
    for i in match:
        print(i)


#print(keyword)
# google images of the keyword
#folder = input('Name of the folder:')





root = Tk()
root.geometry('800x600')
root.configure(background='AntiqueWhite2')
root.resizable(0,0)
root.title('DatasetBuilder')

title = Label(root,text='DATA SET BUILDER',bg='AntiqueWhite2',font=('bold',13))
title.place(x=340,y=30)

logo = Image.open('image.png')
logo = logo.resize((60,60),Image.ANTIALIAS)
logo = logo.save('bob.png','png')
logo = PhotoImage(file='bob.png')

pic = Image.open('bobmax.png')
#pic = pic.resize((360,360),Image.ANTIALIAS)
pic = pic.save('bobmax.png','png')
pic = PhotoImage(file='bobmax.png')


logo_label = Label(root,image=logo,bg='AntiqueWhite2')
logo_label.place(x=275,y=10)


pic_label = Label(root,image=pic,bg='AntiqueWhite2')
pic_label.place(x=530,y=78)

num_images = Label(root,text='Number of Images',bg='AntiqueWhite2',font=('bold',10))
num_images.place(x=20,y=120)
entry1 = Entry(root,justify='center',bg='sandybrown')
entry1.place(x=140,y=122)


images_of = Label(root,text='Keyword of Image',bg='AntiqueWhite2',font=('bold',10))
images_of.place(x=20,y=150)
entry2 = Entry(root,justify='center',bg='sandybrown')
entry2.place(x=140,y=152)


location = Label(root,text='Location of Folder',bg='AntiqueWhite2',font=('bold',10))
location.place(x=20,y=184)
browse_button = Button(text='Browse File Location',bg='sandybrown',activebackground='gold',command=browse)
browse_button.place(x=140,y=180)

download = Button(root,text='Download the Clutter',bg='chocolate3',activebackground='gold',command=download_iamges)
download.place(x=80,y=230)

credits = Label(root,bg='black',fg='white',text='©Developed by Bhavishya Pandit',height=3,width=120)
credits.place(x=0,y=550)

root.mainloop()