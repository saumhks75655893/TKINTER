from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# compulsory window
root = Tk()
root.geometry("1000x680+0+0")
root.title("INPUT FIELDS")
root.configure(bg  = '#99FFCC')
root.iconbitmap(r'image/server_input.ico')


# input window
input_label = LabelFrame(root,text="INPUT WINDOW",font=("times new roman",12,'bold'))
input_label.place(x=2,y=2,width=950,height=630)

# input
input_value = LabelFrame(input_label,text="Input",font=("times new roman",12,'bold'))
input_value.place(x=2,y=5,width=550,height=603)

# output
output_value = LabelFrame(input_label,text="OutPut",font=("times new roman",12,'bold'))
output_value.place(x=555,y=5,width=390,height=603)


# roll number

rolllbl = Label(input_value,text="Roll no : ",font=("times new roman",14,'bold','italic'))
rolllbl.grid(row=0,column=0,padx=10,pady=10)
entry_roll = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_roll.grid(row=0,column=1,padx=10,pady=10)
# name

namelbl = Label(input_value,text="Name : ",font=("times new roman",14,'bold','italic'))
namelbl.grid(row=1,column=0,padx=10,pady=10)
entry_box = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_box.grid(row=1,column=1,padx=10,pady=10)

# father

fatherlbl = Label(input_value,text="Father Name : ",font=("times new roman",14,'bold','italic'))
fatherlbl.grid(row=2,column=0,padx=10,pady=10)
entry_father = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_father.grid(row=2,column=1,padx=10,pady=10)

# mother

motherlbl = Label(input_value,text="mother Name : ",font=("times new roman",14,'bold','italic'))
motherlbl.grid(row=3,column=0,padx=10,pady=10)
entry_mother = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_mother.grid(row=3,column=1,padx=10,pady=10)

# department

departmentlbl = Label(input_value,text="Department : ",font=("times new roman",14,'bold','italic'))
departmentlbl.grid(row=4,column=0,padx=10,pady=10)
entry_department = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_department.grid(row=4,column=1,padx=10,pady=10)

# Semester

semesterlbl = Label(input_value,text="Semester : ",font=("times new roman",14,'bold','italic'))
semesterlbl.grid(row=5,column=0,padx=10,pady=10)
entry_semester = ttk.Entry(input_value,width=20,font=("times new roman",14,'italic'))
entry_semester.grid(row=5,column=1)


# extract value from the all labels
def inputvalue():
    text1 = "Roll No :  " + entry_roll.get()
    lbltext = Label(output_value,text=text1,font=("times new roman",16,'bold','italic'))
    lbltext.grid(row=0, column=0,padx=10,pady=10)
    text2 = "Name : " + entry_box.get()
    lblroll = Label(output_value,text=text2,font=("times new roman",16,'bold','italic'))
    lblroll.grid(row=1, column=0,padx=10,pady=10)
    text3 = "Father Name : " + entry_father.get()
    lblfather = Label(output_value,text=text3,font=("times new roman",16,'bold','italic'))
    lblfather.grid(row=2, column=0,padx=10,pady=10)
    text4 = "Mother Name : " + entry_mother.get()
    lblmother = Label(output_value,text=text4,font=("times new roman",16,'bold','italic'))
    lblmother.grid(row=3, column=0,padx=10,pady=10)
    text5 = "Department : " + entry_department.get()
    lbldepartment = Label(output_value,text=text5,font=("times new roman",16,'bold','italic'))
    lbldepartment.grid(row=4, column=0,padx=10,pady=10)
    text6 = "Semester : " + entry_semester.get()
    lblsemester = Label(output_value,text=text6,font=("times new roman",16,'bold','italic'))
    lblsemester.grid(row=5, column=0,padx=10,pady=10)
    
def exitbutton():
    input_value.destroy()
     
def exitOutputbutton():
    output_value.destroy()

def exitbuttonmain():
    root.destroy()
    
    
# enter button
enter_button = PhotoImage(file = r'image/enter.png')
enterbtn_resize = enter_button.subsample(8,15)
enter_btn = ttk.Button(input_value,image=enterbtn_resize,command=inputvalue)
enter_btn.place(x=470,y=537)

# exit  input window button 
exit_button = PhotoImage(file = r'image/del1.png')
exitbtn_resize = exit_button.subsample(10,15)
exit_btn = ttk.Button(input_value,image=exitbtn_resize,command=exitbutton)
exit_btn.place(x=405,y=537)

# exit output window button

exit_output_button = PhotoImage(file = r'image/delete.png')
exitOutputbtn_resize = exit_output_button.subsample(10,15)
exit_output_btn = ttk.Button(output_value,image=exitOutputbtn_resize,command=exitOutputbutton)
exit_output_btn.place(x=323,y=535)

# exit button (main window)

exitlbl = Label(root,text="Click Here To Exit (Main Window ) : ",font=("times new roman",20,'bold'),bg='#FFE7BA')
exitlbl.place(x=480,y=637)

exit_buttonmain = PhotoImage(file = r'image/letterX.png')
exitbtn_resizemain = exit_buttonmain.subsample(10,15)
exit_btnmain = ttk.Button(root,image=exitbtn_resizemain,command=exitbuttonmain)
exit_btnmain.place(x=935,y=633)




# main window
if __name__ == "__main__":
    Tk.mainloop(root)