from BankData import *
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QFormLayout, QStackedLayout, QLabel, QLineEdit, QPushButton, QWidget, QComboBox, QCheckBox
    


atm = Bank()
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("HZ BANK")
        # Main Window
        layout = QVBoxLayout()
        
        # Create Stacked Layout
        self.stackedLayout = QStackedLayout()
        # Create Login Page
        self.login_page = QWidget()
        
        self.first_line = QHBoxLayout()
        self.Label = QLabel("Login")
        self.Label1 = QLabel("Register")
        self.first_line.addWidget(self.Label)
        self.first_line.addStretch()
        self.first_line.addWidget(self.Label1)
        
        self.second_line = QHBoxLayout()
        self.login_line = QLineEdit()
        self.register_line = QLineEdit()
        self.second_line.addWidget(self.login_line)
        self.second_line.addStretch()
        self.second_line.addWidget(self.register_line)

        self.third_line = QHBoxLayout()
        self.password_line = QLineEdit()
        self.password_line.setEchoMode(QLineEdit.Password)
        self.password_line1 = QLineEdit()
        self.third_line.addWidget(self.password_line)
        self.third_line.addStretch()
        self.third_line.addWidget(self.password_line1)

        self.fourth_line = QHBoxLayout()
        self.Label2 = QLabel("")
        self.reg_password = QLineEdit()
        self.fourth_line.addWidget(self.Label2)
        self.fourth_line.addStretch()
        self.fourth_line.addWidget(self.reg_password)
        
        self.fifth_line = QHBoxLayout()
        self.Label3 = QLabel("Check Your Lines Twice")
        self.fifth_line.addStretch()
        self.fifth_line.addWidget(self.Label3)

        self.sixth_line = QHBoxLayout()
        self.LoginButton = QPushButton("Login")
        self.RegisterButton = QPushButton("Register")
        self.sixth_line.addWidget(self.LoginButton)
        self.sixth_line.addStretch()
        self.sixth_line.addWidget(self.RegisterButton)

        self.loginlayout = QVBoxLayout()
        self.loginlayout.addLayout(self.first_line)
        self.loginlayout.addLayout(self.second_line)
        self.loginlayout.addLayout(self.third_line)
        self.loginlayout.addLayout(self.fourth_line)
        self.loginlayout.addLayout(self.fifth_line)
        self.loginlayout.addLayout(self.sixth_line)
        
        self.login_page.setLayout(self.loginlayout)
        self.stackedLayout.addWidget(self.login_page)

        # Creating Process Page
        self.process_page = QWidget()
        # Buttons
        self.D_button = QPushButton("Deposit")
        self.T_button = QPushButton("Transfer")
        self.w_button = QPushButton("Withdraw")
        self.e_button= QPushButton("Exit")
        self.Back_Button = QPushButton("Back")
        self.with_draw_page = QPushButton("Withdraw")
        self.deposit_page = QPushButton("Deposit")
        self.transfer_page = QPushButton("Transfer")
        self.deposit_back = QPushButton("Back")
        self.withdraw_back = QPushButton("Back")

        # Line Edits
        self.deposit = QLineEdit()
        self.Id = QLineEdit()
        self.Name = QLineEdit()
        self.transfer = QLineEdit()
        self.with_draw = QLineEdit()
        # Informations
        

        self.second_pagelayout = QHBoxLayout()

        self.second_pagevlayout = QVBoxLayout()
        self.Balance = QLabel("")
        self.second_pagevlayout.addStretch()
        self.second_pagevlayout.addWidget(self.Balance)
        self.second_pagevlayout.addWidget(self.with_draw_page)
        self.second_pagevlayout.addWidget(self.deposit_page)
        self.second_pagevlayout.addWidget(self.transfer_page)
        self.second_pagevlayout.addWidget(self.e_button)
        self.second_pagevlayout.addStretch()

        self.second_pagelayout.addStretch()
        self.second_pagelayout.addLayout(self.second_pagevlayout)
        self.second_pagelayout.addStretch()

        self.process_page.setLayout(self.second_pagelayout)
        self.stackedLayout.addWidget(self.process_page)
        # Creating Deposit Page
        self.deposit_layout = QWidget()
        
        self.deposit_label = QLabel("Deposit Page")
        self.deposit_amount_label = QLabel("Amount:")
        self.deposit_situation = QLabel("")
        self.deposit_line = QHBoxLayout()
        self.deposit_line.addStretch()
        self.deposit_line.addWidget(self.deposit_amount_label)
        self.deposit_line.addWidget(self.deposit)
        self.deposit_line.addStretch()

        self.deposit_hlayout = QHBoxLayout()
        self.deposit_vlayout = QVBoxLayout()
        
        self.deposit_vlayout.addStretch()
        self.deposit_vlayout.addWidget(self.deposit_label)
        self.deposit_vlayout.addLayout(self.deposit_line)
        self.deposit_vlayout.addWidget(self.D_button)
        self.deposit_vlayout.addWidget(self.deposit_situation)
        self.deposit_vlayout.addWidget(self.deposit_back)
        self.deposit_vlayout.addStretch()

        self.deposit_hlayout.addStretch()
        self.deposit_hlayout.addLayout(self.deposit_vlayout)
        self.deposit_hlayout.addStretch()

        self.deposit_layout.setLayout(self.deposit_hlayout)
        self.stackedLayout.addWidget(self.deposit_layout)
        # Creating Withdraw Page
        self.withdraw_layout = QWidget()
        
        self.withdraw_label = QLabel("Withdraw Page")
        self.withdraw_amount_label = QLabel("Amount:")
        self.withdraw_situation = QLabel("")
        self.withdraw_line = QHBoxLayout()
        self.withdraw_line.addStretch()
        self.withdraw_line.addWidget(self.withdraw_amount_label)
        self.withdraw_line.addWidget(self.with_draw)
        self.withdraw_line.addStretch()

        self.withdraw_hlayout = QHBoxLayout()
        self.withdraw_vlayout = QVBoxLayout()
        
        self.withdraw_vlayout.addStretch()
        self.withdraw_vlayout.addWidget(self.withdraw_label)
        self.withdraw_vlayout.addLayout(self.withdraw_line)
        self.withdraw_vlayout.addWidget(self.w_button)
        self.withdraw_vlayout.addWidget(self.withdraw_situation)
        self.withdraw_vlayout.addWidget(self.withdraw_back)
        self.withdraw_vlayout.addStretch()

        self.withdraw_hlayout.addStretch()
        self.withdraw_hlayout.addLayout(self.withdraw_vlayout)
        self.withdraw_hlayout.addStretch()

        self.withdraw_layout.setLayout(self.withdraw_hlayout)
        self.stackedLayout.addWidget(self.withdraw_layout)
        # Creating Transer Page
        self.transfer_layout = QWidget()
        
        self.transfer_label = QLabel("Transfer Page")
        self.transfer_amount_label = QLabel("Amount:")
        self.transfer_situation = QLabel("")
        self.transfer_line = QHBoxLayout()
        self.transfer_line.addStretch()
        self.transfer_line.addWidget(self.transfer_amount_label)
        self.transfer_line.addWidget(self.transfer)
        self.transfer_line.addStretch()

        self.nameid_line = QHBoxLayout()
        self.transfer_id = QLabel("Id:")
        self.transef_name = QLabel("Name:")
        self.nameid_line.addStretch()
        self.nameid_line.addWidget(self.transfer_id)
        self.nameid_line.addWidget(self.Id)
        self.nameid_line.addStretch()
        self.nameid_line.addWidget(self.transef_name)
        self.nameid_line.addWidget(self.Name)
        self.nameid_line.addStretch()

        self.transfer_hlayout = QHBoxLayout()
        self.transfer_vlayout = QVBoxLayout()
        
        self.transfer_vlayout.addStretch()
        self.transfer_vlayout.addWidget(self.transfer_label)
        self.transfer_vlayout.addLayout(self.nameid_line)
        self.transfer_vlayout.addLayout(self.transfer_line)
        self.transfer_vlayout.addWidget(self.T_button)
        self.transfer_vlayout.addWidget(self.transfer_situation)
        self.transfer_vlayout.addWidget(self.Back_Button)
        self.transfer_vlayout.addStretch()

        self.transfer_hlayout.addStretch()
        self.transfer_hlayout.addLayout(self.transfer_vlayout)
        self.transfer_hlayout.addStretch()

        self.transfer_layout.setLayout(self.transfer_hlayout)
        self.stackedLayout.addWidget(self.transfer_layout)

        # Connecting Buttons
        self.LoginButton.clicked.connect(self.login)
        self.e_button.clicked.connect(self.exit)
        self.w_button.clicked.connect(self.withdraw_m)
        self.T_button.clicked.connect(self.transfer_m)
        self.D_button.clicked.connect(self.deposit_m)
        self.RegisterButton.clicked.connect(self.register)
        self.transfer_page.clicked.connect(self.transfer_process)
        self.with_draw_page.clicked.connect(self.withdraw_process)
        self.deposit_page.clicked.connect(self.deposit_process)
        self.Back_Button.clicked.connect(self.Back)
        self.withdraw_back.clicked.connect(self.withdraw_back_button)
        self.deposit_back.clicked.connect(self.deposit_back_button)

        self.setLayout(self.stackedLayout)

        self.show()
    def login(self):
        self.id = self.login_line.text()
        if atm.check_password(self.id):
            password = int(self.password_line.text())
            if password == atm.check_password(self.id):
                name = atm.check_name(self.id)
                balance = atm.check_balance(self.id)
                self.login_line.clear()
                self.password_line.clear()
                self.stackedLayout.setCurrentIndex(1)
                self.Label2.setText("")
                self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))

            else:
                self.Label2.setText("Oops! Wrong Password :(")
        else:
            self.Label2.setText("Oops! User Could Not Found:(")

    def exit(self):
        self.deposit.clear()
        self.with_draw.clear()
        self.Id.clear()
        self.Name.clear()
        self.transfer.clear()
        self.stackedLayout.setCurrentIndex(0)
        
        self.id = None
    def withdraw_m(self):
        amount = self.with_draw.text()
        amount = int(amount)
        balance = atm.withdraw(self.id,amount)
        if not balance:
            self.withdraw_situation.setText("Sorry, Unefficient Balance")
        else:
            self.withdraw_situation.setText("Congratulations Process Worked Successfully :)")
            name = atm.check_name(self.id)
            self.with_draw.clear()
            self.withdraw_situation.setText("")
            self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
    def transfer_m(self):
        
        id2 = int(self.Id.text())
        amount = self.transfer.text()
        amount = int(amount)
        name1 = atm.check_name(self.id)
        name2 = self.Name.text()
        
        if name2 != atm.check_name(id2) or id2 != atm.check_id(name2):
            self.transfer_situation.setText("Check Name Or Id")
        else:
            balance = atm.transfer(self.id,id2,amount)
            if balance == 1:
                self.transfer_situation.setText("User Could Not Found")
            elif balance == 2:
                self.transfer_situation.setText("Sorry, Unefficient Balance")
            else:
                self.transfer_situation.setText("Congratulations Process Worked Successfully :)")
                self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name1,self.id,balance))
                self.transfer.clear()
                self.Name.clear()
                self.Id.clear()
                self.transfer_situation.setText("")
    def deposit_m(self):
        amount = self.deposit.text()
        amount = int(amount)
        name = atm.check_name(self.id)
        balance = atm.Deposit(self.id,amount)
        self.deposit_situation.setText("Congratulations Process Worked Successfully :)")
        self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
        self.deposit.clear()
        self.deposit_situation.setText("")
    def register(self):
        name = self.register_line.text()
        password = self.password_line1.text()
        r_password = self.reg_password.text()
        if name == "":
            self.Label3.setText("Please! Write Your Name")
        elif r_password == "" or password == "":
            self.Label3.setText("Please! Write Password Twice")
        elif r_password != password:
            self.Label3.setText("Please! Check Your Password")
        else:
            
            password = int(password)
            r_password = int(r_password)
            situation = atm.new_client(name,password)
            if not situation:
                self.Label3.setText("Sorry! Unefficient ID Stock")
            else:
                self.id = atm.check_id(name)
                balance = atm.check_balance(self.id)
                self.register_line.clear()
                self.password_line1.clear()
                self.reg_password.clear()
                self.stackedLayout.setCurrentIndex(1)
                self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
    def transfer_process(self):
        self.stackedLayout.setCurrentIndex(4)
    def withdraw_process(self):
        self.stackedLayout.setCurrentIndex(3)
    def deposit_process(self):
        self.stackedLayout.setCurrentIndex(2)
    def Back(self):
        self.stackedLayout.setCurrentIndex(1)
        name = atm.check_name(self.id)
        balance = atm.check_balance(self.id)
        self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
            
    def withdraw_back_button(self):
        self.stackedLayout.setCurrentIndex(1)
        name = atm.check_name(self.id)
        balance = atm.check_balance(self.id)
        self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
    def deposit_back_button(self):
        self.stackedLayout.setCurrentIndex(1)
        name = atm.check_name(self.id)
        balance = atm.check_balance(self.id)
        self.Balance.setText("Welcome {}\nYour Id: {}\nBalance: {}USD".format(name,self.id,balance))
        

        






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    bank = Window()

    sys.exit(app.exec_())