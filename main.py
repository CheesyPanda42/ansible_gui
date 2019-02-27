import sys
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, Slot



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('mainwindow.ui', self)

def load_playbook_clicked():
    print("load_playbook_clicked")
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    file = QFile("mainwindow.ui")
    file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(file)
    window.btn_load_inventory.clicked.connect(load_playbook_clicked)
    window.show()
    sys.exit(app.exec_())