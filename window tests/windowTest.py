import tkinter as tk

def create_window():
    window = tk.Toplevel(root)
    return window;

def center_window(window, width=300, height=200):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = tk.Tk()
root.resizable(width=False, height=False)
root.wm_attributes('-fullscreen', True)

new_window = create_window()
new_window.wm_resizable(width=False, height=False)
new_window.attributes('-topmost', True)
center_window(new_window)

root.mainloop()