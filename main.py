import sys, os, pathlib
import configparser
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Slot
from uiloader import loadUi


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('mainwindow.ui', self)

    @Slot()
    def load_playbook_clicked(self):
        print("load_playbook_clicked")
        filename = self.get_file("txtInventoryFile")
        self.txt_playbook_file.setText(filename)

    @Slot()
    def load_inventory_clicked(self):
        print("load_inventory_clicked")
        filename = self.get_file("txtPlaybookFile")
        self.txt_inventory_file.setText(filename)

    def get_file(self, caller):
        homedir = pathlib.Path.home()
        print(caller)
        filename = QFileDialog.getOpenFileName(self, "Select Ansible file", str(homedir), "Ansible files (*.yml)")
        print(filename)
        return filename[0]

if __name__ == "__main__":


#     app = QApplication(sys.argv)
#     file = QFile("mainwindow.ui")
#     file.open(QFile.ReadOnly)
#     loader = QUiLoader()
#     window = loader.load(file)
#     window.btn_load_inventory.clicked.connect(load_playbook_clicked)
#     window.show()
#     sys.exit(app.exec_())

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())