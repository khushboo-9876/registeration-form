from tkinter import *
root=Tk()
root.title("Registeration")
root.geometry("600x470")
root.resizable(False,False)

def register():
    print("registered")

Label(root, text="python registeration form", font="arial 25 bold").pack(pady=50)

Label(text="Name",font=23).place(x=100,y=150)
Label(text="phone",font=23).place(x=100,y=200)
Label(text="gender",font=23).place(x=100,y=250)
Label(text="email",font=23).place(x=100,y=300)



namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emailValue=StringVar()

nameentry=Entry(root, textvariable=namevalue,width=30,bd=2,font=20)
phoneentry=Entry(root,textvariable=phonevalue,width=30,bd=2,font=20)
genderentry=Entry(root, textvariable=gendervalue,width=30,bd=2,font=20)
emailentry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)

nameentry.place(x=200,y=150)
phoneentry.place(x=200,y=200)
genderentry.place(x=200,y=250)
emailentry.place(x=200,y=300)

checkValue=IntVar
checkbtn=Checkbutton(text="remember me?", variable=checkValue)
checkbtn.place(x=200,y=340)

Button(text="Submit", font=20,width=11,height=2,command=register).place(x=250,y=380)

root.mainloop()