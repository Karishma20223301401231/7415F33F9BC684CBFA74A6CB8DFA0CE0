# BankAccount class 
class Bankaccount:

  def __init__(self):

# Function to deposit amount
   def deposit(self):
      amount =float(input("enter                amount to be deposited:"))       
      self.balance+=amount
      print("\n Amount                              Deposited:",amount)

# Function to withdraw the amount
def withdraw (self):
     amount=float(input("enter amount to be withdrawn:"))
     if self.balance>=amount:
       self.balance-=amount
       print("\n you withdraw:, amount")
     else:
       print("\n insufficient balance ")

# Function to display the amount
def display(self):
        print("\n New available balance=", self.balance)

# python program to create Bank account class 
# with both a deposit() and a withdraw () function
class  Bank_Account:
    def __init__(self):
      self.balance=0
      print("Hello!!! Welcome to the deposit & withdrawal machine ")

    def deposit(self):
        amount=float(input("enter amount to be deposited"))
        self.balance+=amount
        print ("\n amount deposited:", amount)

    def withdraw(self):
        amount=float(input("enter amount to be withdraw:"))
        if self.balance>=amount:
           self.balance-=amount
           print("\n you withdraw:", amount)
        else:
          print("\n insufficient balance ")

    def display(self):
        print("\n new available balance=",self.balance)

# Driver code

#creating an object of class
s=Bank_Account()

# calling functions with that class object
s.deposit()
s.withdraw()
s.display()
    
     