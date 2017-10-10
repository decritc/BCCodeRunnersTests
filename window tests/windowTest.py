import tkinter
import time


def create_window():
    window = tkinter.Toplevel(root)
    return window;


def update():
    new_window.attributes('-topmost', True)


root = tkinter.Tk()

root.resizable(width=False, height=False)
root.wm_attributes('-fullscreen', True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='black')

new_window = create_window()

new_window.overrideredirect(True)
new_window.geometry('%dx%d+%d+%d' % (300, 200, 20, 100))
new_window.attributes('-alpha', 0.3)
new_window.configure(background='blue')
new_window.attributes('-topmost', True)

time1 = ''
clock = tkinter.Label(new_window, font=('times', 50, 'bold'), bg='blue', fg='white')
clock.pack(fill=tkinter.BOTH, expand=1)


def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


tick()
root.after(1000, update)
root.mainloop()
