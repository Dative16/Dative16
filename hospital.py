from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg='black')
# ============================= BUTTON FUNCTION ======================
# save Discription
def pd():
    if e1.get()=='' or e2.get()=='':
        messagebox.showerror("Error","All field are required")
    else:
        con = mysql.connector.connect(host="localhost", username = "root",password= "D11aT0208",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameofTablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            nameofpatient.get(),
            dob.get(),
            patientaddress.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Success","Recorded has been inserted")
#fetch data from saver
def fetch_data():
    con = mysql.connector.connect(host="localhost", username="root", password="D11aT0208", database="mydata")
    my_cursor = con.cursor()
    my_cursor.execute('select * from hospital')
    rows = my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        con.commit()
    con.close()
    #Get data into the input place
def get_data(event = ''):
    corsur_row = table.focus()
    data = table.item(corsur_row)
    row= data['values']
    nameofTablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    nameofpatient.set(row[8])
    dob.set(row[9])
    patientaddress.set(row[10])
# presecription
def pre():
    txt_frame.insert(END,'Name of Tablets\t\t\t'+nameofTablets.get()+'\n')
    txt_frame.insert(END, 'Reference no.\t\t\t' + ref.get() + '\n')
    txt_frame.insert(END, 'Dose\t\t\t' + dose.get() + '\n')
    txt_frame.insert(END, 'NO. of Tablets\t\t\t' + nooftablets.get() + '\n')
    txt_frame.insert(END, 'Issue Date\t\t\t' + issuedate.get() + '\n')
    txt_frame.insert(END, 'Exp. DAte\t\t\t' + expdate.get() + '\n')
    txt_frame.insert(END, 'Daily Dose\t\t\t' + dailydose.get() + '\n')
    txt_frame.insert(END, 'side Effect\t\t\t' + sideeffect.get() + '\n')
    txt_frame.insert(END, 'Blood Pressure\t\t\t' + bloodpressuer.get() + '\n')
    txt_frame.insert(END, 'Storage\t\t\t' + storage.get() + '\n')
    txt_frame.insert(END, 'Medication\t\t\t' + medication.get() + '\n')
    txt_frame.insert(END, 'Patient Id\t\t\t' + patientid.get() + '\n')
    txt_frame.insert(END, 'Name of Patient\t\t\t' + nameofpatient.get() + '\n')
    txt_frame.insert(END, 'DOB\t\t\t' + dob.get() + '\n')
    txt_frame.insert(END, 'Patient Address\t\t\t' + patientaddress.get() + '\n')
# delete
def delete():
    con = mysql.connector.connect(host="localhost", username="root", password="D11aT0208", database="mydata")
    my_cursor = con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value = (ref.get(),)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','Patient data has been deleted')

# Clear button
def clear():
    nameofTablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    bloodpressuer.set('')
    storage.set('')
    medication.set('')
    patientid.set('')
    nameofpatient.set('')
    dob.set('')
    patientaddress.set('')
    txt_frame.delete(1.0,END)

# exit button
def exit():
    confirm = messagebox.askquestion('confirmation','Are You Sure You Want To Exit')
    if confirm =='yes':
        win.destroy()
        
#Heading
Label(win,text='Hospital Managmant system',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
#Frame1
frame1=Frame(win,bd=4,relief=RIDGE)
frame1.place(x=0,y=54,width=1280,height=310)

#Lable Frame For Patient information
lf1 = LabelFrame(frame1, text='Patient Iformation',font='ariel 10 bold',bd=4,bg='pink')
lf1.place(x=10,y=0,width=750,height=280)

#Lables for partient information
Label(lf1,text='Name of Tablets',bg='pink').place(x=5,y=10)
Label(lf1,text='Reference No.',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose',bg='pink').place(x=5,y=70)
Label(lf1,text='No. of Tablets',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text='Exp. Date',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effect',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Presuer',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Divice',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient id',bg='pink').place(x=370,y=100)
Label(lf1,text='Name of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address',bg='pink').place(x=370,y=190)

# TextVariable for all labels
nameofTablets = StringVar()
ref = StringVar()
dose = StringVar()
nooftablets = StringVar()
issuedate = StringVar()
expdate = StringVar()
dailydose = StringVar()
sideeffect = StringVar()
bloodpressuer = StringVar()
storage = StringVar()
medication= StringVar()
patientid= StringVar()
nameofpatient = StringVar()
dob = StringVar()
patientaddress = StringVar()
#Entry Field for all Lables
e1= Entry(lf1,bd=2, textvariable=nameofTablets)
e1.place(x=130,y=10,width=200)
e2= Entry(lf1,bd=2, textvariable=ref)
e2.place(x=130,y=40,width=200)
e3= Entry(lf1,bd=2,textvariable=dose)
e3.place(x=130,y=70,width=200)
e4= Entry(lf1,bd=2, textvariable=nooftablets)
e4.place(x=130,y=100,width=200)
e5= Entry(lf1,bd=2, textvariable=issuedate)
e5.place(x=130,y=130,width=200)
e6= Entry(lf1,bd=2, textvariable=expdate)
e6.place(x=130,y=160,width=200)
e7= Entry(lf1,bd=2, textvariable=dailydose)
e7.place(x=130,y=190,width=200)
e8= Entry(lf1,bd=2, textvariable=sideeffect)
e8.place(x=130,y=220,width=200)
e9= Entry(lf1,bd=2, textvariable=bloodpressuer)
e9.place(x=500,y=10,width=200)
e10= Entry(lf1,bd=2,textvariable=storage)
e10.place(x=500,y=40,width=200)
e11= Entry(lf1,bd=2, textvariable=medication)
e11.place(x=500,y=70,width=200)
e12= Entry(lf1,bd=2, textvariable=patientid)
e12.place(x=500,y=100,width=200)
e13= Entry(lf1,bd=2 , textvariable=nameofpatient)
e13.place(x=500,y=130,width=200)
e14= Entry(lf1,bd=2 , textvariable=dob)
e14.place(x=500,y=160,width=200)
e15= Entry(lf1,bd=2, textvariable=patientaddress)
e15.place(x=500,y=190,width=200)

#Lable Frame For priscription
lf2 = LabelFrame(frame1, text='Priscription',font='ariel 12 bold',bd=4)
lf2.place(x=770,y=0,width=470,height=280)
#Textbox for prescription
txt_frame=Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellow')
txt_frame.pack(fill=BOTH)


#frame2
frame2 = Frame(win,bd=4,relief=RIDGE)
frame2.place(x=0,y=360,width=1280,height=250)
#Button
#Delete Button
d_btn = Button(win,text='Delete',font='ariel 15 bold',bg='brown',fg='white',bd=4,cursor='hand2',command=delete)
d_btn.place(x=0,y=600,width=270)
# Prescription Button
p_btn = Button(win,text='Prescription',font='ariel 15 bold',bg='purple',fg='white',bd=4,cursor='hand2', command=pre)
p_btn.place(x=270,y=600,width=330)
# Save Priscription Data
pd_btn = Button(win,text='Sava Prescription Data',font='ariel 15 bold',bg='green',fg='white',bd=4,cursor='hand2',command=pd)
pd_btn.place(x=600,y=600,width=340)
# Clear Button
c_btn = Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=4,cursor='hand2', command=clear)
c_btn.place(x=940,y=600,width=170)
# Exit Button
e_btn = Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=4,cursor='hand2',command=exit)
e_btn.place(x=1110,y=600,width=170)

# Scroll Bar for prescription Data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table=ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)

#Headind for priscription Data
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No.')
table.heading('dose',text='Dose')
table.heading('nots',text='No. of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Exp. Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effect')
table.heading('pn',text='Name of Patient')
table.heading('dob',text='DOB')
table.heading('pa',text='Patient Address')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
# ----------------------------
table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()
