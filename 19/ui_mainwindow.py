# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(242, 178, 55, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(25, 42, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_01 = QPushButton(self.centralwidget)
        self.btn_01.setObjectName(u"btn_01")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_01.sizePolicy().hasHeightForWidth())
        self.btn_01.setSizePolicy(sizePolicy1)
        self.btn_01.setMinimumSize(QSize(111, 111))
        self.btn_01.setMaximumSize(QSize(333, 333))
        palette1 = QPalette()
        brush2 = QBrush(QColor(31, 53, 64, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(49, 196, 190, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_01.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(60)
        font.setBold(True)
        self.btn_01.setFont(font)
        self.btn_01.setFocusPolicy(Qt.StrongFocus)
        self.btn_01.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_01, 0, 0, 1, 1)

        self.btn_02 = QPushButton(self.centralwidget)
        self.btn_02.setObjectName(u"btn_02")
        sizePolicy1.setHeightForWidth(self.btn_02.sizePolicy().hasHeightForWidth())
        self.btn_02.setSizePolicy(sizePolicy1)
        self.btn_02.setMinimumSize(QSize(111, 111))
        self.btn_02.setMaximumSize(QSize(333, 333))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_02.setPalette(palette2)
        self.btn_02.setFont(font)
        self.btn_02.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_02, 0, 1, 1, 1)

        self.btn_03 = QPushButton(self.centralwidget)
        self.btn_03.setObjectName(u"btn_03")
        sizePolicy1.setHeightForWidth(self.btn_03.sizePolicy().hasHeightForWidth())
        self.btn_03.setSizePolicy(sizePolicy1)
        self.btn_03.setMinimumSize(QSize(111, 111))
        self.btn_03.setMaximumSize(QSize(333, 333))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_03.setPalette(palette3)
        self.btn_03.setFont(font)
        self.btn_03.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_03, 0, 2, 1, 1)

        self.btn_04 = QPushButton(self.centralwidget)
        self.btn_04.setObjectName(u"btn_04")
        sizePolicy1.setHeightForWidth(self.btn_04.sizePolicy().hasHeightForWidth())
        self.btn_04.setSizePolicy(sizePolicy1)
        self.btn_04.setMinimumSize(QSize(111, 111))
        self.btn_04.setMaximumSize(QSize(333, 333))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_04.setPalette(palette4)
        self.btn_04.setFont(font)
        self.btn_04.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_04, 0, 3, 1, 1)

        self.btn_05 = QPushButton(self.centralwidget)
        self.btn_05.setObjectName(u"btn_05")
        sizePolicy1.setHeightForWidth(self.btn_05.sizePolicy().hasHeightForWidth())
        self.btn_05.setSizePolicy(sizePolicy1)
        self.btn_05.setMinimumSize(QSize(111, 111))
        self.btn_05.setMaximumSize(QSize(333, 333))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_05.setPalette(palette5)
        self.btn_05.setFont(font)
        self.btn_05.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_05, 1, 0, 1, 1)

        self.btn_06 = QPushButton(self.centralwidget)
        self.btn_06.setObjectName(u"btn_06")
        sizePolicy1.setHeightForWidth(self.btn_06.sizePolicy().hasHeightForWidth())
        self.btn_06.setSizePolicy(sizePolicy1)
        self.btn_06.setMinimumSize(QSize(111, 111))
        self.btn_06.setMaximumSize(QSize(333, 333))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_06.setPalette(palette6)
        self.btn_06.setFont(font)
        self.btn_06.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_06, 1, 1, 1, 1)

        self.btn_07 = QPushButton(self.centralwidget)
        self.btn_07.setObjectName(u"btn_07")
        sizePolicy1.setHeightForWidth(self.btn_07.sizePolicy().hasHeightForWidth())
        self.btn_07.setSizePolicy(sizePolicy1)
        self.btn_07.setMinimumSize(QSize(111, 111))
        self.btn_07.setMaximumSize(QSize(333, 333))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_07.setPalette(palette7)
        self.btn_07.setFont(font)
        self.btn_07.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_07, 1, 2, 1, 1)

        self.btn_08 = QPushButton(self.centralwidget)
        self.btn_08.setObjectName(u"btn_08")
        sizePolicy1.setHeightForWidth(self.btn_08.sizePolicy().hasHeightForWidth())
        self.btn_08.setSizePolicy(sizePolicy1)
        self.btn_08.setMinimumSize(QSize(111, 111))
        self.btn_08.setMaximumSize(QSize(333, 333))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_08.setPalette(palette8)
        self.btn_08.setFont(font)
        self.btn_08.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_08, 1, 3, 1, 1)

        self.btn_09 = QPushButton(self.centralwidget)
        self.btn_09.setObjectName(u"btn_09")
        sizePolicy1.setHeightForWidth(self.btn_09.sizePolicy().hasHeightForWidth())
        self.btn_09.setSizePolicy(sizePolicy1)
        self.btn_09.setMinimumSize(QSize(111, 111))
        self.btn_09.setMaximumSize(QSize(333, 333))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_09.setPalette(palette9)
        self.btn_09.setFont(font)
        self.btn_09.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_09, 2, 0, 1, 1)

        self.btn_10 = QPushButton(self.centralwidget)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy1.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy1)
        self.btn_10.setMinimumSize(QSize(111, 111))
        self.btn_10.setMaximumSize(QSize(333, 333))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_10.setPalette(palette10)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_10, 2, 1, 1, 1)

        self.btn_11 = QPushButton(self.centralwidget)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy1.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy1)
        self.btn_11.setMinimumSize(QSize(111, 111))
        self.btn_11.setMaximumSize(QSize(333, 333))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_11.setPalette(palette11)
        self.btn_11.setFont(font)
        self.btn_11.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_11, 2, 2, 1, 1)

        self.btn_12 = QPushButton(self.centralwidget)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy1.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy1)
        self.btn_12.setMinimumSize(QSize(111, 111))
        self.btn_12.setMaximumSize(QSize(333, 333))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_12.setPalette(palette12)
        self.btn_12.setFont(font)
        self.btn_12.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_12, 2, 3, 1, 1)

        self.btn_13 = QPushButton(self.centralwidget)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy1.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy1)
        self.btn_13.setMinimumSize(QSize(111, 111))
        self.btn_13.setMaximumSize(QSize(333, 333))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_13.setPalette(palette13)
        self.btn_13.setFont(font)
        self.btn_13.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_13, 3, 0, 1, 1)

        self.btn_14 = QPushButton(self.centralwidget)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy1.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy1)
        self.btn_14.setMinimumSize(QSize(111, 111))
        self.btn_14.setMaximumSize(QSize(333, 333))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_14.setPalette(palette14)
        self.btn_14.setFont(font)
        self.btn_14.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_14, 3, 1, 1, 1)

        self.btn_15 = QPushButton(self.centralwidget)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy1.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy1)
        self.btn_15.setMinimumSize(QSize(111, 111))
        self.btn_15.setMaximumSize(QSize(333, 333))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_15.setPalette(palette15)
        self.btn_15.setFont(font)
        self.btn_15.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_15, 3, 2, 1, 1)

        self.btn_16 = QPushButton(self.centralwidget)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy1.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy1)
        self.btn_16.setMinimumSize(QSize(111, 111))
        self.btn_16.setMaximumSize(QSize(333, 333))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.btn_16.setPalette(palette16)
        self.btn_16.setFont(font)
        self.btn_16.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(31, 53, 64)\n"
