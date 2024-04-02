import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("window")

frame1 = tk.Frame(master=window)
button1 = tk.Button(master=frame1, text="Button Text")
text_box1 = tk.Text()
text_box1.insert("1.0", "Hello")
label1 = tk.Label(master=frame1, text="Label Text")

frame1.pack()
label1.pack()
button1.pack()
text_box1.pack()

frame2 = tk.Frame(master=window)
button2 = tk.Button(master=frame2, text="Chief what are you Doing?")
text_box2 = tk.Text()
text_box2.insert("1.0", "\nMeal")
text_box2.insert("1.0", "\nthis")
text_box2.insert("1.0", "Cooking")

frame2.pack()
text_box2.pack()

window.mainloop()