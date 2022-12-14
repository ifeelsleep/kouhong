# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myuidesign.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
from QCandyUi import CandyWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget,QGraphicsScene
from PyQt5.QtCore import QFileInfo
#import unicode

from detectface import my_face_recognition
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.imgPath=""
        self.face_recognize_object =None
        self.showFullImage = True
        self.brand=[]
        self.color=[]
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 630)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 801, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("汉仪唐美人W")
        font.setPointSize(36)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.graphicsView = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("汉仪唐美人W")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QtCore.QSize(20, 50))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setFamily("汉仪唐美人W")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("汉仪唐美人W")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def on_pushButton_clicked(self):
        """
        get the image path and show it in the view
        """
        self.face_recognize_object = my_face_recognition()
        print("onpush")
#        self.imgPath = QDialog.QFileDialog.getOpenFileName( self,"please open excel file", r"D:\homework\大三下信息系统设计",u'Images (*.png *.jpg)')
        fileName, filetype = QFileDialog.getOpenFileName(None, "选择文件", r"D:\homework\大三下信息系统设计", "Images (*.png *.jpg)")
        self.imgPath=fileName
        print (self.imgPath)
        if self.imgPath != '':
            self.face_recognize_object.operates_(self.imgPath)
            if self.showFullImage == True:
                self.face_recognize_object.showImg('original')
            print("showimage")
            scene = QGraphicsScene()                # 创建场景
            pixmap = QtGui.QPixmap(self.imgPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtWidgets.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
            self.textBrowser.clear()
            print("self.textBrowser.clear()")
            self.textBrowser.append(str(self.face_recognize_object.errordetect()))
    def on_pushButton_2_clicked(self):
        self.face_recognize_object.AI()
        self.brand=self.face_recognize_object.register_lps
        self.color=self.face_recognize_object.register_rgb
        print(self.brand)
        self.textBrowser.clear()
        print("self.textBrowser.clear()")
        self.textBrowser.append(str(self.face_recognize_object.errdet))
        print("self.textBrowser.clear()")
        strout="最像您输入的口红的三只色号库内口红分别为!"
        flag=0
        for i in range(len(self.brand)):
            flag=1
            strout=strout+'\n'
            print("flag1")
            for j in range(len(self.brand[i])):
                if(self.brand[i][j]!='none'):
                    strout=strout+str(self.brand[i][j])           
        self.textBrowser.append(strout)
        if(flag==0):
            self.textBrowser.clear()
            self.textBrowser.append("这张图片不可以进行处理，请换一张吧")
            print("flag0")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Original pic"))
        self.pushButton.setText(_translate("Form", "选择文件"))
        self.label_2.setText(_translate("Form", "     result"))
        self.pushButton_2.setText(_translate("Form", "开始识别"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog = CandyWindow.createWindow(Dialog, 'pink')
    Dialog.show()
    sys.exit(app.exec_())

