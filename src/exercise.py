def main():
    #write your code below this line
    acct = Account("Arto's account", 100)
    acct.deposit(20)
    print(acct.balance)

# Don't edit below this line - this setup is required for testingss 
if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account
