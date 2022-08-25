import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("pyqt 5 ders 1")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("yazı denemesii")
    etiket1.move(200,30)
    etiket2=QtWidgets.QLabel(pencere)
    #etiket2.setPixmap(QtGui.QPixmap("kuş.jpg"))

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("BUTON")

    pencere.setGeometry(100,100,500,500)#ilk ikisi ekrandaki yeri diğer ikisi boyut

    pencere.show()

    sys.exit(app.exec_())

Pencere()