# from https://blog.csdn.net/HG0724/article/details/116702824
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Picture(QMainWindow):
    def __init__(self, parent=None, url=None):
        super().__init__(parent)
        self.url = url
        self.ui()

    def ui(self):
        loadUi('./show_pic.ui', self)

        # self.setFixedSize(850, 600)

        total = len(self.url)

        self.qw = QWidget()
        if total % 5 == 0:
            rows = int(total / 5)
        else:
            rows = int(total / 5) + 1
        self.qw.setMinimumSize(850, 230 * rows)
        for i in range(total):

            photo = QPixmap(self.url[i])
            # print('photo:',photo)
            # photo.loadFromData(req.content)
            width = photo.width()
            height = photo.height()
            print('width:', width, '      ', 'height:', height)

            if width == 0 or height == 0:
                continue
            tmp_image = photo.toImage()  # 将QPixmap对象转换为QImage对象
            size = QSize(width, height)
            # photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            photo = photo.fromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))

            # 为每个图片设置QLabel容器
            label = QLabel()
            label.setFixedSize(150, 200)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(photo)
            label.setScaledContents(True)  # 图像自适应窗口大小

            vl = QVBoxLayout()
            vl.addWidget(label)

            tmp = QWidget(self.qw)
            tmp.setLayout(vl)
            tmp.move(160 * (i % 5), 230 * int(i / 5))

        self.scrollArea.setWidget(self.qw)  # 和ui文件中名字相同


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 这是我的文件夹中图片的路径

    import glob

    url = glob.glob(r"C:\waDump\*.jpg")
    pic = Picture(url=url)
    pic.show()
    sys.exit(app.exec_())
