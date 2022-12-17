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
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 408, 180))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Companies = QtWidgets.QFrame(self.layoutWidget)
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
        self.horizontalLayout.addWidget(self.Companies)
        self.Info = QtWidgets.QFrame(self.layoutWidget)
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Period = QtWidgets.QLabel(self.Info)
        self.Period.setObjectName("Period")
        self.verticalLayout_2.addWidget(self.Period)
        self.years = QtWidgets.QComboBox(self.Info)
        self.years.setObjectName("years")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.verticalLayout_2.addWidget(self.years)
        self.StartEF = QtWidgets.QPushButton(self.Info)
        self.StartEF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartEF.setObjectName("StartEF")
        self.verticalLayout_2.addWidget(self.StartEF)
        self.lblBenefits = QtWidgets.QLabel(self.Info)
        self.lblBenefits.setObjectName("lblBenefits")
        self.verticalLayout_2.addWidget(self.lblBenefits)
        self.Benefit = QtWidgets.QLineEdit(self.Info)
        self.Benefit.setObjectName("Benefit")
        self.verticalLayout_2.addWidget(self.Benefit)
        self.lblRisk = QtWidgets.QLabel(self.Info)
        self.lblRisk.setObjectName("lblRisk")
        self.verticalLayout_2.addWidget(self.lblRisk)
        self.Risk = QtWidgets.QLineEdit(self.Info)
        self.Risk.setReadOnly(False)
        self.Risk.setObjectName("Risk")
        self.verticalLayout_2.addWidget(self.Risk)
        self.horizontalLayout.addWidget(self.Info)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.Weight_4 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_4.setObjectName("Weight_4")
        self.gridLayout.addWidget(self.Weight_4, 3, 0, 1, 1)
        self.Weight_3 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_3.setObjectName("Weight_3")
        self.gridLayout.addWidget(self.Weight_3, 2, 0, 1, 1)
        self.Weight_2 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_2.setObjectName("Weight_2")
        self.gridLayout.addWidget(self.Weight_2, 1, 0, 1, 1)
        self.Weight_1 = QtWidgets.QLineEdit(self.frame_2)
        self.Weight_1.setObjectName("Weight_1")
        self.gridLayout.addWidget(self.Weight_1, 0, 0, 1, 1)
        self.StartPG = QtWidgets.QPushButton(self.frame_2)
        self.StartPG.setObjectName("StartPG")
        self.gridLayout.addWidget(self.StartPG, 4, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        Test.setCentralWidget(self.centralwidget)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)
        
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
        
     
    def ShowGraph(Weights=[]):
        scene = QGraphicsScene()
        set_angle = 0
        count1 = 0
        colours = []

        for count in range(len(Weights)):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            colours.append(QColor(number[0],number[1],number[2]))

        for i in Weights:
            circle = QGraphicsEllipseItem(0,0,400,400)
            angle = round(float(i*5760)/1)
            circle.setPos(0,0)
            circle.setStartAngle(set_angle)
            circle.setSpanAngle(angle)
            circle.setBrush(colours[count1])
            set_angle += angle
            count1 += 1
            scene.addItem(circle)


        view = QGraphicsView(scene)
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
        
        self.ShowGraph(Weights=wg)
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())