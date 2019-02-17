from tkinter import *
from bookAppointment import Appointment
from ViewAppointments import AppointmentsList
from doctorslist import DoctorsList
from cancelAppointments import CancelAppt

class Dashboard:
	def __init__(self, user):
		self.user=user
		self.root=Tk()
		self.root.title("Dashboard")
		self.root.geometry('500x620')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Welcome to H-care", font=('courier', 30))
		welcome_label.place(x=50, y=50)

		self.confirmation_label=Label(self.root)
		self.confirmation_label2=Label(self.root)
		btn1=Button(self.root, text="Book an appointment", width=20, height=10, background='green', fg='white', command=self.bookAppointment)
		btn2=Button(self.root, text="View all Appointments", width=20, height=10, background='blue',fg='white', command=self.viewApppointments)
		btn3=Button(self.root, text="Cancel an appointment", width=20, height=10, background='red', command=self.cancelAppointment)
		btn4=Button(self.root, text="View all doctors", width=20, height=10, background='yellow', command=self.checkDoctors)

		self.confirmation_label.place(x=120, y=100)
		self.confirmation_label2.place(x=70, y=120)
		btn1.place(x=100, y=150)
		btn2.place(x=300, y=150)
		btn3.place(x=100, y=350)
		btn4.place(x=300, y=350)

	def bookAppointment(self):
		user=self.user
		Appointment(user)

	def viewApppointments(self):
		AppointmentsList(self.user)

	def cancelAppointment(self):
		CancelAppt(self.user)

	def checkDoctors(self):
		# this option should only be available to the admin
		if self.user[1]=='admin':
			self.root.destroy()
			DoctorsList()
		else:
			self.confirmation_label.config(text="You are not authorized" \
				, fg="red", font=('courier', 15))
			self.confirmation_label2.config(text="You are logged in as : "+str(self.user[1]), fg="red", font=('courier', 15))
