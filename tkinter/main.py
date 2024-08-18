import tkinter

window = tkinter.Tk()
window.title("file to km converer")
window.minsize(width=300, height=200)


def calculate():
    answer = float(miles_input.get()) * 1.6
    km_num_label.config(text=answer)


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_num_label = tkinter.Label(text="0")
km_num_label.grid(column=1, row=1)

km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
