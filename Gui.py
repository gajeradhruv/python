# import tkinter as tk
# from tkinter import ttk  
# win=tk.Tk()
# win.title('GUI')

# name_label = ttk.Label(win, text='Enter the your name:')
# name_label.grid(row=0,column=0 ,sticky= tk.W)

# email_label = ttk.Label(win, text='Enter the email :')
# email_label.grid(row=1,column=0 ,sticky= tk.W)


# age_label = ttk.Label(win, text='Enter the  age:')
# age_label.grid(row=2,column=0,sticky= tk.W)

# gender_label = ttk.Label(win, text='Select Gender:')
# gender_label.grid(row=3,column=0 ,sticky= tk.W)

# #create a entry box in the python
# name_var=tk.StringVar()
# name_entry = ttk.Entry(win,width=16,textvariable=name_var)
# name_entry.grid(row=0,column=1)

# email_var=tk.StringVar()
# email_entry = ttk.Entry(win,width=16,textvariable=email_var)
# email_entry.grid(row=1,column=1)


# age_var=tk.StringVar()
# age_entry = ttk.Entry(win,width=16,textvariable=age_var)
# age_entry.grid(row=2,column=1)


# #create combobox in the python
# gender_var=tk.StringVar()
# gender_combobox = ttk.Combobox(win , width=14 ,textvariable=gender_var,state='readonly')
# gender_combobox['values']=('male','female','other')
# gender_combobox.current(0)
# gender_combobox.grid(row=3,column=1)

# #radio button
# #student,teacher
# usertype=tk.StringVar()
# radiobtn1=ttk.Radiobutton(win,text='student',value='student',variable=usertype)
# radiobtn1.grid(row=4,column=0)


# radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
# radiobtn2.grid(row=4,column=1)

# #check button

# checkbtn_var= tk.IntVar()
# checkbtn = ttk.Checkbutton(win,text='I agree subscribe to our newsletter  ', variable = checkbtn_var)

# checkbtn.grid(row=5,columnspan=3)

# #create a submit button

# def action():
#    username=name_var.get()
#    userage=age_var.get()
#    user_email=email_var.get()
#    print(f'{username} is  {userage} years old,{user_email}')
#    user_gender=gender_var.get()
#    user_type=usertype.get()
#    if checkbtn_var.get() == 0:
#        subscribed='NO'
#    else:
#        subscribed='YES'
#        print(user_gender,user_type,subscribed)
       
#        with open('file.txt', 'a') as f:
#            f.write(f'{username},{user_gender},{user_email},{userage},{user_type},{subscribed}\n')
#            name_entry.delete(0, tk.END)
#            age_entry .delete(0, tk.END)
#            email_entry.delete(0, tk.END)
       
# submit_button = ttk.Button(win,text='Submit',command=action)
# submit_button.grid(row=6,column=0)
# win.mainloop()


