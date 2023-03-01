import sqlite3
import time
import random
class Client():
    def __init__(self,name,id,password,balance):
        self.name = name
        self.id = id
        self.password = password
        self.balance = balance
    def __str__(self):
        return "Client Information\nName: {}\nId: {}\nPassword: {}\nBalance: {}USD".format(self.name,self.id,self.password,self.balance)
class Bank():
    def __init__(self):
        self.make_connection()
    def make_connection(self):
        self.connection = sqlite3.connect("HZ BANK.db")
        self.cursor = self.connection.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS Clients(Name TEXT, Id INT, Password INT, Balance INT)"
        self.cursor.execute(sorgu)
        self.connection.commit()
    def cut_connection(self):
        self.connection.close()
    def hesap_bilgileri(self,id):
        sorgu = "SELECT * FROM Clients WHERE Id =?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        person = Client(liste[0][0],liste[0][1],liste[0][2],liste[0][3])
        print(person)
        time.sleep(3)
    def check_name(self,id):
        sorgu = "SELECT Name FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        
        if len(liste) == 0:
            return False
        else:
            name = liste[0][0]
            return name
    
    def check_password(self,id):
        sorgu = "SELECT Password FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            return 0
        else:
            password = liste[0][0]
            return password
    def check_balance(self,id):
        sorgu = "SELECT Balance FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        balance = liste[0][0]
        
        return balance
        
    def Deposit(self,id,amount):
        sorgu = "SELECT Balance FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        old_balance = liste[0][0]
        new_balance = old_balance + amount
        sorgu1 = "UPDATE Clients SET Balance = ? WHERE Id = ?"
        self.cursor.execute(sorgu1,(new_balance,id))
        self.connection.commit()
        
        
        return new_balance
    def withdraw(self,id,amount):
        sorgu = "SELECT Balance FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu, (id,))
        liste = self.cursor.fetchall()
        old_balance = liste[0][0]
        if amount > old_balance:
            
            
            return False
        else:
            new_balance = old_balance - amount
            sorgu1 = "UPDATE Clients SET Balance = ? WHERE Id = ?"
            self.cursor.execute(sorgu1, (new_balance, id))
            self.connection.commit()
            
            
            return new_balance
    def transfer(self,id,id2,amount):
        sorgu = "SELECT Balance FROM Clients WHERE Id = ?"
        self.cursor.execute(sorgu,(id,))
        liste = self.cursor.fetchall()
        veren_bakiye = liste[0][0]
        self.cursor.execute(sorgu,(id2,))
        liste1 = self.cursor.fetchall()
        if len(liste1) == 0:
            
            
            return 1
        else:
            gelen_bakiye = liste1[0][0]
            if amount > veren_bakiye:
                
                return 2
            else:
                
                
                yeni_veren_bakiye = veren_bakiye - amount
                yeni_gelen_bakiye = gelen_bakiye + amount
                sorgu1 = "UPDATE Clients SET Balance = ? WHERE Id = ?"
                self.cursor.execute(sorgu1, (yeni_veren_bakiye, id))
                self.connection.commit()
                

                
                self.cursor.execute(sorgu1, (yeni_gelen_bakiye, id2))
                self.connection.commit()
                return yeni_veren_bakiye
    def new_client(self,name,password):
        sorgu1 = "SELECT Id FROM Clients"
        sorgu = "INSERT INTO Clients Values(?,?,?,?)"
        self.cursor.execute(sorgu1)
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            id = random.randint(0,100)
            self.cursor.execute(sorgu,(name,id,password,0))
            self.connection.commit()
            sorgu2 = "SELECT * FROM Clients WHERE Id = ?"
            self.cursor.execute(sorgu2,(id,))
            liste1 = self.cursor.fetchall()
            

            
        else:
            sayma = 0
            while True:
                id = random.randint(0,100)
                sayac = 0
                for i in liste:
                    if i[0] == id:
                        sayac += 1
                if sayac == 0:
                    self.cursor.execute(sorgu, (name, id, password, 0))
                    self.connection.commit()
                    
                    return True

                    
                if sayma == 100:
                    
                    return False
                sayma += 1
            
    def check_id(self,name):
        sorgu = "SELECT Id FROM Clients WHERE Name = ?"
        self.cursor.execute(sorgu,(name,))
        liste = self.cursor.fetchall()
        id = liste[0][0]
        return id    
            
            
            
            
            
            
            


    def change_password(self,id,password):
        sorgu = "UPDATE Clients SET Password = ? WHERE Id = ?"
        self.cursor.execute(sorgu,(password,id))
        self.connection.commit()
        time.sleep(3)
        return "Process Worked Successfully"
    def delete_user(self,id):
        sorgu = "DELETE FROM Clients WHERE Id = ?"
        
        
        time.sleep(2)
        self.cursor.execute(sorgu,(id,))
        self.connection.commit()
        return "Account Has Been Deleted Successfully"
        