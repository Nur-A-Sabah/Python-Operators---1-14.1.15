amount = int(input("Please  Enter Amount for Withdraw: "))

note100 = amount//100
note50 = (amount%100)//50
note10 = ((amount%100) % 50)//10

print(f"notes of 100 Taka {note100}")
print(f"notes of 50 Taka {note50}")
print(f"notes of 10 Taka {note10}")