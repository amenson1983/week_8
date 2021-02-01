import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font

class MyCheckbuttonGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        my_font = tkinter.font.Font(family='Arial',size=14,weight='bold')
        self.check_var1 = tkinter.IntVar()
        self.check_var1.set(0)
        self.check_var2 = tkinter.IntVar()
        self.check_var2.set(0)
        self.check_var3 = tkinter.IntVar()
        self.check_var3.set(0)

        self.chb1 = tkinter.Checkbutton(self.top_frame, text='Variant 1', variable=self.check_var1,font=my_font)
        self.chb2 = tkinter.Checkbutton(self.top_frame, text='Variant 2', variable=self.check_var2,font=my_font)
        self.chb3 = tkinter.Checkbutton(self.top_frame, text='Variant 3', variable=self.check_var3,font=my_font)



        self.ok_button = tkinter.Button(self.button_frame, text='OK', command=self.show_result,font=my_font)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font)
        self.quit_button.pack(side='left')

        self.chb1.pack()
        self.chb2.pack()
        self.chb3.pack()
        self.top_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def show_result(self):
        self.message = 'You chose: \n'
        if self.check_var1.get() == 1:
            self.message = self.message + ' 1\n'
        if self.check_var2.get() == 1:
            self.message = self.message + ' 2\n'
        if self.check_var3.get() == 1:
            self.message = self.message + ' 3\n'
        tkinter.messagebox.showinfo('Choice:',self.message)



if __name__ == '__main__':
    my_gui = MyCheckbuttonGUI()