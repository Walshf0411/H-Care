from tkinter import *
from dbOperations import register_user, register_doc

class Register:
	def __init__(self):
		self.root=Tk()
		self.root.title("Register")
		self.root.geometry('500x610')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Welcome to H-Care", font=('courier', 30))
		welcome_label.place(x=50, y=50)

		login_label=Label(self.root, text="Register To H-Care", font=('courier', 20))
		login_label.place(x=100, y=150)

		username_label=Label(self.root, text="Username : ")
		password_label=Label(self.root, text="Password : ")
		email_label=Label(self.root, text="email-id")
		role_label=Label(self.root, text="Role")
		#use this label to tell the user whether he has been registered or not
		self.confirmation_label=Label(self.root)

		username_label.place(x=100, y=200)
		password_label.place(x=100, y=250)
		email_label.place(x=100, y=300)
		self.confirmation_label.place(x=125, y=400)
		role_label.place(x=100, y=350)

		self.username=Entry(self.root)
		self.password=Entry(self.root, show="*")
		self.email=Entry(self.root)
		self.var=StringVar()
		self.var.set('Patient')
		self.role=OptionMenu(self.root, self.var, 'Patient', 'Doctor')

		self.username.place(x=170, y=200)
		self.password.place(x=170, y=250)
		self.email.place(x=170, y=300)
		self.role.place(x=170, y=350)

		register_btn=Button(self.root, text="Register",background="green", command=self.get_details)
		register_btn.place(x=200, y=500)

	def get_details(self):
		username=self.username.get()
		password=self.password.get()
		email=self.email.get()
		if self.var.get()=='Patient':
			if register_user(username, password, email):
				self.confirmation_label.config(text="You have been registered, Kindly login to continue", fg='green')
			else:
				self.confirmation_label.config(text="User already exists", fg='red')
		else:
			if register_doc(username):
				self.confirmation_label.config(text="You have been registered, Kindly login to continue", fg='green')
			else:
				self.confirmation_label.config(text="User already exists", fg='red')