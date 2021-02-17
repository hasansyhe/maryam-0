# import pyqt5 library and all classes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# import sys
import sys

# Author Hasan Mohammed AL-Shikh
# GUI : like SOFTWARE box {interface}
# yout can share this code with ur friends {}
# thanks for MARYAM and AMAL and SHAHD .....!

# app
app = QApplication(sys.argv)

# CREATE MY WINDOW
root = QWidget()
# SET TITLE WINDOW
root.setWindowTitle("Programmer")
# CREATE {MAIN LAYOUT}
bodyLayout = QVBoxLayout()
# SET {MAIN LAYOUT} INSIDE MY WINDOW
root.setLayout(bodyLayout)
#root.resize(900,600)

# CREATE THREE LAYOUT INSIDE {MAIN LAYOUT}
one = QHBoxLayout() # 1 layout
two = QHBoxLayout() # 2 layout
three = QHBoxLayout() # 3 layout
#----------------------------------#

# ADD ABOV LAYOUTs INSIDE {MAIN LAYOUT}
bodyLayout.addLayout(one)
bodyLayout.addLayout(two)
bodyLayout.addLayout(three)
#-----------------------------------#

# CREATE LOGO LABEL
logo = QLabel("LOGO : MARYAM FREE PROJECTS")
# ADD LOGO LABEL INSIDE 1 layout
one.addWidget(logo)
# end

# CREATE TO LAYOUT INSIDE 2 layout {one for Buttons and one for ComboBox and Logs}
sideone = QVBoxLayout() # this layout for buttons and tabs
sideTwo = QVBoxLayout() # this layout for combobox and logs {plaintextedit}
two.addLayout(sideone) # add layout to 2 layout
two.addLayout(sideTwo) # add layout to 2 layout

# I ADD THIS LAYOUT CUZ I WANT TO CREATE TWO {QGroupBox inside it}
actionAll = QHBoxLayout()
sideone.addLayout(actionAll) # ADD THS TO {buttons & tabs layout}

actionBox1 = QGroupBox("Action") # groupbox one for buttons
actionBox2 = QGroupBox("Action") # groupbox two for buttons

action_layoutone = QVBoxLayout() # create layout to add it to groupbox 1
action_layouttwo = QVBoxLayout() # create layout to add it to groupbox 2

actionBox1.setLayout(action_layoutone) # add layout to groupbox 1
actionBox2.setLayout(action_layouttwo) # add layout to groupbox 2

actionAll.addWidget(actionBox1) # add groupbox 1 to {actionAll} layout
actionAll.addWidget(actionBox2) # add groupbox 2 to {actionAll} layout

# left side {buttons}
but1 = QPushButton("text")
but1.setStyleSheet("width:100px;")
but2 = QPushButton("text")
but2.setStyleSheet("width:100px;")
but3 = QPushButton("text")
but3.setStyleSheet("width:100px;")
but4 = QPushButton("text")
but4.setStyleSheet("width:100px;")
but5 = QPushButton("text")
but5.setStyleSheet("width:100px;")
# add buttons to layout inside groupbox 1
action_layoutone.addWidget(but1)
action_layoutone.addWidget(but2)
action_layoutone.addWidget(but3)
action_layoutone.addWidget(but4)
action_layoutone.addWidget(but5)
# end

# right side {buttons}
but6 = QPushButton("text")
but6.setStyleSheet("width:100px;")
but7 = QPushButton("text")
but7.setStyleSheet("width:100px;")
but8 = QPushButton("text")
but8.setStyleSheet("width:100px;")
but9 = QPushButton("text")
but9.setStyleSheet("width:100px;")
but0 = QPushButton("text")
but0.setStyleSheet("width:100px;")
# add buttons to layout inside groupbox 2
action_layouttwo.addWidget(but6)
action_layouttwo.addWidget(but7)
action_layouttwo.addWidget(but8)
action_layouttwo.addWidget(but9)
action_layouttwo.addWidget(but0)
# end

# ceate TABS
notebook = QTabWidget()
tab1 = QWidget() # widget of tab1
tab2 = QWidget() # widget of tab2
tab3 = QWidget() # widget of tab3
tab4 = QWidget() # widget of tab4
notebook.addTab(tab1, "tab1") # add tab to notebook
notebook.addTab(tab2, "tab2") # add tab to notebook
notebook.addTab(tab3, "tab3") # add tab to notebook
notebook.addTab(tab4, "tab4") # add tab to notebook
# add notebook to {sideone} layout
sideone.addWidget(notebook)
# end

# create layout for combobox and logs
logLayout = QVBoxLayout()
# add this layout to {two} 3 layout
two.addLayout(logLayout)

# create groupbox for two combox {adb,com}
port = QGroupBox("Port") # create gbox
logLayout.addWidget(port) # add .....

portlayout = QVBoxLayout() # create layout inside port {groupbox}
port.setLayout(portlayout) # add to

cobmo1 = QComboBox() # combobox 1
cobmo1.addItem("COM")
cobmo2 = QComboBox() # combobox 2
cobmo2.addItem("ADB")

portlayout.addWidget(cobmo1) # add combobox 1 to layout inside port {groupbox}
portlayout.addWidget(cobmo2) # add combobox 2 to layout inside port {groupbox}

# create area for logs using plaintextedit widget
log = QPlainTextEdit()
# resize area
log.setStyleSheet("width:270px;height:200px;")
# add to
logLayout.addWidget(log)


# ----- HERE YOU CAN FIND TWO LAYOUT FOR TWO BUTTONS AND ONE PROGRESSBAR ------#
butBar = QHBoxLayout() # 1 LAYOUT
lineBar = QHBoxLayout() # 2 LAYOUT
three.addLayout(butBar) # ADD
three.addLayout(lineBar) # ADD

butBar1 = QPushButton("text") # BUTTON
butBar2 = QPushButton("text") # BUTTON

butBar.addWidget(butBar1) # ADD
butBar.addWidget(butBar2) # ADD

progress = QProgressBar() # PROGRESSBAR
lineBar.addWidget(progress) # ADD

#----------------------------
# show MY WINDOW
root.show()


sys.exit(app.exec_())