"}")

        self.gridLayout.addWidget(self.btn_16, 3, 3, 1, 1)

        self.btn_17 = QPushButton(self.centralwidget)
        self.btn_17.setObjectName(u"btn_17")
        sizePolicy1.setHeightForWidth(self.btn_17.sizePolicy().hasHeightForWidth())
        self.btn_17.setSizePolicy(sizePolicy1)
        self.btn_17.setMinimumSize(QSize(111, 111))
        self.btn_17.setMaximumSize(QSize(333, 333))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_17.setFont(font1)
        self.btn_17.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(49, 196, 190)\n"
"}")

        self.gridLayout.addWidget(self.btn_17, 4, 0, 1, 1)

        self.btn_18 = QPushButton(self.centralwidget)
        self.btn_18.setObjectName(u"btn_18")
        sizePolicy1.setHeightForWidth(self.btn_18.sizePolicy().hasHeightForWidth())
        self.btn_18.setSizePolicy(sizePolicy1)
        self.btn_18.setMinimumSize(QSize(111, 111))
        self.btn_18.setMaximumSize(QSize(333, 333))
        self.btn_18.setFont(font1)
        self.btn_18.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(242, 178, 55)\n"
"}")

        self.gridLayout.addWidget(self.btn_18, 4, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"15_Puzzle", None))
        self.btn_01.setText("")
        self.btn_02.setText("")
        self.btn_03.setText("")
        self.btn_04.setText("")
        self.btn_05.setText("")
        self.btn_06.setText("")
        self.btn_07.setText("")
        self.btn_08.setText("")
        self.btn_09.setText("")
        self.btn_10.setText("")
        self.btn_11.setText("")
        self.btn_12.setText("")
        self.btn_13.setText("")
        self.btn_14.setText("")
        self.btn_15.setText("")
        self.btn_16.setText("")
        self.btn_17.setText(QCoreApplication.translate("MainWindow", u"YOU", None))
        self.btn_18.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
    # retranslateUi

