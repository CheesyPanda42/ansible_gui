import sys, os
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, Slot
from uiloader import loadUi


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('mainwindow.ui', self)

    @Slot(bool)
    def on_clickMe_clicked(self, is_checked):
        if is_checked:
            message = self.trUtf8(b'I am checked now.')
        else:
            message = self.trUtf8(b'I am unchecked now.')
        QMessageBox.information(self, self.trUtf8(b'You clicked me'), message)

    @Slot()
    def load_playbook_clicked(self):
        print("load_playbook_clicked")

    @Slot()
    def load_inventory_clicked(self):
        print("load_inventory_clicked")

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