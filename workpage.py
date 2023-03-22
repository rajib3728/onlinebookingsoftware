from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
import webbrowser
def vt():
    try:
        db1 = mysql.connector.connect(host="localhost", user="root", password="", database="db_contact")
        mycursor1 = db1.cursor()
        sql="select * from tbl_contact"
        mycursor1.execute(sql)
        rows=mycursor1.fetchall()
        if len(rows)!=0:
            medtab.delete(*medtab.get_children())
        for row in rows:
            medtab.insert('',END,values=row)
        #db1.commit()
        db1.close()
    except:
        messagebox.showinfo("info","sorry some error occured")
def udt():
    try:
        x=e1.get()
        x1=Var1.get()
        x2=e2.get()
        res=x1+"  "+x2
        db1 = mysql.connector.connect(host="localhost", user="root", password="", database="db_contact")
        mycursor1 = db1.cursor()
        sql="UPDATE tbl_contact SET book_stat='"+res+"' WHERE Id='"+str(x)+"'"
        mycursor1.execute(sql)

        db1.commit()
        db1.close()
        messagebox.showinfo("info","update succussful")
    except:
        messagebox.showinfo("info","sorry some error occured")

def dele():
    try:
        x=e1.get()
        db1 = mysql.connector.connect(host="localhost", user="root", password="", database="db_contact")
        mycursor1 = db1.cursor()
        sql="delete from tbl_contact where Id='"+str(x)+"'"
        mycursor1.execute(sql)

        db1.commit()
        db1.close()
        messagebox.showinfo("info","Delete succussful")
    except:
        messagebox.showinfo("info","sorry some error occured")
def vsite():
    webbrowser.open("https://gharsebook.000webhostapp.com/")
def vdata():
    messagebox.showinfo("info",'''
Host: sql12.freesqldatabase.com
Database name: sql12605221
Database user: sql12605221
Database password: 68VjGvBzw3
Port number: 3306''')
    webbrowser.open("http://www.phpmyadmin.co")

root=Tk()
root.title("Online booking")
root.geometry("1600x900")
root.config(bg="white")
photo = PhotoImage(file = "./src/logo.png")
root.iconphoto(False,photo)
#l1=Label(root,text="All field data",font=("Times", 20,"bold"),bg="white")
#l1.place(x=400,y=100)
detfrm=Frame(root,bd=4,relief=RIDGE,bg="grey")
detfrm.place(x=27,y=160,width=950,height=620)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=10,width=920,height=590)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("data1","data2","data3","data4","data5","data6","data7"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("data1",text="Id")
medtab.heading("data2",text="Name")
medtab.heading("data3",text="Email")
medtab.heading("data4",text="Mobile No")
medtab.heading("data5",text="Date")
medtab.heading("data6",text="Reason of booking")
medtab.heading("data7",text="Booking Status")
medtab['show']="headings"
medtab.column("data1",width=10)
medtab.column("data2",width=10)
medtab.column("data3",width=10)
medtab.column("data4",width=10)
medtab.column("data5",width=20)
medtab.column("data6",width=20)
medtab.column("data7",width=20)
medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",vt)

f1=Frame(root,width=510,height=620,bg="grey")
f1.place(x=1000,y=160)
l2=Label(f1,text="Control Panel",font=("Times", 20,"bold"),bg="white")
l2.place(x=150,y=40)
l3=Label(f1,text="See All Data")
l3.place(x=50,y=100)
b1=Button(f1,text="view data",command=vt)
b1.place(x=150,y=100)
l4=Label(f1,text="Give id",padx=16)
l4.place(x=50,y=150)
e1=Entry(f1)
e1.place(x=150,y=150)
l5=Label(f1,text="Bookig Status")
l5.place(x=50,y=200)
Var1 = StringVar()
RBttn = Radiobutton(f1, text = "Confirm Booking", variable = Var1,padx = 18, pady = 3,value = "Confirmed")
RBttn.place(x=150,y=200)

RBttn2 = Radiobutton(f1, text = "Not Confirm Booking", variable = Var1, value ="Not confirmed",padx = 5, pady = 3)
RBttn2.place(x=150,y=250)
l6=Label(f1,text="Give Data",padx=13)
l6.place(x=50,y=300)
e2=Entry(f1)
e2.place(x=150,y=300)
b2=Button(f1,text="Update",command=udt)
b2.place(x=150,y=350)
b3=Button(f1,text="Delete",command=dele)
b3.place(x=240,y=350)

f2=Frame(root,bg="grey",width=1600,height=140)
f2.place(x=0,y=0)
b4=Button(f2,text="view site",padx=15,command=vsite)
b4.place(x=1430,y=30)
b5=Button(f2,text="view database",command=vdata)
b5.place(x=1430,y=60)
root.mainloop()