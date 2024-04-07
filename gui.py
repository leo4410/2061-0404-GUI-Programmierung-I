import sys
import csv
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # window title
        self.setWindowTitle("GUI-Programmierung")
        
        
        # menu bar
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)
        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" (für MacOS)

        filemenu.addAction(save)
        filemenu.addAction(quit)
        
        
        # form fields
        layout = QFormLayout()
        
        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        
        self.datumDateEdit = QDateEdit()
        
        self.landComboBox = QComboBox()
        self.landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
        
        self.button = QPushButton("Speichern")
        self.button.clicked.connect(self.write_file)
        
        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtsdatum:", self.datumDateEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landComboBox)
        layout.addRow(self.button)
        
    

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()
        
        
    # menu bar functions    
    def menu_save(self):
        print("Menu Save wurde gewählt...")

    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()  
        
    # form functions
    def write_file(self):
        print(self.vornameLineEdit.text())
        print(self.nameLineEdit.text())
        print(self.datumDateEdit.text())
        print(self.adresseLineEdit.text())
        print(self.plzLineEdit.text())
        print(self.ortLineEdit.text())
        print(self.landComboBox.currentText())
        
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()