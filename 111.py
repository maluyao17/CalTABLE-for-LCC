from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QVBoxLayout, QWidget, QSlider, QInputDialog
from PyQt5.QtCore import Qt, pyqtSignal
import sys

class ChildWindow(QWidget):
    data_signal = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 20)  # 设置滑块的范围为 0 到 20
        self.slider.valueChanged.connect(self.send_data)

    def send_data(self):
        value = self.slider.value() / 20.0  # 将滑块的值转换为 0 到 1 的浮点数
        self.data_signal.emit(value)  # 发送信号

    def closeEvent(self, event):
        self.send_data()  # 在窗口关闭时发送信号

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Open', self)
        self.button.clicked.connect(self.open_child_window)
        self.label = QLabel('No data', self)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.child_window = ChildWindow()
        self.child_window.data_signal.connect(self.receive_data)

    def open_child_window(self):
        self.child_window.show()

    def receive_data(self, data):
        self.label.setText('Received data: {:.2f}'.format(data))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
