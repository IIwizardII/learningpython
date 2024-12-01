import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout,
                            QGridLayout, QPushButton,
                            QCheckBox, QRadioButton,
                            QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")
        self.setGeometry(500, 250, 500, 500)
        self.setWindowIcon(QIcon("icon.jpg"))
        
        # label = QLabel("Bonjour", self)
        
        # label.setFont(QFont("helvetica", 18))
        # label.setGeometry(0, 0, 500, 50)
        # label.setStyleSheet("color: blue;"
        #                     "background-color: lightblue;")
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # adding image
        # label = QLabel(self)
        # label.setGeometry(0, 0, 500, 500)
        # pixmap = QPixmap("icon.jpg")
        # label.setPixmap(pixmap)
        # label.setScaledContents(True)
        
        # self.button = QPushButton("Click", self)
        # self.label = QLabel("hi", self)
        
        # self.checkbox = QCheckBox("hi", self)
        
        # self.radio1 = QRadioButton("visa", self)
        # self.radio2 = QRadioButton("mastard", self)
        # self.radio3 = QRadioButton("bkash", self)
        # self.radio4 = QRadioButton("store", self)
        # self.radio5 = QRadioButton("online", self)
        
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)
        
        # self.line_edit = QLineEdit(self)
        # self.button = QPushButton("submit", self)
        
        
        self.button = QPushButton("hi", self)
        
        
        self.initUI()
        
    def initUI(self):
        # certral_widget = QWidget()
        # self.setCentralWidget(certral_widget)
            
        # label1 = QLabel("1", self)
        # label2 = QLabel("2", self)
        # label3 = QLabel("3", self)
        
        # label1.setStyleSheet("background-color: red;")
        # label2.setStyleSheet("background-color: blue;")
        # label3.setStyleSheet("background-color: green;")
        
        # vBox = QVBoxLayout()
        
        # vBox.addWidget(label1)
        # vBox.addWidget(label2)
        # vBox.addWidget(label3)
        
        # certral_widget.setLayout(vBox)
        
        # self.button.clicked.connect(self.on_click)
        # self.button.setGeometry(100, 100, 100, 100)
        
        # self.checkbox.stateChanged.connect(self.check_changed)
        
        # self.radio1.setGeometry(0, 0, 300, 50)
        # self.radio2.setGeometry(0, 50, 300, 50)
        # self.radio3.setGeometry(0, 100, 300, 50)
        # self.radio4.setGeometry(0, 150, 300, 50)
        # self.radio5.setGeometry(0, 200, 300, 50)
        
        # self.button_group1.addButton(self.radio1)
        # self.button_group1.addButton(self.radio2)
        # self.button_group1.addButton(self.radio3)
        
        # self.button_group2.addButton(self.radio4)
        # self.button_group2.addButton(self.radio5)
        
        
        
        
        # self.setStyleSheet("QRadioButton{"
        #                     "font-size: 40px;"
        #                 "}")
        
        
        # self.radio1.toggled.connect(self.radio_button_changed)
        # self.radio2.toggled.connect(self.radio_button_changed)
        # self.radio3.toggled.connect(self.radio_button_changed)
        # self.radio4.toggled.connect(self.radio_button_changed)
        # self.radio5.toggled.connect(self.radio_button_changed)
        
        
        
        # self.line_edit.setGeometry(100, 0, 300, 50)
        # self.line_edit.setPlaceholderText("type")
        
        # self.button.clicked.connect(self.submit)
        
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button)
        
        central_widget.setLayout(hbox)
        
        self.button.setObjectName("button")
        
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
            }
            QPushButton#button:hover{
                background-color:blue
            }
        """)
        
        
    # def on_click(self):
    #     self.label.setText("bye")
    
    
    # def check_changed(self, state):
    #     if state == Qt.Checked:
    #         print("checked!")
    #     else:
    #         print("unchecked!")
            
    
    # def radio_button_changed(self):
    #     radio_button = self.sender()
    #     if radio_button.isChecked():
    #         print(radio_button.text())
    
    # def submit(self):
    #     text = self.line_edit.text()
    #     print(text)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()