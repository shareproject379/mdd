# from huawei_lte_api.Client import Client
# from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
# connection = AuthorizedConnection('http://admin:admin@192.168.1.1/')
# client = Client(connection)
# print(client.device.signal())
# print(client.device.information())
# print(client.diagnosis.diagnose_ping())
# print(client.device.basic_information())
# print(client.diagnosis.diagnose_traceroute())


import sys
from PyQt5.QtWidgets import QDialog, QApplication
from templates.BasicInfo import *


class MyInterface(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = BasicInfoUiDialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.change_dialog_title)
        self.show()

    def change_dialog_title(self):
        self.setWindowTitle("Horaaaa")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = MyInterface()
    r.show()
    sys.exit(app.exec_())
