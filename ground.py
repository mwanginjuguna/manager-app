import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    i = input_int.get()
    output_string.set(i)


window = tk.Tk()
window.title('Play Ground ya Buda')
window.geometry('800x400')

# heading
heading_label = ttk.Label(master=window, text="Vitu kwa Ground!", font='Roboto 28 bold')
heading_label.pack()

# input form
input_frame = ttk.Frame(master=window)  # this is like a div in html
input_int = tk.IntVar()  # the value of input element
input_box = ttk.Entry(master=input_frame,textvariable=input_int)  # input element
button = ttk.Button(master=input_frame, text='Convert', command=convert)  # button
input_box.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=5)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Results',
                         font='Roboto 20 italic',
                         textvariable=output_string
                         )
output_label.pack(pady=5)

# run app
window.mainloop()
