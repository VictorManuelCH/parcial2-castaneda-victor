# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 448)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 721, 451))
        self.label.setAutoFillBackground(True)
        self.label.setPixmap(QPixmap(u"Imagenes usadas/a.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(190, 10, 331, 431))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet(u"background-color: rgb(255, 159, 90);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 90, 131, 21))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 110, 171, 21))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 10, 81, 81))
        self.label_4.setPixmap(QPixmap(u"Imagenes usadas/c.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 150, 141, 31))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.registrar = QPushButton(self.frame)
        self.registrar.setObjectName(u"registrar")
        self.registrar.setGeometry(QRect(40, 160, 75, 24))
        self.registrar.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.editar = QPushButton(self.frame)
        self.editar.setObjectName(u"editar")
        self.editar.setGeometry(QRect(40, 200, 75, 24))
        self.editar.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.eliminar = QPushButton(self.frame)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(40, 250, 75, 24))
        self.eliminar.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.reporte = QPushButton(self.frame)
        self.reporte.setObjectName(u"reporte")
        self.reporte.setGeometry(QRect(40, 390, 75, 24))
        self.reporte.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 200, 141, 31))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 250, 141, 31))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 390, 141, 31))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 350, 141, 31))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.listar = QPushButton(self.frame)
        self.listar.setObjectName(u"listar")
        self.listar.setGeometry(QRect(40, 350, 75, 24))
        self.listar.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.reactivar = QPushButton(self.frame)
        self.reactivar.setObjectName(u"reactivar")
        self.reactivar.setGeometry(QRect(40, 300, 75, 24))
        self.reactivar.setStyleSheet(u"background-color: rgb(217, 70, 25);")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 300, 141, 31))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Hola, Bienvenido</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Que, desea hacer hoy?</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">A\u00f1adir un libro</span></p></body></html>", None))
        self.registrar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.editar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.eliminar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.reporte.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Editar un libro</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Eliminar un libro</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Generar Reporte</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Listar Libros</span></p></body></html>", None))
        self.listar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.reactivar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Reactivar un libro</span></p></body></html>", None))
    # retranslateUi

