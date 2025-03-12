
class Bank:
    def __init__(self):
        self.__user_list = []
        self.__account_list = []
        self.__atm_card_list = []
        self.__atm_machine_list = []

    def add_user(self, citizen_id: str, name: str):
        self.__user_list.append(User(citizen_id, name))

    def add_account(self, citizen_id: str, account_number: str, money: int):
        for user in self.__user_list:
            if user.citizen_id == citizen_id:
                self.__account_list.append(Account(account_number, user, money))

    def add_atm_card(self, account_number: str, card_number: str, pin: str):
        for account in self.__account_list:
            if account.account_number == account_number:
                self.__atm_card_list.append(ATMCard(card_number, account, pin))

    def add_atm_machine(self, machine_id: str, initial_amount: float):
        self.__atm_machine_list.append(ATMMachine(machine_id, initial_amount, self))

    @property
    def user_list(self):
        return self.__user_list

    @property
    def account_list(self):
        return self.__account_list

    @property
    def atm_card_list(self):
        return self.__atm_card_list

    @property
    def atm_machine_list(self):
        return self.__atm_machine_list


class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name

    @property
    def citizen_id(self):
        return self.__citizen_id

    @property
    def name(self):
        return self.__name

class Account:
    def __init__(self, account_number: str, owner: User, money: int):
        self.__account_number = account_number
        self.__owner = owner
        self.__money = money
        self.__max_money = 40000
        self.__transactions = []

    def deposit(self, bank : Bank , machine_id : str ,amount : int):
        for atm_machine in bank.atm_machine_list :
            if atm_machine.machine_id == machine_id :
                    temp = self.__money
                    self.__money += amount
                    self.__transactions.append(f'D-ATM:{machine_id}-{temp}-{self.__money}')
                    return True
        return False

    def withdraw(self, bank : Bank , machine_id : str ,amount : int):
        for atm_machine in bank.atm_machine_list :
            if atm_machine.machine_id == machine_id :
                if amount > self.__money : return False
                else :
                    self.__max_money -= amount
                    if self.__max_money < 0 : 
                        self.__max_money += amount
                        return 'Exceeds daily withdrawal limit of 40,000 baht'
                    temp = self.__money
                    self.__money -= amount
                    self.__transactions.append(f'W-ATM:{machine_id}-{temp}-{self.__money}')
                    return True
        return False

    def transfer(self, bank: Bank, machine_id: str, account_number: str, amount: int):
        for atm_machine in bank.atm_machine_list:
            if atm_machine.machine_id == machine_id:
                if  amount > self.__money: return False
                for acc in bank.account_list:
                    if acc.account_number == account_number:
                        temp1 = self.__money
                        temp2 = acc.money  
                        self.__money -= amount  
                        acc.add_money(amount)  
                        acc.transactions.append(f"TD-ATM:{machine_id}-{temp2}-{acc.money}")  
                        self.__transactions.append(f'TW-ATM:{machine_id}-{temp1}-{self.__money}')  
                        return True
                return False
        return False

    @property
    def account_number(self):
        return self.__account_number

    @property
    def money(self):
        return self.__money

    @property
    def transactions(self):
        return self.__transactions

    @property
    def owner(self):
        return self.__owner

    def add_transactions(self, text : str):
        return  self.__transactions.append(text)

    def add_money(self, amount: int):
        self.__money += amount

    def remove_money(self, amount: int):
        self.__money -= amount

class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin

    @property
    def card_number(self):
        return self.__card_number

    @property
    def pin(self):
        return self.__pin

    @property
    def account(self):
        return self.__account


