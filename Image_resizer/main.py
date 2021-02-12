import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resize_image)
        self.btnSave.clicked.connect(self.save_image)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open Image', r'C:\Users\gabri\OneDrive\Pictures')
        self.inputAbrirArquivo.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputHeight.setText(str(self.original_img.width()))
        self.inputWidth.setText(str(self.original_img.height()))

    def resize_image(self):
        height = int(self.inputHeight.text())
        self.new_image = self.original_img.scaledToHeight(height)
        self.labelImg.setPixmap(self.new_image)
        self.inputHeight.setText(str(self.new_image.height()))
        self.inputWidth.setText(str(self.new_image.width()))

    def save_image(self):
        image, _ = QFileDialog.getSaveFileName(self.centralwidget, 'Save Image', r'C:\Users\gabri\OneDrive\Pictures')
        self.new_image.save(image, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    image_resizer = ResizeImage()
    image_resizer.show()
    qt.exec_()