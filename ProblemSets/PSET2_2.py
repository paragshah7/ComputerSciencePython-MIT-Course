balance = 3926
annualInterestRate = 0.2
new_balance = balance
constant_monthly_payment = 10
num_guesses = 0

while True:
    # print('Loop starts')

    for i in range(12):
        monthlyUnpaidBalance = new_balance - constant_monthly_payment
        remainingBalance = monthlyUnpaidBalance + (annualInterestRate/12) * monthlyUnpaidBalance
        new_balance = remainingBalance

    # print('New balance:', new_balance)
    if new_balance <= 0:
        break

    new_balance = balance
    constant_monthly_payment = constant_monthly_payment + 10
    num_guesses = num_guesses + 1
    # print(constant_monthly_payment)

print('Number of guesses:', num_guesses)
print('Lowest Payment:', constant_monthly_payment)
