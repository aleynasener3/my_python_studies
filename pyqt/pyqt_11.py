import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QtGui

from PIL import Image,ImageFilter

class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):


        self.yazi_alani = QLabel("")
        self.kırp_butonu = QPushButton("resmi kırp")


        v_box = QVBoxLayout()


        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)



        self.buton.clicked.connect(self.click())

        self.show()

    def click(self):
        pass

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
