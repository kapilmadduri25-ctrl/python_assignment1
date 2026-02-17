# ps1c.py
annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
r = 0.04
semi_annual_raise = 0.07

months = 36
epsilon = 100

low = 0
high = 10000
steps = 0
best_rate = None
current_savings = 0
test_salary = annual_salary
monthly_salary = test_salary / 12

for month in range(1, months + 1):
    current_savings += current_savings * r / 12
    current_savings += monthly_salary
    if month % 6 == 0:
        test_salary += test_salary * semi_annual_raise
        monthly_salary = test_salary / 12

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while True:
        steps += 1
        mid = (low + high) // 2
        portion_saved = mid / 10000

        current_savings = 0
        test_salary = annual_salary
        monthly_salary = test_salary / 12

        for month in range(1, months + 1):
            current_savings += current_savings * r / 12
            current_savings += monthly_salary * portion_saved
            if month % 6 == 0:
                test_salary += test_salary * semi_annual_raise
                monthly_salary = test_salary / 12

        if abs(current_savings - down_payment) <= epsilon:
            best_rate = portion_saved
            break
        elif current_savings < down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)
