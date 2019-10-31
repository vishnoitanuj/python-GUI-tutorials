#The coarsest way to change the appearance of your application is to set the global Style.
#Everything you see in a (Py)Qt app is a widget: Buttons, labels, windows, dialogs, progress bars etc.
from PyQt5.QtWidgets import *
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()