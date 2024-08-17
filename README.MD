
# 1 单张图片

## 1.1 使用 label 显示图片

特点是最简单，但功能也最少。

![](https://codesimple-blog-images.oss-cn-hangzhou.aliyuncs.com/python/_image/pyqt_img_QLabel.png)

源码：[label.py](./label.py)


## 1.2 使用 pyqtgraph 控件显示图片

参考来源 [【PyQtGraph】显示图像](https://blog.csdn.net/zhy29563/article/details/119754910)  
特点 可以对图片进行缩放操作，继承了pyqtgraph 的一些特点功能。

![](https://codesimple-blog-images.oss-cn-hangzhou.aliyuncs.com/python/_image/pyqt_img_pyqtgraph.gif)

源码：[pyqtgraph.py](./pyqtgraph.py)


# 2 多张图片

## 2.1 使用 scrollArea 显示多张图片

参考来源：[PyQt5-使用scrollArea实现图片查看器功能](https://blog.csdn.net/HG0724/article/details/116702824)

特点是当窗口大小小于scrollArea 区域大小时有滑动条显示，可以拖动滑动条滑动界面。

但是这份代码有个缺点，就是当窗口大小大于scrollArea 区域大小时，你会发现scrollArea 以外的区域是空白的，也就是scrollArea 是固定大小的，区域外不会显示内容。注释掉 self.setFixedSize(850, 600) 可以测试看到。
这份代码的显示原理大致如下：创建一个scrollArea控件，对多张图像依次执行下面循环的操作：1. 创建一个label 显示image；2. label 添加到 一个QVBoxLayout 中，3. QVBoxLayout 作为一个临时的QWidget layout，4. 移动这个临时的 QWidget 到指定坐标。emmm 就不是很优雅。

![](https://codesimple-blog-images.oss-cn-hangzhou.aliyuncs.com/python/_image/pyqt_img_QScrollArea.gif)

源码：[scrollArea.py](./scrollArea.py)

## 2.2 使用 scrollArea + gridLayout 显示多张图片

可以缩放窗口，图像可以随着窗口变化，但只是图像间距拉伸，每行的图片数量没有变化

![](https://codesimple-blog-images.oss-cn-hangzhou.aliyuncs.com/python/_image/pyqt_img_QScrollArea_QGridLayout.gif)

源码：[scrollArea_gridLayout.py](./scrollArea_gridLayout.py)


## 2.3 使用 listWidget + 自定义的 listWidgetItem 显示多张图片

可以缩放窗口，图像可以随着窗口重新排列，自定义的QListWidgetItem 可以灵活自定义显示样式。
代码参考这两个博客 [PyQt使用笔记(六) 可多选, 有右键复制删除功能的ListWidget 2021.03.23](https://blog.csdn.net/qq_17246289/article/details/115135699) 和 [[pyqt] 使用自定义QListWidgetItem](https://blog.csdn.net/Strengthennn/article/details/103747819)

![](https://codesimple-blog-images.oss-cn-hangzhou.aliyuncs.com/python/_image/pyqt_img_QListWidget.gif)

源码：[listWidget_listWidgetItem.py](./listWidget_listWidgetItem.py)

