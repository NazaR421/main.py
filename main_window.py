from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton,QSpinBox, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QButtonGroup,QGroupBox


card_width,card_height=600,500
win_card=QWidget()
win_card.resize(card_width,card_height)
win_card.move(300,300)
win_card.setWindowTitle("Memory Card")




btn_menu=QPushButton("Меню")
btn_rest=QPushButton("Відпочити")
btn_next=QPushButton("Відповісти")
box_Minutes=QSpinBox()
box_Minutes.setValue(30)




RadioGroupBox=QGroupBox("Варіанти відповідей")

lb_Result=QLabel("")
lb_Correct=QLabel("")

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

layout_ans4=QVBoxLayout()
layout_ans5=QHBoxLayout()
layout_ans6=QHBoxLayout()
layout_ans7=QHBoxLayout()
layout_ans8=QHBoxLayout()

layout_ans5.addWidget(btn_menu)
layout_ans5.addStretch(1)
layout_ans5.addWidget(btn_rest)
layout_ans5.addWidget(box_Minutes)

layout_ans6.addWidget(lb_Result,alignment=(Qt.AlignmentFlag.AlignCenter))

layout_ans7.addWidget(RadioGroupBox)

layout_ans8.addStretch(1)
layout_ans8.addWidget(btn_next,stretch=2)
layout_ans8.addStretch(1)

layout_ans4.addLayout(layout_ans5, stretch=1)
layout_ans4.addLayout(layout_ans6,stretch=2)
layout_ans4.addLayout(layout_ans7,stretch=1)
layout_ans4.addLayout(layout_ans8,stretch=2)



win_card.show()
