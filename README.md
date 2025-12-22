# Private Notebook
<p align="justify">
This is a desktop notebook application built using <b>Python</b>, <b>PyQt5</b>, and <b>SQLite</b>. It allows users to generate strong passwords, log in securely, and store personal notes locally on their system.
<br><br>
This application creates a <b>separate database record for each unique username and password combination</b>, ensuring that every user has an isolated and private note space. All changes made to the notes are <b>automatically saved</b> to the local SQLite database in real time, without requiring any manual save action.
<br><br>
Each time a user logs in with the same credentials, their previously stored notes are loaded instantly. If a new username or password is used, a new record is created automatically in the database.
<br><br>
This project demonstrates GUI development, multi-window application design, and local database integration in Python, with a strong focus on privacy, simplicity, and offline usability.
</p>


---

##  Features

-  Secure login using **username and password**
-  Built-in **random password generator**
-  **Private notes** for each unique user
-  Automatic note saving using **SQLite**
-  One-click **copy password** to clipboard
- Clear notes instantly
- **Multi-window application** with separate login and notebook interfaces

---

##  Application Demo

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/120c3940-0ffc-4846-8cb6-ebd15f216198"
    width="450"
    alt="Password Generator Demo"
  />
</p>

---

##  Project Structure

```
PrivateNotebook/
├── UI Files/
│   ├── login.ui
│   └── notes.ui
├── Python_File/
│   ├── firstWindow.py
│   └── secondWindow.py
├── icon/
├── notes.db
├── main.py
├── .gitignore
└── README.md
```

---

##  Quick Start

#### 1. Clone the Repository
```bash
https://github.com/soodeh-hp/Private-Notebook.git
cd Private-Notebook
```


#### 2. Install Dependencies
```bash
pip install PyQt5
```

---

#### 3. Run the Application
```bash
python main.py
```

---

##  Technologies Used

- Python 3 – Application logic
- PyQt5 – GUI and event handling
- Qt Designer – UI design
- SQLite – Local data storage


---

If you enjoyed this project, don’t forget to give it a star ⭐ and follow for more projects ✌️😊
