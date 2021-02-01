import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

class MympgGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x400')
        my_font = tkinter.font.Font(family='Arial', size=14)
        self.main_window.title('GUI for task 3')
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.gallons_prompt_label = tkinter.Label(self.gallons_frame, text="Gallons: ",font=my_font)
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10,font=my_font)
        self.gallons_prompt_label.pack(side='left')
        self.gallons_entry.pack(side='left')


        self.miles_prompt_label = tkinter.Label(self.miles_frame, text='Miles: ',font=my_font)
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10,font=my_font)
        self.miles_prompt_label.pack(side='left')
        self.miles_entry.pack(side='left')



        self.result_label = tkinter.Label(self.mpg_frame, text='Miles per gallon: ',font=my_font)
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg,font=my_font)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')



        self.mpg_button = tkinter.Button(self.button_frame, text='Calculate mpg', command=self.calculate_mpg,font=my_font)
        self.mpg_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font)
        self.quit_button.pack(side='left')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.mpg_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def calculate_mpg(self):
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())
        self.mpg_ = (self.miles / self.gallons )
        self.mpg.set(self.mpg_)


if __name__ == '__main__':
    my_gui = MympgGUI()