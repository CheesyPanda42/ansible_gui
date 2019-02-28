import sys, os, pathlib
 
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
        self.get_file()

    @Slot()
    def load_inventory_clicked(self):
        print("load_inventory_clicked")
        self.get_file()

    def get_file(self):
        homedir = pathlib.Path.home()
        filename = QFileDialog.getOpenFileName(self, "Select Ansible file", str(homedir), "Ansible files (*.yml)")
        print(filename)

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