
# Importing the modules: tkinter and random
from tkinter import *
import random

# The choices of the scale to be generated
scale_choices = {
	"key": list("ABCDEFG"),
	"accidental": ["", " sharp", " flat"],
	"scaleType": ["major", "melodic minor", "harmonic minor"],
	"rhythm": ["with the crotchet on the tonic", "with even notes"],
}


# Starts the tkinter interface
window = Tk()
window.title("Scale Generator")


# Button press function
def click():

	# Making the text writable
	output.configure(state="normal")

	# Clears text box
	output.delete(0.0, END)

	sc = [random.choice(scale_component) for scale_component in scale_choices.values()]

	output.insert(END, f"Your scale is {sc[0]}{sc[1]} {sc[2]} {sc[3]}.")

	# Resetting the text to be read-only
	output.configure(state="disabled")


# Xylophone picture
photo1 = PhotoImage(file="xylophone.png")
Label(window, image=photo1, bg="white") .grid(row=0, column=0, sticky=W)

# Button (generator)
Label(window, text="Press the button to generate a random scale.", bg="white", fg="black", font="none 12 bold") .grid(row=1, column = 0, sticky=W)
Button(window, text="Generate!", width=14, command=click) .grid(row=3, column=0, sticky=W)

# Text box
Label(window, text="\nScale:", bg="white", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)
output = Text(window, width=50, height=3, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)
output.configure(state="disabled") # Making the text read-only

# Button (quit)
Button(window, text="Exit", width=14, command=window.destroy).grid(row=7, column = 0, sticky=W)

window.mainloop()
