import tkinter
from tkinter import *
from tkinter import messagebox

class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,text="Put the distance in km:")
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.descr_label = tkinter.Label(self.mid_frame,text='Converted to miles: ')
        self.miles_labels = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.descr_label.pack(side='left')
        self.miles_labels.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert to miles!', command=self.convert_to_miles)
        self.calc_button.pack(side='left')

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

    def convert_to_miles(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo('Results',str(kilo) + 'km equals to ' + str(miles) + ' miles')
        self.value.set(miles)

if __name__ == '__main__':
    my_gui = MyGUI2()