from modulos.CPF_operations_PyQT5.validator import CPF_validate
from modulos.CPF_operations_PyQT5.generator import CPF_generate
from modulos.CPF_operations_PyQT5.design import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class CPFOperations(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGenerateCPF.clicked.connect(self.generate_cpf)
        self.btnValidateCPF.clicked.connect(self.validate_cpf)

    def generate_cpf(self):
        self.labelOutput.setText(CPF_generate())

    def validate_cpf(self):
        cpf = self.inputValidateCPF.text()
        self.labelOutput.setText(CPF_validate(cpf))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cpf = CPFOperations()
    cpf.show()
    qt.exec_()