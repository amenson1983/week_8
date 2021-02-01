import tkinter
from tkinter import *
from tkinter import messagebox

class MyRadioGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Variant 1',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Variant 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Variant 3', variable=self.radio_var, value=3)



        self.ok_button = tkinter.Button(self.button_frame, text='OK', command=self.show_result)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def show_result(self):
        tkinter.messagebox.showinfo('Choice:','You chose variant '+ str(self.radio_var.get()))



if __name__ == '__main__':
    my_gui = MyRadioGUI()