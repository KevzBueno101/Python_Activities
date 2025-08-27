from tkinter import *
from tkinter import ttk
import sqlite3 as sql


window=Tk()
window.geometry("400x400")
window.resizable(False, False)
window.title("Profile Management System")


#Database
# 
# conn=sql.connect('data.db')
# x=conn.cursor()
# x.execute("""CREATE TABLE InstructorData(
# 	first_name TEXT,
# 	last_name TEXT,
# 	address TEXT,
# 	age INTEGER
# )""")
# 
# conn.commit()
# conn.close()
# # 
# conn=sql.connect('data.db')
# x=conn.cursor()
# x.execute("""CREATE TABLE StudentData(
# 	first_name TEXT,
# 	last_name TEXT,
# 	address TEXT,
# 	age INTEGER
# )""")
# 
# conn.commit()
# conn.close()
# 
# conn=sql.connect('data.db')
# x=conn.cursor()
# x.execute("""CREATE TABLE NonTeachingData(
# 	first_name TEXT,
# 	last_name TEXT,
# 	job TEXT,
# 	age INTEGER
# )""")
# 
# conn.commit()
# conn.close()


#Database
def insdata():
	conn=sql.connect('data.db')
	x=conn.cursor()
	x.execute("INSERT INTO InstructorData VALUES (:fname, :lname, :agee, :sal)",
			{
			"fname": fn_entry.get(),
			"lname": ln_entry.get(),
			"agee": age_entry.get(),
			"sal": sal_entry.get()
			})
	
	conn.commit()
	conn.close()
	fn_entry.delete(0,END)
	ln_entry.delete(0,END)
	age_entry.delete(0,END)
	sal_entry.delete(0,END)
	
def studata():
	conn=sql.connect('data.db')
	x=conn.cursor()
	x.execute("INSERT INTO StudentData VALUES (:fname, :lname, :address, :agee)",
			{
			"fname": fns_entry.get(),
			"lname": lns_entry.get(),
			"address": adds_entry.get(),
			"agee": ages_entry.get()
			})
	
	conn.commit()
	conn.close()
	fns_entry.delete(0,END)
	lns_entry.delete(0,END)
	adds_entry.delete(0,END)
	ages_entry.delete(0,END)

def nondata():
	conn=sql.connect('data.db')
	x=conn.cursor()
	x.execute("INSERT INTO NonTeachingData VALUES (:fname, :lname, :addn, :agee)",
			{
			"fname": fnn_entry.get(),
			"lname": lnn_entry.get(),
			"addn": addn_entry.get(),
			"agee": agen_entry.get()
			})
	
	conn.commit()
	conn.close()
	fnn_entry.delete(0,END)
	lnn_entry.delete(0,END)
	addn_entry.delete(0,END)
	agen_entry.delete(0,END)
	
		
	
#Functions
def crt():
	frame0.place_forget()
	frame1.place(anchor=CENTER,x=200,y=200)
		

def comboselect(a):
	c=combo.get()
	if c=="Instructor":
		frame_non.place_forget()
		frame_stu.place_forget()
		frame_ins.place(anchor=CENTER,x=200,y=205)
	elif c=="Student":
		frame_non.place_forget()
		frame_ins.place_forget()		
		frame_stu.place(anchor=CENTER,x=200,y=205)
	elif c=="Non-Teaching":
		frame_ins.place_forget()
		frame_stu.place_forget()
		frame_non.place(anchor=CENTER,x=200,y=205)	


def viewprofile():
	frame0.place_forget()
	vpframe.place(anchor=CENTER,x=400,y=400)
	
	
def back():
	frame1.place_forget()
	vpframe.place_forget()
	frame0.place(anchor=CENTER,x=200,y=200)	


###FRame Create Profile
frame0=Frame(window,height=400,width=400,bg="grey")
frame1=Frame(window,height=400,width=400,bg="grey")



#FrameCOmbo
frame_non=Frame(frame1,height=300,width=305,bg="black")
frame_stu=Frame(frame1,height=300,width=305,bg="white")
frame_ins=Frame(frame1,height=300,width=305,bg="blue")

#Combobox
combo=ttk.Combobox(frame1,width='30',values=['Instructor','Student','Non-Teaching'])
combo.place(anchor=CENTER,x=200,y=40)
combo.bind('<<ComboboxSelected>>',comboselect)


#Labels for Instructor
fn=Label(frame_ins,text="First Name:", font=("Serif", 10),bg="white", fg="Black")
fn.place(anchor=CENTER,x=55,y=35)
ln=Label(frame_ins,text="Last Name:", font=("Serif", 10),bg="white", fg="Black")
ln.place(anchor=CENTER,x=55,y=65)
age=Label(frame_ins,text="Age:", font=("Serif", 10),bg="white", fg="Black")
age.place(anchor=CENTER,x=55,y=95)
sal=Label(frame_ins,text="Salary:", font=("Serif", 10),bg="white", fg="Black")
sal.place(anchor=CENTER,x=55,y=125)

