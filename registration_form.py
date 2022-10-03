from PySide2.QtWidgets import QApplication, QWidget


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration Form")


app = QApplication([])
window = RegistrationForm()
window.show()
app.exec_()