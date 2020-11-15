
        # self.app = Tk()
        # self.app.title("Publisher DB")
        # self.app.geometry("300x250")
        # self.label = Label(self.app, text="Welcome to the ceid publishing house")
        # self.label.place(x=50, y=40)
        # self.login_btn = Button(self.app, text="Go to login.", pady=5, padx=30, command=login)
        # self.login_btn.place(x=100, y=100)


                self.app = Tk()
        self.app.title("Publisher DB")
        self.app.geometry("300x250")
        self.label = Label(self.app, text="Welcome to the ceid publishing house")
        self.label.place(x=50, y=40)
        self.login_btn = Button(self.app, text="Go to login.", pady=5, padx=30, command=login)
        self.login_btn.place(x=100, y=100)

    def run(self):
        self.app.mainloop()