from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
import sqlite3


class SecondWindow(QMainWindow):
    def __init__(self, password,username):
        super(SecondWindow, self).__init__()

        # define ui file
        uic.loadUi('UI Files/notes.ui', self)

        # define our widget
        self.password = password
        self.username = username
        self.name_label = self.findChild(QLabel, 'name_label')
        self.textEdit = self.findChild(QTextEdit, 'textEdit')
        self.Done_pushButton = self.findChild(QPushButton, 'Done_pushButton')
        self.Clear_pushButton = self.findChild(QPushButton, 'Clear_pushButton')


        # connect buttons to their function
        self.load_content()
        self.textEdit.textChanged.connect(self.save_content)
        self.Done_pushButton.clicked.connect(self.done)
        self.Clear_pushButton.clicked.connect(self.clear)




    def load_content(self):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT content FROM notes WHERE password = ? AND username = ? ',
                           (self.password,self.username))
            result = cursor.fetchone()
            if result:
                self.textEdit.setPlainText(result[0])

            else:
                self.textEdit.setPlainText('')

        self.name_label.setText(self.username)




    def save_content(self):
        content = self.textEdit.toPlainText()
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute('REPLACE INTO notes (username,password, content) VALUES (?,?,?)',
                           (self.username,self.password, content))
            conn.commit()




    def done(self):
        self.close()




    def clear(self):
        self.textEdit.setPlainText("")