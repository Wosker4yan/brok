#!/usr/bin/python
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class my_tableview(QWidget):
	row_table = []
	def __init__(self, xmax, ymax, *args):
                QWidget.__init__(self, *args)
                self.resize(xmax, ymax)
	def create_table(self, l):
		j = 0
		for i in self.row_table:
			j += 1
			if len(i) != len(l) :
				self.show_dialog(self)
				sys.exit()
				return 
	        
		tablemodel = my_tablemodel(self.row_table, self)
		tablemodel.set_header(l)
        	tableview = QTableView()
                tableview.setModel(tablemodel)
               	font = QFont("Cyrillic", 12, 6, True)
		tableview.setFont(font)	
		layout = QVBoxLayout(self)
                layout.addWidget(tableview)
                self.setLayout(layout)
		tableview.setWindowTitle("QTableView Detect Double Click")
		QObject.connect(tableview,SIGNAL("doubleClicked(QModelIndex)"),
                        self,SLOT("ItemDoubleClicked(QModelIndex)")) 
		
	def show_dialog(self, d):
   		msg = QMessageBox()
  		msg.setIcon(QMessageBox.Critical)
		msg.setText("Error:")
   		msg.setInformativeText("Error: Length of table dont match with row.")
   		msg.setWindowTitle("MessageBox demo")
   		msg.setStandardButtons(QMessageBox.Ok)
   		msg.buttonClicked.connect(self.msg_button)
		retval = msg.exec_()
	 
	def msg_button(self, c):
   		print "Button pressed is:", c.text()
	
	def add_row(self, t) :
		self.row_table.append(t)
		
	@pyqtSlot("QModelIndex")
        def ItemDoubleClicked(self,index):
                print index.data().toString()
                ind = str(index.row()) + str(index.column())
                print ind
		r = str(index.row())
		#c = str(index.column())
		dir = "/home/gagik/Desktop/" + ind + "/*.jpg"
            	filter = " File (*.*)"
		picfile = QFileDialog.getOpenFileName(self, "Pictures File", dir, filter)
		print dir, ' , ' , picfile
		if "" != picfile:
			os.system('eog' + str(picfile))
		
class my_tablemodel(QAbstractTableModel):
        
	def __init__(self, datain, parent=None, *args):
               	QAbstractTableModel.__init__(self, parent, *args)
		self.arraydata = datain
        	
	def headerData(self, section, orientation, role=Qt.DisplayRole):
        	if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            		return self.colLabels[section]
		return QAbstractTableModel.headerData (self, section, orientation, role)
	
	def rowCount(self, parent):
                return len(self.arraydata)
        
	def columnCount(self, parent):
                return len(self.colLabels)

        def set_header(self,l):
       	        self.colLabels = l

        def data(self, index, role):
                if not index.isValid():
                       	return QVariant()
               	elif role != Qt.DisplayRole:
                       	return QVariant()
		return QVariant(self.arraydata[index.row()][index.column()]) 
	
def main():
	app = QApplication(sys.argv)
	w = my_tableview(500, 600)
	l = ['dd','ff','aa','cc']
	# = [00,01,02,'nkar']
	t = [01,02,03,'nkar']
	w.add_row(t)
	w.add_row(t)
	w.create_table(l)
	w.show()
	sys.exit(app.exec_())
	
if __name__=='__main__':
	main()
