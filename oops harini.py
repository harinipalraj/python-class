# inheritance
# class(Animal):
    # def __init__ (self,name):
        # self.name=name
    # def speak(self):
        # return("some sounds")
# class Dog(Animal):
    # def speak(self):
        # return("bark")
# class cat(Dog):
    # def speak(self):
        # return("meow")
# class lion(cat):
    # def speak(self):
        # return("roar")
# dog=Dog("buddy")
# cat1=cat("kitty")
# print(dog.name)
# print(dog.speak())
# print(cat1.speak())
# print(cat1.name)
# print(lion.speak())
# encapsulation
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age>0:
#             self.__age=age
#         else:
#             print("age must +")
# p=Person("harini",19)
# # print(p.age)
# print(p.get_age())
# p.set_age(30)
# # print(p.get_age())

# class bankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f"deposited{amount}")
#         else:
#             print("amount+")
#     def withdraw(self,amount):
#         if 0<amount<=self.__balance:
#             self.__balance-=amount
#             print(f"withdraw:{amount}")
#         else:
#             print("Invalid withdraw amount")
#     def get_balance(self):
#         return self.__balance
# # account=bankAccount(5000)
# # harini=bankAccount(4000)
# # harini.deposit(500)
# # harini.withdraw(200)
# # print(harini.get_balance())
# # praveen=bankAccount(50000)
# # praveen.deposit(2500)
# # praveen.withdraw(5000)
# # print(praveen.get_balance())

# polymorphism

# class animal:
#     def speak(self):
#         return"some sounds"
# class dog(animal):
#     def speak(self):
#         return"bark"
# class cat(animal):
#     def speak(self):
#         return"meow"
# Animal=cat()
# print (Animal.speak())

# abstraction
# from abc import ABC,abstractmethod
# class Bank(ABC):
#     @abstractmethod
#     def loan_intrest(self):
#         pass
# class HDFC(Bank):
#     def loan_intrest(self):
#         return "loan intrest rate 8%"
# class SBI(Bank):
#     def loan_intrest(self):
#         return "loan intrest rate 7%"
# a =SBI()
# print(a.loan_intrest())
# print(5/2)





  


