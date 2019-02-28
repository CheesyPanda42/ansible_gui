import sys, os, pathlib
import configparser
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidget, QTreeWidgetItem
from PySide2.QtCore import QFile, Slot
from uiloader import loadUi
import yaml


class MainWindow(QMainWindow):

    def __init__(self, parent=None, options=None):
        print(options)
        self._options = options
        QMainWindow.__init__(self, parent)
        loadUi('mainwindow.ui', self)
    
    def get_file(self, defaultPath):
        filename = QFileDialog.getOpenFileName(self, "Select Ansible file", str(pathlib.Path(defaultPath).resolve()), "Ansible files (*.yml)")
        print(filename)
        return filename[0]

    def load_yml_file(self, filepath):
        return yaml.load(open(filepath, 'r'))


    def insertItemsIntoTree(self, item, tree):
        for i in item:
            print(i)
            subitem = QTreeWidgetItem(tree)
            subitem.setText(0, i)
            if type(item[i]) == dict:
                print(item[i])
                self.insertItemsIntoTree(item[i], subitem)
            # else:
            #     self.insertItemsIntoTree(item[i], tree)
        return

    def insertItemIntoTreeTopLevel(self, value, tree):
        item = QTreeWidgetItem(tree)
        item.setText(0, value)
        tree.insertTopLevelItem(0, item)
        return item

    def populateTree(self, treeData):
        items = []
        tree = self.tree_playbook_breakdown
        print(treeData)
        for key in list(treeData.keys()):
            subtree = self.insertItemIntoTreeTopLevel(key, tree)
            self.insertItemsIntoTree(treeData[key], subtree)





        # QTreeWidgetItem()
        # for i in range(10):
        #     items.append(QTreeWidgetItem(tree, str(i)))
        #     sub_item = []
        #     for j in range(10):
        #         sub_item.append(QTreeWidgetItem(items[i], str(j)))
        #
        #self.tree_playbook_breakdown.insertTopLevelItems(0, items)


################################################
# Slots
################################################
    @Slot()
    def load_inventory_clicked(self):
        print("load_inventory_clicked")
        filename = self.get_file(self._options['ansible_default_paths']['inventory'])
        self.txt_inventory_file.setText(filename)
        inventory_data = self.load_yml_file(filename)
        self.populateTree(inventory_data)

    @Slot()
    def load_playbook_clicked(self):
        print("load_playbook_clicked")
        filename = self.get_file(self._options['ansible_default_paths']['playbook'])
        self.txt_playbook_file.setText(filename)

    
############################################################################################################
############################################################################################################

def loadConfig(configfile):
    config = yaml.load(open(configfile, 'r'))
    return config


if __name__ == "__main__":
    if len(sys.argv) > 1:
        configFilePath = pathlib.Path(sys.argv[1]).resolve()
        print (configFilePath)
    else:
        configFilePath = pathlib.Path('./config.yml').resolve()

    config = loadConfig(configFilePath)

    app = QApplication(sys.argv)
    window = MainWindow(options=config)
    window.show()
    sys.exit(app.exec_())