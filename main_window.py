from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton,QSpinBox, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QButtonGroup,QGroupBox

card_width, card_height=600,500
app=QApplication([])
win_card= QWidget()
win_card.rasize(card_width,card_height)
win_card.move(300,300)
win_card.setWindowTitle("Memory Card")

btn_Sleep = QPushButton("Відпочити")
box_Minutes=QSpinBox()
box_Minutes.setValue(30)

window=QWidget()

btn_menu=QPushButton("Меню")
btn_rest=QPushButton("Відпочити")
btn_nex=QPushButton("Відповисти")
sp_rest=QSpinBox()

RadioGroupBox=QGroupBox("Варіант відповідей")

RadioGroup=QButtonGroup()

rbtn_ans1=QRadioButton("1")
rbtn_ans2=QRadioButton("2")
rbtn_ans3=QRadioButton("3")
rbtn_ans4=QRadioButton("4")

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_ans1)
layout_ans2.addWidget(rbtn_ans2)
layout_ans3.addWidget(rbtn_ans3)
layout_ans3.addWidget(rbtn_ans4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

win_card.show()
