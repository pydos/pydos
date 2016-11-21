from Tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="chose functions do you want to install:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="math", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="explorer", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
#var2 = IntVar()
#Checkbutton(master, text="office", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="office", variable=var3).grid(row=3, sticky=W)
Button(master, text='all', command=select_all).grid(row=4, sticky=W)


Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
#Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()
print var1.get()

