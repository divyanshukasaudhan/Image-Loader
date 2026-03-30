from tkinter import *
from Sliders5 import create_slider
from ImageProcessing4 import set_brightness, set_contrast, set_saturation, set_blur, apply_adjustments
from ImageLoader3 import upload_image

def start_app():

    global root, original_panel, preview_panel

    root = Tk()
    root.title("Image Editor")
    root.geometry("1100x650")
    root.configure(bg="white")

    # TITLE

    title = Label(root,text="Image Editor",
    font=("Arial",24,"bold"),bg="white")
    title.pack(pady=5, anchor="w")

    subtitle = Label(root,
    text="Transform your images with AI-powered tools",
    font=("Arial",10),
    bg="white")
    subtitle.pack(anchor="w")

    # MAIN FRAME

    main_frame = Frame(root,bg="white")
    main_frame.pack(fill=BOTH,expand=True,padx=20,pady=20)

    # LEFT FRAME

    left_frame = Frame(main_frame,bg="white",width=300,height=500,
    highlightbackground="#d0d0d0",highlightthickness=1)

    left_frame.pack(side=LEFT,fill=BOTH,padx=10)
    left_frame.pack_propagate(False)

    Label(left_frame,
    bg="white",
    font=("Arial",12,"bold")).pack(pady=10)

    original_panel = Label(left_frame,bg="#ffffff")
    original_panel.pack()

    # CENTER FRAME

    center_frame = Frame(main_frame,bg="#ffffff",
    highlightbackground="#d0d0d0",highlightthickness=1)

    center_frame.pack(side=LEFT,fill=BOTH,expand=True,padx=10)

    center_label = Label(center_frame,text="Image Editor",
    bg="#ffffff",font=("Arial",12,"bold"))
    center_label.pack(anchor="w",pady=2)

    center_label = Label(center_frame,
    text="Apply edit power to your image",
    bg="#ffffff")
    center_label.pack(anchor="w",pady=5)

    # TABS

    tabs_frame = Frame(center_frame, bg="#ffffff")
    tabs_frame.pack(fill="x",pady=5)

    Button(tabs_frame,text="Basic Adjustments",bg="#ffffff").pack(side=LEFT,fill="x",expand=True,padx=5)
    Button(tabs_frame,text="Transform",bg="#ffffff").pack(side=LEFT,fill="x",expand=True,padx=5)
    Button(tabs_frame,text="AI Filters",bg="#ffffff").pack(side=LEFT,fill="x",expand=True,padx=5)
    Button(tabs_frame,text="Generative Fill",bg="#ffffff").pack(side=LEFT,fill="x",expand=True,padx=5)

    # PREVIEW FRAME

    preview_frame = Frame(center_frame,bg="#ffffff")
    preview_frame.pack(side=LEFT,fill=BOTH,expand=True)

    Label(preview_frame,text="Preview",
    bg="#ffffff").pack(pady=10, anchor="w")

    preview_panel = Label(preview_frame,bg="#ffffff")
    preview_panel.pack()

    # CONTROLS FRAME

    controls_frame = Frame(center_frame,bg="#ffffff",width=220)
    controls_frame.pack(side=RIGHT,fill=Y,padx=20)

    # SLIDERS

    create_slider(controls_frame,"Brightness",0,200,100,set_brightness)
    create_slider(controls_frame,"Contrast",0,200,100,set_contrast)
    create_slider(controls_frame,"Saturation",0,200,100,set_saturation)
    create_slider(controls_frame,"Blur",0,10,0,set_blur)

    # APPLY BUTTON

    apply_btn = Button(controls_frame,
    text="Apply Adjustments",
    bg="#143bb9",
    fg="white",
    width=20,
    command=lambda: apply_adjustments(preview_panel))

    apply_btn.pack(pady=10)

    # UPLOAD BUTTON

    upload_btn = Button(left_frame,
    text="Upload New Image",
    bg="#ffffff",
    command=lambda: upload_image(original_panel,preview_panel))

    upload_btn.pack(pady=20,fill="x")

    root.mainloop()