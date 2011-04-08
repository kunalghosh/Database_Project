from front_end_files.dbmsUI import *
from front_end_files.View_contentsUI import *
from front_end_files.AddStudent import * 
import front_end_files.delete as delete
from front_end_files.Update_details import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from DB.pracTT_Db import *
from string import Template
import string
import webbrowser
db_manager=manage_db_list()
stud_db=practicalDB('DB/'+database_name)
insert_student_details_template=Template('insert into student_details values (\'$usn\',\'$name\',$sem,$elig);')
insert_student_with_arrears_template=Template('insert into studs_with_arrears values (\'$usn\',\'$subject_code\');')
retrieve_details_template=Template('select * from $table $condition;')#add the $condition along with the clause required
class AddStudent_Interface(QtGui.QDialog):
        """

        """
        def __init__(self,parent=None):
        	""""""
            	QtGui.QDialog.__init__(self,parent)
  	        self.ui = Ui_Dialog()
            	self.ui.setupUi(self)
            	QtCore.QObject.connect(self.ui.add_pushButton,QtCore.SIGNAL("clicked()"),self.add_student_to_DB)

	def clear_AddStudent_texts(self):
		self.ui.usn_lineEdit.clear()
		self.ui.name_lineEdit.clear()
		self.ui.semester_lineEdit.clear()
		self.ui.arrear1_lineEdit.clear()
		self.ui.arrear2_lineEdit.clear()
		self.ui.arrear3_lineEdit.clear()
		self.ui.arrear4_lineEdit.clear()
		self.ui.arrear5_lineEdit.clear()
		#uncheck the two check boxes
		self.ui.eligible_checkBox.setCheckState(0)
		self.ui.hasArrears_checkBox.setCheckState(0)
        def add_student_to_DB(self):
             	"""
		Collect all the relevant fields' values and call the
            	sql function to insert
            	"""
	        self.stud_name=self.ui.name_lineEdit.text().toAscii()
            	self.stud_usn=self.ui.usn_lineEdit.text().toAscii()
            	self.stud_sem=self.ui.semester_lineEdit.text()
            	self.stud_elig=self.ui.eligible_checkBox.checkState()
            	if self.stud_elig == 0:
                	self.stud_elig_stat=0
            	else:
                	self.stud_elig_stat=1
	    	self.stud_arrear=[]#Creating a list of all the arrears
	    	arr=self.ui.arrear1_lineEdit.text().toAscii()
	    	if(arr):
			self.stud_arrear.append(arr)
	    	arr=self.ui.arrear2_lineEdit.text().toAscii()
	    	if(arr):                  	    
    			self.stud_arrear.append(arr)
	    	arr=self.ui.arrear3_lineEdit.text().toAscii()
	    	if(arr):
			self.stud_arrear.append(arr)
	    	arr=self.ui.arrear4_lineEdit.text().toAscii()
	    	if(arr):
	 		self.stud_arrear.append(arr)
	    	arr=self.ui.arrear5_lineEdit.text().toAscii()
	    	if(arr):
			self.stud_arrear.append(arr)
	    	#print self.stud_arrear
	    	#list of student's arrears in self.sutd_arrear 
	    	ins_2_stud_details_command=insert_student_details_template.substitute(usn=self.stud_usn,name=self.stud_name,sem=self.stud_sem,elig=self.stud_elig_stat)
		#ins_2_stud_details_command="insert into student_details values(\""+self.stud_usn+"\",\""+self.stud_name+"\","+self.stud_sem+","+self.stud_elig_stat+");"
            	error,result=stud_db.execute(ins_2_stud_details_command)
		if error==0:			
			for arrear_code in self.stud_arrear:
		        	ins_2_studs_with_arrears_command=insert_student_with_arrears_template.substitute(usn=self.stud_usn,subject_code=arrear_code)
				error,result=stud_db.execute(ins_2_studs_with_arrears_command)
				if error==1:
					break
	            	#print self.stud_elig
			if error==0:
	        	    	msgBox=QMessageBox()
	            		msgBox.information(self, "Addition Message", "Student "+self.stud_name+" has been added to the Database")
				self.clear_AddStudent_texts()
				
