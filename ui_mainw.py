# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwlViwIg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QSize(1366, 768))
        MainWindow.setMaximumSize(QSize(1366, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cover_label = QLabel(self.centralwidget)
        self.cover_label.setObjectName(u"cover_label")
        self.cover_label.setGeometry(QRect(650, 30, 450, 450))
        self.cover_label.setMinimumSize(QSize(450, 450))
        self.cover_label.setMaximumSize(QSize(450, 450))
        self.cover_label.setScaledContents(True)
        self.cover_label.setAlignment(Qt.AlignCenter)
        self.music_listWidget = QListWidget(self.centralwidget)
        self.music_listWidget.setObjectName(u"music_listWidget")
        self.music_listWidget.setGeometry(QRect(1108, 29, 249, 701))
        self.music_listWidget.setMaximumSize(QSize(250, 16777215))
        self.viewfld_pushButton = QPushButton(self.centralwidget)
        self.viewfld_pushButton.setObjectName(u"viewfld_pushButton")
        self.viewfld_pushButton.setGeometry(QRect(1020, 700, 75, 24))
        self.about_pushButton = QPushButton(self.centralwidget)
        self.about_pushButton.setObjectName(u"about_pushButton")
        self.about_pushButton.setGeometry(QRect(1020, 730, 75, 24))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(660, 500, 431, 165))
        self.search_pushButton = QPushButton(self.groupBox)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(340, 130, 75, 24))
        self.save_pushButton = QPushButton(self.groupBox)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(224, 130, 111, 24))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 25, 411, 99))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.music_lineEdit = QLineEdit(self.layoutWidget)
        self.music_lineEdit.setObjectName(u"music_lineEdit")

        self.gridLayout.addWidget(self.music_lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.singer_lineEdit = QLineEdit(self.layoutWidget)
        self.singer_lineEdit.setObjectName(u"singer_lineEdit")

        self.gridLayout.addWidget(self.singer_lineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.al_lineEdit = QLineEdit(self.layoutWidget)
        self.al_lineEdit.setObjectName(u"al_lineEdit")

        self.gridLayout.addWidget(self.al_lineEdit, 2, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.size_label = QLabel(self.layoutWidget)
        self.size_label.setObjectName(u"size_label")

        self.gridLayout.addWidget(self.size_label, 3, 1, 1, 1)

        self.cover_listWidget = QListWidget(self.centralwidget)
        self.cover_listWidget.setObjectName(u"cover_listWidget")
        self.cover_listWidget.setGeometry(QRect(9, 29, 635, 721))
        self.cover_listWidget.setMinimumSize(QSize(635, 0))
        font = QFont()
        font.setPointSize(14)
        self.cover_listWidget.setFont(font)
        self.cover_listWidget.setIconSize(QSize(150, 150))
        self.cover_listWidget.setWordWrap(True)
        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(1110, 10, 241, 16))
        self.count_label = QLabel(self.centralwidget)
        self.count_label.setObjectName(u"count_label")
        self.count_label.setGeometry(QRect(1300, 740, 54, 16))
        self.count_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 161, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(650, 10, 111, 16))
        self.file_path_label = QLabel(self.centralwidget)
        self.file_path_label.setObjectName(u"file_path_label")
        self.file_path_label.setGeometry(QRect(660, 670, 431, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.music_listWidget, self.cover_listWidget)
        QWidget.setTabOrder(self.cover_listWidget, self.music_lineEdit)
        QWidget.setTabOrder(self.music_lineEdit, self.singer_lineEdit)
        QWidget.setTabOrder(self.singer_lineEdit, self.al_lineEdit)
        QWidget.setTabOrder(self.al_lineEdit, self.save_pushButton)
        QWidget.setTabOrder(self.save_pushButton, self.search_pushButton)
        QWidget.setTabOrder(self.search_pushButton, self.viewfld_pushButton)
        QWidget.setTabOrder(self.viewfld_pushButton, self.about_pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u5c01\u9762\u7ba1\u7406\u5668", None))
        self.cover_label.setText(QCoreApplication.translate("MainWindow", u"\u5355\u51fb\u5217\u8868\u9879\u76ee\u4ee5\u6d4f\u89c8\u5c01\u9762...", None))
        self.viewfld_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939", None))
        self.about_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u4fe1\u606f", None))
        self.search_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.save_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5d4c\u5165\u5f53\u524d\u4e13\u8f91\u5c01\u9762", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u9762\u5c3a\u5bf8\uff1a", None))
        self.size_label.setText(QCoreApplication.translate("MainWindow", u"N\\A", None))
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6d4f\u89c8\u6587\u4ef6\u5939\uff01", None))
        self.count_label.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u9762\u6765\u81ea\uff1a\u7f51\u6613\u4e91\u97f3\u4e50", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u9762\u9884\u89c8\uff1a", None))
        self.file_path_label.setText("")
    # retranslateUi

