import os

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsScene
from PySide6 import QtGui, QtCore
from UI.main_window import Ui_MainWindow
from UI.enter_ch_name import Ui_Dialog
from crosshair import Crosshair
import aimtrainer
import sys


def le_input(le, slider, min_, max_, digits, factor):
    val = le.text()
    try:
        val = float(val)
        if min_ <= val <= max_:
            val = round(val, digits)
            if not digits:
                val = int(val)
            le.setText(str(val))
            slider.setValue(int(factor * val))
        else:
            le.undo()
    except ValueError:
        le.undo()
    return val
    # self.slide_dot_opacity.setValue()


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class EnterChName(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icon_path)))
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_names = None
        self.ch_names = None
        self.started = False

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icon_path)))
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle('Crosshair Manager 0.1')

        self.lbl_link.setText(u"<a href=\"https://github.com/b0bs0n/valo-crosshair\">Project Home</a>")
        self.ch = Crosshair()
        self.path = aimtrainer.get_crosshair_path()

        self.read_ch_names()
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QtGui.QColor(180, 180, 180))
        self.qgv_crosshair.setScene(self.scene)

        self.le_outline_opacity.editingFinished.connect(self.le_chg_outline_opacity)
        self.slide_outline_opacity.valueChanged.connect(self.sld_chg_outline_opacity)

        self.le_outline_thck.editingFinished.connect(self.le_chg_outline_thck)
        self.slide_outline_thck.valueChanged.connect(self.sld_chg_outline_thck)

        self.le_dot_opacity.editingFinished.connect(self.le_chg_dot_opacity)
        self.slide_dot_opacity.valueChanged.connect(self.sld_chg_dot_opacity)

        self.le_dot_thck.editingFinished.connect(self.le_chg_dot_thck)
        self.slide_dot_thck.valueChanged.connect(self.sld_chg_dot_thck)

        self.le_inner_opacity.editingFinished.connect(self.le_chg_inner_opacity)
        self.slide_inner_opacity.valueChanged.connect(self.sld_chg_inner_opacity)

        self.le_inner_length.editingFinished.connect(self.le_chg_inner_length)
        self.slide_inner_length.valueChanged.connect(self.sld_chg_inner_length)

        self.le_inner_thck.editingFinished.connect(self.le_chg_inner_thck)
        self.slide_inner_thck.valueChanged.connect(self.sld_chg_inner_thck)

        self.le_inner_offset.editingFinished.connect(self.le_chg_inner_offset)
        self.slide_inner_offset.valueChanged.connect(self.sld_chg_inner_offset)

        self.le_outer_opacity.editingFinished.connect(self.le_chg_outer_opacity)
        self.slide_outer_opacity.valueChanged.connect(self.sld_chg_outer_opacity)

        self.le_outer_length.editingFinished.connect(self.le_chg_outer_length)
        self.slide_outer_length.valueChanged.connect(self.sld_chg_outer_length)

        self.le_outer_thck.editingFinished.connect(self.le_chg_outer_thck)
        self.slide_outer_thck.valueChanged.connect(self.sld_chg_outer_thck)

        self.le_outer_offset.editingFinished.connect(self.le_chg_outer_offset)
        self.slide_outer_offset.valueChanged.connect(self.sld_chg_outer_offset)

        self.btn_outline_on.clicked.connect(self.btn_chg_outline_on)
        self.btn_outline_off.clicked.connect(self.btn_chg_outline_off)

        self.btn_dot_on.clicked.connect(self.btn_chg_dot_on)
        self.btn_dot_off.clicked.connect(self.btn_chg_dot_off)

        self.btn_inner_on.clicked.connect(self.btn_chg_inner_on)
        self.btn_inner_off.clicked.connect(self.btn_chg_inner_off)

        self.btn_outer_on.clicked.connect(self.btn_chg_outer_on)
        self.btn_outer_off.clicked.connect(self.btn_chg_outer_off)

        self.btn_save_ch.clicked.connect(self.save_crosshair)
        self.btn_del_ch.clicked.connect(self.delete_crosshair)

        self.qcb_crosshair_color.addItems(self.ch._COLORS.keys())
        self.qcb_crosshair_color.currentIndexChanged.connect(self.qcb_chg_crosshair_color)

        self.qcb_ch_select.activated.connect(self.select_crosshair)
        self.qcb_populate()
        self.load_crosshair()
        self.select_crosshair()

    # slider connection methods

    def le_chg_outline_opacity(self):
        val = le_input(self.le_outline_opacity, self.slide_outline_opacity, 0, 1, 3, 1000)
        self.ch.set_outline_opacity(val)

    def sld_chg_outline_opacity(self):
        self.le_outline_opacity.setText(str(self.slide_outline_opacity.value() / 1000))
        self.ch.set_outline_opacity(self.slide_outline_opacity.value() / 1000)
        self.disp_crosshair()

    def le_chg_outline_thck(self):
        val = le_input(self.le_outline_thck, self.slide_outline_thck, 0, 6, 0, 1)
        self.ch.set_outline_thickness(val)

    def sld_chg_outline_thck(self):
        self.le_outline_thck.setText(str(int(self.slide_outline_thck.value())))
        self.ch.set_outline_thickness(int(self.slide_outline_thck.value()))
        self.disp_crosshair()

    def le_chg_dot_opacity(self):
        val = le_input(self.le_dot_opacity, self.slide_dot_opacity, 0, 1, 3, 1000)
        self.ch.set_dot_opacity(val)

    def sld_chg_dot_opacity(self):
        self.le_dot_opacity.setText(str(self.slide_dot_opacity.value() / 1000))
        self.ch.set_dot_opacity(self.slide_dot_opacity.value() / 1000)
        self.disp_crosshair()

    def le_chg_dot_thck(self):
        val = le_input(self.le_dot_thck, self.slide_dot_thck, 0, 6, 0, 1)
        self.ch.set_dot_thickness(val)

    def sld_chg_dot_thck(self):
        self.le_dot_thck.setText(str(int(self.slide_dot_thck.value())))
        self.ch.set_dot_thickness(int(self.slide_dot_thck.value()))
        self.disp_crosshair()

    def le_chg_inner_opacity(self):
        val = le_input(self.le_inner_opacity, self.slide_inner_opacity, 0, 1, 3, 1000)
        self.ch.set_inner_opacity(val)

    def sld_chg_inner_opacity(self):
        self.le_inner_opacity.setText(str(self.slide_inner_opacity.value() / 1000))
        self.ch.set_inner_opacity(self.slide_inner_opacity.value() / 1000)
        self.disp_crosshair()

    def le_chg_inner_length(self):
        val = le_input(self.le_inner_length, self.slide_inner_length, 0, 20, 0, 1)
        self.ch.set_inner_length(val)

    def sld_chg_inner_length(self):
        self.le_inner_length.setText(str(int(self.slide_inner_length.value())))
        self.ch.set_inner_length(int(self.slide_inner_length.value()))
        self.disp_crosshair()

    def le_chg_inner_thck(self):
        val = le_input(self.le_inner_thck, self.slide_inner_thck, 0, 10, 0, 1)
        self.ch.set_inner_thickness(val)

    def sld_chg_inner_thck(self):
        self.le_inner_thck.setText(str(int(self.slide_inner_thck.value())))
        self.ch.set_inner_thickness(int(self.slide_inner_thck.value()))
        self.disp_crosshair()

    def le_chg_inner_offset(self):
        val = le_input(self.le_inner_offset, self.slide_inner_offset, 0, 20, 0, 1)
        self.ch.set_inner_offset(val)

    def sld_chg_inner_offset(self):
        self.le_inner_offset.setText(str(int(self.slide_inner_offset.value())))
        self.ch.set_inner_offset(int(self.slide_inner_offset.value()))
        self.disp_crosshair()

    def le_chg_outer_opacity(self):
        val = le_input(self.le_outer_opacity, self.slide_outer_opacity, 0, 1, 3, 1000)
        self.ch.set_outer_opacity(val)

    def sld_chg_outer_opacity(self):
        self.le_outer_opacity.setText(str(self.slide_outer_opacity.value() / 1000))
        self.ch.set_outer_opacity(self.slide_outer_opacity.value() / 1000)
        self.disp_crosshair()

    def le_chg_outer_length(self):
        val = le_input(self.le_outer_length, self.slide_outer_length, 0, 20, 0, 1)
        self.ch.set_outer_length(val)

    def sld_chg_outer_length(self):
        self.le_outer_length.setText(str(int(self.slide_outer_length.value())))
        self.ch.set_outer_length(int(self.slide_outer_length.value()))
        self.disp_crosshair()

    def le_chg_outer_thck(self):
        val = le_input(self.le_outer_thck, self.slide_outer_thck, 0, 10, 0, 1)
        self.ch.set_outer_thickness(val)

    def sld_chg_outer_thck(self):
        self.le_outer_thck.setText(str(int(self.slide_outer_thck.value())))
        self.ch.set_outer_thickness(int(self.slide_outer_thck.value()))
        self.disp_crosshair()

    def le_chg_outer_offset(self):
        val = le_input(self.le_outer_offset, self.slide_outer_offset, 0, 20, 0, 1)
        self.ch.set_outer_offset(val)

    def sld_chg_outer_offset(self):
        self.le_outer_offset.setText(str(int(self.slide_outer_offset.value())))
        self.ch.set_outer_offset(int(self.slide_outer_offset.value()))
        self.disp_crosshair()

    def qcb_chg_crosshair_color(self):
        color = self.qcb_crosshair_color.currentText()
        self.ch.set_color(color)
        self.disp_crosshair()

    def btn_chg_outline_on(self):
        self.btn_outline_on.setChecked(True)
        self.btn_outline_off.setChecked(False)
        self.ch.set_outlines(True)
        self.disp_crosshair()

    def btn_chg_outline_off(self):
        self.btn_outline_on.setChecked(False)
        self.btn_outline_off.setChecked(True)
        self.ch.set_outlines(False)
        self.disp_crosshair()

    def btn_chg_dot_on(self):
        self.btn_dot_on.setChecked(True)
        self.btn_dot_off.setChecked(False)
        self.ch.set_dot(True)
        self.disp_crosshair()

    def btn_chg_dot_off(self):
        self.btn_dot_on.setChecked(False)
        self.btn_dot_off.setChecked(True)
        self.ch.set_dot(False)
        self.disp_crosshair()

    def btn_chg_inner_on(self):
        self.btn_inner_on.setChecked(True)
        self.btn_inner_off.setChecked(False)
        self.ch.set_inner(True)
        self.disp_crosshair()

    def btn_chg_inner_off(self):
        self.btn_inner_on.setChecked(False)
        self.btn_inner_off.setChecked(True)
        self.ch.set_inner(False)
        self.disp_crosshair()

    def btn_chg_outer_on(self):
        self.btn_outer_on.setChecked(True)
        self.btn_outer_off.setChecked(False)
        self.ch.set_outer(True)
        self.disp_crosshair()

    def btn_chg_outer_off(self):
        self.btn_outer_on.setChecked(False)
        self.btn_outer_off.setChecked(True)
        self.ch.set_outer(False)
        self.disp_crosshair()

    def read_ch_names(self):
        files, chs = aimtrainer.get_managed_crosshairs(self.path)
        self.ch_names = [i[:-4] for i in chs]
        self.file_names = [i[:-4] for i in files]

    def qcb_populate(self):
        self.qcb_ch_select.clear()
        self.qcb_ch_select.addItems(self.ch_names)
        self.qcb_ch_select.addItem('New Crosshair...', userData=-1)
        self.qcb_ch_select.setCurrentIndex(0)

    def disp_crosshair(self):
        img = self.ch.draw_crosshair()
        pixmap = img.toqpixmap()
        self.scene.clear()
        self.scene.addPixmap(pixmap)

    def select_crosshair(self):
        # print(self.qcb_ch_select.currentData())
        if self.qcb_ch_select.currentData() == -1 and self.started:
            dlg = EnterChName()
            ok = dlg.exec()
            text = dlg.lineEdit.text()
            if ok and len(text) >= 3 and text not in self.file_names:
                self.ch_names.append(text)
                self.qcb_populate()
                self.qcb_ch_select.setCurrentText(text)
        else:
            self.started = True
            try:
                self.ch.load_png(self.path + '\\' + self.qcb_ch_select.currentText() + '.png')
                self.load_crosshair()
            except FileNotFoundError:
                pass
            else:
                self.read_ch_names()
                entries = [self.qcb_ch_select.itemText(i) for i in range(self.qcb_ch_select.count())]
                for i in entries:
                    if i not in self.ch_names and i != 'New Crosshair...':
                        index = self.qcb_ch_select.findText(i)
                        self.qcb_ch_select.removeItem(index)
            self.disp_crosshair()

    def save_crosshair(self):
        name = self.qcb_ch_select.currentText()
        if name != 'New Crosshair...':
            self.ch.save_png(self.path + '\\' + self.qcb_ch_select.currentText() + '.png')

    def delete_crosshair(self):
        name = self.qcb_ch_select.currentText()
        if name != 'New Crosshair...' and name not in self.file_names:
            self.qcb_ch_select.removeItem(self.qcb_ch_select.currentIndex())
            self.qcb_ch_select.setCurrentIndex(0)
            self.select_crosshair()
        elif name != 'New Crosshair...':
            os.remove(self.path + '\\' + self.qcb_ch_select.currentText() + '.png')
            self.qcb_ch_select.removeItem(self.qcb_ch_select.currentIndex())
            self.qcb_ch_select.setCurrentIndex(0)
            self.select_crosshair()

    def load_crosshair(self):
        self.qcb_crosshair_color.setCurrentText(self.ch._color)
        #  outlines
        self.btn_outline_on.setChecked(self.ch._outlines[0])
        self.btn_outline_off.setChecked(not self.ch._outlines[0])
        self.le_outline_opacity.setText(str(self.ch._outlines[1]))
        self.slide_outline_opacity.setValue(1000 * self.ch._outlines[1])
        self.le_outline_thck.setText(str(self.ch._outlines[2]))
        self.slide_outline_thck.setValue(self.ch._outlines[2])
        #  center dot
        self.btn_dot_on.setChecked(self.ch._dot[0])
        self.btn_dot_off.setChecked(not self.ch._dot[0])
        self.le_dot_opacity.setText(str(self.ch._dot[1]))
        self.slide_dot_opacity.setValue(1000 * self.ch._dot[1])
        self.le_dot_thck.setText(str(self.ch._dot[2]))
        self.slide_dot_thck.setValue(self.ch._dot[2])
        #  inner
        self.btn_inner_on.setChecked(self.ch._inner[0])
        self.btn_inner_off.setChecked(not self.ch._inner[0])
        self.le_inner_opacity.setText(str(self.ch._inner[1]))
        self.slide_inner_opacity.setValue(1000 * self.ch._inner[1])
        self.le_inner_length.setText(str(self.ch._inner[2]))
        self.slide_inner_length.setValue(self.ch._inner[2])
        self.le_inner_thck.setText(str(self.ch._inner[3]))
        self.slide_inner_thck.setValue(self.ch._inner[3])
        self.le_inner_offset.setText(str(self.ch._inner[4]))
        self.slide_inner_offset.setValue(self.ch._inner[4])
        # outer
        self.btn_outer_on.setChecked(self.ch._outer[0])
        self.btn_outer_off.setChecked(not self.ch._outer[0])
        self.le_outer_opacity.setText(str(self.ch._outer[1]))
        self.slide_outer_opacity.setValue(1000 * self.ch._outer[1])
        self.le_outer_length.setText(str(self.ch._outer[2]))
        self.slide_outer_length.setValue(self.ch._outer[2])
        self.le_outer_thck.setText(str(self.ch._outer[3]))
        self.slide_outer_thck.setValue(self.ch._outer[3])
        self.le_outer_offset.setText(str(self.ch._outer[4]))
        self.slide_outer_offset.setValue(self.ch._outer[4])


if __name__ == '__main__':
    icon_path = resource_path('icon.png')
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
