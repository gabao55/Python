import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, \
    QLineEdit, QSizePolicy
import math

class MyCalculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator made by Gabriel Rosin')
        self.setStyleSheet('background-color: black; border-color: black')
        self.setFixedSize(400, 500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.display.setDisabled(True)
        self.display.setStyleSheet('*{background: black; color: white; font-size: 40px; format: .:6f}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton(u"\u221A"), 1, 3, 1, 1, self.square_root, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('%'), 1, 2, 1, 1, lambda: self.display.setText(str(int(self.display.text())/100)), 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('C'), 1, 1, 1, 1, lambda: self.display.setText(self.display.text()[:-1]), 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: red; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('AC '), 1, 0, 1, 1, lambda: self.display.setText(''), 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: red; font-weight: 300; font-size: 25px;')

        self.add_btn(QPushButton('7'), 2, 0, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('8'), 2, 1, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('9'), 2, 2, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('/ '), 2, 3, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')

        self.add_btn(QPushButton('4'), 3, 0, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('5'), 3, 1, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('6'), 3, 2, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('-'), 3, 3, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')

        self.add_btn(QPushButton('1'), 4, 0, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('2'), 4, 1, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('3'), 4, 2, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')

        self.add_btn(QPushButton('.'), 5, 0, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('0'), 5, 1, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('='), 5, 3, 1, 1, self.equal, 'border-radius: 36px; border-style: outset; background: green; color: white; font-weight: 300; font-size: 25px;')
        self.add_btn(QPushButton('+'), 5, 2, 1, 1, None, 'border-radius: 36px; border-style: outset; background: #4F4F4F; color: #00FF00; font-weight: 300; font-size: 25px;')


        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        else:
            btn.clicked.connect(function)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet(style)

    def equal(self):
        try:
            if len(self.display.text()) > 9:
                self.display.setText(str(eval(self.display.text()))[:9])
            else:
                self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Invalid operation.')

    def square_root(self):
        try:
            number = float(self.display.text())
            sqrt = '{:.8f}'.format(math.sqrt(number))

            self.display.setText(str(sqrt))

        except Exception as e:
            self.display.setText('Invalid operation.')

    # def division(self):
    #     try:
    #         self.display.setText(str(eval(self.display.text())))
    #     except Exception as e:
    #         self.display.setText('Invalid operation.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculator = MyCalculator()
    calculator.show()
    qt.exec_()
