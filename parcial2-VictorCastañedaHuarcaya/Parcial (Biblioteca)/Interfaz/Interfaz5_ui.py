# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz5.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(376, 226)
        Form.setStyleSheet(u"background-color: rgb(255, 239, 207);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 130, 291, 41))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.aceptar_1 = QPushButton(Form)
        self.aceptar_1.setObjectName(u"aceptar_1")
        self.aceptar_1.setGeometry(QRect(140, 180, 75, 24))
        self.aceptar_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 20, 101, 111))
        self.label_2.setPixmap(QPixmap(u"Imagenes usadas/d.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Reporte Generado con Exito</span></p></body></html>", None))
        self.aceptar_1.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.label_2.setText("")
    # retranslateUi

