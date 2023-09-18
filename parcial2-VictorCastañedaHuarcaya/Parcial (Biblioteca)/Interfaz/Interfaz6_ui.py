# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz6.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(255, 239, 207);")
        self.aceptar = QPushButton(Form)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setGeometry(QRect(130, 240, 75, 24))
        self.aceptar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 180, 111, 31))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.id = QLineEdit(Form)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(210, 180, 151, 31))
        self.id.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cancelar = QPushButton(Form)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(220, 240, 75, 24))
        self.cancelar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 30, 101, 111))
        self.label_2.setPixmap(QPixmap(u"Imagenes usadas/d.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.aceptar.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Ingrese el ID:</span></p></body></html>", None))
        self.cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.label_2.setText("")
    # retranslateUi

