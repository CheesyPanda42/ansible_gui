import sys, os, pathlib
import configparser
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Slot
from uiloader import loadUi
import yaml


class MainWindow(QMainWindow):

    def __init__(self, parent=None, options=None):
        print(options)
        self._options = options
        QMainWindow.__init__(self, parent)
        loadUi('mainwindow.ui', self)

    @Slot()
    def load_playbook_clicked(self):
        print(self._options)
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

def loadConfig(configfile):
    config = yaml.load(open(configfile, 'r'))
    print(config)
    return



if __name__ == "__main__":
    if len(sys.argv) > 1:
        configFilePath = pathlib.Path(sys.argv[1]).resolve()
        print (configFilePath)
    else:
        configFilePath = pathlib.Path('./config.yml').resolve()

    loadConfig(configFilePath)


    app = QApplication(sys.argv)
    window = MainWindow(options=configFilePath)
    window.show()
    sys.exit(app.exec_())