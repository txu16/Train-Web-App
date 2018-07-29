from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QCheckBox, QWidget, QMessageBox, QMainWindow, QDateEdit, QTimeEdit)

from PyQt5 import QtGui, QtPrintSupport
from PyQt5.QtCore import (Qt,QDate,QTime)
import sys
import pymysql
from pymysql import cursors
#from searchResults import Ui_SearchResultsWindow

class Login(QDialog):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        #Login and Password boxes, password gets censored
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.textPass.setEchoMode(QLineEdit.Password)

        username = QLabel("Email")
        pw = QLabel('Password')

        # LAYOUT CONTAINER FOR WIDGETS AND BUTTONS
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(lambda: self.on_button(2))
        #self.buttonLogin.clicked.connect(self.close)

        self.buttonRegister = QPushButton('Register', self)
        self.buttonRegister.clicked.connect(lambda: self.on_button(1))
        self.buttonRegister.clicked.connect(self.close)

        loginbox = QGridLayout(self)
        loginbox.setSpacing(10)

        loginbox.addWidget(username,1,0)
        loginbox.addWidget(self.textName,1,1)

        loginbox.addWidget(pw,2,0)
        loginbox.addWidget(self.textPass,2,1)

        loginbox.addWidget(self.buttonRegister,3,0)
        loginbox.addWidget(self.buttonLogin,3,1)

        self.setWindowTitle("SNCF Login")

    def on_button(self, n):

        if n == 1:
            self.window = Registration()
            self.window.show()

        elif n == 2:
            checkSQL = "select exists (select 1 from user where email = %s and password = %s)"
            cursor.execute(checkSQL, (self.textName.text(), self.textPass.text()))
            dictionary = cursor.fetchall()[0]
            check = (list(dictionary.values()))[0]
            if (check == 1):
                userIDSQL = "select user_id from user where email = %s and password = %s"
                cursor.execute(userIDSQL, (self.textName.text(), self.textPass.text()))
                dict2 = cursor.fetchall()[0]
                global userID
                userID = (list(dict2.values()))[0]

                check2SQL = "select exists (select 1 from customer where user_id = %s)"
                cursor.execute(check2SQL, (str(userID)))
                dict3 = cursor.fetchall()[0]
                check2 = (list(dict3.values()))[0]
                if (check2 == 1):
                    self.hide()
                    self.window = Search()
                    self.window.show()

                else:
                    self.hide()
                    self.window = Admin_Dashboard()
                    self.window.show()

            else:
                QMessageBox.warning(self,
                    'Error', "Vous avez un email ou un mot de passe incorrect. Veuillez ressayer.")


class Admin_Dashboard(QMainWindow):
    def __init__(self, parent=None):
        super(Admin_Dashboard, self).__init__(parent)
        self.setWindowTitle("Admin Dashboard")


class Customer_Dashboard(QMainWindow):
    def __init__(self, parent=None):
        super(Customer_Dashboard, self).__init__(parent)
        self.setWindowTitle("Customer Dashboard")

