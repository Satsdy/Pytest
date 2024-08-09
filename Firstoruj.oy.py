from PyQt5.QtCore import *
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()

win.resize(1000,900)

win.setWindowTitle('Test')
 
win_style="background-color:gray"
win.setStyleSheet(win_style)
win.move(500,500)
win.show()

app.exec_()
                