import tkinter as tk

root = tk.Tk()
root.title('Place example')
root.geometry('400x400+200+300')

tv1 = tk.StringVar()
tv2 = tk.StringVar()
tv3 = tk.StringVar()


lb1 = tk.Button(text = '1')
lb2 = tk.Button(text = '2')
lb3 = tk.Button(text = '3')
lb4 = tk.Button(text = '==4==')


lb1.config(font=("Courier", 44))
lb2.config(font=("Courier", 44))
lb3.config(font=("Courier", 44))
lb4.config(font=("Courier", 44))

#btn1 = tk.Button(text = 'RUN!' )
#btn1.config(font=("Courier", 44))

lb1.grid(row = 0, column = 0, sticky = tk.W)
lb2.grid(row = 0, column = 1, sticky = tk.E)
lb3.grid(row = 0, column = 2, rowspan = 2, sticky = (tk.N, tk.S))
lb4.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)



root.mainloop()
