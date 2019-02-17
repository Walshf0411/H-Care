from tkinter import *
from dbOperations import is_user_valid, is_doc_valid
from dashboard import Dashboard
class Login:
	def __init__(self):
		self.root=Tk()
		self.root.title('Login')
		self.root.geometry('500x610')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Welcome to H-care", font=('courier', 30))
		welcome_label.place(x=50, y=50)

		login_label=Label(self.root, text="Kindly Login", font=('courier', 20))
		login_label.place(x=100, y=150)

		username_label=Label(self.root, text="Username : ")
		password_label=Label(self.root, text="Password : ")
		self.confirmation_label=Label(self.root)

		username_label.place(x=100, y=250)
		password_label.place(x=100, y=350)
		self.confirmation_label.place(x=120, y=180)

		self.username=Entry(self.root)
		self.password=Entry(self.root, show="*	")

		self.username.place(x=170, y=250)
		self.password.place(x=170, y=350)

		login_btn=Button(self.root, text="Login",background="green", command=self.get_details)
		login_btn.place(x=200, y=500)

	def get_details(self):
		username=self.username.get()
		password=self.password.get()
		print(username, password)
		#just a dummy case, insert a db query method to validate the user in the below space
		user=is_user_valid(username, password)
		user1=is_doc_valid(username)
		if user is None and user1 is None:
			#here comes the db query 
			self.confirmation_label.config(text='Invalid Username or password', fg='red')
		else:
			if user is None:
				self.root.destroy()
				Dashboard(user1)
			else:
				self.root.destroy()
				Dashboard(user)
