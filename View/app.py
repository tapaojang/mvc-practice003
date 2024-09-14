import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QLineEdit, QPushButton
from Controller.milkProduced import cowMilkProduced
from Controller.milkProduced import totalMilk
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cow Strike")
        self.setGeometry(100, 200, 500, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Enter your id : ')
        self.layout.addWidget(self.label)

        self.idInput = QLineEdit()
        self.layout.addWidget(self.idInput)
        self.idInput.setStyleSheet("padding: 10px;")

        self.totalMilk = QLabel()
        self.layout.addWidget(self.totalMilk)

        self.submitButton = QPushButton('Enter')
        self.layout.addWidget(self.submitButton)
        self.submitButton.setStyleSheet("padding: 12px;")
        self.submitButton.clicked.connect(self.submitButtonClicked) 
        
        self.setLayout(self.layout)


    def submitButtonClicked(self):
        cowId = self.idInput.text()
        if cowId and cowId[0] != '0'and len(cowId) == 8:
            liter = cowMilkProduced(cowId)
            self.label.setText(f'Your cow can produce milk : {liter} ')
        else:
            self.label.setText('Invalid id')

        total = totalMilk()
        self.totalMilk.setText(f'Total milk produced by all cows : {total}')
        self.idInput.clear()

