
from PyQt5.QtWidgets import  QMainWindow, QLabel, QPushButton,  QLineEdit, QApplication

from PyQt5 import uic
import random
import string
import sqlite3

from Python_File.secondWindow import SecondWindow




#create a database 
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
        username TEXT,
        password TEXT ,
        content TEXT ,
        PRIMARY KEY (username, password)
        )
        ''')
    conn.commit()
    conn.close()




class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi('UI Files/login.ui',self)

        # define our widgets
        self.window2 = None
        self.username_label = self.findChild(QLabel, 'username_label')
        self.password_label = self.findChild(QLabel, 'password_label')
        self.generator_label = self.findChild(QLabel, 'generator_label')
        self.username_lineEdit = self.findChild(QLineEdit, 'username_lineEdit')
        self.password_lineEdit = self.findChild(QLineEdit, 'password_lineEdit')
        self.generator_lineEdit = self.findChild(QLineEdit, 'generator_lineEdit')
        self.login_pushButton = self.findChild(QPushButton, 'login_pushButton')
        self.copy_pushButton = self.findChild(QPushButton, 'copy_pushButton')
        self.redo_pushButton = self.findChild(QPushButton, 'redo_pushButton')


        # connect buttons to their function
        self.login_pushButton.clicked.connect(self.login)
        self.copy_pushButton.clicked.connect(self.copy)
        self.redo_pushButton.clicked.connect(self.redo)


        self.redo()     #set redo bt default
        self.show()     #show app




    def login(self):
        password = self.password_lineEdit.text()
        username = self.username_lineEdit.text()
        if password and username:
            self.window2 = SecondWindow(password,username)
            self.window2.show()





    def copy(self):
        text = self.generator_lineEdit.text()
        QApplication.clipboard().setText(text)




    def redo(self):
        char = string.ascii_letters + string.digits + string.punctuation
        random_password = ''.join(random.choices(char, k= 20))
        self.generator_lineEdit.setText(random_password)

