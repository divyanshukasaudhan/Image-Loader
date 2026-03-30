from tkinter import *

def create_slider(parent,label,minimum,maximum,start,command):

    frame = Frame(parent,bg="#ffffff")
    frame.pack(pady=3,fill="x")

    top = Frame(frame,bg="#ffffff")
    top.pack(fill="x")

    Label(top,text=label,bg="#ffffff").pack(side="left")

    value_label = Label(top,text=str(start)+"%",bg="#ffffff")
    value_label.pack(side="right")

    canvas = Canvas(frame,width=200,height=40,
                    bg="#ffffff",
                    highlightthickness=0)
    canvas.pack(pady=1)

    canvas.create_line(10,20,190,20,width=4,fill="#eeeeee",capstyle=ROUND)

    progress = canvas.create_line(10,20,12,20,width=4,fill="#6c63ff",capstyle=ROUND)

    thumb = canvas.create_oval(8,16,16,24,fill="white",outline="#6c63ff",width=2)

    x = 10 + (start - minimum) / (maximum - minimum) * 180

    canvas.coords(thumb,x-6,14,x+6,26)
    canvas.coords(progress,10,20,x,20)

    def move(e):

        x = max(10,min(190,e.x))

        canvas.coords(thumb,x-6,14,x+6,26)
        canvas.coords(progress,10,20,x,20)

        value = minimum + (x-10)/180*(maximum-minimum)

        value_label.config(text=str(int(value))+"%")

        command(value)

    canvas.bind("<B1-Motion>",move)