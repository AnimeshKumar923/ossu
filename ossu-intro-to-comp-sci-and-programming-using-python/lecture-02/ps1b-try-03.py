annual_salary = float(input("Enter your annual salary:"))


monthly_salary = float(annual_salary / 12)
print("monthly salary is:", monthly_salary)

portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))


total_cost = float(input("Enter the cost of your dream home:"))


semi_annual_raise = float(input("Enter your salary raise, as a decimal:"))


current_savings = 0  # amount saved so far
rate = 0.04  # annual rate of investment return

portion_down_payment = float(0.25 * total_cost)

print("down payment is:", portion_down_payment)


sem_annual_raise = float(annual_salary * semi_annual_raise)

print("semi-annual raise is", sem_annual_raise)


months = 1


while current_savings <= portion_down_payment:

    portion_saved = float(portion_saved * monthly_salary)
    # print("portion saved is:", portion_saved)

    monthly_return = float(current_savings * rate / 12)
    # print("monthly return is:", monthly_return)

    current_savings += float(monthly_return + portion_saved)

    # print("current saving is:", current_savings)

    months += 1

    if months % 6 == 0:
        annual_salary = float(annual_salary + sem_annual_raise)
        monthly_salary = float(annual_salary / 12)
        print("monthly salary after raise", monthly_salary)


print("annual salary after raises is", annual_salary)

print("number of months =", months)
