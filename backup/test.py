# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(936, 723)
        Test.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 398, 256))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Companies = QtWidgets.QFrame(self.widget)
        self.Companies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Companies.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Companies.setObjectName("Companies")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Companies)
        self.verticalLayout.setObjectName("verticalLayout")
        self.C1 = QtWidgets.QComboBox(self.Companies)
        self.C1.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C1.setObjectName("C1")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.C1.addItem("")
        self.verticalLayout.addWidget(self.C1)
        self.C2 = QtWidgets.QComboBox(self.Companies)
        self.C2.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C2.setObjectName("C2")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.C2.addItem("")
        self.verticalLayout.addWidget(self.C2)
        self.C3 = QtWidgets.QComboBox(self.Companies)
        self.C3.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C3.setObjectName("C3")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.C3.addItem("")
        self.verticalLayout.addWidget(self.C3)
        self.C4 = QtWidgets.QComboBox(self.Companies)
        self.C4.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C4.setObjectName("C4")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.C4.addItem("")
        self.verticalLayout.addWidget(self.C4)
        self.C5 = QtWidgets.QComboBox(self.Companies)
        self.C5.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C5.setObjectName("C5")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.C5.addItem("")
        self.verticalLayout.addWidget(self.C5)
        self.C6 = QtWidgets.QComboBox(self.Companies)
        self.C6.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C6.setObjectName("C6")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.C6.addItem("")
        self.verticalLayout.addWidget(self.C6)
        self.C7 = QtWidgets.QComboBox(self.Companies)
        self.C7.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C7.setObjectName("C7")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.C7.addItem("")
        self.verticalLayout.addWidget(self.C7)
        self.C8 = QtWidgets.QComboBox(self.Companies)
        self.C8.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C8.setObjectName("C8")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.C8.addItem("")
        self.verticalLayout.addWidget(self.C8)
        self.C9 = QtWidgets.QComboBox(self.Companies)
        self.C9.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C9.setObjectName("C9")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.C9.addItem("")
        self.verticalLayout.addWidget(self.C9)
        self.C10 = QtWidgets.QComboBox(self.Companies)
        self.C10.setStyleSheet("QComboBox {\n"
"    background-color:white;\n"
"}")
        self.C10.setObjectName("C10")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.C10.addItem("")
        self.verticalLayout.addWidget(self.C10)
        self.horizontalLayout.addWidget(self.Companies)
        self.Info = QtWidgets.QFrame(self.widget)
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.widget1 = QtWidgets.QWidget(self.Info)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 137, 199))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.widget1)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.Percentage = QtWidgets.QWidget()
        self.Percentage.setObjectName("Percentage")
        self.formLayout_3 = QtWidgets.QFormLayout(self.Percentage)
        self.formLayout_3.setObjectName("formLayout_3")
        self.PerOpt = QtWidgets.QComboBox(self.Percentage)
        self.PerOpt.setObjectName("PerOpt")
        self.PerOpt.addItem("")
        self.PerOpt.addItem("")
        self.PerOpt.addItem("")
        self.PerOpt.addItem("")
        self.PerOpt.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.PerOpt)
        self.tabWidget.addTab(self.Percentage, "")
        self.quantile = QtWidgets.QWidget()
        self.quantile.setObjectName("quantile")
        self.formLayout_2 = QtWidgets.QFormLayout(self.quantile)
        self.formLayout_2.setObjectName("formLayout_2")
        self.QuantOpt = QtWidgets.QComboBox(self.quantile)
        self.QuantOpt.setObjectName("QuantOpt")
        self.QuantOpt.addItem("")
        self.QuantOpt.addItem("")
        self.QuantOpt.addItem("")
        self.QuantOpt.addItem("")
        self.QuantOpt.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.QuantOpt)
        self.tabWidget.addTab(self.quantile, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Period = QtWidgets.QLabel(self.widget1)
        self.Period.setObjectName("Period")
        self.verticalLayout_2.addWidget(self.Period)
        self.days = QtWidgets.QComboBox(self.widget1)
        self.days.setObjectName("days")
        self.days.addItem("")
        self.days.addItem("")
        self.days.addItem("")
        self.days.addItem("")
        self.days.addItem("")
        self.verticalLayout_2.addWidget(self.days)
        self.Start = QtWidgets.QPushButton(self.widget1)
        self.Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start.setObjectName("Start")
        self.verticalLayout_2.addWidget(self.Start)
        self.Benefit = QtWidgets.QLineEdit(self.widget1)
        self.Benefit.setObjectName("Benefit")
        self.verticalLayout_2.addWidget(self.Benefit)
        self.Risk = QtWidgets.QLineEdit(self.widget1)
        self.Risk.setReadOnly(False)
        self.Risk.setObjectName("Risk")
        self.verticalLayout_2.addWidget(self.Risk)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.Info)
        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)
        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "MainWindow"))
        self.C1.setItemText(0, _translate("Test", "None"))
        self.C1.setItemText(1, _translate("Test", "1"))
        self.C1.setItemText(2, _translate("Test", "2"))
        self.C1.setItemText(3, _translate("Test", "3"))
        self.C1.setItemText(4, _translate("Test", "4"))
        self.C1.setItemText(5, _translate("Test", "5"))
        self.C1.setItemText(6, _translate("Test", "6"))
        self.C1.setItemText(7, _translate("Test", "7"))
        self.C1.setItemText(8, _translate("Test", "Apple"))
        self.C1.setItemText(9, _translate("Test", "Microsoft"))
        self.C1.setItemText(10, _translate("Test", "Yandex"))
        self.C2.setItemText(0, _translate("Test", "None"))
        self.C2.setItemText(1, _translate("Test", "1"))
        self.C2.setItemText(2, _translate("Test", "2"))
        self.C2.setItemText(3, _translate("Test", "3"))
        self.C2.setItemText(4, _translate("Test", "4"))
        self.C2.setItemText(5, _translate("Test", "5"))
        self.C2.setItemText(6, _translate("Test", "6"))
        self.C2.setItemText(7, _translate("Test", "7"))
        self.C2.setItemText(8, _translate("Test", "Apple"))
        self.C2.setItemText(9, _translate("Test", "Microsoft"))
        self.C2.setItemText(10, _translate("Test", "Yandex"))
        self.C3.setItemText(0, _translate("Test", "None"))
        self.C3.setItemText(1, _translate("Test", "1"))
        self.C3.setItemText(2, _translate("Test", "2"))
        self.C3.setItemText(3, _translate("Test", "3"))
        self.C3.setItemText(4, _translate("Test", "4"))
        self.C3.setItemText(5, _translate("Test", "5"))
        self.C3.setItemText(6, _translate("Test", "6"))
        self.C3.setItemText(7, _translate("Test", "7"))
        self.C3.setItemText(8, _translate("Test", "Apple"))
        self.C3.setItemText(9, _translate("Test", "Microsoft"))
        self.C3.setItemText(10, _translate("Test", "Yandex"))
        self.C4.setItemText(0, _translate("Test", "None"))
        self.C4.setItemText(1, _translate("Test", "1"))
        self.C4.setItemText(2, _translate("Test", "2"))
        self.C4.setItemText(3, _translate("Test", "3"))
        self.C4.setItemText(4, _translate("Test", "4"))
        self.C4.setItemText(5, _translate("Test", "5"))
        self.C4.setItemText(6, _translate("Test", "6"))
        self.C4.setItemText(7, _translate("Test", "7"))
        self.C4.setItemText(8, _translate("Test", "Apple"))
        self.C4.setItemText(9, _translate("Test", "Microsoft"))
        self.C4.setItemText(10, _translate("Test", "Yandex"))
        self.C5.setItemText(0, _translate("Test", "None"))
        self.C5.setItemText(1, _translate("Test", "1"))
        self.C5.setItemText(2, _translate("Test", "2"))
        self.C5.setItemText(3, _translate("Test", "3"))
        self.C5.setItemText(4, _translate("Test", "4"))
        self.C5.setItemText(5, _translate("Test", "5"))
        self.C5.setItemText(6, _translate("Test", "6"))
        self.C5.setItemText(7, _translate("Test", "7"))
        self.C5.setItemText(8, _translate("Test", "Apple"))
        self.C5.setItemText(9, _translate("Test", "Microsoft"))
        self.C5.setItemText(10, _translate("Test", "Yandex"))
        self.C6.setItemText(0, _translate("Test", "None"))
        self.C6.setItemText(1, _translate("Test", "1"))
        self.C6.setItemText(2, _translate("Test", "2"))
        self.C6.setItemText(3, _translate("Test", "3"))
        self.C6.setItemText(4, _translate("Test", "4"))
        self.C6.setItemText(5, _translate("Test", "5"))
        self.C6.setItemText(6, _translate("Test", "6"))
        self.C6.setItemText(7, _translate("Test", "7"))
        self.C6.setItemText(8, _translate("Test", "Apple"))
        self.C6.setItemText(9, _translate("Test", "Microsoft"))
        self.C6.setItemText(10, _translate("Test", "Yandex"))
        self.C7.setItemText(0, _translate("Test", "None"))
        self.C7.setItemText(1, _translate("Test", "1"))
        self.C7.setItemText(2, _translate("Test", "2"))
        self.C7.setItemText(3, _translate("Test", "3"))
        self.C7.setItemText(4, _translate("Test", "4"))
        self.C7.setItemText(5, _translate("Test", "5"))
        self.C7.setItemText(6, _translate("Test", "6"))
        self.C7.setItemText(7, _translate("Test", "7"))
        self.C7.setItemText(8, _translate("Test", "Apple"))
        self.C7.setItemText(9, _translate("Test", "Microsoft"))
        self.C7.setItemText(10, _translate("Test", "Yandex"))
        self.C8.setItemText(0, _translate("Test", "None"))
        self.C8.setItemText(1, _translate("Test", "1"))
        self.C8.setItemText(2, _translate("Test", "2"))
        self.C8.setItemText(3, _translate("Test", "3"))
        self.C8.setItemText(4, _translate("Test", "4"))
        self.C8.setItemText(5, _translate("Test", "5"))
        self.C8.setItemText(6, _translate("Test", "6"))
        self.C8.setItemText(7, _translate("Test", "7"))
        self.C8.setItemText(8, _translate("Test", "Apple"))
        self.C8.setItemText(9, _translate("Test", "Microsoft"))
        self.C8.setItemText(10, _translate("Test", "Yandex"))
        self.C9.setItemText(0, _translate("Test", "None"))
        self.C9.setItemText(1, _translate("Test", "1"))
        self.C9.setItemText(2, _translate("Test", "2"))
        self.C9.setItemText(3, _translate("Test", "3"))
        self.C9.setItemText(4, _translate("Test", "4"))
        self.C9.setItemText(5, _translate("Test", "5"))
        self.C9.setItemText(6, _translate("Test", "6"))
        self.C9.setItemText(7, _translate("Test", "7"))
        self.C9.setItemText(8, _translate("Test", "Apple"))
        self.C9.setItemText(9, _translate("Test", "Microsoft"))
        self.C9.setItemText(10, _translate("Test", "Yandex"))
        self.C10.setItemText(0, _translate("Test", "None"))
        self.C10.setItemText(1, _translate("Test", "1"))
        self.C10.setItemText(2, _translate("Test", "2"))
        self.C10.setItemText(3, _translate("Test", "3"))
        self.C10.setItemText(4, _translate("Test", "4"))
        self.C10.setItemText(5, _translate("Test", "5"))
        self.C10.setItemText(6, _translate("Test", "6"))
        self.C10.setItemText(7, _translate("Test", "7"))
        self.C10.setItemText(8, _translate("Test", "Apple"))
        self.C10.setItemText(9, _translate("Test", "Microsoft"))
        self.C10.setItemText(10, _translate("Test", "Yandex"))
        self.PerOpt.setItemText(0, _translate("Test", "None"))
        self.PerOpt.setItemText(1, _translate("Test", "99%"))
        self.PerOpt.setItemText(2, _translate("Test", "95%"))
        self.PerOpt.setItemText(3, _translate("Test", "90%"))
        self.PerOpt.setItemText(4, _translate("Test", "50%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Percentage), _translate("Test", "percantage"))
        self.QuantOpt.setItemText(0, _translate("Test", "None"))
        self.QuantOpt.setItemText(1, _translate("Test", "2.326"))
        self.QuantOpt.setItemText(2, _translate("Test", "1.645"))
        self.QuantOpt.setItemText(3, _translate("Test", "1.282"))
        self.QuantOpt.setItemText(4, _translate("Test", "0.001"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.quantile), _translate("Test", "quantile"))
        self.Period.setText(_translate("Test", "Period"))
        self.days.setItemText(0, _translate("Test", "1"))
        self.days.setItemText(1, _translate("Test", "5"))
        self.days.setItemText(2, _translate("Test", "10"))
        self.days.setItemText(3, _translate("Test", "15"))
        self.days.setItemText(4, _translate("Test", "20"))
        self.Start.setText(_translate("Test", "Start"))
        self.Start.clicked.connect(self.start)
        self.PerOpt.currentTextChanged.connect(self.prcChange)
        self.QuantOpt.currentTextChanged.connect(self.quaChange)

    def start(self):
             
        a1 = self.C1.currentText()
        a2 = self.C2.currentText()
        a3 = self.C3.currentText()
        a4 = self.C4.currentText()
        a5 = self.C5.currentText()
        a6 = self.C6.currentText()
        a7 = self.C7.currentText()
        a8 = self.C8.currentText()
        a9 = self.C9.currentText()
        a10 = self.C10.currentText()
        prc = self.PerOpt.currentText()
        qua = float (self.QuantOpt.currentText())
        per = float(self.days.currentText())
        pat = ['D:\Projects\X-max hack\Comp\GAZP_220103_221216.txt']
        rez = []
        for a in pat:
                rez.append(ActLoose(a, qua, per)) 
        self.Risk.setText(str(rez[0]))
        rez = getActValues(pat[0])
        gp = StandartOtklon(rez)
        self.Benefit.setText(str(gp))

    def prcChange(self):
        self.QuantOpt.setCurrentIndex(self.PerOpt.currentIndex())
    def quaChange(self):
        self.PerOpt.setCurrentIndex(self.QuantOpt.currentIndex())
def getActValues(path):
        with open(path, 'r') as f:
                lines = f.readlines()
                lines.pop(0)
                values = []
        for line in lines:
                values.append(float(line.split(';')[4]))
        return values

def ActLoose(pp, q, t):
        actValues = getActValues(pp)
        pva = actValues[len(actValues) - 1]
        de = DailyChanges(actValues)
        ep = np.average(de)
        gp = StandartOtklon(actValues) ** 0.5
        return pva * (ep * t - q * gp * (t ** 0.5))

def StandartOtklon(actValues):
        aav = np.average(actValues)
        sum = 0
        for a in actValues:
                sum += a - aav
        return sum/(len(actValues) - 1)

def DailyChanges(actValues):
        changes = []
        for i in range(len(actValues)-1):
                changes.append((actValues[i+1] - actValues[i])/actValues[i] * 100)
        return changes

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())