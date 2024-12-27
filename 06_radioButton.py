from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# compulsory window
root = Tk()
root.geometry("500x400+300+0")
root.resizable(0,0)
root.title("RADIO BUTTON")
root.configure(bg='#F4A460')
root.iconbitmap(r'image/buttons2.ico')

# radio button


def radio_get():
    print("The gender is : ", gender.get())

def exit_button():
    root.destroy()

gender = StringVar()
radio_male = Radiobutton(root, variable=gender, value='male', text='Male', font=(
    "times new roman", 26, "bold", "italic"), bg="#F4A460")
radio_male.place(x=110, y=50)
gender.set(None)

radio_female = Radiobutton(root, variable=gender, value='female', text='Female', font=(
    "times new roman", 26, "bold", "italic"), bg="#F4A460")
radio_female.place(x=300, y=50)

# radio button to

radio_button = Button(root, text="Click Me", font=(
    "times new roman", 20, "bold"), border=10, bg='#0000FF', fg='#7FFFD4', command=radio_get)
radio_button.place(x=190, y=200)


exit_image = PhotoImage(file=r"image/del1.png")
exit_image_resize = exit_image.subsample(5, 10)
exit_button = Button(root, image=exit_image_resize,command=exit_button,border=10)
exit_button.place(x=200,y=280)


# main window running
if __name__ == "__main__":
    Tk.mainloop(root)
