import tkinter as tk
import random

def run_baraban():
    tv1.set(str(random.choice(range(10))))
    tv2.set(str(random.choice(range(10))))
    tv3.set(str(random.choice(range(10))))
    
    t1 = tv1.get()
    t2 = tv2.get()
    t3 = tv3.get()
    
    if t1 == t2 == t3:
        print('WIN!')
    else:
        print('LOOSE!')

root = tk.Tk()
root.title('Bandit')
root.geometry('200x400+200+300')

tv1 = tk.StringVar()
tv2 = tk.StringVar()
tv3 = tk.StringVar()


lb1 = tk.Label(text = 'X')
lb2 = tk.Label(text = 'X')
lb3 = tk.Label(text = 'X')

lb1.config(font=("Courier", 44), textvariable = tv1)
lb2.config(font=("Courier", 44), textvariable = tv2)
lb3.config(font=("Courier", 44), textvariable = tv3)

btn1 = tk.Button(text = 'RUN!', command = run_baraban )
btn1.config(font=("Courier", 44))

lb1.pack()
lb2.pack()
lb3.pack()
btn1.pack()



root.mainloop()
