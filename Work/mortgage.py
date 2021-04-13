# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0

while principal > 0:
    if current_month < 12:
        principal = principal * (1+rate/12) - ( payment + 1000 )
        total_paid = total_paid + payment + 1000
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    current_month += 1

print('Total paid', total_paid, 'Current month', current_month)