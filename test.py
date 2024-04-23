from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QSlider, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.lineEdit = QLineEdit()
        self.label = QLabel("Input")
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.syncLineEdit)
        self.lineEdit.textChanged.connect(self.syncSlider)

    def syncLineEdit(self, value):
        self.lineEdit.setText(str(value))

    def syncSlider(self, text):
        if text.isdigit():
            self.slider.setValue(int(text))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(["Option 1", "Option 2", "Option 3"])
        self.comboBox1.activated.connect(self.showCustomWidget)
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox1)
        self.setLayout(layout)

    def showCustomWidget(self):
        self.customWidget = CustomWidget()
        self.customWidget.show()

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
