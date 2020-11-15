import tkinter as tk


def do_nothing():
    pass


def do_red():
    print('doing the red thing')


def do_yellow():
    print('doing the yellow thing')


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Select First Color")
        self.selected = tk.IntVar()
        self.selected.set(0)

        self.rad1 = tk.Radiobutton(self, text='RED', value=1, variable=self.selected)     
        self.rad2 = tk.Radiobutton(self, text='YELLOW', value=2, variable=self.selected)

        self.button1 = tk.Button(self, text="Select", command=self.clicked)                    
        self.button2 = tk.Button(self, text="Quit", command=self.destroy)

        self.rad1.grid(column=0, row=0)
        self.rad2.grid(column=1, row=0)
        self.button1.grid(column=6, row=0)
        self.button2.grid(column=6, row=1)

        self.mainloop()

    def clicked(self):
        print(f'clicked {self.selected.get()}')

        v = self.selected.get()
        if v == 0:
            do_nothing()
        elif v == 1:
            do_red()
        elif v == 2:
            do_yellow()
        else:
            print('an error occurred, the wrong value was received')


GUI()