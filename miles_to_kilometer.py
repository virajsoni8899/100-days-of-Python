# this program will convert miles to kilometers
from tkinter import *

def miles_to_kilometers():
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    kilometer_result_label.config(text=f"{kilometers}") 


window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)


kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometers_label = Label(text="km")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)











window.mainloop()