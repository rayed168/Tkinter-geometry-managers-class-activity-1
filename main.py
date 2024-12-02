from tkinter import *
window=Tk()
window.title("Login app")
window.geometry("400x400")

frame=Frame(master=window,height=200,width=350,bg="#3349ff")
lb1=Label(master=frame,text="Full name",bg="#ff3333",fg="White")
lb2=Label(master=frame,text="Email id",bg="#ff3333",fg="White")
lb3=Label(master=frame,text="Password",bg="#ff3333",fg="White")

en1=Entry(master=frame)
en2=Entry(master=frame)
en3=Entry(master=frame,show="*")

def display_message():
    name=en1.get()
    greetings="Hi " + name + "\nCongratulations on your new account"
    text_box.insert(END,greetings)

button=Button(master=window,text="Create an account",command=display_message,bg="black",fg="white")
text_box=Text(bg="white",fg="black")

frame.place(x=20,y=0)
lb1.place(x=20,y=20)
en1.place(x=150,y=20)

lb2.place(x=20,y=80)
en2.place(x=150,y=80)

lb3.place(x=20,y=140)
en3.place(x=150,y=140)

button.place(x=130,y=210)
text_box.place(y=250)
window.mainloop()
