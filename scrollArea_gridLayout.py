
# -*- coding: utf-8 -*-
import glob
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout


class Picture(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Picture, self).__init__(parent)
        print('Picture init')
        self.setWindowTitle('All Images')
        self.resize(800, 600)

        # ui components
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.scrollArea)
        self.setLayout(self.v_layout)

        # vars
        self.max_columns = 5

    def load_images(self, paths):
        print('load images --start')
        total = len(paths)
        col = 0
        row = 0
        for i in range(total):
            self.max_columns = total if total < 5 else 5

            photo = QPixmap(paths[i])
            width = photo.width()
            height = photo.height()

            if width == 0 or height == 0:
                continue
            tmp_image = photo.toImage()  # 将QPixmap对象转换为QImage对象
            size = QSize(width, height)
            # photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            photo = photo.fromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))

            # 为每个图片设置QLabel容器
            label = QLabel()
            w = int(self.width() / self.max_columns * 0.8)
            h = int(w * photo.height() / photo.width())
            label.setFixedSize(w, h)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(photo)
            label.setScaledContents(True)  # 图像自适应窗口大小

            self.gridLayout.addWidget(label, row, col)
            # 计算下一个label 位置
            if col < self.max_columns - 1:
                col = col + 1
            else:
                col = 0
                row += 1

        print('load images --end')


if __name__ == '__main__':
    start_time = time.time()
    print('main layout show')
    app = QApplication([])
    main_window = Picture()
    main_window.show()
    image_list = url = glob.glob(r"C:\waDump\*.jpg")
    # 加载图像显示
    main_window.load_images(image_list)
    print("耗时: {:.3f}秒".format(time.time() - start_time))
    app.exec_()