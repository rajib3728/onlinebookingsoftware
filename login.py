from tkinter import *
from PIL import ImageTk
import mysql.connector
from tkinter import ttk,messagebox
def login():
    try:
        x=e1.get()
        y=e2.get()
        db1 = mysql.connector.connect(host="localhost", user="root", password="", database="db_contact")
        mycursor1 = db1.cursor()
        sql="select * from tbl_contact1  where username= '"+x+"' and password= '"+y+"';"
        mycursor1.execute(sql)
        
        rows=mycursor1.fetchall()
        l=[]
        for i in rows:
            l.extend(list(i))
        
        db1.commit()
        if l[1]==x and l[2]==y:
            messagebox.showinfo("info","Login succussful")
            root.destroy()
            import workpage
        db1.close()
    except:
        messagebox.showinfo("info","sorry some error occured")
def register():
    try:
        x=e3.get()
        y=e4.get()
        db1 = mysql.connector.connect(host="localhost", user="root", password="", database="db_contact")
        mycursor1 = db1.cursor()
        sql="insert into tbl_contact1 (username,password) values ('"+x+"','"+y+"');"
        mycursor1.execute(sql)

        db1.commit()
        db1.close()
        messagebox.showinfo("info","Register succussful")
    except:
        messagebox.showinfo("info","sorry some error occured")
root=Tk()
root.geometry("1600x900")
root.title("Register and login")
photo = PhotoImage(file = "./src/logo.png")
root.iconphoto(False,photo)
root.config(bg="black")
bg=ImageTk.PhotoImage(file="./src/login_bg.jpg")
bglb=Label(root,image=bg)
bglb.place(x=0,y=0,relheight=1,relwidth=1)
f1=Frame(root,bg="white",width=500,height=400)
f1.place(x=870,y=200)
l1=Label(f1,text="Login",font=("Times", 20,"bold"),bg="white")
l1.place(x=220,y=50)
l2=Label(f1,text="Username",bg="white")
l2.place(x=100,y=150)
e1=Entry(f1)
e1.place(x=200,y=150)
l3=Label(f1,text="Password",bg="white")
l3.place(x=100,y=200)
e2=Entry(f1)
e2.place(x=200,y=200)
b1=Button(f1,text="Submit",bg="blue",padx=100,command=login)
b1.place(x=140,y=250)
c1=Canvas(root,height=900,width=2,bg="black")
line=c1.create_line(800,0,800,900,fill="black")
c1.place(x=800,y=0)

f2=Frame(root,bg="black",width=500,height=400)
f2.place(x=150,y=200)
l4=Label(f2,text="Register",font=("Times", 20,"bold"),bg="black",fg="white")
l4.place(x=220,y=50)
l5=Label(f2,text="Username",bg="black",fg="white")
l5.place(x=100,y=150)
e3=Entry(f2)
e3.place(x=200,y=150)
l6=Label(f2,text="Password",fg="white",bg="black")
l6.place(x=100,y=200)
e4=Entry(f2)
e4.place(x=200,y=200)
b2=Button(f2,text="Submit",bg="blue",padx=100,command=register)
b2.place(x=140,y=250)
root.mainloop()