import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
Name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    Name=Name_var.get()
    password=passw_var.get()
    print("the name is:"+Name)
    print("the password is:"+password)
    Name_var.set("")
    passw_var.set("")

name_label = tk.Label(root,text = 'Username',font=('Arial',10,'bold'))
name_entry = tk.Entry(root,textvariable = Name_var,font=('Arial',10,'normal'))
passw_label = tk.Label(root,text='Password',font =('Arial',10,'bold'))
passw_entry = tk.Entry(root,textvariable=passw_var,font=('Arial',10,'normal'),show='*')
sub_btn=tk.Button(root,text = 'Submit',command = submit)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1) 
root.mainloop()