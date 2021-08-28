import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.a = 0
frame = tk.Frame(root)
frame.pack()

def add():
    root.a += 1
    print(root.a)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    foreground="white",
    background="black",
    command=add
)

button.pack(side=tk.LEFT)

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

label.pack(side=tk.RIGHT)

root.mainloop()


