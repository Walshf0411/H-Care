from tkinter import *
from dbOperations import retrieve_appt_no, delete_appointment
from tkinter import messagebox

class CancelAppt:
	def __init__(self, user):
		self.user=user
		self.root=Tk()
		self.root.title("Cancel an Appointment")
		self.root.geometry('530x610')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Cancel an Appointment", font=('courier', 30))
		welcome_label.place(x=20, y=50)

		self.confirmation_label=Label(self.root)
		self.confirmation_label.place(x=70, y=100)

		search_label=Label(self.root, text="Search for Appointment", fg="Green", font=('courier', 15))
		search_label.place(x=100, y=150)

		search_help=Label(self.root, text="Enter the Appointment number", fg="green", font=('courier', 15)).place(x=100, y=180)
		self.search=Entry(self.root, width=70)
		self.search.place(x=70, y=220)

		search_btn=Button(self.root, text="Search", fg="white", background="green", command=self.get_appt_no)
		search_btn.place(x=200, y=260)

	def get_appt_no(self):
		try:
			appt_no=int(self.search.get())
		except:
			self.confirmation_label.config(text="Please enter an appointment number", fg="red")

		patient_id=self.user[0]
		result=retrieve_appt_no(patient_id, appt_no)
		if result is not None:
			#there exists an appointment number
			if messagebox.askquestion('Confirm Deletion', "Do you really want to delete the appointment?"):
				delete_appointment(result)
		else:
			self.confirmation_label.config(text="No such appointment number exists", fg="red")