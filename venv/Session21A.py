from tkinter import *
from Session21 import *

def onClick():
    name = entryName.get()
    phone = entryPhone.get()
    age = int(entryAge.get())
    address = entryAddress.get()

    c1 = Customer(0, name, phone, age, address)
    c1.showCustomer()

    db = DBHelper()
    db.saveCustomer(c1)



window = Tk()

lblTitle = Label(window, text="Enter Customer Details")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblAge = Label(window, text="Enter Customer Age")
lblAge.pack()

entryAge = Entry(window)
entryAge.pack()

lblAddress = Label(window, text="Enter Customer Address")
lblAddress.pack()

entryAddress = Entry(window)
entryAddress.pack()

btnAdd = Button(window, text="Add Customer", command=onClick)
btnAdd.pack()

window.mainloop()