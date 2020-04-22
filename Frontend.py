from tkinter import *
from PIL import Image
from tkinter import filedialog

def browse():
    global folder_path,file_name
    file_name = filedialog.askdirectory()
    folder_path.set(file_name)

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

download = Button(root,text='Download the Clutter',bg='chocolate3',activebackground='gold')
download.place(x=80,y=230)

credits = Label(root,bg='black',fg='white',text='©Developed by Bhavishya Pandit',height=3,width=120)
credits.place(x=0,y=550)

root.mainloop()