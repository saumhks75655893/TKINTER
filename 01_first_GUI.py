from tkinter import * 

# From this command start the tkinter window 
root = Tk()
# geometory command is used to set the new window display size and +0+0 (from first 0 is for x -xis and second 0 is for the y-axis) is used for from where the window show to the user 
root.geometry("500x500+0+0")
# title is used to change the name of the title of tkinter window.
root.title("MY FIRST GUI")
# iconbitmap is used to change the logo of the tkinter window.
root.iconbitmap(r'tiger.ico')
# This command is used to stop the window till the user want.
root.mainloop()