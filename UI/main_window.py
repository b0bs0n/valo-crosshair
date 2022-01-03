# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(541, 849)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 521, 766))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hlay_inner_opacity = QHBoxLayout()
        self.hlay_inner_opacity.setObjectName(u"hlay_inner_opacity")
        self.le_inner_opacity = QLineEdit(self.gridLayoutWidget)
        self.le_inner_opacity.setObjectName(u"le_inner_opacity")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_inner_opacity.sizePolicy().hasHeightForWidth())
        self.le_inner_opacity.setSizePolicy(sizePolicy1)
        self.le_inner_opacity.setMinimumSize(QSize(0, 0))
        self.le_inner_opacity.setMaximumSize(QSize(50, 16777215))
        self.le_inner_opacity.setAlignment(Qt.AlignCenter)
        self.le_inner_opacity.setReadOnly(False)

        self.hlay_inner_opacity.addWidget(self.le_inner_opacity)

        self.slide_inner_opacity = QSlider(self.gridLayoutWidget)
        self.slide_inner_opacity.setObjectName(u"slide_inner_opacity")
        self.slide_inner_opacity.setMinimumSize(QSize(230, 0))
        self.slide_inner_opacity.setMaximum(1000)
        self.slide_inner_opacity.setOrientation(Qt.Horizontal)
        self.slide_inner_opacity.setTickPosition(QSlider.TicksBelow)
        self.slide_inner_opacity.setTickInterval(100)

        self.hlay_inner_opacity.addWidget(self.slide_inner_opacity)


        self.gridLayout.addLayout(self.hlay_inner_opacity, 13, 1, 1, 2)

        self.btn_outline_on = QPushButton(self.gridLayoutWidget)
        self.btn_outline_on.setObjectName(u"btn_outline_on")
        self.btn_outline_on.setCheckable(True)
        self.btn_outline_on.setChecked(True)
        self.btn_outline_on.setAutoDefault(False)
        self.btn_outline_on.setFlat(False)

        self.gridLayout.addWidget(self.btn_outline_on, 4, 1, 1, 1)

        self.lbl_outline_opacity = QLabel(self.gridLayoutWidget)
        self.lbl_outline_opacity.setObjectName(u"lbl_outline_opacity")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_outline_opacity.sizePolicy().hasHeightForWidth())
        self.lbl_outline_opacity.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outline_opacity, 5, 0, 1, 1)

        self.lbl_crosshair_color = QLabel(self.gridLayoutWidget)
        self.lbl_crosshair_color.setObjectName(u"lbl_crosshair_color")
        sizePolicy2.setHeightForWidth(self.lbl_crosshair_color.sizePolicy().hasHeightForWidth())
        self.lbl_crosshair_color.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_crosshair_color, 3, 0, 1, 1)

        self.lbl_inner_lines_offset = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_offset.setObjectName(u"lbl_inner_lines_offset")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_offset.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_offset.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_offset, 16, 0, 1, 1)

        self.hlay_inner_offset = QHBoxLayout()
        self.hlay_inner_offset.setObjectName(u"hlay_inner_offset")
        self.le_inner_offset = QLineEdit(self.gridLayoutWidget)
        self.le_inner_offset.setObjectName(u"le_inner_offset")
        sizePolicy1.setHeightForWidth(self.le_inner_offset.sizePolicy().hasHeightForWidth())
        self.le_inner_offset.setSizePolicy(sizePolicy1)
        self.le_inner_offset.setMinimumSize(QSize(0, 0))
        self.le_inner_offset.setMaximumSize(QSize(50, 16777215))
        self.le_inner_offset.setAlignment(Qt.AlignCenter)
        self.le_inner_offset.setReadOnly(False)

        self.hlay_inner_offset.addWidget(self.le_inner_offset)

        self.slide_inner_offset = QSlider(self.gridLayoutWidget)
        self.slide_inner_offset.setObjectName(u"slide_inner_offset")
        self.slide_inner_offset.setMinimumSize(QSize(230, 0))
        self.slide_inner_offset.setMinimum(0)
        self.slide_inner_offset.setMaximum(20)
        self.slide_inner_offset.setOrientation(Qt.Horizontal)
        self.slide_inner_offset.setTickPosition(QSlider.TicksBelow)
        self.slide_inner_offset.setTickInterval(1)

        self.hlay_inner_offset.addWidget(self.slide_inner_offset)


        self.gridLayout.addLayout(self.hlay_inner_offset, 16, 1, 1, 2)

        self.hlay_outer_thck = QHBoxLayout()
        self.hlay_outer_thck.setObjectName(u"hlay_outer_thck")
        self.le_outer_thck = QLineEdit(self.gridLayoutWidget)
        self.le_outer_thck.setObjectName(u"le_outer_thck")
        sizePolicy1.setHeightForWidth(self.le_outer_thck.sizePolicy().hasHeightForWidth())
        self.le_outer_thck.setSizePolicy(sizePolicy1)
        self.le_outer_thck.setMinimumSize(QSize(0, 0))
        self.le_outer_thck.setMaximumSize(QSize(50, 16777215))
        self.le_outer_thck.setAlignment(Qt.AlignCenter)
        self.le_outer_thck.setReadOnly(False)

        self.hlay_outer_thck.addWidget(self.le_outer_thck)

        self.slide_outer_thck = QSlider(self.gridLayoutWidget)
        self.slide_outer_thck.setObjectName(u"slide_outer_thck")
        self.slide_outer_thck.setMinimumSize(QSize(230, 0))
        self.slide_outer_thck.setMinimum(0)
        self.slide_outer_thck.setMaximum(10)
        self.slide_outer_thck.setOrientation(Qt.Horizontal)
        self.slide_outer_thck.setTickPosition(QSlider.TicksBelow)
        self.slide_outer_thck.setTickInterval(1)

        self.hlay_outer_thck.addWidget(self.slide_outer_thck)


        self.gridLayout.addLayout(self.hlay_outer_thck, 21, 1, 1, 2)

        self.lbl_ch_select = QLabel(self.gridLayoutWidget)
        self.lbl_ch_select.setObjectName(u"lbl_ch_select")
        sizePolicy2.setHeightForWidth(self.lbl_ch_select.sizePolicy().hasHeightForWidth())
        self.lbl_ch_select.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_ch_select, 1, 0, 1, 1)

        self.btn_outer_on = QPushButton(self.gridLayoutWidget)
        self.btn_outer_on.setObjectName(u"btn_outer_on")
        self.btn_outer_on.setCheckable(True)
        self.btn_outer_on.setChecked(True)
        self.btn_outer_on.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_outer_on, 18, 1, 1, 1)

        self.hlay_outer_offset = QHBoxLayout()
        self.hlay_outer_offset.setObjectName(u"hlay_outer_offset")
        self.le_outer_offset = QLineEdit(self.gridLayoutWidget)
        self.le_outer_offset.setObjectName(u"le_outer_offset")
        sizePolicy1.setHeightForWidth(self.le_outer_offset.sizePolicy().hasHeightForWidth())
        self.le_outer_offset.setSizePolicy(sizePolicy1)
        self.le_outer_offset.setMinimumSize(QSize(0, 0))
        self.le_outer_offset.setMaximumSize(QSize(50, 16777215))
        self.le_outer_offset.setAlignment(Qt.AlignCenter)
        self.le_outer_offset.setReadOnly(False)

        self.hlay_outer_offset.addWidget(self.le_outer_offset)

        self.slide_outer_offset = QSlider(self.gridLayoutWidget)
        self.slide_outer_offset.setObjectName(u"slide_outer_offset")
        self.slide_outer_offset.setMinimumSize(QSize(230, 0))
        self.slide_outer_offset.setMinimum(0)
        self.slide_outer_offset.setMaximum(20)
        self.slide_outer_offset.setOrientation(Qt.Horizontal)
        self.slide_outer_offset.setTickPosition(QSlider.TicksBelow)
        self.slide_outer_offset.setTickInterval(1)

        self.hlay_outer_offset.addWidget(self.slide_outer_offset)


        self.gridLayout.addLayout(self.hlay_outer_offset, 22, 1, 1, 2)

        self.hlay_outer_opacity = QHBoxLayout()
        self.hlay_outer_opacity.setObjectName(u"hlay_outer_opacity")
        self.le_outer_opacity = QLineEdit(self.gridLayoutWidget)
        self.le_outer_opacity.setObjectName(u"le_outer_opacity")
        sizePolicy1.setHeightForWidth(self.le_outer_opacity.sizePolicy().hasHeightForWidth())
        self.le_outer_opacity.setSizePolicy(sizePolicy1)
        self.le_outer_opacity.setMinimumSize(QSize(0, 0))
        self.le_outer_opacity.setMaximumSize(QSize(50, 16777215))
        self.le_outer_opacity.setAlignment(Qt.AlignCenter)
        self.le_outer_opacity.setReadOnly(False)

        self.hlay_outer_opacity.addWidget(self.le_outer_opacity)

        self.slide_outer_opacity = QSlider(self.gridLayoutWidget)
        self.slide_outer_opacity.setObjectName(u"slide_outer_opacity")
        self.slide_outer_opacity.setMinimumSize(QSize(230, 0))
        self.slide_outer_opacity.setMaximum(1000)
        self.slide_outer_opacity.setOrientation(Qt.Horizontal)
        self.slide_outer_opacity.setTickPosition(QSlider.TicksBelow)
        self.slide_outer_opacity.setTickInterval(100)

        self.hlay_outer_opacity.addWidget(self.slide_outer_opacity)


        self.gridLayout.addLayout(self.hlay_outer_opacity, 19, 1, 1, 2)

        self.hlay_inner_length = QHBoxLayout()
        self.hlay_inner_length.setObjectName(u"hlay_inner_length")
        self.le_inner_length = QLineEdit(self.gridLayoutWidget)
        self.le_inner_length.setObjectName(u"le_inner_length")
        sizePolicy1.setHeightForWidth(self.le_inner_length.sizePolicy().hasHeightForWidth())
        self.le_inner_length.setSizePolicy(sizePolicy1)
        self.le_inner_length.setMinimumSize(QSize(0, 0))
        self.le_inner_length.setMaximumSize(QSize(50, 16777215))
        self.le_inner_length.setAlignment(Qt.AlignCenter)
        self.le_inner_length.setReadOnly(False)

        self.hlay_inner_length.addWidget(self.le_inner_length)

        self.slide_inner_length = QSlider(self.gridLayoutWidget)
        self.slide_inner_length.setObjectName(u"slide_inner_length")
        self.slide_inner_length.setMinimumSize(QSize(230, 0))
        self.slide_inner_length.setMinimum(0)
        self.slide_inner_length.setMaximum(20)
        self.slide_inner_length.setOrientation(Qt.Horizontal)
        self.slide_inner_length.setTickPosition(QSlider.TicksBelow)
        self.slide_inner_length.setTickInterval(1)

        self.hlay_inner_length.addWidget(self.slide_inner_length)


        self.gridLayout.addLayout(self.hlay_inner_length, 14, 1, 1, 2)

        self.lbl_stretch_res = QLabel(self.gridLayoutWidget)
        self.lbl_stretch_res.setObjectName(u"lbl_stretch_res")

        self.gridLayout.addWidget(self.lbl_stretch_res, 24, 0, 1, 1)

        self.btn_outline_off = QPushButton(self.gridLayoutWidget)
        self.btn_outline_off.setObjectName(u"btn_outline_off")
        self.btn_outline_off.setCheckable(True)
        self.btn_outline_off.setChecked(False)
        self.btn_outline_off.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_outline_off, 4, 2, 1, 1)

        self.hlay_outline_opacity = QHBoxLayout()
        self.hlay_outline_opacity.setObjectName(u"hlay_outline_opacity")
        self.le_outline_opacity = QLineEdit(self.gridLayoutWidget)
        self.le_outline_opacity.setObjectName(u"le_outline_opacity")
        sizePolicy1.setHeightForWidth(self.le_outline_opacity.sizePolicy().hasHeightForWidth())
        self.le_outline_opacity.setSizePolicy(sizePolicy1)
        self.le_outline_opacity.setMinimumSize(QSize(0, 0))
        self.le_outline_opacity.setMaximumSize(QSize(50, 16777215))
        self.le_outline_opacity.setAlignment(Qt.AlignCenter)
        self.le_outline_opacity.setReadOnly(False)

        self.hlay_outline_opacity.addWidget(self.le_outline_opacity)

        self.slide_outline_opacity = QSlider(self.gridLayoutWidget)
        self.slide_outline_opacity.setObjectName(u"slide_outline_opacity")
        self.slide_outline_opacity.setMinimumSize(QSize(230, 0))
        self.slide_outline_opacity.setMaximum(1000)
        self.slide_outline_opacity.setOrientation(Qt.Horizontal)
        self.slide_outline_opacity.setTickPosition(QSlider.TicksBelow)
        self.slide_outline_opacity.setTickInterval(100)

        self.hlay_outline_opacity.addWidget(self.slide_outline_opacity)


        self.gridLayout.addLayout(self.hlay_outline_opacity, 5, 1, 1, 2)

        self.btn_inner_on = QPushButton(self.gridLayoutWidget)
        self.btn_inner_on.setObjectName(u"btn_inner_on")
        self.btn_inner_on.setCheckable(True)
        self.btn_inner_on.setChecked(True)
        self.btn_inner_on.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_inner_on, 12, 1, 1, 1)

        self.lbl_inner_lines_length = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_length.setObjectName(u"lbl_inner_lines_length")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_length.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_length.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_length, 14, 0, 1, 1)

        self.lbl_inner_lines_thck = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_thck.setObjectName(u"lbl_inner_lines_thck")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_thck.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_thck.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_thck, 15, 0, 1, 1)

        self.lbl_outer_lines_offset = QLabel(self.gridLayoutWidget)
        self.lbl_outer_lines_offset.setObjectName(u"lbl_outer_lines_offset")
        sizePolicy2.setHeightForWidth(self.lbl_outer_lines_offset.sizePolicy().hasHeightForWidth())
        self.lbl_outer_lines_offset.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outer_lines_offset, 22, 0, 1, 1)

        self.lbl_inner_lines_length_2 = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_length_2.setObjectName(u"lbl_inner_lines_length_2")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_length_2.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_length_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_length_2, 20, 0, 1, 1)

        self.btn_outer_off = QPushButton(self.gridLayoutWidget)
        self.btn_outer_off.setObjectName(u"btn_outer_off")
        self.btn_outer_off.setCheckable(True)
        self.btn_outer_off.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_outer_off, 18, 2, 1, 1)

        self.hlay_inner_thck = QHBoxLayout()
        self.hlay_inner_thck.setObjectName(u"hlay_inner_thck")
        self.le_inner_thck = QLineEdit(self.gridLayoutWidget)
        self.le_inner_thck.setObjectName(u"le_inner_thck")
        sizePolicy1.setHeightForWidth(self.le_inner_thck.sizePolicy().hasHeightForWidth())
        self.le_inner_thck.setSizePolicy(sizePolicy1)
        self.le_inner_thck.setMinimumSize(QSize(0, 0))
        self.le_inner_thck.setMaximumSize(QSize(50, 16777215))
        self.le_inner_thck.setAlignment(Qt.AlignCenter)
        self.le_inner_thck.setReadOnly(False)

        self.hlay_inner_thck.addWidget(self.le_inner_thck)

        self.slide_inner_thck = QSlider(self.gridLayoutWidget)
        self.slide_inner_thck.setObjectName(u"slide_inner_thck")
        self.slide_inner_thck.setMinimumSize(QSize(230, 0))
        self.slide_inner_thck.setMinimum(0)
        self.slide_inner_thck.setMaximum(10)
        self.slide_inner_thck.setOrientation(Qt.Horizontal)
        self.slide_inner_thck.setTickPosition(QSlider.TicksBelow)
        self.slide_inner_thck.setTickInterval(1)

        self.hlay_inner_thck.addWidget(self.slide_inner_thck)


        self.gridLayout.addLayout(self.hlay_inner_thck, 15, 1, 1, 2)

        self.lbl_outer_lines_thck = QLabel(self.gridLayoutWidget)
        self.lbl_outer_lines_thck.setObjectName(u"lbl_outer_lines_thck")
        sizePolicy2.setHeightForWidth(self.lbl_outer_lines_thck.sizePolicy().hasHeightForWidth())
        self.lbl_outer_lines_thck.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outer_lines_thck, 21, 0, 1, 1)

        self.hlay_dot_thck = QHBoxLayout()
        self.hlay_dot_thck.setObjectName(u"hlay_dot_thck")
        self.le_dot_thck = QLineEdit(self.gridLayoutWidget)
        self.le_dot_thck.setObjectName(u"le_dot_thck")
        sizePolicy1.setHeightForWidth(self.le_dot_thck.sizePolicy().hasHeightForWidth())
        self.le_dot_thck.setSizePolicy(sizePolicy1)
        self.le_dot_thck.setMinimumSize(QSize(0, 0))
        self.le_dot_thck.setMaximumSize(QSize(50, 16777215))
        self.le_dot_thck.setAlignment(Qt.AlignCenter)
        self.le_dot_thck.setReadOnly(False)

        self.hlay_dot_thck.addWidget(self.le_dot_thck)

        self.slide_dot_thck = QSlider(self.gridLayoutWidget)
        self.slide_dot_thck.setObjectName(u"slide_dot_thck")
        self.slide_dot_thck.setMinimumSize(QSize(230, 0))
        self.slide_dot_thck.setMinimum(1)
        self.slide_dot_thck.setMaximum(6)
        self.slide_dot_thck.setOrientation(Qt.Horizontal)
        self.slide_dot_thck.setTickPosition(QSlider.TicksBelow)
        self.slide_dot_thck.setTickInterval(1)

        self.hlay_dot_thck.addWidget(self.slide_dot_thck)


        self.gridLayout.addLayout(self.hlay_dot_thck, 9, 1, 1, 2)

        self.hlay_outline_thck = QHBoxLayout()
        self.hlay_outline_thck.setObjectName(u"hlay_outline_thck")
        self.le_outline_thck = QLineEdit(self.gridLayoutWidget)
        self.le_outline_thck.setObjectName(u"le_outline_thck")
        sizePolicy1.setHeightForWidth(self.le_outline_thck.sizePolicy().hasHeightForWidth())
        self.le_outline_thck.setSizePolicy(sizePolicy1)
        self.le_outline_thck.setMinimumSize(QSize(0, 0))
        self.le_outline_thck.setMaximumSize(QSize(50, 16777215))
        self.le_outline_thck.setAlignment(Qt.AlignCenter)
        self.le_outline_thck.setReadOnly(False)

        self.hlay_outline_thck.addWidget(self.le_outline_thck)

        self.slide_outline_thck = QSlider(self.gridLayoutWidget)
        self.slide_outline_thck.setObjectName(u"slide_outline_thck")
        self.slide_outline_thck.setMinimumSize(QSize(230, 0))
        self.slide_outline_thck.setMinimum(1)
        self.slide_outline_thck.setMaximum(6)
        self.slide_outline_thck.setOrientation(Qt.Horizontal)
        self.slide_outline_thck.setTickPosition(QSlider.TicksBelow)
        self.slide_outline_thck.setTickInterval(1)

        self.hlay_outline_thck.addWidget(self.slide_outline_thck)


        self.gridLayout.addLayout(self.hlay_outline_thck, 6, 1, 1, 2)

        self.qcb_crosshair_color = QComboBox(self.gridLayoutWidget)
        self.qcb_crosshair_color.setObjectName(u"qcb_crosshair_color")

        self.gridLayout.addWidget(self.qcb_crosshair_color, 3, 1, 1, 2)

        self.lbl_outer_lines_show = QLabel(self.gridLayoutWidget)
        self.lbl_outer_lines_show.setObjectName(u"lbl_outer_lines_show")
        sizePolicy2.setHeightForWidth(self.lbl_outer_lines_show.sizePolicy().hasHeightForWidth())
        self.lbl_outer_lines_show.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outer_lines_show, 18, 0, 1, 1)

        self.btn_dot_off = QPushButton(self.gridLayoutWidget)
        self.btn_dot_off.setObjectName(u"btn_dot_off")
        self.btn_dot_off.setCheckable(True)
        self.btn_dot_off.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_dot_off, 7, 2, 1, 1)

        self.lbl_inner_lines_show = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_show.setObjectName(u"lbl_inner_lines_show")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_show.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_show.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_show, 12, 0, 1, 1)

        self.lbl_outer_lines = QLabel(self.gridLayoutWidget)
        self.lbl_outer_lines.setObjectName(u"lbl_outer_lines")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_outer_lines.sizePolicy().hasHeightForWidth())
        self.lbl_outer_lines.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(12)
        self.lbl_outer_lines.setFont(font)
        self.lbl_outer_lines.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.lbl_outer_lines, 17, 0, 1, 3)

        self.lbl_outlines = QLabel(self.gridLayoutWidget)
        self.lbl_outlines.setObjectName(u"lbl_outlines")
        sizePolicy2.setHeightForWidth(self.lbl_outlines.sizePolicy().hasHeightForWidth())
        self.lbl_outlines.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outlines, 4, 0, 1, 1)

        self.btn_inner_off = QPushButton(self.gridLayoutWidget)
        self.btn_inner_off.setObjectName(u"btn_inner_off")
        self.btn_inner_off.setCheckable(True)
        self.btn_inner_off.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_inner_off, 12, 2, 1, 1)

        self.hlay_dot_opacity = QHBoxLayout()
        self.hlay_dot_opacity.setObjectName(u"hlay_dot_opacity")
        self.le_dot_opacity = QLineEdit(self.gridLayoutWidget)
        self.le_dot_opacity.setObjectName(u"le_dot_opacity")
        sizePolicy1.setHeightForWidth(self.le_dot_opacity.sizePolicy().hasHeightForWidth())
        self.le_dot_opacity.setSizePolicy(sizePolicy1)
        self.le_dot_opacity.setMinimumSize(QSize(0, 0))
        self.le_dot_opacity.setMaximumSize(QSize(50, 16777215))
        self.le_dot_opacity.setAlignment(Qt.AlignCenter)
        self.le_dot_opacity.setReadOnly(False)

        self.hlay_dot_opacity.addWidget(self.le_dot_opacity)

        self.slide_dot_opacity = QSlider(self.gridLayoutWidget)
        self.slide_dot_opacity.setObjectName(u"slide_dot_opacity")
        self.slide_dot_opacity.setMinimumSize(QSize(230, 0))
        self.slide_dot_opacity.setMaximum(1000)
        self.slide_dot_opacity.setOrientation(Qt.Horizontal)
        self.slide_dot_opacity.setTickPosition(QSlider.TicksBelow)
        self.slide_dot_opacity.setTickInterval(100)

        self.hlay_dot_opacity.addWidget(self.slide_dot_opacity)


        self.gridLayout.addLayout(self.hlay_dot_opacity, 8, 1, 1, 2)

        self.hlay_ch_select = QHBoxLayout()
        self.hlay_ch_select.setObjectName(u"hlay_ch_select")
        self.qcb_ch_select = QComboBox(self.gridLayoutWidget)
        self.qcb_ch_select.setObjectName(u"qcb_ch_select")
        self.qcb_ch_select.setMaximumSize(QSize(300, 16777215))

        self.hlay_ch_select.addWidget(self.qcb_ch_select)

        self.qgv_crosshair = QGraphicsView(self.gridLayoutWidget)
        self.qgv_crosshair.setObjectName(u"qgv_crosshair")
        sizePolicy.setHeightForWidth(self.qgv_crosshair.sizePolicy().hasHeightForWidth())
        self.qgv_crosshair.setSizePolicy(sizePolicy)
        self.qgv_crosshair.setMinimumSize(QSize(50, 50))
        self.qgv_crosshair.setMaximumSize(QSize(50, 50))
        self.qgv_crosshair.setBaseSize(QSize(50, 50))
        self.qgv_crosshair.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.qgv_crosshair.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.hlay_ch_select.addWidget(self.qgv_crosshair)


        self.gridLayout.addLayout(self.hlay_ch_select, 1, 1, 1, 2)

        self.lbl_outer_lines_opacity = QLabel(self.gridLayoutWidget)
        self.lbl_outer_lines_opacity.setObjectName(u"lbl_outer_lines_opacity")
        sizePolicy2.setHeightForWidth(self.lbl_outer_lines_opacity.sizePolicy().hasHeightForWidth())
        self.lbl_outer_lines_opacity.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outer_lines_opacity, 19, 0, 1, 1)

        self.lbl_center_dot_thck = QLabel(self.gridLayoutWidget)
        self.lbl_center_dot_thck.setObjectName(u"lbl_center_dot_thck")
        sizePolicy2.setHeightForWidth(self.lbl_center_dot_thck.sizePolicy().hasHeightForWidth())
        self.lbl_center_dot_thck.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_center_dot_thck, 9, 0, 1, 1)

        self.btn_dot_on = QPushButton(self.gridLayoutWidget)
        self.btn_dot_on.setObjectName(u"btn_dot_on")
        self.btn_dot_on.setCheckable(True)
        self.btn_dot_on.setChecked(True)
        self.btn_dot_on.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_dot_on, 7, 1, 1, 1)

        self.lbl_center_dot_opacity = QLabel(self.gridLayoutWidget)
        self.lbl_center_dot_opacity.setObjectName(u"lbl_center_dot_opacity")
        sizePolicy2.setHeightForWidth(self.lbl_center_dot_opacity.sizePolicy().hasHeightForWidth())
        self.lbl_center_dot_opacity.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_center_dot_opacity, 8, 0, 1, 1)

        self.lbl_center_dot = QLabel(self.gridLayoutWidget)
        self.lbl_center_dot.setObjectName(u"lbl_center_dot")
        sizePolicy2.setHeightForWidth(self.lbl_center_dot.sizePolicy().hasHeightForWidth())
        self.lbl_center_dot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_center_dot, 7, 0, 1, 1)

        self.lbl_inner_lines_opacity = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines_opacity.setObjectName(u"lbl_inner_lines_opacity")
        sizePolicy2.setHeightForWidth(self.lbl_inner_lines_opacity.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines_opacity.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_inner_lines_opacity, 13, 0, 1, 1)

        self.lbl_outline_thck = QLabel(self.gridLayoutWidget)
        self.lbl_outline_thck.setObjectName(u"lbl_outline_thck")
        sizePolicy2.setHeightForWidth(self.lbl_outline_thck.sizePolicy().hasHeightForWidth())
        self.lbl_outline_thck.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lbl_outline_thck, 6, 0, 1, 1)

        self.hlay_outer_length = QHBoxLayout()
        self.hlay_outer_length.setObjectName(u"hlay_outer_length")
        self.le_outer_length = QLineEdit(self.gridLayoutWidget)
        self.le_outer_length.setObjectName(u"le_outer_length")
        sizePolicy1.setHeightForWidth(self.le_outer_length.sizePolicy().hasHeightForWidth())
        self.le_outer_length.setSizePolicy(sizePolicy1)
        self.le_outer_length.setMinimumSize(QSize(0, 0))
        self.le_outer_length.setMaximumSize(QSize(50, 16777215))
        self.le_outer_length.setAlignment(Qt.AlignCenter)
        self.le_outer_length.setReadOnly(False)

        self.hlay_outer_length.addWidget(self.le_outer_length)

        self.slide_outer_length = QSlider(self.gridLayoutWidget)
        self.slide_outer_length.setObjectName(u"slide_outer_length")
        self.slide_outer_length.setMinimumSize(QSize(230, 0))
        self.slide_outer_length.setMinimum(0)
        self.slide_outer_length.setMaximum(20)
        self.slide_outer_length.setOrientation(Qt.Horizontal)
        self.slide_outer_length.setTickPosition(QSlider.TicksBelow)
        self.slide_outer_length.setTickInterval(1)

        self.hlay_outer_length.addWidget(self.slide_outer_length)


        self.gridLayout.addLayout(self.hlay_outer_length, 20, 1, 1, 2)

        self.lbl_crosshair = QLabel(self.gridLayoutWidget)
        self.lbl_crosshair.setObjectName(u"lbl_crosshair")
        sizePolicy3.setHeightForWidth(self.lbl_crosshair.sizePolicy().hasHeightForWidth())
        self.lbl_crosshair.setSizePolicy(sizePolicy3)
        self.lbl_crosshair.setFont(font)
        self.lbl_crosshair.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.lbl_crosshair, 2, 0, 1, 3)

        self.lbl_inner_lines = QLabel(self.gridLayoutWidget)
        self.lbl_inner_lines.setObjectName(u"lbl_inner_lines")
        sizePolicy3.setHeightForWidth(self.lbl_inner_lines.sizePolicy().hasHeightForWidth())
        self.lbl_inner_lines.setSizePolicy(sizePolicy3)
        self.lbl_inner_lines.setFont(font)
        self.lbl_inner_lines.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.lbl_inner_lines, 10, 0, 1, 3)

        self.lbl_screen_stretch = QLabel(self.gridLayoutWidget)
        self.lbl_screen_stretch.setObjectName(u"lbl_screen_stretch")
        self.lbl_screen_stretch.setFont(font)

        self.gridLayout.addWidget(self.lbl_screen_stretch, 23, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_res_screen_w = QLineEdit(self.gridLayoutWidget)
        self.le_res_screen_w.setObjectName(u"le_res_screen_w")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.le_res_screen_w.sizePolicy().hasHeightForWidth())
        self.le_res_screen_w.setSizePolicy(sizePolicy4)
        self.le_res_screen_w.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_res_screen_w)

        self.le_res_screen_h = QLineEdit(self.gridLayoutWidget)
        self.le_res_screen_h.setObjectName(u"le_res_screen_h")
        sizePolicy4.setHeightForWidth(self.le_res_screen_h.sizePolicy().hasHeightForWidth())
        self.le_res_screen_h.setSizePolicy(sizePolicy4)
        self.le_res_screen_h.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_res_screen_h)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.le_res_game_w = QLineEdit(self.gridLayoutWidget)
        self.le_res_game_w.setObjectName(u"le_res_game_w")
        sizePolicy4.setHeightForWidth(self.le_res_game_w.sizePolicy().hasHeightForWidth())
        self.le_res_game_w.setSizePolicy(sizePolicy4)
        self.le_res_game_w.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_res_game_w)

        self.le_res_game_h = QLineEdit(self.gridLayoutWidget)
        self.le_res_game_h.setObjectName(u"le_res_game_h")
        sizePolicy4.setHeightForWidth(self.le_res_game_h.sizePolicy().hasHeightForWidth())
        self.le_res_game_h.setSizePolicy(sizePolicy4)
        self.le_res_game_h.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_res_game_h)

        self.btn_stretch_apply = QPushButton(self.gridLayoutWidget)
        self.btn_stretch_apply.setObjectName(u"btn_stretch_apply")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_stretch_apply.sizePolicy().hasHeightForWidth())
        self.btn_stretch_apply.setSizePolicy(sizePolicy5)
        self.btn_stretch_apply.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.btn_stretch_apply)


        self.gridLayout.addLayout(self.horizontalLayout, 24, 1, 1, 2)

        self.btn_save_ch = QPushButton(self.centralwidget)
        self.btn_save_ch.setObjectName(u"btn_save_ch")
        self.btn_save_ch.setGeometry(QRect(10, 800, 141, 41))
        self.lbl_link = QLabel(self.centralwidget)
        self.lbl_link.setObjectName(u"lbl_link")
        self.lbl_link.setGeometry(QRect(280, 820, 241, 20))
        self.lbl_link.setTextFormat(Qt.RichText)
        self.lbl_link.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_link.setOpenExternalLinks(True)
        self.btn_del_ch = QPushButton(self.centralwidget)
        self.btn_del_ch.setObjectName(u"btn_del_ch")
        self.btn_del_ch.setGeometry(QRect(180, 800, 141, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_outline_on.setDefault(False)
        self.btn_outer_on.setDefault(False)
        self.btn_outline_off.setDefault(False)
        self.btn_inner_on.setDefault(False)
        self.btn_dot_on.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crosshair Manager", None))
        self.le_inner_opacity.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.btn_outline_on.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.lbl_outline_opacity.setText(QCoreApplication.translate("MainWindow", u"Outline Opacity", None))
        self.lbl_crosshair_color.setText(QCoreApplication.translate("MainWindow", u"Crosshair Color", None))
        self.lbl_inner_lines_offset.setText(QCoreApplication.translate("MainWindow", u"Inner Lines Offset", None))
        self.le_inner_offset.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_outer_thck.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_ch_select.setText(QCoreApplication.translate("MainWindow", u"Select Crosshair", None))
        self.btn_outer_on.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.le_outer_offset.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_outer_opacity.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.le_inner_length.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_stretch_res.setText(QCoreApplication.translate("MainWindow", u"Screen Res / Game Res", None))
        self.btn_outline_off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.le_outline_opacity.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.btn_inner_on.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.lbl_inner_lines_length.setText(QCoreApplication.translate("MainWindow", u"Inner Lines Length", None))
        self.lbl_inner_lines_thck.setText(QCoreApplication.translate("MainWindow", u"Inner Lines Thiccness", None))
        self.lbl_outer_lines_offset.setText(QCoreApplication.translate("MainWindow", u"Outer Lines Offset", None))
        self.lbl_inner_lines_length_2.setText(QCoreApplication.translate("MainWindow", u"Outer Lines Length", None))
        self.btn_outer_off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.le_inner_thck.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_outer_lines_thck.setText(QCoreApplication.translate("MainWindow", u"Outer Lines Thiccness", None))
        self.le_dot_thck.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_outline_thck.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_outer_lines_show.setText(QCoreApplication.translate("MainWindow", u"Show Outer Lines", None))
        self.btn_dot_off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.lbl_inner_lines_show.setText(QCoreApplication.translate("MainWindow", u"Show Inner Lines", None))
        self.lbl_outer_lines.setText(QCoreApplication.translate("MainWindow", u"Outer Lines", None))
        self.lbl_outlines.setText(QCoreApplication.translate("MainWindow", u"Outlines", None))
        self.btn_inner_off.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.le_dot_opacity.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.lbl_outer_lines_opacity.setText(QCoreApplication.translate("MainWindow", u"Outer Lines Opacity", None))
        self.lbl_center_dot_thck.setText(QCoreApplication.translate("MainWindow", u"Center Dot Thiccness", None))
        self.btn_dot_on.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.lbl_center_dot_opacity.setText(QCoreApplication.translate("MainWindow", u"Center Dot Opacity", None))
        self.lbl_center_dot.setText(QCoreApplication.translate("MainWindow", u"Center Dot", None))
        self.lbl_inner_lines_opacity.setText(QCoreApplication.translate("MainWindow", u"Inner Lines Opacity", None))
        self.lbl_outline_thck.setText(QCoreApplication.translate("MainWindow", u"Outline Thiccness", None))
        self.le_outer_length.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_crosshair.setText(QCoreApplication.translate("MainWindow", u"Crosshair", None))
        self.lbl_inner_lines.setText(QCoreApplication.translate("MainWindow", u"Inner Lines", None))
        self.lbl_screen_stretch.setText(QCoreApplication.translate("MainWindow", u"Screen Stretch", None))
        self.btn_stretch_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.btn_save_ch.setText(QCoreApplication.translate("MainWindow", u"Save Crosshair", None))
        self.lbl_link.setText(QCoreApplication.translate("MainWindow", u"<a href=\"http://example.com/\">Project Home</a>", None))
        self.btn_del_ch.setText(QCoreApplication.translate("MainWindow", u"Delete Crosshair", None))
    # retranslateUi

