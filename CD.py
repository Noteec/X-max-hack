from PyQt5.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsEllipseItem
from PyQt5.Qt import QColor
import sys, random

def ShowGraph():
    app = QApplication(sys.argv)
    scene = QGraphicsScene()

    Weights = [50,25,25]
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
        angle = round(float(i*5760)/sum(Weights))
        circle.setPos(0,0)
        circle.setStartAngle(set_angle)
        circle.setSpanAngle(angle)
        circle.setBrush(colours[count1])
        set_angle += angle
        count1 += 1
        scene.addItem(circle)


    view = QGraphicsView(scene)
    view.show()
    app.exec_()

ShowGraph()