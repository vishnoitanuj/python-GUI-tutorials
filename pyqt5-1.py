from PyQt5.QtWidgets import QApplication, QLabel

#This is a requirement of Qt: Every GUI app must have exactly one instance of QApplication
app = QApplication([]) #[] here are parameters to be passed
label = QLabel('Hello World!')
label.show()
app.exec_()