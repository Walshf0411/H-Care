from tkinter import *
from dbOperations import retrieve_docs

class DoctorsList:
	def __init__(self):
		self.root=Tk()
		self.addComponents()
		self.root.geometry('510x600')
		self.root.title('All Doctors')
		self.root.mainloop()

	def addComponents(self):
		welcome_label=Label(self.root, text="All Doctors present", font=('courier', 30))
		welcome_label.place(x=30, y=50)

		results=retrieve_docs()
		if results is not None:
			frame=Frame(self.root, width=200, height=200)
			b1=Label(frame, text="ApptNo", width=10, font=('courier', 15))
			b2=Label(frame, text="Doctor Id", width=10, font=('courier', 15))

			b1.grid(row=0, column=0)
			b2.grid(row=0, column=1)

			#code for table creation will come here
			for i in range(1, len(results)+1):
				for j in range(2):
					b=Label(frame, text=results[i-1][j], width=15)
					b.grid(row=i, column=j)

			frame.place(x=120, y=200)