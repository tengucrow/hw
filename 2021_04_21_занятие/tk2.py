import tkinter as tk

def calculate():
    try:
        value = float(foot.get())
        meters.set(str(int(0.3048 * value * 10000.0 + 0.5)/10000.0))
    except ValueError:
        pass



root = tk.Tk()
root.title('Place example')
root.geometry('400x400+200+300')




foot = tk.StringVar()
meters = tk.StringVar()

btn1 = tk.Button(text = "Посчитать", command = calculate)
en1 = tk.Entry(text = "Введите футы",  textvariable = foot)

lb1 = tk.Label(text = "футов")
lb2 = tk.Label(text = "Равно: ")
lb3 = tk.Label(textvariable = meters)
lb4 = tk.Label(text = "метрам")

en1.grid(row = 0 , column = 0, columnspan = 2)
lb1.grid(row = 0 , column = 2)

lb2.grid(row = 1 , column = 0)
lb3.grid(row = 1 , column = 1)
lb4.grid(row = 1 , column = 2)
btn1.grid(row = 2 , column = 2)




root.mainloop()
