import sqlite3
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,os

database_name='pracTT'#default database name

class mbox(QDialog):
	def __init__(self,parent=None):
	 	QDialog.__init__(self,parent)		
	def create(self,title,message):
		msgBox=QMessageBox()
		msgBox.critical(self, title, message)

class practicalDB:
    """

    """
    def __init__(self,dbname):
	self.con=sqlite3.connect(dbname)
	self.cur=self.con.cursor()
    def execute(self,command):
	"""executes an sql query and returns a 0 on success and 1 on an error"""
	#print command
        try:
		result=self.cur.execute(command)
	except sqlite3.IntegrityError, (ErrorMessage):
		#print type(QString(ErrorMessage.message))
		#QMessageBox().__init__(self, "Addition Message", "Student has been added to the Database",parent=None)
		msgBox=mbox()
                msgBox.create("SQL Error",QString(str(ErrorMessage)))
        	return 1
	except(ErrorMessage):
		msgBox=mbox()
                msgBox.create("SQL Error",QString(str(ErrorMessage)))
        	return 1
	else:
		self.con.commit()
		return 0,result
	def close(self):
		self.con.close()
		
class manage_db_list:
	def __init__(self):	#check if the list exists if not create it
		try:
			f=open("DB/dblist.txt")
		except IOError:
			f=open("DB/dblist.txt","w")#assuming DB folder exists
			f.write(database_name+"\n")
		f.close()
	def read_list_of_db(self):
		f=open("DB/dblist.txt","r")
		return f.readlines()		
	def write_to_list_of_db(self,db):
		f=open("DB/dblist.txt","a")
		f.write(db+"\n")
		os.system(str("cp DB/template DB/"+db))
		f.close()
	
