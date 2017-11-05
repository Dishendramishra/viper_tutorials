people_wallet: public({
    account_name: bytes32,
    account_balance: num,
    password: bytes <= 18,
    }[bytes32]) 

meetups: public({
    person1: bytes <= 32,
    person2: bytes<= 32,
    location: bytes <= 23,
    date: bytes <= 8,
    time_interval: bytes <= 11,
    sercurity_amount: num,
    sercurity_wallet: num
    }[num])

pointer: num

def __init__():
    pass

def createMettup(_person1: bytes<=32, _person2: bytes<= 32,_location: bytes<=23,_date: bytes<=8,_time_interval: bytes<=11,_sercurity_amount: num):
    self.meetups[self.pointer].person1 = _person1
    self.meetups[self.pointer].person2 = _person2
    self.meetups[self.pointer].location = _location
    self.meetups[self.pointer].date = _date
    self.meetups[self.pointer].time_interval = _time_interval
    self.meetups[self.pointer].sercurity_amount = _sercurity_amount
    self.pointer += 1

@constant
def walletExists(_name: bytes32) -> bool:
    if self.people_wallet[_name].account_balance == 0:
        return false
    return True

# get the details of the people_wallet
@constant
def getWalletDetails(_name: bytes32) -> (bytes32, num):
    return (self.people_wallet[_name].account_name, self.people_wallet[_name].account_balance)

def createWallet(_name: bytes32, _account_balance: num, _password:bytes<=18):
    if not self.walletExists(_name):
        self.people_wallet[_name].account_name = _name
        self.people_wallet[_name].account_balance = _account_balance
        self.people_wallet[_name].password = _password