class delete_interface(QtGui.QDialog):
        """

        """
       	def __init__(self,parent=None):
         	QtGui.QDialog.__init__(self,parent)
            	self.ui = delete.Ui_Dialog()
            	self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.search_pushButton,QtCore.SIGNAL("clicked()"),self.usn_show)
	def usn_show(self):
	    retrieve_details=retrieve_details_template.substitute(table="student_details",condition="where usn='"+str(self.ui.usn_lineEdit.text())+"'")
	    error,result=stud_db.execute(retrieve_details)
	    iter(result)
	    data="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>TextFixer.com - Table with Images</title>
</head>

<body>

<style type="text/css">
table.imagetable {
	font-family: verdana,arial,sans-serif;
	font-size:11px;
	color:#333333;
	border-width: 1px;
	border-color: #999999;
	border-collapse: collapse;
}
table.imagetable th {
	background:#b5cfd2 url('cell-blue.jpg');
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #999999;
}
table.imagetable td {
	background:#dcddc0 url('cell-grey.jpg');
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #999999;
}
</style>

<table class="imagetable">
<tr>
	<th>USN</th><th>NAME</th><th>ELIGIBLE</th><th>SEMESTER</th>
</tr>
<tr>"""
	    del_file=open("del.html",'w')
	    
	    for i in result:
		data=data+"<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td></tr>"
		
	    data=data+"""</table><!--  The table code can be found here: http://www.textfixer/resources/css-tables.php -->
