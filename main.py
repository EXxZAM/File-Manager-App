

# ?    Map
# TODO 1- Let the user to select a Directory
# TODO 2- make a list of the files inside of the directory and show it on the window
# TODO 3- let the user choose an item from the list
# TODO 4- show desc like name, type, size, date of the file and let the user to open it if wanted to
# TODO 5- Done

# TODO: 1- open directory button ✔
# TODO: 2- open the file button ✔
# TODO: 3- name, time, size, type of the file chosen labels ✔
# TODO: 4- a list of the files inside the selected dir ( LabelList ) ✔
# TODO: 5- functions for changing the dir, opening the file, getting file information

# ? Packages Used
# * 1- Tkinter
# * 2- Time
# * 3- Random
# * 4- OS


# Importing packages
from tkinter import *
from tkinter import filedialog
import random
import time
import os, os.path

# Making the window
root = Tk()
root.title('File Manager')
root.geometry('670x320')
root.resizable(0,0)

# Functions
def change_dir():
    global direcotry
    direcotry = filedialog.askdirectory()
    os.chdir(direcotry)
    files = os.listdir()
    
    for file in files:
        filelist.insert(END,file)

def show_detail():
    
    file_name = filelist.get(ACTIVE)
    file_add = direcotry +'/'+ file_name
    print(file_add)
    
    os.stat(file_add)
    name, extension = os.path.splitext(file_add)
    if extension == '':
        file_type_label.config(text='File Type: Folder')
    else:
        file_type_label.config(text='File Type: {} File'.format(extension))
    file_name_label.config(text='File Name: {}'.format(file_name))

def open_file():
    file_name = filelist.get(ACTIVE)
    file_add = direcotry +'/'+ file_name
    os.startfile(file_add)
# Designing the Program

open_dir_btn = Button(root, text='Open Folder', padx=10, pady=3, borderwidth=3, bg='#121000', fg='white', command=change_dir)
open_dir_btn.grid(row=0,column=0, padx=20,pady=20)


open_file_btn = Button(root, text='Open File', padx=18, pady=3, borderwidth=3, bg='#121000', fg='white', command=open_file)
open_file_btn.grid(row=0,column=1, padx=20,pady=0)

file_name_label = Label(root, text='File Name: main.py', anchor="e", justify=LEFT,font=("Arial",10,'italic'))
file_name_label.grid(row=2,column=0,pady=10,sticky=W,padx=20)

file_size_label = Label(root, text='File Size: 100MB',anchor="e",justify=LEFT ,font=("Arial",10,'italic') )
file_size_label.grid(row=2,column=1,pady=10,sticky=W,padx=20)

file_date_label = Label(root, text='File Date: 2020-10-20',anchor="e",justify=LEFT  ,font=("Arial",10,'italic'))
file_date_label.grid(row=3,column=0,pady=10,sticky=W,padx=20)

file_type_label = Label(root, text='File Type: Python File',anchor="e",justify=LEFT ,font=("Arial",10,'italic'))
file_type_label.grid(row=3,column=1,pady=10,sticky=W,padx=20)

show_detail_btn = Button(root, text='Show File Detail',  borderwidth=3, bg='#121000', fg='white',padx=100,pady=5, command=show_detail)
show_detail_btn.place(relx=0.25, rely=0.7, anchor='c')



# Inserting scrollbar
scrol_y = Scrollbar(root,orient=VERTICAL,)
# Inserting Playlist listbox
filelist = Listbox(root,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("Arial",12,'bold'),bg="silver",fg="#121212",bd=5,relief=GROOVE, width=30, height=14)
# Applying Scrollbar to listbox
scrol_y.place(x=650, y=30)

scrol_y.config(command=filelist.yview)
filelist.place(relx=0.75, rely=0.5, anchor='c')

# # Changing Directory for fetching Songs
# os.chdir(r"F:\10 Tkinter Projects\9-Music_Player\songs")

# # Fetching Songs
# songtracks = os.listdir()
# .get(ACTIVE)
# Calling the main window's mainloop
root.mainloop()







