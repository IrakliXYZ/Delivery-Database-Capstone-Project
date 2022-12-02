import sys,time,os
import UI.ui_Main
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Extra import *
import backend.main

class MainWindow(QMainWindow):
    CheckingStatus = pyqtSignal(str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.WINDOW_SIZE = 0
        self.ui = UI.ui_Main.Ui_MainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint) # Remove Window Frame
        self.ui.setupUi(self)
        windowType(self)
        self.show()


        def CreateNew():
            backend.main.name = self.ui.cName.text()
            backend.main.phone = self.ui.cTPno.text()
            backend.main.address = self.ui.cPickupAddr.text()
            backend.main.destination = self.ui.cDistAddr.text()
            backend.main.cpayment = self.ui.cPaymentMethod.text()
            backend.main.tip = self.ui.cOrderTip.text()
            backend.main.total = self.ui.cOrderTotal.text()
            backend.main.status = self.ui.cOrderStat.text()
            backend.main.type = self.ui.cDecision.text()
            FormStatus = backend.main.create_order()
            if FormStatus:
                print(FormStatus)
            else:
                try: 
                    backend.main.create_new_order()
                    self.ui.btnG.setText("Saved !")
                    self.ui.cName.setText('')
                    self.ui.cTPno.setText('')
                    self.ui.cPickupAddr.setText('')
                    self.ui.cDistAddr.setText('')
                    self.ui.cPaymentMethod.setText('')
                    self.ui.cOrderTip.setText('')
                    self.ui.cOrderTotal.setText('')
                    self.ui.cOrderStat.setText('')
                    self.ui.cDecision.setText('')
                    print("Saved !")
                except Exception as e: 
                    print(f"Error : {e}")
        self.ui.btnG.clicked.connect(lambda: CreateNew())
        
        
        def MainPage():
            self.ui.stackedWidget.setCurrentWidget(self.ui.create_new_order)
            self.ui.btnG.setText("Make Order !")
        self.ui.btnMain.clicked.connect(lambda: MainPage())

        def clickedIncomp():
            self.ui.stackedWidget.setCurrentWidget(self.ui.incomplete)
            try: 
                status = backend.main.incomplete()
                self.ui.textLog_incolmpleate.setText(str(status))
            except Exception as e:
                print(f"Error : {e}")
        self.ui.btnIncomp.clicked.connect(lambda: clickedIncomp())

        def clickedStats():
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_status)
            try: 
                status = backend.main.stats()
                self.ui.textLog_Stats.setText(status)
            except Exception as e:
                print(f"Error : {e}")
        self.ui.btnStats.clicked.connect(lambda: clickedStats())

        def clickedTable():
            self.ui.stackedWidget.setCurrentWidget(self.ui.whole_table)
            try: 
                table = backend.main.retrieve_table()

                while (self.ui.tableWidget.rowCount() > 0):
                    self.ui.tableWidget.removeRow(0)

                for row in table:
                    rowPosition = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(rowPosition)
                    for i,cell in enumerate(row):
                        self.ui.tableWidget.setItem(rowPosition, i, QTableWidgetItem(str(cell)))

            except Exception as e:
                print(f"Error : {e}")
        self.ui.btnTable.clicked.connect(lambda: clickedTable())

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            print("Q")
        event.accept()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress):
            print('key press:', (event.key(), event.text())) 
        return super(MainWindow, self).eventFilter(source, event)

if __name__ == "__main__":
    os.environ["QT_FONT_DPI"] = "96"
    qapp = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(qapp.exec_())