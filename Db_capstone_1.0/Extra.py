
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import datetime

def windowType(self):

    self.ui.btnMini.clicked.connect(lambda: self.showMinimized())
    self.ui.btnCls.clicked.connect(lambda: self.close())

    self.ui.btnMenu.clicked.connect(lambda: slideLeftMenu(self))

    self.ui.Today.setText(datetime.datetime.now().strftime("%Y/%m/%d"))

    self.ui.stackedWidget.setCurrentWidget(self.ui.Empty)
    
    def moveWindow(e):
        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    self.ui.Header.mouseMoveEvent = moveWindow

    def slideLeftMenu(self):
        width = self.ui.leftBar.width()

        if width == 45:
            newWidth = 150
        else:
            newWidth = 45

        self.animation = QPropertyAnimation(self.ui.leftBar, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth) 
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

        
    font = QFont()
    font.setFamily(u"Mongolian Baiti")
    font.setPointSize(13)
    font.setBold(False)
    font.setItalic(False)
    font.setWeight(50)
    font.setKerning(True)
    self.ui.tableWidget.setFont(font)
    self.ui.tableWidget.setStyleSheet(u"QTableWidget{\n"
                                    "    font: 12pt \"Mongolian Baiti\";\n"
                                    "    color: rgb(185, 228, 240);\n"
                                    "    background-color: rgb(44, 49, 56);\n"
                                    "}\n"
                                    "\n"
                                    "QHeaderView::section{\n"
                                    "font: 12pt \"Mongolian Baiti\";\n"
                                    "background-color: rgb(75, 83, 95);\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar:horizontal {\n"
                                    "    border: none;\n"
                                    "    background-color: rgb(194, 220, 255);\n"
                                    "    height: 20px;\n"
                                    "    margin: 0px 20px 0 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::handle:horizontal {\n"
                                    "    background-color: rgb(152, 171, 255);\n"
                                    "    min-width: 20px;\n"
                                    "    border-radius: 4px;\n"
                                    "    image: url(:/icons/icons/cil-options-horizontal.png);\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::add-line:horizontal {\n"
                                    "    background: none;\n"
                                    "    width: 20px;\n"
                                    "    subcontrol-position: right;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::sub-line:horizontal {\n"
                                    "    background: none;\n"
                                    "    width: 20px;\n"
                                    "    subcontrol-position: top left;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    position: absolute;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar:vertical {\n"
                                    "    border: none;\n"
                                    "    background-color: rgb(194, 220, 255);\n"
                                    "    width: 20px;\n"
                                    "    margin: 20px 0 20px 0;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::handle:vertical {\n"
                                    "    background-color: rgb(152, 171, 255);\n"
                                    "    min-height: 20px;\n"
                                    "    border-radius: 4px;\n"
                                    "    image: url(:/icons/icons/cil-options.png);\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::add-line:vertical {\n"
                                    "    background: none;\n"
                                    "    height: 20px;\n"
                                    "    subcontrol-position: bottom;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "}\n"
                                    "\n"
                                    "QScrollBar::sub-line:vertical {\n"
                                    "    back"
                                    "ground: none;\n"
                                    "    height: 20px;\n"
                                    "    subcontrol-position: top left;\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    position: absolute;\n"
                                    "\n"
                                    "}")
    self.ui.tableWidget.setAutoScroll(True)
    self.ui.tableWidget.setTabKeyNavigation(True)
    self.ui.tableWidget.setProperty("showDropIndicator", True)
    self.ui.tableWidget.setDragDropOverwriteMode(True)
    self.ui.tableWidget.setShowGrid(True)
    self.ui.tableWidget.setGridStyle(Qt.SolidLine)
    self.ui.tableWidget.setWordWrap(True)
    self.ui.tableWidget.setCornerButtonEnabled(True)
    self.ui.tableWidget.horizontalHeader().setVisible(True)
    self.ui.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
    self.ui.tableWidget.horizontalHeader().setHighlightSections(True)
    self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
    self.ui.tableWidget.verticalHeader().setVisible(True)
    self.ui.tableWidget.verticalHeader().setCascadingSectionResizes(False)
    self.ui.tableWidget.verticalHeader().setHighlightSections(True)