# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz2.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 433)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(360, 220, 271, 111))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 239, 207);\n"
"color: rgb(24, 24, 24);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 20, 91, 21))
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.genero = QLineEdit(self.frame_3)
        self.genero.setObjectName(u"genero")
        self.genero.setGeometry(QRect(150, 60, 113, 24))
        self.genero.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 60, 101, 21))
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 40, 271, 291))
        self.frame.setStyleSheet(u"background-color: rgb(255, 239, 207);\n"
"color: rgb(24, 24, 24);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 91, 21))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nombre = QLineEdit(self.frame)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(150, 60, 113, 24))
        self.nombre.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10000 = QLabel(self.frame)
        self.label_10000.setObjectName(u"label_10000")
        self.label_10000.setGeometry(QRect(10, 60, 101, 21))
        self.label_10000.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 101, 21))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 101, 21))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 121, 21))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fecha_nacimiento = QDateEdit(self.frame)
        self.fecha_nacimiento.setObjectName(u"fecha_nacimiento")
        self.fecha_nacimiento.setGeometry(QRect(150, 150, 110, 25))
        self.fecha_nacimiento.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.apellido_paterno = QLineEdit(self.frame)
        self.apellido_paterno.setObjectName(u"apellido_paterno")
        self.apellido_paterno.setGeometry(QRect(150, 90, 113, 24))
        self.apellido_paterno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.apellido_materno = QLineEdit(self.frame)
        self.apellido_materno.setObjectName(u"apellido_materno")
        self.apellido_materno.setGeometry(QRect(150, 120, 113, 24))
        self.apellido_materno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 190, 101, 21))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 230, 101, 21))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pais = QLineEdit(self.frame)
        self.pais.setObjectName(u"pais")
        self.pais.setGeometry(QRect(150, 190, 113, 24))
        self.pais.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.editorial = QLineEdit(self.frame)
        self.editorial.setObjectName(u"editorial")
        self.editorial.setGeometry(QRect(150, 230, 113, 24))
        self.editorial.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(360, 40, 271, 171))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 239, 207);\n"
"color: rgb(24, 24, 24);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 10, 91, 21))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.titulo = QLineEdit(self.frame_2)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(150, 40, 113, 24))
        self.titulo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 40, 101, 21))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 90, 101, 21))
        self.label_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 130, 121, 21))
        self.label_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fecha_publicacion = QDateEdit(self.frame_2)
        self.fecha_publicacion.setObjectName(u"fecha_publicacion")
        self.fecha_publicacion.setGeometry(QRect(150, 130, 110, 25))
        self.fecha_publicacion.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tomo = QLineEdit(self.frame_2)
        self.tomo.setObjectName(u"tomo")
        self.tomo.setGeometry(QRect(150, 90, 113, 24))
        self.tomo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 721, 451))
        self.label_17.setPixmap(QPixmap(u"Imagenes usadas/b.jpg"))
        self.label_17.setScaledContents(True)
        self.aceptar = QPushButton(self.centralwidget)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setGeometry(QRect(260, 370, 75, 24))
        self.aceptar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cancelar = QPushButton(self.centralwidget)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setGeometry(QRect(350, 370, 75, 24))
        self.cancelar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_17.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.aceptar.raise_()
        self.cancelar.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Categoria</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.genero.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.genero.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.genero.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Genero</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Datos del Autor</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.nombre.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.nombre.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.nombre.setText("")
        self.label_10000.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Nombre</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Apellido Paterno</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Apellido Materno</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Fecha de Nacimiento</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.apellido_paterno.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.apellido_paterno.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.apellido_paterno.setText("")
#if QT_CONFIG(tooltip)
        self.apellido_materno.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.apellido_materno.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.apellido_materno.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Pais</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Editorial</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pais.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pais.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pais.setText("")
#if QT_CONFIG(tooltip)
        self.editorial.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.editorial.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.editorial.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Datos del Libro</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.titulo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.titulo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.titulo.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Titulo</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Tomo</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#121212;\">Fecha de Publicacion</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.tomo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Hola</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tomo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tomo.setText("")
        self.label_17.setText("")
        self.aceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

