# Importing Tkinter module & initializing root window design
from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(background="#A020f0")
root.title('To-Do List Application')
root.geometry("750x500")

#Defining font style and frame widget
my_font = Font(family="Arial", size=22, weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=10)

#Defining listbox widget characteristics
my_list = Listbox(my_frame, font=my_font, width=40, height=7, bg="#cf9fff", bd=0, fg="#5c4033", highlightthickness=0, selectbackground="#ff0000", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

#Defining a scrollbar for display on right side of frame, (binding scrollbar to listbox widget)
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Defining entry widget for user input (To-Do tasks)
my_entry = Entry(root, font=("Arial", 22), width=26, bg='#cf9fff')
my_entry.pack(pady=20)

#Defining a frame for button organization
button_frame = Frame(root, bg='#a020f0')
button_frame.pack(pady=20) 

#Defining Delete function, passing ANCHOR parameter to tie function to listbox
def delete_item():
    my_list.delete(ANCHOR)

#Defining Add Item function, using Get function to retrieve value input by user to end of list 
#Using Delete function to automatically delete entry widget text after element is added to list
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

#Defining Cross-off Item function, using Item Config method to change the font color of the selected item task faint. 
def cross_off_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.selection_clear(0, END)

#Defining Uncross Item function, changing font color back to original
def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#5c4033")
    my_list.selection_clear(0, END)

#Defining Delete Crossed function, defining Counter variable, iterating until it is less than the size of the list
def delete_crossed():
    count = 0

    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

#Defining buttons for above functions, placing them in button frame, setting button click functions
delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="#e7305b", font=("arial", 12, "bold"))
add_button = Button(button_frame, text="Add Item", command=add_item, bg="#e7305b", font=("arial", 12, "bold"))
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item, bg="#e7305b", font=("arial", 12, "bold"))
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item, bg="#e7305b", font=("arial", 12, "bold"))
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed, bg="#e7305b", font=("arial",12, "bold"))

#Organizing buttons into a single row and five columns
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

#Defining Mainloop function to run Tkinter event loop and listen for events until the window is closed
root.mainloop()

