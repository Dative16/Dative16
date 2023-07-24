from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')


        lbl_title = Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('impack 31 bold'),bg='blue',fg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo = Image.open('images/grow.jpg')
        img_logo = img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_lolo = ImageTk.PhotoImage(img_logo)
        
        self.logo = Label(self.root,image=self.photo_lolo)
        self.logo.place(x= 270, y= 0, width=50, height=50)






root = Tk()
obj = Employee(root)
root.mainloop()