import tkinter
from tkinter import *
from tkinter import messagebox

class MyMarksGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.test1_prompt_label = tkinter.Label(self.test1_frame, text="Put test 1 mark: ")
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test1_prompt_label.pack(side='left')
        self.test1_entry.pack(side='left')


        self.test2_prompt_label = tkinter.Label(self.test2_frame, text='Put test 2 mark: ')
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)
        self.test2_prompt_label.pack(side='left')
        self.test2_entry.pack(side='left')

        self.test3_prompt_label = tkinter.Label(self.test3_frame, text='Put test 3 mark: ')
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)
        self.test3_prompt_label.pack(side='left')
        self.test3_entry.pack(side='left')



        self.result_label = tkinter.Label(self.average_frame, text='Average mark: ')
        self.average = tkinter.StringVar()
        self.average_label = tkinter.Label(self.average_frame,textvariable=self.average)
        self.result_label.pack(side='left')
        self.average_label.pack(side='left')



        self.average_button = tkinter.Button(self.button_frame, text='Calculate average', command=self.calculate_average)
        self.average_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.average_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def calculate_average(self):
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.av = (self.test1 + self.test2 + self.test3) / 3.0
        self.average.set(self.av)


if __name__ == '__main__':
    my_gui = MyMarksGUI()