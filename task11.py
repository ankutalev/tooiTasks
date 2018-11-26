
class BankAccount:
    __balance: int = 322
    __password: str = "qwertyqwe"
    name: str = "Dummy User With Stupid Password"
    account_id : int = 1

    def __init__(self, n: str, id: int, pswrd: str):
        self.name = n
        self.account_id = id

    def change_balance(self, pswrd: str, new_balance_value: int):
        if self.__check_password(pswrd):
            if self.__is_valid_balance(new_balance_value):
                self.__balance = new_balance_value
                print("Balance changed! New balance is ",new_balance_value)
            else:
                print("New balance value incorrect!")
        else:
            print("Incorrect password! Get out!")


    def balance_info(self, pswrd: str):
        if self.__check_password(pswrd):
            print("Balance ", self.__balance)
        else:
            print("Incorrect password! Get out!")


    def __check_password(self, pswrd: str ):
        return pswrd == self.__password

    def __is_valid_balance(self, new_balance_value: int):
        if new_balance_value > 322222:
            print("Incorrect balance value!")
            return False
        else:
            return True


my_acc: BankAccount = BankAccount("Kek", 12,"qwertyqwe")

my_acc.balance_info("q")
my_acc.balance_info("qwertyqwe")
my_acc.change_balance("w",1231)
my_acc.balance_info("qwertyqwe")
my_acc.change_balance("qwertyqwe",1)
my_acc.change_balance("qwertyqwe",1222222222222222222222222222)
my_acc.balance_info("qwertyqwe")