class Registration(QDialog):

    def __init__(self):
        super(Registration, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.clickSearch)
        #buttonBox.accepted.connect(self.close)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Registration")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Registration Form")
        layout = QFormLayout(self)

        self.email = QLineEdit()
        layout.addRow(QLabel("*Email:"), self.email)
        self.confirmEmail = QLineEdit()
        layout.addRow(QLabel("*Confirm Email:"), self.confirmEmail)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmPassword = QLineEdit()
        self.confirmPassword.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("*Password:"), self.password)

        layout.addRow(QLabel("*Confirm Password:"), self.confirmPassword)

        self.firstName = QLineEdit()
        layout.addRow(QLabel("*First Name:"), self.firstName)
        self.lastName = QLineEdit()
        layout.addRow(QLabel("*Last Name:"), self.lastName)
        self.address1 = QLineEdit()
        layout.addRow(QLabel("*Address 1:"), self.address1)
        self.address2 = QLineEdit()
        layout.addRow(QLabel("Address 2:"), self.address2)
        self.city = QLineEdit()
        layout.addRow(QLabel("*City:"), self.city)
        self.state = QLineEdit()
        layout.addRow(QLabel("*State:"), self.state)
        self.postalCode = QLineEdit()
        layout.addRow(QLabel("*Postal Code:"), self.postalCode)

        self.combo = QComboBox(self)
        self.combo.addItem("AFG")
        self.combo.addItem("ALB")
        self.combo.addItem("DZA")
        self.combo.addItem("ASM")
        self.combo.addItem("AND")
        self.combo.addItem("AGO")
        self.combo.addItem("AIA")
        self.combo.addItem("ATA")
        self.combo.addItem("ATG")
        self.combo.addItem("ARG")
        self.combo.addItem("ARM")
        self.combo.addItem("ABW")
        self.combo.addItem("AUS")
        self.combo.addItem("AUT")
        self.combo.addItem("AZE")
        self.combo.addItem("BHS")
        self.combo.addItem("BHR")
        self.combo.addItem("BGD")
        self.combo.addItem("BRB")
        self.combo.addItem("BLR")
        self.combo.addItem("BEL")
        self.combo.addItem("BLZ")
        self.combo.addItem("BEN")
        self.combo.addItem("BMU")
        self.combo.addItem("BTN")
        self.combo.addItem("BOL")
        self.combo.addItem("BES")
        self.combo.addItem("BIH")
        self.combo.addItem("BWA")
        self.combo.addItem("BVT")
        self.combo.addItem("BRA")
        self.combo.addItem("IOT")
        self.combo.addItem("BRN")
        self.combo.addItem("BGR")
        self.combo.addItem("BFA")
        self.combo.addItem("BDI")
        self.combo.addItem("KHM")
        self.combo.addItem("CMR")
        self.combo.addItem("CAN")
        self.combo.addItem("CPV")
        self.combo.addItem("CYM")
        self.combo.addItem("CAF")
        self.combo.addItem("TCD")
        self.combo.addItem("CHL")
        self.combo.addItem("CHN")
        self.combo.addItem("CXR")
        self.combo.addItem("CCK")
        self.combo.addItem("COL")
        self.combo.addItem("COM")
        self.combo.addItem("COG")
        self.combo.addItem("COD")
        self.combo.addItem("COK")
        self.combo.addItem("CRI")
        self.combo.addItem("HRV")
        self.combo.addItem("CUB")
        self.combo.addItem("CUW")
        self.combo.addItem("CYP")
        self.combo.addItem("CZE")
        self.combo.addItem("CIV")
        self.combo.addItem("DNK")
        self.combo.addItem("DJI")
        self.combo.addItem("DMA")
        self.combo.addItem("DOM")
        self.combo.addItem("ECU")
        self.combo.addItem("EGY")
        self.combo.addItem("SLV")
        self.combo.addItem("GNQ")
        self.combo.addItem("ERI")
        self.combo.addItem("EST")
        self.combo.addItem("ETH")
        self.combo.addItem("FLK")
        self.combo.addItem("FRO")
        self.combo.addItem("FJI")
        self.combo.addItem("FIN")
        self.combo.addItem("FRA")
        self.combo.addItem("GUF")
        self.combo.addItem("PYF")
        self.combo.addItem("ATF")
        self.combo.addItem("GAB")
        self.combo.addItem("GMB")
        self.combo.addItem("GEO")
        self.combo.addItem("DEU")
        self.combo.addItem("GHA")
        self.combo.addItem("GIB")
        self.combo.addItem("GRC")
        self.combo.addItem("GRL")
        self.combo.addItem("GRD")
        self.combo.addItem("GLP")
        self.combo.addItem("GUM")
        self.combo.addItem("GTM")
        self.combo.addItem("GGY")
        self.combo.addItem("GIN")
        self.combo.addItem("GNB")
        self.combo.addItem("GUY")
        self.combo.addItem("HTI")
        self.combo.addItem("HMD")
        self.combo.addItem("VAT")
        self.combo.addItem("HND")
        self.combo.addItem("HKG")
        self.combo.addItem("HUN")
        self.combo.addItem("ISL")
        self.combo.addItem("IND")
        self.combo.addItem("IDN")
        self.combo.addItem("IRN")
        self.combo.addItem("IRQ")
        self.combo.addItem("IRL")
        self.combo.addItem("IMN")
        self.combo.addItem("ISR")
        self.combo.addItem("ITA")
        self.combo.addItem("JAM")
        self.combo.addItem("JPN")
        self.combo.addItem("JEY")
        self.combo.addItem("JOR")
        self.combo.addItem("KAZ")
        self.combo.addItem("KEN")
        self.combo.addItem("KIR")
        self.combo.addItem("PRK")
        self.combo.addItem("KOR")
        self.combo.addItem("KWT")
        self.combo.addItem("KGZ")
        self.combo.addItem("LAO")
        self.combo.addItem("LVA")
        self.combo.addItem("LBN")
        self.combo.addItem("LSO")
        self.combo.addItem("LBR")
        self.combo.addItem("LBY")
        self.combo.addItem("LIE")
        self.combo.addItem("LTU")
        self.combo.addItem("LUX")
        self.combo.addItem("MAC")
        self.combo.addItem("MKD")
        self.combo.addItem("MDG")
        self.combo.addItem("MWI")
        self.combo.addItem("MYS")
        self.combo.addItem("MDV")
        self.combo.addItem("MLI")
        self.combo.addItem("MLT")
        self.combo.addItem("MHL")
        self.combo.addItem("MTQ")
        self.combo.addItem("MRT")
        self.combo.addItem("MUS")
        self.combo.addItem("MYT")
        self.combo.addItem("MEX")
        self.combo.addItem("FSM")
        self.combo.addItem("MDA")
        self.combo.addItem("MCO")
        self.combo.addItem("MNG")
        self.combo.addItem("MNE")
        self.combo.addItem("MSR")
        self.combo.addItem("MAR")
        self.combo.addItem("MOZ")
        self.combo.addItem("MMR")
        self.combo.addItem("NAM")
        self.combo.addItem("NRU")
        self.combo.addItem("NPL")
        self.combo.addItem("NLD")
        self.combo.addItem("NCL")
        self.combo.addItem("NZL")
        self.combo.addItem("NIC")
        self.combo.addItem("NER")
        self.combo.addItem("NGA")
        self.combo.addItem("NIU")
        self.combo.addItem("NFK")
        self.combo.addItem("MNP")
        self.combo.addItem("NOR")
        self.combo.addItem("OMN")
        self.combo.addItem("PAK")
        self.combo.addItem("PLW")
        self.combo.addItem("PSE")
        self.combo.addItem("PAN")
        self.combo.addItem("PNG")
        self.combo.addItem("PRY")
        self.combo.addItem("PER")
        self.combo.addItem("PHL")
        self.combo.addItem("PCN")
        self.combo.addItem("POL")
        self.combo.addItem("PRT")
        self.combo.addItem("PRI")
        self.combo.addItem("QAT")
        self.combo.addItem("ROU")
        self.combo.addItem("RUS")
        self.combo.addItem("RWA")
        self.combo.addItem("REU")
        self.combo.addItem("BLM")
        self.combo.addItem("SHN")
        self.combo.addItem("KNA")
        self.combo.addItem("LCA")
        self.combo.addItem("MAF")
        self.combo.addItem("SPM")
        self.combo.addItem("VCT")
        self.combo.addItem("WSM")
        self.combo.addItem("SMR")
        self.combo.addItem("STP")
        self.combo.addItem("SAU")
        self.combo.addItem("SEN")
        self.combo.addItem("SRB")
        self.combo.addItem("SYC")
        self.combo.addItem("SLE")
        self.combo.addItem("SGP")
        self.combo.addItem("SXM")
        self.combo.addItem("SVK")
        self.combo.addItem("SVN")
        self.combo.addItem("SLB")
        self.combo.addItem("SOM")
        self.combo.addItem("ZAF")
        self.combo.addItem("SGS")
        self.combo.addItem("SSD")
        self.combo.addItem("ESP")
        self.combo.addItem("LKA")
        self.combo.addItem("SDN")
        self.combo.addItem("SUR")
        self.combo.addItem("SJM")
        self.combo.addItem("SWZ")
        self.combo.addItem("SWE")
        self.combo.addItem("CHE")
        self.combo.addItem("SYR")
        self.combo.addItem("TWN")
        self.combo.addItem("TJK")
        self.combo.addItem("TZA")
        self.combo.addItem("THA")
        self.combo.addItem("TLS")
        self.combo.addItem("TGO")
        self.combo.addItem("TKL")
        self.combo.addItem("TON")
        self.combo.addItem("TTO")
        self.combo.addItem("TUN")
        self.combo.addItem("TUR")
        self.combo.addItem("TKM")
        self.combo.addItem("TCA")
        self.combo.addItem("TUV")
        self.combo.addItem("UGA")
        self.combo.addItem("UKR")
        self.combo.addItem("ARE")
        self.combo.addItem("GBR")
        self.combo.addItem("USA")
        self.combo.addItem("UMI")
        self.combo.addItem("URY")
        self.combo.addItem("UZB")
        self.combo.addItem("VUT")
        self.combo.addItem("VEN")
        self.combo.addItem("VNM")
        self.combo.addItem("VGB")
        self.combo.addItem("VIR")
        self.combo.addItem("WLF")
        self.combo.addItem("ESH")
        self.combo.addItem("YEM")
        self.combo.addItem("ZMB")
        self.combo.addItem("ZWE")
        layout.addRow(QLabel("*Country:"),self.combo)

        self.ccNum = QLineEdit()
        layout.addRow(QLabel("*Credit Card#:"), self.ccNum)

        default = QDate.currentDate().toPyDate()
        self.ccExpiry = QDateEdit(QDate(default.year, default.month, default.day))
        layout.addRow(QLabel("*CC Expiry:"), self.ccExpiry)

        default = QDate.currentDate().toPyDate()
        self.birthdate = QDateEdit(QDate(default.year, default.month, default.day))
        layout.addRow(QLabel("*Birth Date:"), self.birthdate)

        self.formGroupBox.setLayout(layout)

    def clickSearch(self):

        ccMonth = str(self.ccExpiry.date().month()).zfill(2)
        ccDay = str(self.ccExpiry.date().day()).zfill(2)
        ccYear = str(self.ccExpiry.date().year())
        ccDate = ccYear + ccMonth + ccDay
        #print(ccDate)

        bMonth = str(self.birthdate.date().month()).zfill(2)
        bDay = str(self.birthdate.date().day()).zfill(2)
        bYear = str(self.birthdate.date().year())
        bDate = bYear + bMonth + bDay

        if (self.email.text() == '' or self.password.text() == '' or self.firstName.text() == '' or self.lastName.text() == ''
            or self.address1.text() == '' or self.city.text() == '' or self.state.text() =='' or self.postalCode.text() == ''
            or self.combo.currentText() == '' or self.ccNum.text() == ''):

            QMessageBox.warning(self,
                    'Error', "Please fill out all required lines.")

        elif (self.email.text() != self.confirmEmail.text()):
            QMessageBox.warning(self,
                    'Error', "Emails do not match.")

        elif (self.password.text() != self.confirmPassword.text()):
            QMessageBox.warning(self,
                    'Error', "Passwords do not match.")

        else:
            self.hide()
            self._new_window = Search()
            self._new_window.show()

            userSQL = "insert into user(email,password,first_name,last_name) values(%s, %s, %s, %s);"
            cursor.execute(userSQL, (self.email.text(),self.password.text(), self.firstName.text(), self.lastName.text()))

            userIDSQL = "select user_id from user where email = %s and password = %s;"
            cursor.execute(userIDSQL, (self.email.text(), self.password.text()))
            dict1 = cursor.fetchall()[0]
            list1 = list(dict1.values())
            global userID
            userID = (list(dict1.values()))[0]


            addressSQL = "insert into address(line1,line2,city,state,post_code,country) values(%s,%s,%s,%s,%s,%s);"
            cursor.execute(addressSQL, (self.address1.text(), self.address2.text(), self.city.text(), self.state.text(), self.postalCode.text(), self.combo.currentText()))

            addressIDSQL = "select address_id from address where line1=%s and line2=%s and city=%s and state=%s and post_code=%s and country=%s;"
            cursor.execute(addressIDSQL, (self.address1.text(), self.address2.text(), self.city.text(), self.state.text(), self.postalCode.text(), self.combo.currentText()))
            dict2 = cursor.fetchall()[0]
            list2 = list(dict2.values())
            addressID = (list(dict2.values()))[0]


            customerSQL = "insert into customer(user_id, address_id, birthdate, credit_card_no, credit_card_expiry) values(%s, %s, %s, %s, %s);"
            cursor.execute(customerSQL, (str(userID), str(addressID), bDate, self.ccNum.text(),ccDate))
            connection.commit()



