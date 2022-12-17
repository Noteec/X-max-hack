
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsEllipseItem
from PyQt5.Qt import QColor

import sys, random
from portfel import Portfel


class Ui_Test(object):
    def __init__(self):
        self.portf = Portfel()
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(1135, 901)
        Test.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1111, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Companies = QtWidgets.QFrame(self.frame)
        self.Companies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Companies.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Companies.setObjectName("Companies")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Companies)
        self.verticalLayout.setObjectName("verticalLayout")
        self.box_accii = QtWidgets.QComboBox(self.Companies)
        self.box_accii.setObjectName("box_accii")
        comp = self.portf.Companies
        for c in comp:
            self.box_accii.addItem(c)
        self.verticalLayout.addWidget(self.box_accii)
        self.box_obl = QtWidgets.QComboBox(self.Companies)
        self.box_obl.setObjectName("box_obl")
        for c in comp:
            self.box_obl.addItem(c)
        self.verticalLayout.addWidget(self.box_obl)
        self.box_bezrisk = QtWidgets.QComboBox(self.Companies)
        self.box_bezrisk.setAcceptDrops(False)
        self.box_bezrisk.setObjectName("box_bezrisk")
        for c in comp:
            self.box_bezrisk.addItem(c)
        self.verticalLayout.addWidget(self.box_bezrisk)
        self.box_money = QtWidgets.QLineEdit(self.Companies)
        self.box_money.setObjectName("box_money")
        self.verticalLayout.addWidget(self.box_money)
        self.horizontalLayout.addWidget(self.Companies, 0, QtCore.Qt.AlignTop)
        self.Info = QtWidgets.QFrame(self.frame)
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Info)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Period = QtWidgets.QLabel(self.Info)
        self.Period.setObjectName("Period")
        self.gridLayout_3.addWidget(self.Period, 0, 0, 1, 1)
        self.years = QtWidgets.QComboBox(self.Info)
        self.years.setObjectName("years")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.gridLayout_3.addWidget(self.years, 1, 0, 1, 1)
        self.StartEF = QtWidgets.QPushButton(self.Info)
        self.StartEF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartEF.setObjectName("StartEF")
        self.gridLayout_3.addWidget(self.StartEF, 2, 0, 1, 1)
        self.lblBenefits = QtWidgets.QLabel(self.Info)
        self.lblBenefits.setObjectName("lblBenefits")
        self.gridLayout_3.addWidget(self.lblBenefits, 3, 0, 1, 1)
        self.Benefit = QtWidgets.QLineEdit(self.Info)
        self.Benefit.setObjectName("Benefit")
        self.gridLayout_3.addWidget(self.Benefit, 4, 0, 1, 1)
        self.lblRisk = QtWidgets.QLabel(self.Info)
        self.lblRisk.setObjectName("lblRisk")
        self.gridLayout_3.addWidget(self.lblRisk, 5, 0, 1, 1)
        self.Risk = QtWidgets.QLineEdit(self.Info)
        self.Risk.setReadOnly(False)
        self.Risk.setObjectName("Risk")
        self.gridLayout_3.addWidget(self.Risk, 6, 0, 1, 1)
        self.horizontalLayout.addWidget(self.Info, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Weight_1 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_1.setObjectName("Weight_1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Weight_1)
        self.Weight_2 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_2.setObjectName("Weight_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Weight_2)
        self.Weight_3 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_3.setObjectName("Weight_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Weight_3)
        self.Weight_4 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_4.setObjectName("Weight_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Weight_4)
        self.StartPG = QtWidgets.QPushButton(self.frame_2)
        self.StartPG.setObjectName("StartPG")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.StartPG)
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)
    
        self.StartEF.clicked.connect(self.startEF)
        self.StartPG.clicked.connect(self.startPG)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "MainWindow"))
        self.box_accii.setItemText(0, _translate("Test", "Yandex"))
        self.box_accii.setItemText(1, _translate("Test", "Yt"))
        self.box_accii.setItemText(2, _translate("Test", "Yahoo"))
        self.box_obl.setItemText(0, _translate("Test", "1"))
        self.box_obl.setItemText(1, _translate("Test", "2"))
        self.box_bezrisk.setItemText(0, _translate("Test", "1"))
        self.Period.setText(_translate("Test", "Period"))
        self.years.setItemText(0, _translate("Test", "1"))
        self.years.setItemText(1, _translate("Test", "2"))
        self.years.setItemText(2, _translate("Test", "3"))
        self.years.setItemText(3, _translate("Test", "5"))
        self.StartEF.setText(_translate("Test", "Start EF"))
        self.lblBenefits.setText(_translate("Test", "benefits"))
        self.lblRisk.setText(_translate("Test", "Risk"))
        self.StartPG.setText(_translate("Test", "Start PG"))
        
        self.StartEF.clicked.connect(self.startEF)
        self.StartPG.clicked.connect(self.startPG)
        

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "MainWindow"))
        self.Period.setText(_translate("Test", "Period"))
        self.years.setItemText(0, _translate("Test", "1"))
        self.years.setItemText(1, _translate("Test", "2"))
        self.years.setItemText(2, _translate("Test", "3"))
        self.years.setItemText(3, _translate("Test", "5"))
        self.StartEF.setText(_translate("Test", "Start EF"))
        self.lblBenefits.setText(_translate("Test", "benefits"))
        self.lblRisk.setText(_translate("Test", "Risk"))
        self.StartPG.setText(_translate("Test", "Start PG"))
        
     
    def ShowGraph(self,wgt):
        scene = QGraphicsScene()
        set_angle = 0
        count1 = 0
        colours = []
        comp = [self.box_accii.currentText(), self.box_obl.currentText(),self.box_bezrisk.currentText(),'Index MosBirzhy']
        
        for count in range(len(wgt)):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            colours.append(QColor(number[0],number[1],number[2]))          
        
        for i in wgt:
            circle = QGraphicsEllipseItem(0,0,400,400)
            angle = round(float(i*5760)/1)
            circle.setPos(0,0)
            circle.setStartAngle(set_angle)
            circle.setSpanAngle(angle)
            circle.setBrush(colours[count1])
            set_angle += angle
            scene.addItem(circle)
            count1 += 1


        view = QGraphicsView(scene,self.graphicsView)
        view.show()
       
    def startEF(self):
        self.portf.AddCompanyToPort(self.box_accii.currentText())
        self.portf.AddCompanyToPort(self.box_obl.currentText())
        self.portf.AddCompanyToPort(self.box_bezrisk.currentText())
        self.portf.Tickers.append('MCFTR.INDX')
        self.portf.CreatePortfel()
        self.portf.MakeEfficientyFrontDiagramm()
    
    def startPG(self):
        ben = float(self.Benefit.text())
        risk = float(self.Risk.text())
        wg = self.portf.GetWeights(risk, ben)
        self.Weight_1.setText(str(wg[0]))
        self.Weight_2.setText(str(wg[1]))
        self.Weight_3.setText(str(wg[2]))
        self.Weight_4.setText(str(wg[3]))
        
        self.portf.MakeForecastDiagramm(year = int(self.years.currentText()))
        
        self.ShowGraph(wg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())
