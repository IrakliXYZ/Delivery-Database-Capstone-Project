
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 70))
        self.Header.setMaximumSize(QSize(16777215, 70))
        self.Header.setStyleSheet(u"background-color: rgb(23, 24, 30);")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.Header)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(110, 0))
        self.Menu.setMaximumSize(QSize(100, 16777215))
        self.Menu.setFrameShape(QFrame.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.btnMenu = QPushButton(self.Menu)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(20, 20, 41, 31))
        self.btnMenu.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(170, 0, 255, 100);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/ico/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.Menu)

        self.Title = QFrame(self.Header)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"")
        self.Title.setFrameShape(QFrame.StyledPanel)
        self.Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(310, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.frame_5 = QFrame(self.Title)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 20, 301, 31))
        font = QFont()
        font.setFamily(u"Garamond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(170, 255, 255);\n"
"font: 20pt \"Garamond\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_5)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_3 = QFrame(self.Title)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(90, 16777215))
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(170, 85, 255, 150);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnMini = QPushButton(self.frame_3)
        self.btnMini.setObjectName(u"btnMini")
        self.btnMini.setMinimumSize(QSize(25, 25))
        self.btnMini.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/ico/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMini.setIcon(icon1)
        self.btnMini.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnMini)

        self.btnCls = QPushButton(self.frame_3)
        self.btnCls.setObjectName(u"btnCls")
        self.btnCls.setMinimumSize(QSize(25, 25))
        self.btnCls.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/ico/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCls.setIcon(icon2)
        self.btnCls.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnCls)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.Title)


        self.verticalLayout.addWidget(self.Header)

        self.Main = QFrame(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setFrameShape(QFrame.NoFrame)
        self.Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBar = QFrame(self.Main)
        self.leftBar.setObjectName(u"leftBar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBar.sizePolicy().hasHeightForWidth())
        self.leftBar.setSizePolicy(sizePolicy)
        self.leftBar.setMinimumSize(QSize(0, 0))
        self.leftBar.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.leftBar.setFont(font1)
        self.leftBar.setStyleSheet(u"background-color: rgb(23, 24, 30);")
        self.leftBar.setFrameShape(QFrame.NoFrame)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MainTabs = QFrame(self.leftBar)
        self.MainTabs.setObjectName(u"MainTabs")
        self.MainTabs.setMinimumSize(QSize(0, 170))
        self.MainTabs.setMaximumSize(QSize(16777215, 185))
        self.MainTabs.setFont(font1)
        self.MainTabs.setStyleSheet(u"")
        self.MainTabs.setFrameShape(QFrame.NoFrame)
        self.MainTabs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.MainTabs)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 5, 0, 0)
        self.btnMain = QRadioButton(self.MainTabs)
        self.btnMain.setObjectName(u"btnMain")
        self.btnMain.setMinimumSize(QSize(0, 36))
        self.btnMain.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	padding: 0px 0px 0px 5px;\n"
"	border-top-left-radius: 17px;\n"
"	border-bottom-left-radius: 17px;\n"
"}\n"
"QRadioButton:hover {\n"
"	background-color: rgba(250, 250, 250, 100);\n"
"}\n"
"QRadioButton:checked {\n"
"	background-color: rgb(250, 250, 250);\n"
"	color: rgb(23, 24, 29);\n"
"}\n"
"QRadioButton::indicator {\n"
"	image: url(:/icons/ico/cil-library-add.png);\n"
"    padding: 0px -5px 0px 7px;\n"
"    width: 25px;\n"
"	border-radius: 3px;\n"
"    height: 25px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/ico/cil-library-addB.png);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnMain)

        self.btnIncomp = QRadioButton(self.MainTabs)
        self.btnIncomp.setObjectName(u"btnIncomp")
        self.btnIncomp.setMinimumSize(QSize(0, 36))
        self.btnIncomp.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	padding: 0px 0px 0px 5px;\n"
"	border-top-left-radius: 17px;\n"
"	border-bottom-left-radius: 17px;\n"
"}\n"
"QRadioButton:hover {\n"
"	background-color: rgba(250, 250, 250, 100);\n"
"}\n"
"QRadioButton:checked {\n"
"	background-color: rgb(250, 250, 250);\n"
"	color: rgb(23, 24, 29);\n"
"}\n"
"QRadioButton::indicator {\n"
"	image: url(:/icons/ico/cil-vertical-align-center.png);\n"
"    padding: 0px -5px 0px 8px;\n"
"    width: 25px;\n"
"	border-radius: 3px;\n"
"    height: 25px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/ico/cil-vertical-align-centerB.png);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnIncomp)

        self.btnStats = QRadioButton(self.MainTabs)
        self.btnStats.setObjectName(u"btnStats")
        self.btnStats.setMinimumSize(QSize(0, 36))
        self.btnStats.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	padding: 0px 0px 0px 5px;\n"
