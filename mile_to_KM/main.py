from tkinter import  *
import math

def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.609
    kilometer_result.config(text=f"{km}")


window=Tk()
window.title("Miles to KM converter")
window.config(padx=20,pady=20)
miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

kilometer_result=Label(text="0")
kilometer_result.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=1,row=2)

button=Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)

window.mainloop()