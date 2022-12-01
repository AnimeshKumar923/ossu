# final solution

annual_salary = input("Enter your annual salary:")
float_annual_salary = float(annual_salary)
# print(float_annual_salary)

monthly_salary = float(float_annual_salary / 12)
print("monthly salary is:", monthly_salary)

portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
float_portion_saved = float(portion_saved)
# print(float_portion_saved)

total_cost = input("Enter the cost of your dream home:")
float_total_cost = float(total_cost)

semi_annual_raise = input("Enter your salary raise, as a decimal:")
float_semi_annual_raise = float(semi_annual_raise)

current_savings = 0  # amount saved so far
rate = 0.04  # annual rate of investment return

portion_down_payment = float(0.25 * float_total_cost)

print("down payment is:", portion_down_payment)


# print("semi-annual raise is", sem_annual_raise)


months = 0


while current_savings <= portion_down_payment:

    sem_annual_raise = float(float_annual_salary * float_semi_annual_raise)

    portion_saved = float(float_portion_saved * monthly_salary)
    # print("portion saved is:", portion_saved)

    monthly_return = float(current_savings * rate / 12)
    # print("monthly return is:", monthly_return)

    current_savings += float(monthly_return + portion_saved)

    # print("current saving is:", current_savings)

    months += 1

    if months % 6 == 0:
        float_annual_salary = float(float_annual_salary + sem_annual_raise)
        monthly_salary = float(float_annual_salary / 12)
        print("monthly salary after raise", monthly_salary)


print("annual salary after raises is", float_annual_salary)

print("number of months =", months)
