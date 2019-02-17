from tkinter import *
from login import Login
from register import Register
class WelcomePage:
	def __init__(self):
		self.root = Tk()
		self.addComponents()
		self.root.title('Welcome')
		self.root.geometry('550x630')
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Welcome to H-care", font=('courier', 30))
		welcome_label.place(x=50, y=50)

		login_btn=Button(self.root, text="Login", background="Green", width=20 ,height=10, command=self.login)
		signup_btn=Button(self.root, text="SignUp", background="Red", width=20, height=10, command=self.signup)

		login_btn.place(x=200, y=200)
		signup_btn.place(x=200, y=400)

	def login(self):
		self.root.destroy()
		l=Login()		

	def signup(self):
		r=Register()


#main code
a = WelcomePage()