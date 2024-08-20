import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QVBoxLayout,QHBoxLayout,QSpinBox,QLineEdit,QComboBox,QTableWidget,QTableWidgetItem,QPushButton,QMessageBox)


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(-999,999)
        
        self.lineEdit = QLineEdit(self)
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(['Option1', 'Option2', 'Option3'])
        
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['SpinBox', 'ComboBox', 'LineEdit'])
        
        self.addButton = QPushButton('Add',self)
        
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()        
        
        hbox.addWidget(self.spinBox)
        hbox.addWidget(self.comboBox)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.addButton)
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.tableWidget)
        
        self.setLayout(vbox)
        
        self.addButton.clicked.connect(self.addRecord)
        
        
    def addRecord(self):
        if not self.lineEdit.text():
            QMessageBox.warning(self, 'LineEdit cant be empty')
            return
        
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(self.spinBox.value())))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.comboBox.currentText()))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(self.lineEdit.text()))
        self.tableWidget.itemSelectionChanged.connect(self.loadSelectedRow)
        
    
    def loadSelectedRow(self):
        selectedRow = self.tableWidget.currentRow()
        self.spinBox.setValue(int(self.tableWidget.item(selectedRow, 0).text()))
        self.comboBox.setCurrentText(self.tableWidget.item(selectedRow, 1).text())
        self.lineEdit.setText(self.tableWidget.item(selectedRow, 2).text())
        
        
        
    
    
if  __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
    