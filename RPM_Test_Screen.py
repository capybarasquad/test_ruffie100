#Library Imports for App / LIA
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from RPM_Test_Settings import *

#Small Settings / SS
app = QApplication([])
window = QWidget()
window.resize(1000, 800)
window.setWindowTitle("Здоровья")

#Main Script / MS
lb_text = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
lb_text2 = QLabel("Бла бла бла много тексту")
lb_QPushbutton = QPushButton("Почати!")

v_main = QVBoxLayout()
v_main.addWidget(lb_text, alignment=Qt.AlignmentFlag.AlignCenter)
v_main2 = QVBoxLayout()
v_main2.addWidget(lb_text2, alignment=Qt.AlignmentFlag.AlignCenter)
v_main3 = QVBoxLayout()
v_main3.addWidget(lb_QPushbutton, alignment=Qt.AlignmentFlag.AlignBottom)
v_main.addLayout(v_main2)
v_main.addLayout(v_main3)

#Small Settings / SS
window.setLayout(v_main)
window.show()
app.exec()