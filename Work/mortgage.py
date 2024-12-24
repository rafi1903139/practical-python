# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
total_month = 1

while principal > 0:
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month:

        current_principal = principal * (1 + rate/12) 
        current_payment = (payment + extra_payment)
        if current_principal >= current_payment:
            principal = current_principal - current_payment
        else:
            principal = 0
            current_payment = current_principal

        total_paid = total_paid + current_payment 
    else:
        current_principal = principal * (1 + rate/12) 
        current_payment = payment
        if current_principal >= current_payment:
            principal = current_principal - current_payment
        else:
            principal = 0
            current_payment = current_principal

        total_paid = total_paid + current_payment 
    
    if principal > 0:
        total_month += 1
    
    print(f'{total_month}\t {round(total_paid, ndigits=2)}\t {round(principal, ndigits=2)}')
    



print(f'Total paid: {round(total_paid, ndigits=2)}')
print(f'Months {total_month}')