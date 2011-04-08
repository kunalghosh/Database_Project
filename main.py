import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import UI_classes



if __name__ == "__main__":
    '''This is the main function of the Practical Time Table Management
    Portal.
    This Portal uses Sqlite3 as its backend Database and PyQt4 to 
    design its frontend
    '''
    app = QApplication(sys.argv)
    myapp = UI_classes.Main_Interface()
    myapp.show()    
    sys.exit(app.exec_())
