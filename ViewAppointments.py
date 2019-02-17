from tkinter import *
from dbOperations import doc_by_id, allAppointments

class AppointmentsList:
	def __init__(self, user):
		self.user=user
		self.root=Tk()
		self.root.title("Appointments List")
		self.root.geometry('700x610')
		self.addComponents()
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="Welcome "+str(self.user[1]), font=('courier', 30))
		welcome_label.place(x=75, y=50)

		results=allAppointments(self.user[0])
		if results is not None:
			frame=Frame(self.root, width=200, height=200)
			b1=Label(frame, text="ApptNo", width=10, font=('courier', 10))
			b2=Label(frame, text="Doctor Id", width=10, font=('courier', 10))
			b3=Label(frame, text="PatientID", width=10, font=('courier', 10))
			b4=Label(frame, text="Contact No", width=10, font=('courier', 10))
			b5=Label(frame, text="Gender", width=10, font=('courier', 10))

			b1.grid(row=0, column=0)
			b2.grid(row=0, column=1)
			b3.grid(row=0, column=2)
			b4.grid(row=0, column=3)
			b5.grid(row=0, column=4)

			for i in range(1, len(results)+1):
				for j in range(5):
					b=Label(frame, text=results[i-1][j], width=15)
					b.grid(row=i, column=j)
			print(results)

			for i in range(len(results)+2, 5):
				for i in range(5):
					c=Entry(frame, width=15)
					c.grid(row=i, column=j)
					
			btn=[]
			for i in range(1, len(results)+1):
				btn.append(Button(frame, background="red", text="Delete", fg='white', \
				 command=lambda: self.delete_appointment()))

				btn[i-1].grid(row=i, column=6)

			frame.place(x=10, y=200)
		else:
			warning_label=Label(self.root, text="Sorry you do not have any upcoming appointments", fg='red')
			warning_label.place(x=50, y=350)


	def delete_appointment(self, i):
		pass




