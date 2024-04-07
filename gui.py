import sys
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
        
        vornameLineEdit = QLineEdit()
        nameLineEdit = QLineEdit()
        adresseLineEdit = QLineEdit()
        plzLineEdit = QLineEdit()
        ortLineEdit = QLineEdit()
        
        datumDateEdit = QDateEdit()
        
        landComboBox = QComboBox()
        landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
        
        button = QPushButton("Speichern")
        
        # Layout füllen:
        layout.addRow("Vorname:", vornameLineEdit)
        layout.addRow("Name:", nameLineEdit)
        layout.addRow("Geburtsdatum:", datumDateEdit)
        layout.addRow("Adresse:", adresseLineEdit)
        layout.addRow("Postleitzahl:", plzLineEdit)
        layout.addRow("Ort:", ortLineEdit)
        layout.addRow("Land:", landComboBox)
        layout.addRow(button)

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
    
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()