import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")

label1 = tk.Label(
    window, 
    text="Name",
    foreground="white",
    background="blue")

label2 = tk.Label(
    window, 
    text="Address Line 1",
    foreground="white",
    background="green")

label3 = tk.Label(
    window, 
    text="Address Line 2",
    foreground="white",
    background="teal")

label4 = tk.Label(
    window, 
    text="City",
    foreground="white",
    background="purple")

label5 = tk.Label(
    window, 
    text="State",
    foreground="black",
    background="cyan")

label6 = tk.Label(
    window, 
    text="Zip Code",
    foreground="white",
    background="red")

label7 = tk.Label(
    window, 
    text="Phone Number",
    foreground="white",
    background="orange")

label8 = tk.Label(
    window, 
    text="Email Address",
    foreground="black",
    background="yellow")

button = tk.Button(
    window, 
    text="Submit",
    fg="black",
    bg="white")

entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)
entry5 = tk.Entry(window)
entry6 = tk.Entry(window)
entry7 = tk.Entry(window)
entry8 = tk.Entry(window)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()
entry4.pack()
label5.pack()
entry5.pack()
label6.pack()
entry6.pack()
label7.pack()
entry7.pack()
label8.pack()
entry8.pack()
button.pack()

window.mainloop()