class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000, bank: Bank = None):
        self.__machine_id = machine_id
        self.__initial_amount = initial_amount
        self.__bank = bank

    @property
    def machine_id(self):
        return self.__machine_id

    def insert_card(self, atm_card: ATMCard, pin: str):
        if atm_card.pin == pin:
            return atm_card.card_number, atm_card.account.account_number, 'Success'
        else:
            return 'Invalid Pin'

    @property
    def get_balance(self):
        return self.__initial_amount

    def deposit(self, account: Account, amount: int):
        if amount < 0 : return 'Error'
        if account.deposit(self.__bank, self.__machine_id, amount):  
            self.__initial_amount += amount  
            return "Success"
        return "Error"
        
    def withdraw(self, account: Account, amount: int):
        if amount > self.__initial_amount:
            return "ATM has insufficient funds"
        if account.withdraw(self.__bank, self.__machine_id, amount):  
            self.__initial_amount -= amount
            return "Success"
        return "Error"
        
    def transfer(self, source_account: Account, target_account: Account, amount: int):
        if source_account.transfer(self.__bank, self.__machine_id, target_account.account_number, amount):  
            return "Success"
        return "Error"



my_bank = Bank()
my_bank.add_user('1-1101-12345-12-0', 'Harry Potter')
my_bank.add_user('1-1101-12345-13-0', 'Hermione Jean Granger')
my_bank.add_account('1-1101-12345-12-0', '1234567890', 20000)
my_bank.add_account('1-1101-12345-13-0', '0987654321', 1000)
my_bank.add_atm_card('1234567890', '12345', '1234')
my_bank.add_atm_card('0987654321', '12346', '1234')
my_bank.add_atm_machine('1001', 1000000)
my_bank.add_atm_machine('1002', 200000)


# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print('------Test Case 1------')
print(my_bank.atm_machine_list[0].insert_card(my_bank.atm_card_list[0],'1234')) 

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print('------Test Case 2------')
print('before :{0}'.format(my_bank.account_list[1].money))
my_bank.atm_machine_list[1].deposit(my_bank.account_list[1], 1000)
print('after :{0}'.format(my_bank.account_list[1].money))

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print('------Test Case 3------')
print(my_bank.atm_machine_list[1].deposit(my_bank.account_list[1], -1))


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print('------Test Case 4------')
print('before :{0}'.format(my_bank.account_list[1].money))
my_bank.atm_machine_list[1].withdraw(my_bank.account_list[1], 500)
print('after :{0}'.format(my_bank.account_list[1].money))

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print('------Test Case 5------')
print(my_bank.atm_machine_list[1].withdraw(my_bank.account_list[1], 2000))

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print('------Test Case 6------')
print('Harry before :{0}'.format(my_bank.account_list[0].money))
print('Herminone before :{0}'.format(my_bank.account_list[1].money))
my_bank.atm_machine_list[1].transfer(my_bank.account_list[0],my_bank.account_list[1], 10000)
print('Harry after :{0}'.format(my_bank.account_list[0].money))
print('Herminone after :{0}'.format(my_bank.account_list[1].money))


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500

print('------Test Case 7 ------')
for x in my_bank.account_list[1].transactions :
    print(x)

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
print('------Test Case 8 ------')
atm_machine = my_bank.atm_machine_list[0]
print(atm_machine.insert_card(my_bank.atm_card_list[0], '9999'))  


# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
print('------Test Case 9 ------')
my_bank.account_list[0].add_money(100000)
atm_machine = my_bank.atm_machine_list[0]
account = atm_machine.insert_card(my_bank.atm_card_list[0], '1234')  # PIN ถูกต้อง
if account[2] == 'Success' :
    harry = my_bank.account_list[0]
print(f"Harry account before test: {harry.money}")
print("Attempting to withdraw 45,000 baht...")
result = harry.withdraw(my_bank , '1001', 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {harry.money}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ

atm_machine = my_bank.atm_machine_list[1]
account = atm_machine.insert_card(my_bank.atm_card_list[0], '1234')

if account[2] == 'Success':
    acc = my_bank.account_list[0]  # 
print('------Test Case 10 ------')
print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.get_balance}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(acc, 250000)  
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")  
print(f"ATM machine balance after: {atm_machine.get_balance}")
print("-------------------------")
