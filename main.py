from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Employee.db")



db = Database("Employee.db")

root = Tk()
root.title('Système de Gestion des Employés')  # Changed from 'Employee Managent System'
root.geometry('1240x615+100+100')
root.resizable(False, False)
root.configure(bg='#2c3e80')

# Defining variables in French
nom = StringVar()  # Name
age = StringVar()
travail = StringVar()  # Job
sexe = StringVar()  # Gender
email = StringVar()
mobile = StringVar()




# Load the icon image and resize it
logo = PhotoImage(file='code.png')
small_logo = logo.subsample(5)
lbl_logo = Label(root, image=small_logo, bg='#2c3e80')
lbl_logo.place(x=130, y=510)





entries_frame = Frame(root, bg='#2c3e80')
entries_frame.place(x=1, y=1, width=360, height=510)
title = Label(entries_frame, text='Entreprise des Employés', font=('Calibri', 18, 'bold'), bg='#2c3e80', fg='white')
title.place(x=10, y=1)

lblNom = Label(entries_frame, text='Nom:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblNom.place(x=10, y=50)
textNom = Entry(entries_frame, textvariable=nom, width=20, font=('Calibri', 16))
textNom.place(x=120, y=50)

lblTravail = Label(entries_frame, text='Travail:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblTravail.place(x=10, y=90)
textTravail = Entry(entries_frame, textvariable=travail, width=20, font=('Calibri', 16))
textTravail.place(x=120, y=90)

lblSexe = Label(entries_frame, text='Sexe:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblSexe.place(x=10, y=130)
comboSexe = ttk.Combobox(entries_frame, textvariable=sexe, state='readonly', width=18, font=('Calibri', 16))
comboSexe['values'] = ('Homme', 'Femme')
comboSexe.place(x=120, y=130)

lblAge = Label(entries_frame, text='Âge:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblAge.place(x=10, y=170)
textAge = Entry(entries_frame, textvariable=age, width=20, font=('Calibri', 16))
textAge.place(x=120, y=170)

lblEmail = Label(entries_frame, text='Email:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblEmail.place(x=10, y=210)
textEmail = Entry(entries_frame, textvariable=email, width=20, font=('Calibri', 16))
textEmail.place(x=120, y=210)

lblMobile = Label(entries_frame, text='telephone:', font=('Calibri', 16), bg='#2c3e80', fg='white')
lblMobile.place(x=10, y=250)
textMobile = Entry(entries_frame, textvariable=mobile, width=20, font=('Calibri', 16))
textMobile.place(x=120, y=250)

lblAddress =Label(entries_frame,text='Address:',font=('Calibri',16),bg='#2c3e80',fg='white')
lblAddress.place(x=10,y=290)
textAddress = Text(entries_frame,width=30,height=2,font=('Calibri',16))
textAddress.place(x=10,y=330)





def hide():
    root.geometry('360x515+100+100')
def show():
    root.geometry('1240x615+100+100')
btnhide = Button(entries_frame,text='HIDE',command=hide,bg='#10284c',fg='white',cursor='hand2',relief=SOLID,bd=1)
btnhide.place(x=270,y=10)


btnshow = Button(entries_frame,text='SHOW',command=show,bg='#2c5e10',fg='white',cursor='hand2',relief=SOLID,bd=1)
btnshow.place(x=310,y=10)

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    nom.set(row[1])
    age.set(row[2])
    travail.set(row[3])
    email.set(row[4])
    sexe.set(row[5])
    mobile.set(row[6])
    textAddress.delete(1.0, END)
    textAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def delete():
    db.remove(row[0])
    Clear()
    displayAll()

def Clear():
    nom.set("")
    age.set("")
    travail.set("")
    sexe.set("")
    email.set("")
    mobile.set("")
    textAddress.delete(1.0,END)





def add_employee():
    if textNom.get() == "" or textAge.get() == "" or textTravail.get() == "" or textEmail.get() == "" or comboSexe.get() == "" or textAddress.get(1.0,END) == "" or textMobile.get() == "":
        messagebox.showerror("Error","please Fill all the Entry")
        return
    db.insert(
        textNom.get(),
        textAge.get(),
        textTravail.get(),
        textEmail.get(),
        textMobile.get(),
        comboSexe.get(),
        textAddress.get(1.0,END))
    messagebox.showinfo("Success","Added new Employee")
    Clear()
    displayAll()
def update():
    if textNom.get() == "" or textAge.get() == "" or textTravail.get() == "" or textEmail.get() == "" or comboSexe.get() == "" or textAddress.get(1.0,END) == "" or textMobile.get() == "":
        messagebox.showerror("Error","please Fill all the Entry")
        return
    db.update(row[0],
        textNom.get(),
        textAge.get(),
        textTravail.get(),
        textEmail.get(),
        textMobile.get(),
        comboSexe.get(),
        textAddress.get(1.0,END))
    messagebox.showinfo('Success','The employee data is update')
    Clear()
    displayAll()


btn_frame = Frame(entries_frame,bg='white',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)
btnAdd = Button(btn_frame,
               text='Add Details',
               width='14',
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#2c5e50',
               bd=0,
               command=add_employee
                ).place(x=4,y=5)
btnEdit = Button(btn_frame,
               text='Update Details',
               width='14',
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#2c5e99',
               command=update,
               bd=0,
                ).place(x=4,y=50)
btnDelete = Button(btn_frame,
               text='Delete Details',
               width='14',
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#c0392b',
               command=delete,
               bd=0,
                ).place(x=170,y=5)
btnClear = Button(btn_frame,
               text='Clear Details',
               width='14',
               height=1,
               font=('Calibri',16),
               fg='white',
               bg='#f39c12',
               bd=0,
               command=Clear
                ).place(x=170,y=50)





tree_frame = Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=610)
style= ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure('mystyle,Treeview.Heading',font=('Calibri',13))

tv= ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
tv.heading('1', text='ID')
tv.column('1',width='40')

tv.heading('2', text='Name')
tv.column('2',width='140')

tv.heading('3', text='Age')
tv.column('3',width='50')

tv.heading('4', text='Job')
tv.column('4',width='120')

tv.heading('5', text='Email')
tv.column('5',width='150')

tv.heading('6', text='Gender')
tv.column('6',width='90')

tv.heading('7', text='Mobile')
tv.column('7',width='150')

tv.heading('8', text='Address')
tv.column('8',width='150')

tv['show']='headings'
tv.bind("<ButtonRelease-1>", getData)
tv.place(x=1,y=1,height=610,width=875)


displayAll()






root.mainloop()