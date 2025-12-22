import sys
from PyQt5.QtWidgets import QApplication
from Python_File.firstWindow import UI, init_db




if __name__ == "__main__":

    init_db()      # make database
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())

