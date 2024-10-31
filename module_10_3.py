import threading
from time import sleep
from datetime import datetime
from threading import Thread,Lock
import random

class Bank:
    def __init__(self, balance: int=0, Lock =Lock()):
        self.balance = balance
        self.Lock = Lock

    def deposit(self):
        for i in range(100):
            randome = random.randint(50, 500)
            print(f"Пополнение: {randome}. Баланс: {self.balance} ")
            self.balance += randome
            if self.balance >= 500 and  self.Lock.locked():
                self.Lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            randome = random.uniform(50, 500)
            print(f"Запрос на {randome}")
            if randome <= self.balance:
                self.balance -= randome
                print(f"Снятие: {randome}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.Lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

