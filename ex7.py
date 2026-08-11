account_balance=50000
withdrawal_amount=input("Enter the amount you want to withdraw: ")

if float(withdrawal_amount) <= account_balance:
    account_balance = account_balance - float(withdrawal_amount)
    print("Withdrawal successful!")
    print("Remaining Balance:", account_balance)
else:
    print("insufficient balance")