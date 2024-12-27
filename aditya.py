from tkinter import *
from tkinter import ttk
# from pIL import Image,ImageTk
from tkinter import messagebox


class Login_window:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Login")
        self.root.geometry("550x800+0+0")

        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=150, width=340, height=450)


if __name__ == "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()