#Labels for Student
fns=Label(frame_stu,text="First Name:", font=("Serif", 10),bg="white", fg="Black")
fns.place(anchor=CENTER,x=55,y=35)
lns=Label(frame_stu,text="Last Name:", font=("Serif", 10),bg="white", fg="Black")
lns.place(anchor=CENTER,x=55,y=65)
adds=Label(frame_stu,text="Address:", font=("Serif", 10),bg="white", fg="Black")
adds.place(anchor=CENTER,x=55,y=95)
ages=Label(frame_stu,text="Age:", font=("Serif", 10),bg="white", fg="Black")
ages.place(anchor=CENTER,x=55,y=125)


#Labels for Non-Teaching
fn=Label(frame_non,text="First Name:", font=("Serif", 10),bg="white", fg="Black")
fn.place(anchor=CENTER,x=55,y=35)
lns=Label(frame_non,text="Last Name:", font=("Serif", 10),bg="white", fg="Black")
lns.place(anchor=CENTER,x=55,y=65)
adds=Label(frame_non,text="Address:", font=("Serif", 10),bg="white", fg="Black")
adds.place(anchor=CENTER,x=55,y=95)
ages=Label(frame_non,text="Age:", font=("Serif", 10),bg="white", fg="Black")
ages.place(anchor=CENTER,x=55,y=125)
dep=Label(frame_non,text="Department:", font=("Serif", 10),bg="white", fg="Black")
dep.place(anchor=CENTER,x=55,y=155)


#ENTRY for INstructor
fn_entry=Entry(frame_ins, font=("Serif", 13),bg="white", fg="Black")
fn_entry.place(anchor=CENTER,x=195,y=35)
ln_entry=Entry(frame_ins, font=("Serif", 13),bg="white", fg="Black")
ln_entry.place(anchor=CENTER,x=195,y=65)
age_entry=Entry(frame_ins, font=("Serif", 13),bg="white", fg="Black")
age_entry.place(anchor=CENTER,x=195,y=95)
sal_entry=Entry(frame_ins, font=("Serif", 13),bg="white", fg="Black")
sal_entry.place(anchor=CENTER,x=195,y=125)

#ENTRY for Student
fns_entry=Entry(frame_stu, font=("Serif", 13),bg="white", fg="Black")
fns_entry.place(anchor=CENTER,x=195,y=35)
lns_entry=Entry(frame_stu, font=("Serif", 13),bg="white", fg="Black")
lns_entry.place(anchor=CENTER,x=195,y=65)
adds_entry=Entry(frame_stu, font=("Serif", 13),bg="white", fg="Black")
adds_entry.place(anchor=CENTER,x=195,y=95)
ages_entry=Entry(frame_stu, font=("Serif", 13),bg="white", fg="Black")
ages_entry.place(anchor=CENTER,x=195,y=125)


#ENTRY for NonTeaching
fnn_entry=Entry(frame_non, font=("Serif", 13),bg="white", fg="Black")
fnn_entry.place(anchor=CENTER,x=195,y=35)
lnn_entry=Entry(frame_non, font=("Serif", 13),bg="white", fg="Black")
lnn_entry.place(anchor=CENTER,x=195,y=65)
addn_entry=Entry(frame_non, font=("Serif", 13),bg="white", fg="Black")
addn_entry.place(anchor=CENTER,x=195,y=95)
agen_entry=Entry(frame_non, font=("Serif", 13),bg="white", fg="Black")
agen_entry.place(anchor=CENTER,x=195,y=125)
dep_entry=Entry(frame_non, font=("Serif", 13),bg="white", fg="Black")
dep_entry.place(anchor=CENTER,x=195,y=155)

#Button
#0
cpb=Button(frame0,text="Create Profile", bg="grey",fg="white",command=crt)
vpb=Button(frame0,text="View Profile", bg="grey",fg="white", command=viewprofile)
upb=Button(frame0,text="Update Profile", bg="grey",fg="white")
dpb=Button(frame0,text="Update Profile", bg="grey",fg="white")
bb=Button(frame1,text="Back", bg="blue",fg="white",command=back)
bb.place(anchor=CENTER,x=40,y=370)#Back Button

ins_but=Button(frame_ins,text="Done", bg="white",fg="black",command=insdata)
ins_but.place(anchor=CENTER,x=280,y=285)

stu_but=Button(frame_stu,text="Done", bg="white",fg="black",command=studata)
stu_but.place(anchor=CENTER,x=280,y=285)

non_but=Button(frame_non,text="Done", bg="white",fg="black",command=nondata)
non_but.place(anchor=CENTER,x=280,y=285)

#Placements
#frames
frame0.place(anchor=CENTER,x=200,y=200)

#buttons
cpb.place(anchor=CENTER,x=200,y=100)
vpb.place(anchor=CENTER,x=200,y=150)
upb.place(anchor=CENTER,x=200,y=200)
dpb.place(anchor=CENTER,x=200,y=250)

##############   View Profile     #######################

###Frame View Profile
vpframe=Frame(window,height=800,width=800,bg="grey")

#Buttons

bb2=Button(vpframe,text="Back", bg="blue",fg="white",command=back)
bb2.place(anchor=CENTER,x=40,y=370)#Back Button

#Buttons for 3 options[Instructor,Student, etc]
insbutton=Button(vpframe, text="Instructor", bg="aqua",fg="black")
insbutton.place(anchor=CENTER,x=100,y=370)










window.mainloop()