</body>
</html>"""
	    #self.ui.display_webView.load("file:///del.html")
	    del_file.write(data)
	    webbrowser.open("del.html")		       
class update_interface(QtGui.QDialog):
        """

        """
       	def __init__(self,parent=None):
         	QtGui.QDialog.__init__(self,parent)
            	self.ui = Ui_Dialog()
            	self.ui.setupUi(self)

class Report_Interface(QtGui.QDialog):
        """

        """
       	def __init__(self,parent=None):
         	QtGui.QDialog.__init__(self,parent)
            	self.ui = Ui_FormReport()
            	self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.studentDetails_pushButton,QtCore.SIGNAL("clicked()"),self.show_student_details)
		QtCore.QObject.connect(self.ui.subjects_pushButton,QtCore.SIGNAL("clicked()"),self.show_subjects)
		QtCore.QObject.connect(self.ui.examDates_pushButton,QtCore.SIGNAL("clicked()"),self.show_exam_dates)
		QtCore.QObject.connect(self.ui.labs_pushButton,QtCore.SIGNAL("clicked()"),self.show_labs)
		self.show_student_details()
	def show_exam_dates(self):
		'''populates the viewContents_tableWidget with the exam dates available'''
		self.ui.studentDetails_pushButton.setEnabled(1)
		self.ui.subjects_pushButton.setEnabled(1)
		self.ui.examDates_pushButton.setEnabled(0)
		self.ui.labs_pushButton.setEnabled(1)
		self.ui.viewContentsMain_label.setText("Exam Dates")
		
	def show_labs(self):
		'''populates the viewContents_tableWidget with the labs available'''
		self.ui.studentDetails_pushButton.setEnabled(1)
		self.ui.subjects_pushButton.setEnabled(1)
		self.ui.examDates_pushButton.setEnabled(1)
		self.ui.labs_pushButton.setEnabled(0)
		self.ui.viewContentsMain_label.setText("Labs")
		
	def show_subjects(self):
		'''populates the viewContents_tableWidget with the subjects available to the student'''
		self.ui.studentDetails_pushButton.setEnabled(1)
		self.ui.subjects_pushButton.setEnabled(0)
		self.ui.examDates_pushButton.setEnabled(1)
		self.ui.labs_pushButton.setEnabled(1)
		self.ui.viewContentsMain_label.setText("Subjects")	
	
	def show_student_details(self):
		'''Populates the viewContents_tableWidget with all the student's details\n
		  This method uses while_prevent variable to reinitialise the form to circumvent the clicking show_student_details button twice problem of messing table values
		'''
		print database_name
		self.ui.studentDetails_pushButton.setEnabled(0)
		self.ui.subjects_pushButton.setEnabled(1)
		self.ui.examDates_pushButton.setEnabled(1)
		self.ui.labs_pushButton.setEnabled(1)
		self.ui.viewContentsMain_label.setText("Student's Details")		
		#self.ui.viewContents_tableWidget.clear()
		self.ui.viewContents_tableWidget.setRowCount(0)		
		self.ui.viewContents_tableWidget.setColumnCount(5)		
		self.ui.viewContents_tableWidget.setHorizontalHeaderLabels(["USN", "NAME", "SEMESTER","ELIGIBLE", "ARREARS"])
		retrieve_details=retrieve_details_template.substitute(table="(student_details NATURAL JOIN studs_with_arrears)",condition="")
		#print retrieve_details
		error,result=stud_db.execute(retrieve_details)
		#list=result[0]
		#print result
		self.row,self.column=0,0
		self.ui.viewContents_tableWidget.setRowCount(self.row+1)	
		self.alist=""
		self.prev_row_usn=""
		self.curr_row_usn=""		
		skip_flag=0#the moment self.prev_row_usn==self.curr_row_usn occurs we have to add the arrear to alist so skip till we reach arrear i.e col 4
		iter(result)
		for i in result:			
			for value in i:			
				#the arrears get printed after comparing next row's usn
				#----del from here
				if (self.column==0 and self.row==0):
					#if self.prev_row_usn.=="":
					if self.prev_row_usn=="":
						#print "self.prev_row_usn==\"\""#debug code
						self.curr_row_usn=value
						list=QTableWidgetItem(str(value).upper())
						self.ui.viewContents_tableWidget.setItem(self.row,self.column,list)
						
						self.column=self.column+1
					else :
						self.curr_row_usn=value
						if self.prev_row_usn != self.curr_row_usn:
							#print "self.prev_row_usn != self.curr_row_usn"#debug code							
							list=QTableWidgetItem(str(self.alist).upper())
							self.ui.viewContents_tableWidget.setItem(self.row,4,list)
							self.alist=""
							self.prev_row_usn=""
							self.curr_row_usn=""
							self.row=self.row+1
						if self.prev_row_usn==self.curr_row_usn:
							#print "self.prev_row_usn == self.curr_row_usn"#debug code
							#print self.curr_row_usn
							skip_flag=1
						self.column=self.column+1							
				else:
					if self.column==4:
						skip_flag=0
						#print "skipping @ column 4"
						self.prev_row_usn=self.curr_row_usn
						self.alist=self.alist+" "+str(value)
						#print self.alist#debug code
					else :
						if skip_flag == 1:
							self.column=self.column+1							
						else:
							list=QTableWidgetItem(str(value).upper())
							self.ui.viewContents_tableWidget.setItem(self.row,self.column,list)						
							#----del to here
							self.column=self.column+1				
			self.column=0
			self.ui.viewContents_tableWidget.setRowCount(self.row+1)
			
		#---code snippet for the last record
		list=QTableWidgetItem(str(self.alist).upper())
		self.ui.viewContents_tableWidget.setItem(self.row,4,list)
		self.row=self.row+1
		
		#--code snippet ends
		#The code above only gets students with arrear for students without the code below is used
		self.ui.viewContents_tableWidget.setRowCount(self.row+1)
		retrieve_details=retrieve_details_template.substitute(table="student_details",condition="where usn not in (select usn from (student_details NATURAL JOIN studs_with_arrears))")
		#the previous query eliminates the students already inserted into the table (ie. students with arrears)
		error,result=stud_db.execute(retrieve_details)		
		
		for i in result:			
			for value in i:				
				list=QTableWidgetItem(str(value).upper())
				self.ui.viewContents_tableWidget.setItem(self.row,self.column,list)
				self.column=self.column+1
				
			self.row=self.row+1
			self.column=0
			self.ui.viewContents_tableWidget.setRowCount(self.row+1)
		#self.ui.viewContents_tableWidget.sortByColumn(0,0)#sort table by column 1 ie name in ascending order ie 0
		#sorting the columns screws up the contents the next time we click the show_student_details button
		self.ui.viewContents_tableWidget.setRowCount(self.row)
		self.ui.viewContents_tableWidget.resizeColumnsToContents()

class Main_Interface(QtGui.QTabWidget):
        '''This Class initialises the main window of The Practical Time Table Management Portal
        It has 2 methods
        __init__ as the initializer
        file_dialog has the code to call the file chooser  when Upload button is clicked
        '''
        def __init__(self, parent=None):
        	QtGui.QWidget.__init__(self, parent)
            	self.ui = Ui_TabWidget()
            	self.ui.setupUi(self)
		self.ui.createdB_frame.hide()
		#initialise the select db combo box item		
		for db_name in db_manager.read_list_of_db():#db_manager defined globally
		    self.ui.selectDB_comboBox.addItem(QtCore.QString(db_name[0:-1]))#-1 to remove the trailing \n added while writing
		#end of initialization
            	QtCore.QObject.connect(self.ui.upload_pushButton,QtCore.SIGNAL("clicked()"), self.file_dialog)
            	QtCore.QObject.connect(self.ui.addStudent_pushButton,QtCore.SIGNAL("clicked()"),self.invoke_add_stud_interface)
            	QtCore.QObject.connect(self.ui.view_pushButton,QtCore.SIGNAL("clicked()"),self.invoke_view_interface)
		QtCore.QObject.connect(self.ui.ok_pushButton,QtCore.SIGNAL("clicked()"),self.create_db_interface)
		QtCore.QObject.connect(self.ui.selectdb_pushButton,QtCore.SIGNAL("clicked()"),self.change_db)
		QtCore.QObject.connect(self.ui.deleteStudent_pushButton,QtCore.SIGNAL("clicked()"),self.invoke_delete_interface)
		QtCore.QObject.connect(self.ui.updateStudent_pushButton,QtCore.SIGNAL("clicked()"),self.invoke_update_interface)
	def invoke_update_interface(self):
		view_ui_update=update_interface(self)
		view_ui_update.show()
	def invoke_delete_interface(self):
		view_ui_Del=delete_interface(self)
		view_ui_Del.show()
	def change_db(self):		
		#print self.ui.selectDB_comboBox.currentText()#debug code
		database_name=str(self.ui.selectDB_comboBox.currentText())
		stud_db.close()
		stud_db=practicalDB('DB/'+database_name)
		
		
	def create_db_interface(self):
		#QtGui.QInputDialog.setBaseSize(self,100,100)
		#a=QtGui.QInputDialog.getText(self,"Database","Enter Name of dB to Create:",QtGui.QLineEdit.Normal,"")
		if self.ui.selectDB_comboBox.findText(self.ui.createDB_lineEdit.text()) == -1:
		    QMessageBox.information(self,"Information","Database Created")
		    self.ui.selectDB_comboBox.addItem(QtCore.QString(self.ui.createDB_lineEdit.text()))
		    db_manager.write_to_list_of_db(self.ui.createDB_lineEdit.text())
		    self.ui.createdB_frame.hide()
		else :
		    QMessageBox.critical(self,"ERROR","Database Already Exists !")
        def invoke_view_interface(self):
		view_ui=Report_Interface(self)
		view_ui.show()		
        def invoke_add_stud_interface(self):
            	'''method to invoke the AddStudent_Interface the moment the addstudent_pushButton
            	is clicked.'''
            	a=AddStudent_Interface(self)
            	a.show()		
        def file_dialog(self):
            	'''This method calls the QFileDialog with self as the argument to
            	invoke the File Chooser . If the choosen object is a file then
                it is assigned to the uploadFile_LineEdit widget else its not'''       		
            	a = 0
            	while(not a):
                	fd=QtGui.QFileDialog(self)
                	fname=fd.getOpenFileName()
                	from os.path import isfile
                	a=isfile(fname)
            	if isfile(fname):
                	self.filename=fd
                	self.ui.uploadFile_LineEdit.setText(fname)