"	border-top-left-radius: 17px;\n"
"	border-bottom-left-radius: 17px;\n"
"}\n"
"QRadioButton:hover {\n"
"	background-color: rgba(250, 250, 250, 100);\n"
"}\n"
"QRadioButton:checked {\n"
"	background-color: rgb(250, 250, 250);\n"
"	color: rgb(23, 24, 29);\n"
"}\n"
"QRadioButton::indicator {\n"
"	image: url(:/icons/ico/cil-chart-line.png);\n"
"    padding: 0px -5px 0px 8px;\n"
"    width: 25px;\n"
"	border-radius: 3px;\n"
"    height: 25px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/ico/cil-chart-lineB.png);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnStats)

        self.btnTable = QRadioButton(self.MainTabs)
        self.btnTable.setObjectName(u"btnTable")
        self.btnTable.setMinimumSize(QSize(0, 36))
        self.btnTable.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	padding: 0px 0px 0px 5px;\n"
"	border-top-left-radius: 17px;\n"
"	border-bottom-left-radius: 17px;\n"
"}\n"
"QRadioButton:hover {\n"
"	background-color: rgba(250, 250, 250, 100);\n"
"}\n"
"QRadioButton:checked {\n"
"	background-color: rgb(250, 250, 250);\n"
"	color: rgb(23, 24, 29);\n"
"}\n"
"QRadioButton::indicator {\n"
"	image: url(:/icons/ico/cil-browser.png);\n"
"    padding: 0px -5px 0px 8px;\n"
"    width: 25px;\n"
"	border-radius: 3px;\n"
"    height: 25px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	image: url(:/icons/ico/cil-browserB.png);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnTable)


        self.verticalLayout_3.addWidget(self.MainTabs)

        self.MiddleTab = QFrame(self.leftBar)
        self.MiddleTab.setObjectName(u"MiddleTab")
        self.MiddleTab.setFrameShape(QFrame.StyledPanel)
        self.MiddleTab.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.MiddleTab)


        self.horizontalLayout.addWidget(self.leftBar)

        self.frame_4 = QFrame(self.Main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainItem = QFrame(self.frame_4)
        self.MainItem.setObjectName(u"MainItem")
        self.MainItem.setStyleSheet(u"background-color: rgb(248, 252, 255);")
        self.MainItem.setFrameShape(QFrame.NoFrame)
        self.MainItem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MainItem)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.MainItem)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.incomplete = QWidget()
        self.incomplete.setObjectName(u"incomplete")
        self.incomplete.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.incomplete)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.incomplete)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(800, 430))
        self.frame_2.setMaximumSize(QSize(800, 16777215))
        self.frame_2.setStyleSheet(u"QLabel{\n"
"	border-radius: 7px;\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"}\n"
" QLineEdit{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	font: 13pt \"Mongolian Baiti\";\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(24, 100, 213);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(248, 251, 250);\n"
"}\n"
" QPushButton:hover{\n"
"	background-color: rgb(24, 50, 150);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 20, 231, 21))
        font2 = QFont()
        font2.setFamily(u"Mongolian Baiti")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_31.setFont(font2)
        self.textLog_incolmpleate = QLabel(self.frame_2)
        self.textLog_incolmpleate.setObjectName(u"textLog_incolmpleate")
        self.textLog_incolmpleate.setGeometry(QRect(90, 60, 611, 431))
        self.textLog_incolmpleate.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(170, 255, 255);\n"
