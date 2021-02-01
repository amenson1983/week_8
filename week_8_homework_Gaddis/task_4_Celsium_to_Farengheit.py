import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

class MympgGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x400')
        my_font = tkinter.font.Font(family='Arial', size=14)
        self.main_window.title('GUI for task 4')
        self.celsium_frame = tkinter.Frame(self.main_window)
        self.farengheit_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.celsium_prompt_label = tkinter.Label(self.celsium_frame, text="Celsium: ", font=my_font)
        self.celsium_entry = tkinter.Entry(self.celsium_frame, width=10, font=my_font)
        self.celsium_prompt_label.pack(side='left')
        self.celsium_entry.pack(side='left')



        self.result_label = tkinter.Label(self.farengheit_frame, text='Farengheit: ', font=my_font)
        self.farengheit = tkinter.StringVar()
        self.farengheit_label = tkinter.Label(self.farengheit_frame, textvariable=self.farengheit, font=my_font)
        self.result_label.pack(side='left')
        self.farengheit_label.pack(side='left')



        self.farengheit_button = tkinter.Button(self.button_frame, text='Convert to Farengheight', command=self.calculate_farengheit,font=my_font)
        self.farengheit_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font)
        self.quit_button.pack(side='left')

        self.celsium_frame.pack()
        self.farengheit_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def calculate_farengheit(self):
        self.celsium = float(self.celsium_entry.get())
        self.farengheit_ = ((self.celsium / 5.0 )*9) + 32.0
        self.farengheit.set(self.farengheit_)


if __name__ == '__main__':
    my_gui = MympgGUI()