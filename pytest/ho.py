from Tkinter import *
root = Tk()
frame = Frame(root).grid()

class state:
    def read_states():
        arry = list(map(lambda var: var.get(), states))
        for n in range(len(arry)):
            print(arry[n])
        print('----')
    def change_states(x):
        for n in range(len(folder1)):
            x[n].set(1)
    def clear_states():
        for n in range(len(states)):
            states[n].set(0)
states = []
bgs = []
folder1 = []
folder2 = []
folder_break = []
for n in range(10):
    var = IntVar()
    chk = Checkbutton(frame, text=n+1, variable=var)
    chk.grid(row=n+3)
    if n < 5:
        folder1.append(var)
    else:
        folder2.append(var)
    states.append(var)


btn_2 = Button(frame, text='Change', command=lambda w=folder1: state.change_states(w))
btn_2.grid(row=1)
btn_3 = Button(frame, text='Change2', command=lambda w=folder2: state.change_states(w))
btn_3.grid(row=1, column=1)
btn_4 = Button(frame, text='Clear', command=state.clear_states)
btn_4.grid(row=2)
btn = Button(frame, text='GO', command=state.read_states)
btn.grid(row=0)

root.mainloop()
