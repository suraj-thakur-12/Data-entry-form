import tkinter 
from tkinter import *
from tkinter import ttk

def Enter_data():
    if accept_var.get() == "accepted":
        # user info
        firstname = frist_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        # course info
        registered_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemester = numsemester_spinbox.get()
    
        print("First Name:", firstname, "Last Name:", lastname)
        print("Title:", title, "Age:", age, "Nationality:", nationality)
        print("Courses:", numcourses, "Semester:", numsemester)
        print("Registration Status:", registered_status)
        print("-------------------------------------")
    else:
        print("Error: You must accept the terms and conditions!")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User Info Frame
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

frist_name_label = tkinter.Label(user_info_frame, text="First Name")
frist_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

frist_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
frist_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr", "Mrs", "Dr"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "India", "Asia", "Europe"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# Padding
for widget in user_info_frame.winfo_children():
    widget.grid(padx=10, pady=5)

# Course Info Frame
courses_fram = tkinter.LabelFrame(frame, text="Course Information")
courses_fram.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_fram, text="Registration Status")
reg_status_var = tkinter.StringVar(value="not registered")
registered_check = tkinter.Checkbutton(courses_fram, text="Currently Registered", variable=reg_status_var, onvalue="registered", offvalue="not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_fram, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_fram, from_=0, to=999)
numcourses_label.grid(row=0, column=2)
numcourses_spinbox.grid(row=1, column=2)

numsemester_label = tkinter.Label(courses_fram, text="# Semesters")
numsemester_spinbox = tkinter.Spinbox(courses_fram, from_=0, to=20)
numsemester_label.grid(row=0, column=4)
numsemester_spinbox.grid(row=1, column=4)

# Terms and Conditions
term_fram = tkinter.LabelFrame(frame, text="Terms & Conditions")
term_fram.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="not accepted")
term_check = tkinter.Checkbutton(term_fram, text="I accept the terms and conditions", variable=accept_var, onvalue="accepted", offvalue="not accepted")
term_check.grid(row=0, column=0)

# Submit Button
submit_button = tkinter.Button(frame, text="Enter Data", command=Enter_data)
submit_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
