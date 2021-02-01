import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

class MyestatetaxGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x400')
        my_font = tkinter.font.Font(family='Arial', size=14)
        self.main_window.title('GUI for task 5')
        self.gross_cost_frame = tkinter.Frame(self.main_window)
        self.evaluation_cost_frame = tkinter.Frame(self.main_window)
        self.tax_amount_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.gross_cost_prompt_label = tkinter.Label(self.gross_cost_frame, text="Gross cost of estate: ", font=my_font)
        self.gross_cost_entry = tkinter.Entry(self.gross_cost_frame, width=10, font=my_font)
        self.gross_cost_prompt_label.pack(side='left')
        self.gross_cost_entry.pack(side='left')

        self.evaluation_cost = tkinter.StringVar()
        self.result_cost_label = tkinter.Label(self.evaluation_cost_frame, text='Evaluation cost: ', font=my_font)
        self.evaluation_cost_label = tkinter.Label(self.evaluation_cost_frame, textvariable=self.evaluation_cost, font=my_font)
        self.result_cost_label.pack(side='left')
        self.evaluation_cost_label.pack(side='left')

        self.tax_amount = StringVar()
        self.result_tax_label = tkinter.Label(self.tax_amount_frame, text='Tax amount: ', font=my_font)
        self.tax_cost_label = tkinter.Label(self.tax_amount_frame, textvariable=self.tax_amount,
                                                   font=my_font)
        self.result_tax_label.pack(side='left')
        self.tax_cost_label.pack(side='left')



        self.tax_button = tkinter.Button(self.button_frame, text='Calculate tax', command=self.calculate_tax_amount, font=my_font)
        self.tax_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font)
        self.quit_button.pack(side='left')


        self.gross_cost_frame.pack()

        self.evaluation_cost_frame.pack()

        self.tax_amount_frame.pack()

        self.button_frame.pack()


        tkinter.mainloop()

    def calculate_tax_amount(self):
        self.gross_cost = float(self.gross_cost_entry.get())
        self.evaluation_cost_ = (self.gross_cost )*0.6
        self.evaluation_cost.set(float(self.evaluation_cost_))
        self.tax = float(self.evaluation_cost.get())/100.0 * 0.75
        self.tax_amount.set(self.tax)



if __name__ == '__main__':
    my_gui = MyestatetaxGUI()