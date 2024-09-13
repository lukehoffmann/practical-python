# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0

monthly_interest = (1 + rate / 12)

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.00


month = 0
while principal > 0:
    month += 1
    principal *= monthly_interest

    payment = monthly_payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment += extra_payment
    if payment > principal:
        payment = principal

    total_paid += payment
    principal -= payment 
    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
