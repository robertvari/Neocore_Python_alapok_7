from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import json


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration Form")
        self.resize(600, 0)

        root_layout = QVBoxLayout(self)

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Name")
        root_layout.addWidget(self.name_field)

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email")
        root_layout.addWidget(self.email_field)

        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Phone")
        root_layout.addWidget(self.phone_field)

        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Address")
        root_layout.addWidget(self.address_field)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.button_clicked)
        root_layout.addWidget(save_button)
    
    def button_clicked(self):
        name = self.name_field.text()
        email = self.email_field.text()
        phone = self.phone_field.text()
        address = self.address_field.text()

        user_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
        }

        self.save_data(user_data)
        self.name_field.clear()
        self.phone_field.clear()
        self.email_field.clear()
        self.address_field.clear()

    def save_data(self, user_data):
        with open("user_data.json", "w") as f:
            json.dump(user_data, f)

app = QApplication([])
window = RegistrationForm()
window.show()
app.exec_()