"	background-color: rgb(14, 15, 17);\n"
"	border :1px solid blue;\n"
"	border-radius: 5px;\n"
"}")
        self.textLog_incolmpleate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textLog_incolmpleate.setMargin(5)
        self.textLog_incolmpleate.setIndent(5)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.incomplete)
        self.page_status = QWidget()
        self.page_status.setObjectName(u"page_status")
        self.horizontalLayout_6 = QHBoxLayout(self.page_status)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_status)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(800, 430))
        self.frame_6.setMaximumSize(QSize(800, 16777215))
        self.frame_6.setStyleSheet(u"QLabel{\n"
"	border-radius: 7px;\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"}\n"
" QLineEdit{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	font: 13pt \"Mongolian Baiti\";\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(24, 100, 213);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(248, 251, 250);\n"
"}\n"
" QPushButton:hover{\n"
"	background-color: rgb(24, 50, 150);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.frame_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 20, 231, 21))
        self.label_32.setFont(font2)
        self.textLog_Stats = QLabel(self.frame_6)
        self.textLog_Stats.setObjectName(u"textLog_Stats")
        self.textLog_Stats.setGeometry(QRect(90, 60, 611, 431))
        self.textLog_Stats.setStyleSheet(u"QLabel{\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(170, 255, 255);\n"
"	background-color: rgb(14, 15, 17);\n"
"	border :1px solid blue;\n"
"	border-radius: 5px;\n"
"}")
        self.textLog_Stats.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textLog_Stats.setMargin(5)
        self.textLog_Stats.setIndent(5)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_status)
        self.whole_table = QWidget()
        self.whole_table.setObjectName(u"whole_table")
        self.horizontalLayout_9 = QHBoxLayout(self.whole_table)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.whole_table)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(1000, 430))
        self.frame_7.setMaximumSize(QSize(1000, 16777215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 76, 91);\n"
"}\n"
"QLabel{\n"
"	border-radius: 7px;\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"}\n"
" QLineEdit{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	font: 13pt \"Mongolian Baiti\";\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(24, 100, 213);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(248, 251, 250);\n"
"}\n"
" QPushButton:hover{\n"
"	background-color: rgb(24, 50, 150);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_33)

        self.tableWidget = QTableWidget(self.frame_7)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.whole_table)
        self.create_new_order = QWidget()
        self.create_new_order.setObjectName(u"create_new_order")
        self.create_new_order.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.create_new_order)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.frm1 = QFrame(self.create_new_order)
        self.frm1.setObjectName(u"frm1")
        self.frm1.setStyleSheet(u"#frm1{\n"
"	border :1px solid blue;\n"
"	border-radius: 16px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"	border-radius: 7px;\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"}\n"
" QLineEdit{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	font: 13pt \"Mongolian Baiti\";\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(24, 100, 213);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"	color: rgb(248, 251, 250);\n"
"}\n"
" QPushButton:hover{\n"
"	background-color: rgb(24, 50, 150);\n"
"}")
        self.frm1.setFrameShape(QFrame.StyledPanel)
        self.frm1.setFrameShadow(QFrame.Raised)
        self.label_34 = QLabel(self.frm1)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(60, 100, 231, 21))
        self.label_34.setFont(font2)
        self.label_35 = QLabel(self.frm1)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(60, 60, 161, 21))
        self.label_35.setFont(font2)
        self.cTPno = QLineEdit(self.frm1)
        self.cTPno.setObjectName(u"cTPno")
        self.cTPno.setGeometry(QRect(350, 100, 351, 23))
        self.cTPno.setMinimumSize(QSize(0, 23))
        self.cName = QLineEdit(self.frm1)
        self.cName.setObjectName(u"cName")
        self.cName.setGeometry(QRect(350, 60, 351, 23))
        self.cName.setMinimumSize(QSize(0, 23))
        self.label_30 = QLabel(self.frm1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 20, 231, 21))
        self.label_30.setFont(font2)
        self.btnG = QPushButton(self.frm1)
        self.btnG.setObjectName(u"btnG")
        self.btnG.setGeometry(QRect(260, 460, 181, 27))
        self.btnG.setMinimumSize(QSize(0, 27))
        self.label_36 = QLabel(self.frm1)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 140, 141, 21))
        self.label_36.setFont(font2)
        self.label_40 = QLabel(self.frm1)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(60, 180, 161, 21))
        self.label_40.setFont(font2)
        self.label_41 = QLabel(self.frm1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(60, 220, 231, 21))
        self.label_41.setFont(font2)
        self.label_42 = QLabel(self.frm1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(60, 260, 161, 21))
        self.label_42.setFont(font2)
        self.label_43 = QLabel(self.frm1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(60, 300, 181, 21))
        self.label_43.setFont(font2)
        self.label_44 = QLabel(self.frm1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(60, 340, 181, 21))
        self.label_44.setFont(font2)
        self.label_45 = QLabel(self.frm1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(60, 380, 231, 21))
        self.label_45.setFont(font2)
        self.cPickupAddr = QLineEdit(self.frm1)
        self.cPickupAddr.setObjectName(u"cPickupAddr")
        self.cPickupAddr.setGeometry(QRect(350, 140, 351, 23))
        self.cPickupAddr.setMinimumSize(QSize(0, 23))
        self.cDistAddr = QLineEdit(self.frm1)
        self.cDistAddr.setObjectName(u"cDistAddr")
        self.cDistAddr.setGeometry(QRect(350, 180, 351, 23))
        self.cDistAddr.setMinimumSize(QSize(0, 23))
        self.cPaymentMethod = QLineEdit(self.frm1)
        self.cPaymentMethod.setObjectName(u"cPaymentMethod")
        self.cPaymentMethod.setGeometry(QRect(350, 220, 351, 23))
        self.cPaymentMethod.setMinimumSize(QSize(0, 23))
        self.cOrderTip = QLineEdit(self.frm1)
        self.cOrderTip.setObjectName(u"cOrderTip")
        self.cOrderTip.setGeometry(QRect(350, 260, 351, 23))
        self.cOrderTip.setMinimumSize(QSize(0, 23))
        self.cOrderTotal = QLineEdit(self.frm1)
        self.cOrderTotal.setObjectName(u"cOrderTotal")
        self.cOrderTotal.setGeometry(QRect(350, 300, 351, 23))
        self.cOrderTotal.setMinimumSize(QSize(0, 23))
        self.cOrderStat = QLineEdit(self.frm1)
        self.cOrderStat.setObjectName(u"cOrderStat")
        self.cOrderStat.setGeometry(QRect(350, 340, 351, 23))
        self.cOrderStat.setMinimumSize(QSize(0, 23))
        self.cDecision = QLineEdit(self.frm1)
        self.cDecision.setObjectName(u"cDecision")
        self.cDecision.setGeometry(QRect(350, 380, 351, 23))
        self.cDecision.setMinimumSize(QSize(0, 23))

        self.verticalLayout_11.addWidget(self.frm1)

        self.stackedWidget.addWidget(self.create_new_order)
        self.Empty = QWidget()
        self.Empty.setObjectName(u"Empty")
        self.stackedWidget.addWidget(self.Empty)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.MainItem)

        self.Footer = QFrame(self.frame_4)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 27))
        self.Footer.setMaximumSize(QSize(16777215, 100))
        self.Footer.setStyleSheet(u"background-color: rgb(205, 205, 215);")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Footer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.Footer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setStyleSheet(u"QLabel {\n"
"	color: rgb(23, 24, 29);\n"
"	font: 12pt \"Garamond\";\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.status = QLabel(self.frame_9)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(0, 0, 181, 21))
        self.status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(200, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 0, 51, 21))
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Today = QLabel(self.frame_10)
        self.Today.setObjectName(u"Today")
        self.Today.setGeometry(QRect(90, 0, 91, 21))
        self.Today.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.frame_10)


        self.horizontalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.Main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnMenu.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Delivery Database Manager", None))
        self.btnMini.setText("")
        self.btnCls.setText("")
        self.btnMain.setText(QCoreApplication.translate("MainWindow", u"   New", None))
        self.btnIncomp.setText(QCoreApplication.translate("MainWindow", u"  Incomplete", None))
        self.btnStats.setText(QCoreApplication.translate("MainWindow", u"  Stats", None))
        self.btnTable.setText(QCoreApplication.translate("MainWindow", u"  Table", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Retrieve incomplete orders :", None))
        self.textLog_incolmpleate.setText(QCoreApplication.translate("MainWindow", u"< Incomplete orders >", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"See stats :", None))
        self.textLog_Stats.setText(QCoreApplication.translate("MainWindow", u"< Stats >", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"    See whole table :", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Telephone", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Payment", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Payment Tip", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total Payment", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Payment Type", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Order Type", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Order Date", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Order Status", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Pick", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DropOff", None));
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Customer's phone number:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Customer's name:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Enter new order :", None))
        self.btnG.setText(QCoreApplication.translate("MainWindow", u"Make Order !", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Pickup address:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Destination address:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Customer's payment method:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Customer's order tip:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Customer's order total:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Customer's order status:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Type \"package\" or \"person\":", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"[Status]", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.Today.setText(QCoreApplication.translate("MainWindow", u"05/29/2022", None))
    # retranslateUi

