#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel


class ImageLabel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 400)
        self.setWindowTitle("label image")

        pix = QPixmap(r'C:\fruits.jpg')
        label = QLabel(self)
        label.setPixmap(pix)
        label.setScaledContents(True)  # 自适应QLabel大小

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = ImageLabel()
    mainWidget.show()
    sys.exit(app.exec_())
