import os.path
import tkinter as tk
from tkinter import*
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
def ShowRecord():
    top=Toplevel()
    print("NOT SHOW THE RULE ")
    top.mainloop()
def SubmitRecord():
    naam=myname.get()
    lnaam=lastname.get()
    gen1=gender.get()
    address=add.get()
    city1=city.get()
    state1=state.get()
    mobile=phone.get()
    email1=email.get()
    cheak1=cheak.get()
    whom=whom1.get()
    room=room1.get()
    rent1=rent.get()
    con=sqlite3.connect("isha.db")
    cur=con.cursor()
    s="create table if not exists room(name text,lname text,gender text,address text,city text,state text,phone text,email text,cheack text,whom text,room text,rent varchar)"
    cur.execute(s)
    con.commit()
    
    s1="insert into room values('"+str(naam)+"','"+str(lnaam)+"','"+str(gen1)+"','"+str(address)+"','"+str(city1)+"','"+str(state1)+"','"+str(mobile)+"','"+str(email1)+"','"+str(cheak1)+"','"+str(whom)+"','"+str(room)+"','"+str(rent1)+"')"
    cur.execute(s1)
    con.commit()
    con.close()
    messagebox.showinfo("Success","Data saved Successfully!!")
    
root=tk.Tk()
myname=StringVar()
lastname=StringVar()
gender=StringVar()
add=StringVar()
city=StringVar()
state=StringVar()
phone=StringVar()
email=StringVar()
cheak=StringVar()
whom1=StringVar()
room1=StringVar()
show=StringVar()
img=Variable()
img2=Variable()
rent=StringVar()
root.geometry("900x1000")
root['background']='#856ff8'
root.title("ROOM BOOKING FORM")
room=["1 BHK","2 BHK","3 BHK","ONLY ONE ROOM"]
whom=["Bachelor","Job","Family"]
gen=["M","F"]

head_label=tk.Label(root,text="ROOM BOOKING FORM",width="50",bg="white")
head_label.grid(row=1,column=1,columnspan=2)
name_label=tk.Label(root,text="FIRST NAME :")
name_label.grid(row=3,column=0)
name_entry=tk.Entry(root,width="30",textvariable=myname)
name_entry.grid(row=3,column=1)
last_label=tk.Label(root,text="LAST NAME :")
last_label.grid(row=3,column=2)
last_entry=tk.Entry(root,width="30",textvariable=lastname)
last_entry.grid(row=3,column=3)
gender_label=tk.Label(root,text="GENDER :")
gender_label.grid(row=4,column=0)

gender_btn=ttk.Combobox(root,value=gen,width=5,textvariable=gender)
gender_btn.grid(row=4,column=1)
add1_label=tk.Label(root,text="ADDRESS :")
add1_label.grid(row=5,column=0)
add1_entry=tk.Entry(root,width="50",textvariable=add)
add1_entry.grid(row=5,column=1)
city_label=tk.Label(root,text="CITY :")
city_label.grid(row=6,column=0)
city_entry=tk.Entry(root,width="50",textvariable=city)
city_entry.grid(row=6,column=1)
state_label=tk.Label(root,text="STATE :")
state_label.grid(row=6,column=2)
state_entry=tk.Entry(root,width="30",textvariable=state)
state_entry.grid(row=6,column=3)
phone_label=tk.Label(root,text="PHONE NUMBER :")
phone_label.grid(row=7,column=0)
phone_entry=tk.Entry(root,width="30",textvariable=phone)
phone_entry.grid(row=7,column=1)
email_label=tk.Label(root,text="EMAIL ADDRESS :")
email_label.grid(row=7,column=2)
email_entry=tk.Entry(root,width="50",textvariable=email)
email_entry.grid(row=7,column=3)
cheak_label=tk.Label(root,text="CHECKING IN DATE :")
cheak_label.grid(row=8,column=0)
cheak_entry=tk.Entry(root,width="40",textvariable=cheak)
cheak_entry.grid(row=8,column=1)
for_label=tk.Label(root,text=" FOR WHOM :")
for_label.grid(row=9,column=0)
whom_btn=ttk.Combobox(root,value=whom,width=10,textvariable=whom1)
whom_btn.grid(row=9,column=1)
room_label=tk.Label(root,text="Room Preference :")
room_label.grid(row=10,column=0)
room_label1=ttk.Combobox(root,value=room,width=10,textvariable=room1)
room_label1.grid(row=10,column=1)
photo_label=tk.Label(root,text='Add Photo All Member :')
photo_label.grid(row=11,column=0)
photo_btn=tk.Button(root,text='Upload File', width=20,command =lambda:upload_file1())
photo_btn.grid(row=11,column=1)
photo1_label=tk.Label(root,text='Add Aadhar Photo All Member :')
photo1_label.grid(row=12,column=0)
photo1_btn=tk.Button(root,text='Upload File', width=20,command =lambda:upload_file2())
photo1_btn.grid(row=12,column=1)
   
def upload_file1():
    global img,filename
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    from PIL import Image 
# creating a image object (main image) 
    im1 = Image.open(filename)   
# save a image using extension
    im1 = im1.save("a.jpg")
    print(filename)
    b2 =tk.Button(root,image=img,width=100,height=100) # using Button 
    b2.grid(row=13,column=1)

def upload_file2():
    global img2,filename2
    f_types2 = [('Jpg Files', '*.jpg')]
    filename2 = filedialog.askopenfilename(filetypes=f_types2)
    img2 = ImageTk.PhotoImage(file=filename2)
    from PIL import Image 
# creating a image object (main image) 
    im2 = Image.open(filename2)   
# save a image using extension
    im2 = im2.save("a2.jpg")
    print(filename2)
    b22 =tk.Button(root,image=img2,width=100,height=100) # using Button 
    b22.grid(row=13,column=2)
rent_lbl=tk.Label(root,text="MONTHLY  RENT :")
rent_lbl.grid(row=15,column=0)
rent_enty=tk.Entry(root,width="20",textvariable=rent)
rent_enty.grid(row=15,column=1)
#############################SHOW DATA####################################

show_btn=tk.Button(root,text='Show Data', width=20,command =lambda:show_all())
show_btn.grid(row=18,column=1)

def show_all():
    show1=myname.get()
    if len(show1)==0:
        messagebox.showinfo("Warning","plese entry Data")
        name_entry.focus()
    else:
        con=sqlite3.connect("isha.db")
        cur=con.cursor()
        s="select lname,address,state,phone,cheack,rent from room where name='"+show1+"'"
        cur.execute(s)
        r_set=cur.fetchall()
        for column in r_set:
            lastname.set(column[0])
            add.set(column[1])
            state.set(column[2])
            phone.set(column[3])
            cheak.set(column[4])
            rent.set(column[5])
            break
        else:
            messagebox.showinfo("Error!","No such Record")
#############################print##########################################


prnt_btn=Button(root,text="SHOW RULE",command=lambda:ShowRecord())
prnt_btn.grid(row=16,column=1)

############################sumbit button###################################
submit_btn=tk.Button(root,text="Submit",width="10",command=SubmitRecord)
submit_btn.grid(row=17,column=1)

root.mainloop()
