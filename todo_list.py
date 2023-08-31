from PyQt5 import QtCore as Qt
import PyQt5.QtWidgets as qtw
from todo_design import Ui_MainWindow

tasks = [" "]
class MainWindow (qtw.QMainWindow, Ui_MainWindow):
    def _init_(self):
        super()._init_()
        self.setupUi(self)
        self.add.clicked.connect(self.add_tasks)
        self.search.clicked.connect(self.search_tasks)
        self.delete_2.clicked.connect(self.delete_task)
        self.delete_all.clicked.connect(self.delete_task)        
        self.sort_deadline.clicked.connect(self.sort_tasks)
        self.sort_name.clicked.connect(self.sort_tasks)

    def add_tasks(self):
        for i in range(1):
            item=qtw.QListWidgetItem(qtw.QCheckBox(qtw.QListWidgetItem))
            item.setText(self.lineEdit.text())
            
    def search_tasks(self):
        item = self.lineEdit_2.text()
        self.item = qtw.QListWidgetItem(item)
        self.item.setFlags(self.item.flags() , Qt.ItemIsUserCheckable)
        self.item.setCheckState(Qt.Unchecked)
        for i in range(len(tasks)):
            if tasks[i] == item:
                self.listWidget.clear()
                self.listWidget.addItem(self.item)

    def sort_tasks(self):
        self.listWidget.sortItems()

    def delete_task(self):
        sel_row = self.listWidget.currentRow()
        if sel_row >= 0:
            item = self.listWidget.takeItem(sel_row)
            del item
    def delete_all_tasks(self):
        pass        

app = qtw.QApplication([])
window = MainWindow()
window.show()
app.exec()