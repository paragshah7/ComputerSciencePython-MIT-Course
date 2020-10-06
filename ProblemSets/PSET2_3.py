balance = 999999
annualInterestRate = 0.18
new_balance = balance
num_guesses = 0

monthlyInterestRate = annualInterestRate/12
low = balance/12
high = (balance * (1 + monthlyInterestRate)**12) / 12.0
constant_monthly_payment = (low + high)/2.0


# for r in range(20):
# print('Loop starts')
while True:

    for i in range(12):
        monthlyUnpaidBalance = new_balance - constant_monthly_payment
        remainingBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        new_balance = remainingBalance

    # print('New balance:', new_balance)

    if new_balance < 0:
        high = constant_monthly_payment
        # print('New high:', high)
    else:
        low = constant_monthly_payment
        # print('New low:', low)
    # print(low, '', high)
    constant_monthly_payment = (low + high) / 2.0
    # print('************ New constant monthly payment:', constant_monthly_payment)
    num_guesses = num_guesses + 1

    if -0.01 < new_balance < 0.01:
        break
    new_balance = balance

# print('Number of guesses:', num_guesses)
print('Lowest Payment:', round(constant_monthly_payment, 2))
