import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 728)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Suisse Intl")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Icones/icone_showroom.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0.472, y1:0.523182, x2:0.466, y2:0, stop:0 rgba(137, 27, 40, 255), stop:1 rgba(219, 57, 70, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.btn_fechar = QToolButton(self.centralwidget)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fechar.setStyleSheet(u"border-radius: 15px;\n"
"border-width: 2px;")
        icon1 = QIcon()
        icon1.addFile(u"Icones/fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_fechar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 90))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 80))
        self.label_6.setMaximumSize(QSize(250, 80))
        self.label_6.setSizeIncrement(QSize(0, 0))
        self.label_6.setBaseSize(QSize(0, 0))
        self.label_6.setStyleSheet(u"background-color: transparent;")
        self.label_6.setPixmap(QPixmap(u"Icones/logo_renner.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(250, 80))
        self.label_3.setMaximumSize(QSize(250, 80))
        self.label_3.setSizeIncrement(QSize(0, 0))
        self.label_3.setBaseSize(QSize(0, 0))
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_3.setPixmap(QPixmap(u"Icones/Voice_of_Colour_TM_Vert_1_REV.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.Pages = QStackedWidget(self.frame_2)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy1)
        self.Pages.setMaximumSize(QSize(1600, 900))
        self.Pages.setLayoutDirection(Qt.LeftToRight)
        self.Pages.setAutoFillBackground(False)
        self.Pages.setStyleSheet(u"background-color: transparent;")
        self.Pages.setFrameShape(QFrame.NoFrame)
        self.Pages.setLineWidth(0)
        self.Pages.setMidLineWidth(0)
        self.pg_cor = QWidget()
        self.pg_cor.setObjectName(u"pg_cor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pg_cor.sizePolicy().hasHeightForWidth())
        self.pg_cor.setSizePolicy(sizePolicy2)
        self.pg_cor.setMaximumSize(QSize(16777215, 16777215))
        self.pg_cor.setLayoutDirection(Qt.LeftToRight)
        self.pg_cor.setAutoFillBackground(False)
        self.verticalLayout_7 = QVBoxLayout(self.pg_cor)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.pg_cor)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(1600, 900))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_9.setFont(font2)
        self.label_9.setPixmap(QPixmap(u"Icones/PPG-003622_sistema_tintometrico_telas_de_descanso_1.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(False)

        self.verticalLayout_7.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_cor)
        self.pg_cor_1 = QWidget()
        self.pg_cor_1.setObjectName(u"pg_cor_1")
        self.verticalLayout_3 = QVBoxLayout(self.pg_cor_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.pg_cor_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(1600, 900))
        self.label_5.setPixmap(QPixmap(u"Icones/PPG-003622_sistema_tintometrico_telas_de_descanso_2.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_5)

        self.Pages.addWidget(self.pg_cor_1)
        self.pg_cor_2 = QWidget()
        self.pg_cor_2.setObjectName(u"pg_cor_2")
        self.verticalLayout_5 = QVBoxLayout(self.pg_cor_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.pg_cor_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(1600, 900))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_10.setFont(font3)
        self.label_10.setPixmap(QPixmap(u"Icones/PPG-003622_sistema_tintometrico_telas_de_descanso_3.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)

        self.Pages.addWidget(self.pg_cor_2)
        self.pg_cor_3 = QWidget()
        self.pg_cor_3.setObjectName(u"pg_cor_3")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cor_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.pg_cor_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(1600, 900))
        self.label_11.setFont(font2)
        self.label_11.setPixmap(QPixmap(u"Icones/PPG-003622_sistema_tintometrico_telas_de_descanso_4.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_11)

        self.Pages.addWidget(self.pg_cor_3)
        self.pg_cor_4 = QWidget()
        self.pg_cor_4.setObjectName(u"pg_cor_4")
        sizePolicy1.setHeightForWidth(self.pg_cor_4.sizePolicy().hasHeightForWidth())
        self.pg_cor_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.pg_cor_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.pg_cor_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(1600, 900))
        self.label_2.setPixmap(QPixmap(u"Icones/PPG-003622_sistema_tintometrico_telas_de_descanso_5.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_2)

        self.Pages.addWidget(self.pg_cor_4)
        self.pg_cor_5 = QWidget()
        self.pg_cor_5.setObjectName(u"pg_cor_5")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_cor_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.pg_cor_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1600, 900))
        self.label.setPixmap(QPixmap(u"Icones/_1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.Pages.addWidget(self.pg_cor_5)
        self.pg_cor_6 = QWidget()
        self.pg_cor_6.setObjectName(u"pg_cor_6")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_cor_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.pg_cor_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(1600, 900))
        self.label_7.setPixmap(QPixmap(u"Icones/_2.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.Pages.addWidget(self.pg_cor_6)
        self.pg_cor7 = QWidget()
        self.pg_cor7.setObjectName(u"pg_cor7")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_cor7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_cor7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(1600, 900))
        self.label_8.setPixmap(QPixmap(u"Icones/_3.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.Pages.addWidget(self.pg_cor7)

        self.horizontalLayout_8.addWidget(self.Pages)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.btn_voltar = QToolButton(self.centralwidget)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet(u"border-radius: 15px;\n"
"border-width: 2px;")
        icon2 = QIcon()
        icon2.addFile(u"Icones/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voltar.setIcon(icon2)
        self.btn_voltar.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_voltar)

        self.btn_avancar = QToolButton(self.centralwidget)
        self.btn_avancar.setObjectName(u"btn_avancar")
        self.btn_avancar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_avancar.setStyleSheet(u"border-radius: 15px;\n"
"border-width: 2px;")
        icon3 = QIcon()
        icon3.addFile(u"Icones/avan\u00e7ar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_avancar.setIcon(icon3)
        self.btn_avancar.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.btn_avancar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btn_avancar.clicked.connect(lambda: self.switchPageUp())
        self.btn_voltar.clicked.connect(lambda: self.switchPageDown())
        self.btn_fechar.clicked.connect(self.close)
        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.switchPageUp)
        self.timer.start()

    def switchPageDown(self):
            index = self.Pages.currentIndex() - 1
            if index < 0:
                    index = 7
            self.Pages.setCurrentIndex(index)

    def switchPageUp(self):
            index = self.Pages.currentIndex() + 1
            if index == self.Pages.count():
                    index = 0
            self.Pages.setCurrentIndex(index)

    def close(self):
            self.close()

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            self.btn_fechar.setText(_translate("MainWindow", "..."))
            self.label_4.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">AO ACIONAR QUALQUER TECLA O SHOW ROOM SERÁ FINALIZADO</span></p></body></html>"))
            self.btn_voltar.setText(_translate("MainWindow", "..."))
            self.btn_avancar.setText(_translate("MainWindow", "..."))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
            QMainWindow.__init__(self, parent=parent)
            self.setupUi(self)
            QApplication.instance().installEventFilter(self)

    def eventFilter(self, obj, event):
            if event.type() == event.KeyPress:
                    QTimer.singleShot(0, QApplication.quit)
                    return True
            return super().eventFilter(obj, event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.showMaximized()
    sys.exit(app.exec_())