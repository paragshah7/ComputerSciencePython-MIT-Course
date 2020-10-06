balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
remainingBalance = 0

for i in range(12):
    minimumMonthlyPayment = balance * monthlyPaymentRate
    # print('Minimum monthly payment =', minimumMonthlyPayment)  # 100

    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    # print('Monthly unpaid balance =', monthlyUnpaidBalance)    # 4900

    remainingBalance = monthlyUnpaidBalance + (annualInterestRate/12) * monthlyUnpaidBalance   # 4900 + 75.5
    # print('Remaining balance:', round(remainingBalance, 2))    # 4973.5

    balance = remainingBalance
print('Remaining balance:', round(remainingBalance, 2))
