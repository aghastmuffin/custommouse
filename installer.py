from tkinter import * 
from tkinter.ttk import *
import os
# creating tkinter window
root = Tk()
  
# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
  
# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
#    os.system("git fetch git://github.com/aghastmuffin/custommouse")
    os.system("https://raw.githubusercontent.com/aghastmuffin/custommouse/main/installer.py")
    os.system("passed 1")

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.1)
    progress['value'] = 100

    time.sleep(0.1)
    progress["value"] = (0)
  
progress.pack(pady = 10)
  
# This button will initialize
# the progress bar
Button(root, text = 'Start Install', command = bar).pack(pady = 10)
  
# infinite loop
mainloop()
