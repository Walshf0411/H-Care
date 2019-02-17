from pymysql import *

'''Methods for operation on users table start here'''
#this method works fine
def db_connect():
	'''Returns a connection object if connection is set else returns None'''
	conn=connect(host='localhost', user='root', password='Gitbtitw1@', database='lol')
	if conn.open:
		#this print is for debigging purposes
		print("Connection established")
		return conn
	else:
		print("Connection not established")
		return None

#this method works fine
def is_user_valid(username, password):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	args=(username, password)
	#Query 
	query="Select * from users where username='%s' and password='%s';"
	cursor.execute(query%args)
	if cursor.rowcount==1:
		return cursor.fetchone()
	else:
		return None

#this method works fine
def register_user(username, password, email):
	#First check if username is unique
	if user_exists(username):
		print("User exists")
		return

	args=(username, password, email)
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Insert into users(username, password, email) values ('%s', '%s', '%s');"
	
	try:
		cursor.execute(query%args)
		conn.commit()
		print("Values inserted")
		return True
	except:
		print("Values not inserted...")
		conn.rollback()
		return False
	finally:
		cursor.close()
		conn.close()

#this method works fine
def user_exists(username):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()

	query="Select * from users where username='%s'"
	cursor.execute(query%username)

	if cursor.rowcount>=1:
		return True
	else:
		return False

def retrieve_user(name):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Select name from users where name='%s'"
	cursor.execute(query%name)

	if cursor.rowcount<1:
		print("No docs of this name")
		return
	else:
		doc=cursor.fetchone()
		patient_id=doc[0]
		return patient_id
'''All methods on users table end here'''

'''All methods related to doctors table'''
def register_doc(name):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()

	query="Select * from doctors where name='%s'"
	cursor.execute(query%name)
	if cursor.rowcount==1:
		return False

	query="Insert into doctors(name) values('%s')"
	try:
		cursor.execute(query%name)
		conn.commit()
		return True
	except:
		conn.rollback()
		return False
	finally:
		cursor.close()
		conn.close()

def retrieve_docts():
	doc_list=[]
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Select * from doctors"
	cursor.execute(query)
	if cursor.rowcount<0:
		return None
	else:
		for doc in cursor.fetchall():
			doc_list.append(doc[1])

		return doc_list

def retrieve_docs():
	doc_list=[]
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Select * from doctors"
	cursor.execute(query)
	if cursor.rowcount<0:
		return None
	else:
		for doc in cursor.fetchall():
			doc_list.append(doc)

		return doc_list


def retrieve_doc(name):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Select * from doctors where name='%s'"
	cursor.execute(query%name)

	if cursor.rowcount<1:
		print("No docs of this name")
		return
	else:
		doc=cursor.fetchone()
		doc_id=doc[0]
		return int(doc_id)

def doc_by_id(did):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="Select * from doctors where did=%d"
	cursor.execute(query%did)

	if cursor.rowcount<1:
		print("No docs of this id")
		return
	else:
		doc=cursor.fetchone()
		doc_name=doc[1]
		return str(doc_name)

def is_doc_valid(username):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	args=(username)
	#Query 
	query="Select * from doctors where name='%s';"
	cursor.execute(query%args)
	print(query%args)
	if cursor.rowcount>=1:
		return cursor.fetchone()
	else:
		return None

'''Methods for doctors table end here'''

'''Methods for action on appointments table Here'''
def bookAppointment(patient_id, contact_no, doctor, gender):
	doc_id=retrieve_doc(doctor)
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	args=(doc_id, patient_id, contact_no, gender)
	query="Insert into appointments(doc_id, patient_id, usercontact, gender) values(%d, %d, '%s', '%s');"
	
	try:
		cursor.execute(query%args)
		conn.commit()
		print("Value inserted")
		return True
	except:
		conn.rollback()
		print(query%args)
		print("Not inserted")
		return False
	finally:
		cursor.close()
		conn.close()
	
def allAppointments(uid):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()
	query="select * from appointments where patient_id=%d"
	cursor.execute(query%uid)

	if cursor.rowcount>=1:
		results=cursor.fetchall()
		return results
	else:
		return None

def retrieve_appt_no(patient_id, appt_no):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()

	args=(patient_id, appt_no)
	query="Select appointment_no from appointments where patient_id=%d and appointment_no=%d;"
	cursor.execute(query%args)

	if cursor.rowcount<1:
		return None
	else:
		return appt_no

def delete_appointment(appt_no):
	conn=db_connect()
	if conn is None:
		print("Connection not established")
		return
	#cursor object created
	cursor=conn.cursor()

	args=(appt_no)
	query="Delete from appointments where appointment_no=%d"
	
	try:
		cursor.execute(query%args)
		conn.commit()
	except:
		conn.rollback()
	finally:
		cursor.close()
		conn.close()

'''Appointments tables actions end here'''