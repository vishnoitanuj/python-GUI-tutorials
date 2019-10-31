#Qt uses a mechanism called signals to let you react to events such as the user clicking a button.
from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Click')
def on_button_click():
    alert = QMessageBox();
    alert.setText('You have clicked the button')
    alert.exec_()

button.clicked.connect(on_button_click)
button.show()
app.exec_()


'''
The interesting line is button.clicked is a signal, 
.connect(...) lets us install a so-called slot on it. 
This is simply a function that gets called when the signal occurs. 
In the above example, our slot shows a message box.
'''