class Search(QDialog):
        def clickedSearch(self):
            dHour = str(self.deptTime1.time().hour()).zfill(2)
            dMin = str(self.deptTime1.time().minute()).zfill(2)
            global dTime
            dTime = dHour + dMin + "00"

            aHour = str(self.arrTime2.time().hour()).zfill(2)
            aMin = str(self.arrTime2.time().minute()).zfill(2)
            aTime = aHour + aMin + "00"

            global arrivalStation
            arrivalStation= self.toText1.text()
            global departureStation
            departureStation = self.fromText1.text()

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SearchResultsWindow()
            self.ui.searchResultSetupUi(self.window)
            self.hide()
            Ui_BookTrip.loadTripData(self.ui)
            self.window.show()

        def __init__(self):
            super(Search, self).__init__()
            self.createSearch()

            btn = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            btn.accepted.connect(self.clickedSearch)
            btn.rejected.connect(self.reject)
            checkBtn = QCheckBox("Return")

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(self.formGroupBox)
            mainLayout.addWidget(checkBtn)
            mainLayout.addWidget(btn)
            self.setLayout(mainLayout)
            checkBtn.stateChanged.connect(self.transform)
            self.setWindowTitle("Search Trips")

        def createSearch(self):
            self.formGroupBox = QGroupBox("Search Form")
            self.formGroupBox1 = QGroupBox()
            layout = QFormLayout()

            self.fromText1 = QLineEdit()
            self.toText1 = QLineEdit()


            layout.addRow(QLabel("From:"), self.fromText1)
            layout.addRow(QLabel("To:"), self.toText1)

            defaultDate = QDate.currentDate().toPyDate()
            self.deptDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))
            self.arrDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))

            layout.addRow(QLabel("Departure Date:"), self.deptDate1)
            layout.addRow(QLabel("Arrival Date:"), self.arrDate1)

            defaultTime = QTime.currentTime().toPyTime()
            self.deptTime1 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))
            self.arrTime2 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))

            layout.addRow(QLabel("Departure Time:"), self.deptTime1)
            layout.addRow(QLabel("Arrival Time:"), self.arrTime2)
            self.formGroupBox.setLayout(layout)

        def layoutOne(self):
            QWidget().setLayout(self.layout())
            checkBtn = QCheckBox("Return")
            self.formGroupBox = QGroupBox("Search Form")
            self.formGroupBox1 = QGroupBox()
            layout = QFormLayout()

            self.fromText1 = QLineEdit()
            self.toText1 = QLineEdit()

            defaultDate = QDate.currentDate().toPyDate()
            layout.addRow(QLabel("From:"), self.fromText1)
            layout.addRow(QLabel("To:"), self.toText1)

            self.deptDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))
            self.arrDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))

            layout.addRow(QLabel("Departure Date:"), self.deptDate1)
            layout.addRow(QLabel("Arrival Date:"), self.arrDate1)

            defaultTime = QTime.currentTime().toPyTime()
            self.deptTime1 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))
            self.arrTime2 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))

            layout.addRow(QLabel("Departure Time:"), self.deptTime1)
            layout.addRow(QLabel("Arrival Time:"), self.arrTime2)
            self.formGroupBox.setLayout(layout)
            checkBtn.stateChanged.connect(self.transform)

        def layoutTwo(self):
            QWidget().setLayout(self.layout())
            checkBtn = QCheckBox("Return")
            self.formGroupBox = QGroupBox("Search Form")
            self.formGroupBox1 = QGroupBox()
            layout = QFormLayout()

            self.fromText1 = QLineEdit()
            self.toText1 = QLineEdit()

            layout.addRow(QLabel("From:"), self.fromText1)
            layout.addRow(QLabel("To:"), self.toText1)

            defaultDate = QDate.currentDate().toPyDate()
            self.deptDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))
            self.arrDate1 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))

            layout.addRow(QLabel("Departure Date:"), self.deptDate1)
            layout.addRow(QLabel("Arrival Date:"), self.arrDate1)

            defaultTime = QTime.currentTime().toPyTime()

            self.deptTime1 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))
            self.arrTime2 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))

            layout.addRow(QLabel("Departure Time:"), self.deptTime1)
            layout.addRow(QLabel("Arrival Time:"), self.arrTime2)

            self.fromText2 = QLineEdit()
            self.toText2 = QLineEdit()

            layout.addRow(QLabel("From:"), self.fromText2)
            layout.addRow(QLabel("To:"), self.toText2)

            layout.addRow(QLabel("Departure Date:"), QLineEdit())
            layout.addRow(QLabel("Arrival Date:"), QLineEdit())

            self.DeptDate2 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))
            self.ArriveDate2 = QDateEdit(QDate(defaultDate.year, defaultDate.month, defaultDate.day))

            layout.addRow(QLabel("Departure Date:"), self.DeptDate2)
            layout.addRow(QLabel("Arrival Date:"), self.ArriveDate2)



            self.DeptTime2 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))
            self.arrTime2 = QTimeEdit(QTime(defaultTime.hour, defaultTime.minute, defaultTime.second))

            layout.addRow(QLabel("Departure Time:"), self.DeptTime2)
            layout.addRow(QLabel("Arrival Time:"), self.arrTime2)
            self.formGroupBox.setLayout(layout)
            checkBtn.stateChanged.connect(self.transform)


            self.formGroupBox.setLayout(layout)
            checkBtn.stateChanged.connect(self.transform)

        def transform(self, state):
            checkBtn = QCheckBox("Return")
            btn = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            btn.accepted.connect(self.accept)
            btn.rejected.connect(self.reject)

            if state == Qt.Checked:
                self.layoutTwo()
                checkBtn.toggle()
            else:
                self.layoutOne()
                checkBtn.toggle()

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(self.formGroupBox)
            mainLayout.addWidget(checkBtn)
            mainLayout.addWidget(btn)
            self.setLayout(mainLayout)
            checkBtn.stateChanged.connect(self.transform2)

        def transform2(self, state):
            checkBtn = QCheckBox("Return")
            btn = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            btn.accepted.connect(self.accept)
            btn.rejected.connect(self.reject)

            if state == Qt.Checked:
                self.layoutTwo()
            else:
                self.layoutOne()

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(self.formGroupBox)
            mainLayout.addWidget(checkBtn)
            mainLayout.addWidget(btn)
            self.setLayout(mainLayout)
            checkBtn.stateChanged.connect(self.transform)

