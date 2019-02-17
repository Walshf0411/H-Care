from tkinter import *
from dbOperations import retrieve_docts, bookAppointment
class Appointment:
	def __init__(self, user):
		self.user=user
		self.root=Tk()
		self.root.title('Book an Appointment')
		self.root.geometry('520x610')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Book an appointment", font=('courier', 30))
		welcome_label.place(x=50, y=50)

		self.confirmation_label=Label(self.root)
		name_label=Label(self.root, text="Doctor\'s Name : ")
		contact_label=Label(self.root, text="Contact : ")
		gender_label=Label(self.root, text="Gender : ")

		name_label.place(x=150, y=150)
		contact_label.place(x=150, y=200)
		gender_label.place(x=150, y=250)

		self.confirmation_label.place(x=120, y=180)
		self.var1=StringVar()
		self.var2=StringVar()
		self.var2.set('Male')
		# this method will return all the doctors and store it in this variable
		choices=retrieve_docts()
		self.doctorsList=OptionMenu(self.root, self.var1,*choices)
		self.contact_no=Entry(self.root)
		self.genderList=OptionMenu(self.root, self.var2, 'Male', 'Female', 'Others')

		self.doctorsList.place(x=250, y=150)
		self.contact_no.place(x=250, y=200)
		self.genderList.place(x=250, y=250)

		book_btn=Button(self.root, text="Book Appointment", background="green", command=self.get_details)
		book_btn.place(x=200, y=350)

	def get_details(self):
		# all details are retrieved, only checkbox selection has to be done
		uid=int(self.user[0])
		contact_no=self.contact_no.get()
		doctor=self.var1.get()
		gender=self.var2.get()
		if bookAppointment(uid, contact_no, doctor, gender):
			self.confirmation_label.config(text="Appointment placed", fg='green')
		else:
			self.confirmation_label.config(text="Opps appointment couldn\'t be placed")
