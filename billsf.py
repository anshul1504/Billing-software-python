from tkinter import *
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(s,t):
        s.t=t
        s.t.resizable(0,0)
        s.t.geometry("1350x700+90+70")
        s.t.title("billing software")
        title=Label(s.t,text="Billing Software",bd=12,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",30,"bold"),pady=2)
        title.place(x=0,y=0,width=1350)
        #variables
        #---cosmetic---
        s.a1=IntVar()
        s.a2=IntVar()
        s.a3=IntVar()
        s.a4=IntVar()
        s.a5=IntVar()
        s.a6=IntVar()
        #---grocery---
        s.b1=IntVar()
        s.b2=IntVar()
        s.b3=IntVar()
        s.b4=IntVar()
        s.b5=IntVar()
        s.b6=IntVar()
        #----cold----
        s.c1=IntVar()
        s.c2=IntVar()
        s.c3=IntVar()
        s.c4=IntVar()
        s.c5=IntVar()
        s.c6=IntVar()
        #totalp----
        s.d1=StringVar()
        s.d2=StringVar()
        s.d3=StringVar()
        s.f1=StringVar()
        s.f2=StringVar()
        s.f3=StringVar()
        #customer
        s.cname=StringVar()
        s.cphn=StringVar()
        
        s.billno=StringVar()
        x=random.randint(1000,9999)
        s.billno.set(str(x))
        s.search=StringVar()
        #customer_detail
        f1=LabelFrame(s.t,text="Customer Details",bd=7,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",15,"bold"))
        f1.place(x=0,y=80,relwidth=1)
        u1=Label(f1,text="Customer Name",bg="#074463",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        e1=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=s.cname).grid(row=0,column=1,padx=10,pady=5)
        u2=Label(f1,text="Phone N0",bg="#074463",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        e2=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=s.cphn).grid(row=0,column=3,padx=10,pady=5)
        u2=Label(f1,text="Bill Number",bg="#074463",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        e3=Entry(f1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=s.search).grid(row=0,column=5,padx=10,pady=5)
        b1=Button(f1,width=10,command=s.findbill,text="search",font="arial 12 bold").grid(row=0,column=6,padx=5,pady=10)
        #COSMETIC
        f2=LabelFrame(s.t,text="Cosmetics",bd=7,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",15,"bold"))
        f2.place(x=5,y=170,width=325,height=380)
        u1=Label(f2,text="Bath Soap",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        e1=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a1).grid(row=0,column=1,padx=10,pady=10)
        u2=Label(f2,text="Face Cream",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a2).grid(row=1,column=1,padx=10,pady=10)
        u3=Label(f2,text="Face Wash",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a3).grid(row=2,column=1,padx=10,pady=10)
        u4=Label(f2,text="Hair Spray",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        e4=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a4).grid(row=3,column=1,padx=10,pady=10)
        u5=Label(f2,text="Hair Gel",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        e5=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a5).grid(row=4,column=1,padx=10,pady=10)
        u6=Label(f2,text="Body Cream",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        e6=Entry(f2,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.a6).grid(row=5,column=1,padx=10,pady=10)
        #grossery
        f3=LabelFrame(s.t,text="Grocery",bd=7,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",15,"bold"))
        f3.place(x=340,y=170,width=325,height=380)
        u1=Label(f3,text="Rice",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        e1=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b1).grid(row=0,column=1,padx=10,pady=10)
        u2=Label(f3,text="Food Oil",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b2).grid(row=1,column=1,padx=10,pady=10)
        u3=Label(f3,text="Wheat",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b3).grid(row=2,column=1,padx=10,pady=10)
        u4=Label(f3,text="Daal",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        e4=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b4).grid(row=3,column=1,padx=10,pady=10)
        u5=Label(f3,text="Sugar",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        e5=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b5).grid(row=4,column=1,padx=10,pady=10)
        u6=Label(f3,text="Tea",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        e6=Entry(f3,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.b6).grid(row=5,column=1,padx=10,pady=10)
        #drinks
        f4=LabelFrame(s.t,text="Cold Drink",bd=7,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",15,"bold"))
        f4.place(x=670,y=170,width=325,height=380)
        u1=Label(f4,text="Maaza",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        e1=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c1).grid(row=0,column=1,padx=10,pady=10)
        u2=Label(f4,text="Frooti",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c2).grid(row=1,column=1,padx=10,pady=10)
        u3=Label(f4,text="Thums up",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        e2=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c3).grid(row=2,column=1,padx=10,pady=10)
        u4=Label(f4,text="Pepsi",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        e4=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c4).grid(row=3,column=1,padx=10,pady=10)
        u5=Label(f4,text="Limka",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        e5=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c5).grid(row=4,column=1,padx=10,pady=10)
        u6=Label(f4,text="Mountain Dew",bg="#074463",fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        e6=Entry(f4,width=10,font="arial 16",bd=5,relief=SUNKEN,textvariable=s.c6).grid(row=5,column=1,padx=10,pady=10)
        #billarea
        f5=Frame(s.t,bd=10,relief=GROOVE)
        f5.place(x=1000,y=170,width=350,height=380)
        u1=Label(f5,text="Bill Area",bd=7,relief=GROOVE,font=("arial",15,"bold")).pack(fill=X)
        
        s1=Scrollbar(f5,orient=VERTICAL)
        s.txtarea=Text(f5,yscrollcommand=s1.set)
        s1.pack(side=RIGHT,fill=Y)
        s1.config(command=s.txtarea.yview)
        s.txtarea.pack(fill=BOTH,expand=1)
        #button
        f6=LabelFrame(s.t,text="Bill Menu",bd=7,relief=GROOVE,bg="#074463",fg="gold",font=("times new roman",15,"bold"))
        f6.place(x=0,y=555,relwidth=1,height=145)
        u1=Label(f6,text="Total Cosmetics Price",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        e1=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.d1).grid(row=0,column=1,padx=10,pady=1)
        u2=Label(f6,text="Total Grocery Price",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        e2=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.d2).grid(row=1,column=1,padx=10,pady=1)
        u3=Label(f6,text="Total Cold Drink Price",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        e3=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.d3).grid(row=2,column=1,padx=10,pady=1)

        u4=Label(f6,text="Cosmetics Tax",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        e4=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.f1).grid(row=0,column=3,padx=10,pady=1)
        u5=Label(f6,text="Grocery Tax",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        e5=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.f2).grid(row=1,column=3,padx=10,pady=1)
        u6=Label(f6,text="Cold Drink Tax",bg="#074463",fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        e6=Entry(f6,width=18,font="arial 10",bd=7,relief=SUNKEN,textvariable=s.f3).grid(row=2,column=3,padx=10,pady=1)

        f7=Frame(f6,bd=7,relief=GROOVE)
        f7.place(x=750,width=580,height=105)
        b1=Button(f7,command=s.total,text="Total",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        b2=Button(f7,text="Genrate Bill",command=s.billarea,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        b3=Button(f7,text="Clear",bg="cadetblue",command=s.clear,fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        b4=Button(f7,text="Exit",command=s.exit,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        s.welcome()
    def total(s):
        s.a=s.a1.get()*40
        s.b=s.a2.get()*120
        s.c=s.a3.get()*60
        s.d=s.a4.get()*180
        s.e=s.a5.get()*140
        s.f=s.a6.get()*180
        s.totalcosmetic=float(s.a+s.b+s.c+s.d+s.e+s.f)
        s.d1.set("Rs. "+str(s.totalcosmetic))
        s.ctax=round((s.totalcosmetic*0.05),2)
        s.f1.set("Rs. "+str(s.ctax))
        
        s.g=s.b1.get()*80
        s.h=s.b2.get()*110
        s.i=s.b3.get()*120
        s.j=s.b4.get()*90
        s.k=s.b5.get()*45
        s.l=s.b6.get()*80
        s.totalgrocery=float(s.g+s.h+s.i+s.j+s.k+s.l)
        s.d2.set("Rs. "+str(s.totalgrocery))
        s.gtax=round((s.totalgrocery*0.01),2)
        s.f2.set("Rs. "+str(s.gtax))
        
        s.m=s.c1.get()*30
        s.n=s.c2.get()*40
        s.o=s.c3.get()*50
        s.p=s.c4.get()*60
        s.q=s.c5.get()*80
        s.r=s.c6.get()*100
        s.totaldrink=float(s.m+s.n+s.o+s.p+s.q+s.r)
        s.d3.set("Rs. "+str(s.totaldrink))
        s.dtax=round((s.totaldrink*0.05),2)
        s.f3.set("Rs. "+str(s.dtax))
        
        
        s.Total_bill=float(s.totalcosmetic+s.totalgrocery+s.totaldrink+s.ctax+s.gtax+s.dtax)
        
        
        
    def welcome(s):
        s.txtarea.delete('1.0',END)
        s.txtarea.insert(END,"\n\tWelcome Web Code Bill")
        s.txtarea.insert(END,f"\n\n Bill Number :  {s.billno.get()}")
        s.txtarea.insert(END,f"\n Cutomer Name :   {s.cname.get()} ")
        s.txtarea.insert(END,f"\n Phone No :       {s.cphn.get()}")
        s.txtarea.insert(END,f"\n======================================")
        s.txtarea.insert(END,f"\n Products\t\t Qty\t\tPrice")
        
        s.txtarea.insert(END,f"\n======================================")
        
    def billarea(s):
        if s.cname.get()=="" or s.cphn.get()=="":
            messagebox.showerror("Error","Customer Detail are Must")
        elif s.d1.get()=="Rs. 0.0" and s.d2.get()=="Rs. 0.0" and s.d3.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:    
            s.welcome()
            #cosmetics
            if s.a1.get()!=0:
                        s.txtarea.insert(END,f"\n Bath Soap \t\t  {s.a1.get()}\t\t{s.a}")
            if s.a2.get()!=0:
                        s.txtarea.insert(END,f"\n Face Cream \t\t  {s.a2.get()}\t\t{s.b}")
            if s.a3.get()!=0:
                        s.txtarea.insert(END,f"\n Face Wash \t\t  {s.a3.get()}\t\t{s.c}")
            if s.a4.get()!=0:
                        s.txtarea.insert(END,f"\n Hair Spray \t\t  {s.a4.get()}\t\t{s.d}")
            if s.a5.get()!=0:
                        s.txtarea.insert(END,f"\n Hair Gel \t\t  {s.a5.get()}\t\t{s.e}")
            if s.a6.get()!=0:
                        s.txtarea.insert(END,f"\n Body Cream \t\t  {s.a6.get()}\t\t{s.f}")
            #grocery
            if s.b1.get()!=0:
                s.txtarea.insert(END,f"\n Rice \t\t  {s.b1.get()}\t\t{s.g}")
            if s.b2.get()!=0:
                        s.txtarea.insert(END,f"\n Food Oil \t\t  {s.b2.get()}\t\t{s.h}")
            if s.b3.get()!=0:
                        s.txtarea.insert(END,f"\n Wheat \t\t  {s.b3.get()}\t\t{s.i}")
            if s.b4.get()!=0:
                        s.txtarea.insert(END,f"\n Daal \t\t  {s.b4.get()}\t\t{s.j}")
            if s.b5.get()!=0:
                        s.txtarea.insert(END,f"\n Sugar \t\t  {s.b5.get()}\t\t{s.k}")
            if s.b6.get()!=0:
                        s.txtarea.insert(END,f"\n Tea \t\t  {s.b6.get()}\t\t{s.l}")
            #drink
            if s.c1.get()!=0:
                s.txtarea.insert(END,f"\n Rice \t\t {s.c1.get()}\t\t{s.m}")
            if s.c2.get()!=0:
                        s.txtarea.insert(END,f"\n Maaza \t\t  {s.c2.get()}\t\t{s.n}")
            if s.c3.get()!=0:
                        s.txtarea.insert(END,f"\n Frooti \t\t  {s.c3.get()}\t\t{s.o}")
            if s.c4.get()!=0:
                        s.txtarea.insert(END,f"\n Thums up \t\t  {s.c4.get()}\t\t{s.p}")
            if s.c5.get()!=0:
                        s.txtarea.insert(END,f"\n Limka \t\t  {s.c5.get()}\t\t{s.q}")
            if s.c6.get()!=0:
                        s.txtarea.insert(END,f"\n Mountain Dew \t\t  {s.c6.get()}\t\t{s.r}")
            
            
            s.txtarea.insert(END,f"\n--------------------------------------")
            if s.f1.get()!="Rs. 0.0":
                s.txtarea.insert(END,f"\n Cosmetics Tax \t\t\t {s.f1.get()}")
            if s.f2.get()!="Rs. 0.0":
                s.txtarea.insert(END,f"\n Grocery Tax \t\t\t {s.f2.get()}")
            if s.f2.get()!="Rs. 0.0":
                s.txtarea.insert(END,f"\n Drink Tax \t\t\t {s.f3.get()}")
           
            s.txtarea.insert(END,f"\n Total Bill :\t\t\t Rs. {s.Total_bill}")
                
            s.txtarea.insert(END,f"\n-------------------------------------")
            s.save_bill()
    def save_bill(s):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            s.data=s.txtarea.get("1.0",END)
            f1=open("bills/"+str(s.billno.get())+".txt","w")
            f1.write(s.data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {s.billno.get()}  Saved Sucessfully ")
        else:
            return

    def findbill(s):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==s.search.get():
                f1=open(f"bills/{i}","r")
                s.txtarea.delete('1.0',END)
                for d in f1:
                    s.txtarea.insert(END,d)
                
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
            
    def clear(s):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            
            s.a1.set(0)
            s.a2.set(0)
            s.a3.set(0)
            s.a4.set(0)
            s.a5.set(0)
            s.a6.set(0)
            
            #---grocery---
            s.b1.set(0)
            s.b1.set(0)
            s.b1.set(0)
            s.b1.set(0)
            s.b1.set(0)
            #----cold----
            s.c1.set(0)
            s.c2.set(0)
            s.c3.set(0)
            s.c4.set(0)
            s.c5.set(0)
            s.c6.set(0)
            #totalp----
            s.d1.set("")
            s.d2.set("")
            s.d3.set("")
            s.f1.set("")
            s.f2.set("")
            s.f3.set("")
            #customer
            s.cname.set("")
            s.cphn.set("")
            
            s.billno.set("")
            x=random.randint(1000,9999)
            s.billno.set(str(x))
            s.search.set("")
            s.welcome()
            
    def exit(s):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            s.t.destroy()
t=Tk()
obj = Bill_App(t)
t.mainloop()    