class Ui_SearchResultsWindow(object):

    def searchResultSetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.outBoundLbl = QtWidgets.QLabel(self.centralwidget)
        self.outBoundLbl.setObjectName("outBoundLbl")
        self.gridLayout.addWidget(self.outBoundLbl, 0, 0, 1, 1)
        self.outboundTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.outboundTableWidget.setObjectName("outboundTableWidget")
        self.outboundTableWidget.setColumnCount(5)
        self.outboundTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.outboundTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outboundTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outboundTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outboundTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.outboundTableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.outboundTableWidget, 1, 0, 1, 4)
        self.returnLbl = QtWidgets.QLabel(self.centralwidget)
        self.returnLbl.setObjectName("returnLbl")
        self.gridLayout.addWidget(self.returnLbl, 2, 0, 1, 1)
        self.returnDate = QtWidgets.QLabel(self.centralwidget)
        self.returnDate.setObjectName("returnDate")
        self.gridLayout.addWidget(self.returnDate, 2, 2, 1, 1)
        self.returnTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.returnTableWidget.setObjectName("returnTableWidget")
        self.returnTableWidget.setColumnCount(5)
        self.returnTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.returnTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnTableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.returnTableWidget, 3, 0, 1, 4)
        self.bookBtn = QtWidgets.QPushButton(self.centralwidget)
        self.bookBtn.setObjectName("bookBtn")
        self.gridLayout.addWidget(self.bookBtn, 4, 3, 1, 1)
        self.bookBtn.clicked.connect(self.clickBook)
        self.outBoundDate = QtWidgets.QLabel(self.centralwidget)
        self.outBoundDate.setObjectName("outBoundDate")
        self.gridLayout.addWidget(self.outBoundDate, 0, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 4, 2, 1, 1)
        self.cancelBtn.clicked.connect(self.clickCancel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.searchResultRetranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clickCancel(self):
        QApplication.quit()

    def clickBook(self):
        selectedValues = self.outboundTableWidget.selectedItems()

        query = 'insert into trip(customer_id, price) values(%s,%s)'
        query2 = 'select customer_id from customer where user_id = %s'
        cursor.execute(query2, userID)
        c = cursor.fetchall()[0]
        cID = (list(c.values()))[0]
        cursor.execute(query,(str(cID),"100.00"))
        connection.commit()

        query3 = 'select last_insert_id()'
        cursor.execute(query3)
        d = cursor.fetchall()[0]

        global trip_id_value
        trip_id_value = (list(d.values()))[0]
        train_id_value = selectedValues[0].text()
        departure_time_value = selectedValues[2].text()

        arrival_time_value = selectedValues[4].text()
        query4 = 'select stop_id from stop where train_id = %s and departure_time = %s'
        cursor.execute(query4, (train_id_value, departure_time_value))
        e = cursor.fetchall()[0]
        embark_stop_id_value = (list(e.values()))[0]

        query5 = 'select stop_id from stop where train_id = %s and arrival_time = %s'
        cursor.execute(query5, (train_id_value, arrival_time_value))
        f = cursor.fetchall()[0]
        disembark_stop_id_value = (list(f.values()))[0]

        query6 = 'insert into trip_train values (%s, %s, %s)'
        cursor.execute(query6, (str(trip_id_value), str(embark_stop_id_value), str(disembark_stop_id_value)))
        connection.commit()

        self.window = QtWidgets.QDialog()
        self.ui = Ui_BookTrip()
        self.ui.setupUi(self.window)
        self.window.show()

    def searchResultRetranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Results"))
        self.outBoundLbl.setText(_translate("MainWindow", "Welcome! Please select entire row:"))
        item = self.outboundTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Train"))
        item = self.outboundTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Departure Station"))
        item = self.outboundTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Departure Time"))
        item = self.outboundTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Arrival Station"))
        item = self.outboundTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Arrival Time"))
        self.returnLbl.setText(_translate("MainWindow", "Return:"))
        self.returnDate.setText(_translate("MainWindow", "Date:"))
        item = self.returnTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Train"))
        item = self.returnTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Departure Station"))
        item = self.returnTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Departure Time"))
        item = self.returnTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Arrival Station"))
        item = self.returnTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Arrival Time"))
        self.bookBtn.setText(_translate("MainWindow", "Book"))
        self.outBoundDate.setText(_translate("MainWindow", "Date:"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))

class Ui_BookTrip(object):

    def loadTripData(self):
        query = "select train_id, start.name, start.departure_time, ending.name, ending.arrival_time from (select name, train_id, arrival_time, departure_time from stop join station using (station_id)) as start join (select name, train_id, arrival_time, departure_time from stop join station using (station_id)) as ending using (train_id) where (start.name = %s and ending.name = %s and start.arrival_time is NULL and ending.departure_time is NULL and start.departure_time >= %s)"

        cursor.execute(query, (departureStation, arrivalStation, dTime))
        result = cursor.fetchall()
        self.outboundTableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.outboundTableWidget.insertRow(row_number)
            for column_number, key in enumerate(row_data):
                value = row_data[key]
                self.outboundTableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(value)))

    def setupUi(self, BookTrip):
        BookTrip.setObjectName("BookTrip")
        BookTrip.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(BookTrip)
        self.gridLayout.setObjectName("gridLayout")
        self.costLabel = QtWidgets.QLabel(BookTrip)
        self.costLabel.setObjectName("costLabel")
        self.gridLayout.addWidget(self.costLabel, 1, 0, 1, 1)
        self.bookBtn = QtWidgets.QPushButton(BookTrip)
        self.bookBtn.setObjectName("bookBtn")
        self.gridLayout.addWidget(self.bookBtn, 2, 2, 1, 1)
        self.addPassBtn = QtWidgets.QPushButton(BookTrip)
        self.addPassBtn.setObjectName("addPassBtn")
        self.gridLayout.addWidget(self.addPassBtn, 2, 1, 1, 1)
        self.addPassBtn.clicked.connect(self.clickAddPass)
        self.cancelBtn = QtWidgets.QPushButton(BookTrip)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 2, 0, 1, 1)
        self.cancelBtn.clicked.connect(self.clickCancel)
        self.bookTable = QtWidgets.QTableWidget(BookTrip)
        self.bookTable.setObjectName("bookTable")
        self.bookTable.setColumnCount(3)
        self.bookTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.bookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.bookTable, 0, 0, 1, 3)

        self.retranslateUi(BookTrip)
        QtCore.QMetaObject.connectSlotsByName(BookTrip)

    def clickAddPass(self):
        self.windowPass = QtWidgets.QMainWindow()
        self.ui = Ui_AddPassWindow()
        self.ui.setupUi(self.windowPass)
        self.windowPass.show()

    def clickCancel(self):
        QApplication.quit()

    def retranslateUi(self, BookTrip):
        _translate = QtCore.QCoreApplication.translate
        BookTrip.setWindowTitle(_translate("BookTrip", "Passengers"))
        self.costLabel.setText(_translate("BookTrip", "Total Cost:"))
        self.bookBtn.setText(_translate("BookTrip", "Book"))
        self.addPassBtn.setText(_translate("BookTrip", "Add Passenger"))
        self.cancelBtn.setText(_translate("BookTrip", "Cancel"))
        item = self.bookTable.horizontalHeaderItem(0)
        item.setText(_translate("BookTrip", "Last Name"))
        item = self.bookTable.horizontalHeaderItem(1)
        item.setText(_translate("BookTrip", "First Name"))
        item = self.bookTable.horizontalHeaderItem(2)
        item.setText(_translate("BookTrip", "Birth Date"))

