import tkinter
import PIL.ImageTk
from PIL import Image
import os
import clock

dir_path = os.path.dirname(os.path.realpath(__file__))


def create_window():
    window = tkinter.Toplevel(root)
    return window;


def update():
    new_window.attributes('-topmost', True)
    clockWindow.config(text=clock.tick())
    root.after(200, update)


root = tkinter.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.resizable(width=False, height=False)
root.wm_attributes('-fullscreen', True)
root.configure(background='black')

image1 = Image.open(dir_path + '/textured_background.jpg')
image1 = image1.resize((screen_width, screen_height), Image.ANTIALIAS)
background_image = PIL.ImageTk.PhotoImage(image1)
background_label = tkinter.Label(root, image=background_image)
background_label.place(x=0, y=0)
background_label.pack()

new_window = create_window()

new_window.overrideredirect(True)
new_window.geometry('%dx%d+%d+%d' % (300, 300, 20, 100))
new_window.attributes('-alpha', 0.3)
new_window.configure(background='blue')
new_window.attributes('-topmost', True)

clockWindow = tkinter.Label(new_window, font=('times', 50, 'bold'), bg='blue', fg='white')
clockWindow.pack(fill=tkinter.BOTH, expand=1)

root.after(1000, update)
root.mainloop()
