import tkinter as tk

window = tk.Tk()
window.title('Mile to Kilometers Converter')
window.config(padx=20, pady=20)




def miles_to_km():
    mile = float(entry.get())
    if mile:
        km = round(mile * 1.6)
        display_label.config(text=f"{km}")



miles_label = tk.Label(text="Miles", font=('Arial', 10))
miles_label.grid(row=2, column=5)

display_label = tk.Label(text='0', font=('Arial', 10))
display_label.grid(row=3, column=3)

is_equal_label = tk.Label(text='is equal to', font=('Arial', 10))
is_equal_label.grid(row=3, column=1)

km_label = tk.Label(text='km', font=('Arial', 10))
km_label.grid(row=3, column=5)

entry = tk.Entry(width=10)
entry.grid(row=2, column=3)

button = tk.Button(text='Calculate', command=miles_to_km)
button.grid(row=4, column=3)









window.mainloop()