class Ui_AddPassWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.fNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.fNameLabel.setMinimumSize(QtCore.QSize(81, 16))
        self.fNameLabel.setObjectName("fNameLabel")
        self.gridLayout.addWidget(self.fNameLabel, 0, 0, 1, 1)

        self.lastName = QtWidgets.QLineEdit(self.centralwidget)

        self.lastName.setObjectName("lastName")
        self.gridLayout.addWidget(self.lastName, 1, 2, 1, 1)
        self.lNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lNameLabel.setObjectName("lNameLabel")
        self.gridLayout.addWidget(self.lNameLabel, 1, 0, 1, 1)
        self.bDayLabel = QtWidgets.QLabel(self.centralwidget)
        self.bDayLabel.setObjectName("bDayLabel")
        self.gridLayout.addWidget(self.bDayLabel, 2, 0, 1, 1)

        self.firstName = QtWidgets.QLineEdit(self.centralwidget)

        self.firstName.setMinimumSize(QtCore.QSize(113, 21))
        self.firstName.setObjectName("firstName")
        self.gridLayout.addWidget(self.firstName, 0, 2, 1, 1)

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)

        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 2, 1, 1)
        self.OKBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OKBtn.setObjectName("OKBtn")
        self.OKBtn.clicked.connect(self.clickedOK)
        self.gridLayout.addWidget(self.OKBtn, 3, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 3, 0, 1, 1)
        self.cancelBtn.clicked.connect(self.clickCancel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clickedOK(self):

        bMonth = str(self.dateEdit.date().month()).zfill(2)
        bDay = str(self.dateEdit.date().day()).zfill(2)
        bYear = str(self.dateEdit.date().year())
        bDate = bYear + bMonth + bDay

        sql = "insert into passenger(first_name, last_name, birthdate, trip_id) values (%s,%s,%s,%s);"
        cursor.execute(sql, (self.firstName.text(), self.lastName.text(),bDate, trip_id_value))
        connection.commit()
        self.windowPass.hide()


    def clickCancel(self):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passenger"))
        self.fNameLabel.setText(_translate("MainWindow", "*First Name:"))
        self.lNameLabel.setText(_translate("MainWindow", "*Last Name:"))
        self.bDayLabel.setText(_translate("MainWindow", "*Birth Date:"))
        self.OKBtn.setText(_translate("MainWindow", "OK"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Login')
    login = Login()
    login.show()
    global connection
    connection = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         db='sncf_team5',
                         charset='utf8mb4')

    cursor = connection.cursor(cursors.DictCursor)
    sys.exit(app.exec_())
