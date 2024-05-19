from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.geometry("500x500+0+0")
root.title("MY FIRST GUI")
root.iconbitmap(r'tiger.ico')

# # 1. pack() : In Tkinter, the pack geometry manager is used to organize widgets in blocks before placing them in the parent widget. The pack method is called on a widget to add it to the parent widget.
# '''
# Pack a widget in the parent widget. Use as options:
#         after=widget - pack it after you have packed widget
#         anchor=NSEW (or subset) - position widget according to
#                                   given direction
#         before=widget - pack it before you will pack widget
#         expand=bool - expand widget if parent size grows
#         fill=NONE or X or Y or BOTH - fill widget if widget grows
#         in=master - use master to contain this widget
#         in_=master - see 'in' option description
#         ipadx=amount - add internal padding in x direction
#         ipady=amount - add internal padding in y direction
#         padx=amount - add padding in x direction
#         pady=amount - add padding in y direction
#         side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
# '''
# # first lable
# lable1 = Label(root, text="First label")
# lable1.pack(side=RIGHT)

# # second lable , expand true with side make the text in centre.
# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',15,'bold'))
# lable2.pack(expand=True)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',20,'bold'))
# lable2.pack(side=RIGHT)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',20,'bold'))
# lable2.pack(side=TOP)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',20,'bold'))
# lable2.pack(side=BOTTOM)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',20,'bold'))
# lable2.pack(side=LEFT)

# # creating a Frame, which can expand according to the size of the window
# pane = Frame(root)
# pane.pack(fill=BOTH, expand=True)

# # button widgets which can also expand and fill in the parent widget entirely
# # Button 1
# b1 = Button(root, text="Click me !")
# b1.pack(fill=BOTH, expand=True)

# # Button 2
# b2 = Button(root, text="Click me too")
# b2.pack(fill=BOTH, expand=True)


# # Grid() : In Tkinter, the grid geometry manager is used to organize widgets in a table-like structure. With the grid manager, you can specify the row and column positions of each widget, as well as its size and alignment within the grid.

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',16,'bold'))
# lable2.grid(row=0,column=0)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',16,'bold'))
# lable2.grid(row=0,column=1)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',16,'bold'))
# lable2.grid(row=1,column=0)

# lable2 = Label(root, text='Second Lable',font=('TIMES NEW ROMAN',16,'bold'))
# lable2.grid(row=1,column=1)


# def submit_btn():
#     msg = messagebox.showinfo("Submit","The file have been submitted !! ")

# txt_button = ttk.Button(root,text="SUBMIT",command=submit_btn)
# txt_button.grid(row=5,column=0,ipadx=6,ipady=6)

# def helloCallBack():
#     msg = messagebox.showinfo("Hello Python","Hello World")

# del_button = ttk.Button(root,text="DELETE",compound=LEFT,command=helloCallBack)
# del_button.grid(row=5,column=1,ipadx=6,ipady=6)

# # place() : In Tkinter, the place manager is one of the three geometry managers used to position widgets within a container. It allows you to specify exact coordinates (x, y) for the widget to be placed

lable2 = Label(root, text='Second Lable', font=('TIMES NEW ROMAN', 16, 'bold'))
lable2.place(x=190, y=200)

txt_button = ttk.Button(root,text="CLICK ME")
txt_button.place(x=205,y=235)

if __name__ == "__main__":
    root.mainloop()
