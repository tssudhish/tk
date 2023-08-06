import tkinter as tk
from tkinter import filedialog, ttk

MAX_WIDTH = 800
MAX_HEIGHT = 500

root = tk.Tk()
root.title("Wing Architectect Assitant")

root.configure(width=MAX_WIDTH, height=MAX_HEIGHT)


main_frame = tk.LabelFrame(root, text="Fishtail Map")
main_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")


tabControl = ttk.Notebook(main_frame)
buttons = ttk.Frame(main_frame)

  
cover_archi = ttk.Frame(tabControl)
bolt_map = ttk.Frame(tabControl)
  
tabControl.add(cover_archi, text ='Cover Architecture')
tabControl.configure(padding=1, width=MAX_WIDTH, height=MAX_HEIGHT)


tabControl.add(bolt_map, text ='Bolt Map')
sample_text = ttk.Label(bolt_map,text ="Bolt Map for the Wing Cover model")



alignment_var = tk.StringVar()
alignments = ('Left', 'Center', 'Right')

# create radio buttons and place them on the label frame

grid_column = 0
for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(cover_archi, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid column
    grid_column += 1

# Button for opening the file explorer window
open_file = tk.Button(buttons, text="Load JSON File", command=lambda: filedialog.askopenfilename(initialdir="/", 
                                                                                                 title="Select a File", 
                                                                                                 filetypes=(("JSON files", "*.json*"), 
                                                                                                 ("all files", "*.*"))))


# Button to save the file
save_file = tk.Button(buttons, text="Save JSON File", command=lambda: filedialog.asksaveasfilename(initialdir="/",
                                                                                                    title="Select a File",
                                                                                                    filetypes=(("JSON files", "*.json*"),
                                                                                                    ("all files", "*.*"))))


# Open New Window
def launch():
    global second
    second = tk.Toplevel()
    second.title("Child Window")
    second.geometry("400x400")
 
# Show the window
def show():
    second.deiconify()
 
# Hide the window
def hide():
    second.withdraw()




launch_button = tk.Button(buttons, text="launch Window", command=launch)
show_button = tk.Button(buttons, text="Show", command=show)
hide_button  =  tk.Button(buttons, text="Hide", command=hide)

'''
Grids
'''
tabControl.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
sample_text.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
buttons.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
open_file.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
save_file.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
launch_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
show_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
hide_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")




root.mainloop()



