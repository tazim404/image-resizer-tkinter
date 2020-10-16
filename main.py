from tkinter import *
from PIL import Image
from tkinter import filedialog
import ntpath
import tkinter.messagebox as box
window = Tk()
icon_photo = PhotoImage(
    file='/home/tazim/Desktop/Python project/Image Resizer Program/logo.png')
window.iconphoto(True, icon_photo)
window.geometry('250x250')
window.title("Image Resizer Program")
width_var = IntVar()
height_var = IntVar()

frame = Frame(window)


def open_image():
    global filename
    filename = filedialog.askopenfilename(title="Select Image")
    splited_filname = ntpath.split(filename)
    status_bar['text'] = "Image Selected: "+splited_filname[1]


def info():
    try:
        images_details = Image.open(filename)
        image_mode = images_details.mode
        image_size = images_details.size
        image_format = images_details.format
        final_details = "Image Mode:" + \
            str(image_mode)+"\n"+"Image Size: "+str(image_size) + \
            "\n"+"Image Format: "+str(image_format)
        box.showinfo("Details", str(final_details))
    except:
        box.showerror("Error", "I think image is not selected")


def convert():
    try:
        width = width_var.get()
        height = height_var.get()
        image = Image.open(filename)
        resized_image = image.resize((width, height))
        resized_image.save("Resized_image."+str(image.format))
    except:
        box.showerror("Error", "Please selcet the image first")


width_label = Label(frame, text="Width").grid(row=1, column=1)
height_label = Label(frame, text="Height").grid(row=2, column=1, pady=5)
width_entry = Entry(frame, textvariable=width_var).grid(row=1, column=2)
height_entry = Entry(frame, textvariable=height_var).grid(
    row=2, column=2, pady=5)
open_img = Button(frame, text="Select Image", command=open_image).grid(
    row=3, column=1, padx=5, pady=5)
quit_btn = Button(frame, text="Get Image Info", command=info).grid(
    row=3, column=2, padx=5, pady=5)
convert_btn = Button(frame, text="Covert", command=convert).grid(
    row=4, column=1, columnspan=2, ipadx=70)
status_bar = Label(window, text="", relief=SUNKEN)
status_bar.pack(side=BOTTOM, fill=X)
frame.pack()
window.mainloop()
