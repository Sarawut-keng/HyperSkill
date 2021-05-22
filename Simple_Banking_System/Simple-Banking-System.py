import sqlite3
import random


class CardAnatomy:

    def __init__(self):
        self.card_num = None
        self.card_pin = None
        self.check = []
        self.conn = None
        self.cur = None
        self.number = None

    def database(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            'create table if not exists card(id integer, number text, pin text, balance integer default 0)')
        self.conn.commit()

    def store_data(self):
        self.cur.execute(f'insert into card(number, pin) values({self.card_num},{self.card_pin})')
        self.conn.commit()

    def main(self):
        self.database()
        print("1. Create an account\n2. Log into account\n0. Exit")
        choose = int(input())
        if choose == 1:
            return self.account()
        elif choose == 2:
            return self.login()
        elif choose == 0:
            print("Bye!")
            pass
        else:
            pass

    def account(self):
        print("\nYour card has been created")
        self.card_num = ['4', '0', '0', '0', '0', '0']
        for _ in range(9):
            num = str(random.randint(0, 9))
            self.check.append(int(num))
            self.card_num.append(num)
        self.luhn()
        self.card_num = ''.join(self.card_num)
        print(f"Your card number:\n{self.card_num}")
        self.card_pin = []
        for _ in range(4):
            pin = str(random.randint(0, 9))
            self.card_pin.append(pin)
        self.card_pin = ''.join(self.card_pin)
        print(f"Your card PIN:\n{self.card_pin}\n")
        self.store_data()
        return self.main()

    def luhn(self):
        for i in range(0, 9, 2):
            self.check[i] *= 2
            if self.check[i] > 9:
                self.check[i] -= 9
        total = 8
        for n in self.check:
            total += n
        last = str(10 - (total % 10))
        self.card_num.append("0" if last == "10" else last)
        self.check = []

    def login(self):
        print("\nEnter your card number:")
        self.number = input()
        print("Enter your PIN:")
        pin = input()
        self.cur.execute('select number, pin from card')
        login_ = self.cur.fetchall()
        for i in range(0, len(login_)):
            if login_[i][0] == self.number:
                if login_[i][1] == pin:
                    print("\nYou have successfully logged in!\n")
                    return self.sub_main()
                else:
                    print("Wrong card number or PIN!")
                    return self.main()
        print("Wrong card number or PIN!")
        return self.main()

    def sub_main(self):
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
        choice = int(input())
        if choice == 1:
            self.cur.execute(f'select balance from card where number = {self.number}')
            balance = self.cur.fetchone()
            print(f"Balance: {balance[0]}\n")
            return self.sub_main()
        elif choice == 2:
            print("Enter income:")
            income = int(input())
            self.cur.execute(f'update card set balance = balance + {income} where number = {self.number}')
            self.conn.commit()
            print("Income was added!\n")
            return self.sub_main()
        elif choice == 3:
            return self.transfer()
        elif choice == 4:
            self.cur.execute(f'delete from card where number = {self.number}')
            self.conn.commit()
            return self.sub_main()
        elif choice == 5:
            print("\nYou have successfully logged out!\n")
            return self.main()
        elif choice == 0:
            print("\nBye!")
            pass

    def transfer(self):
        print("Transfer\nEnter card number:")
        enter = input()
        self.cur.execute('select number from card')
        enter_ = self.cur.fetchall()
        luhn = []
        for w in enter:
            luhn.append(int(w))
        if len(luhn) != 16:
            print("wrong number!!!")
            return self.sub_main()
        for j in range(0, 15, 2):
            luhn[j] *= 2
            if luhn[j] > 9:
                luhn[j] -= 9
        total = 0
        for n in range(15):
            total += luhn[n]
        last = 10 - (total % 10)
        if last == 10:
            last = 0
        else:
            pass
        if last != luhn[15]:
            print("Probably you made mistake in the card number. Please try again!\n")
            return self.sub_main()
        if enter == self.number:
            print("You can't transfer money to the same account!\n")
            return self.sub_main()
        for num in range(len(enter_)):
            if enter in enter_[num]:
                print("Enter how much money you want to transfer:")
                money = int(input())
                self.cur.execute(f'select balance from card where number = {self.number}')
                money_ = self.cur.fetchone()
                if money > money_[0]:
                    print("Not enough money!")
                    return self.sub_main()
                else:
                    self.cur.execute(f'update card set balance = balance - {money} where number = {self.number}')
                    self.cur.execute(f'update card set balance = balance + {money} where number = {enter}')
                    self.conn.commit()
                    print("Success!")
                    return self.sub_main()
        print("Such a card does not exist.\n")
        return self.sub_main()


banking_system = CardAnatomy()
banking_system.main()
