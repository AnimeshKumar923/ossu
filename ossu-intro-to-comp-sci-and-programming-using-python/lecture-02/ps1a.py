annual_salary = input("Enter your annual salary:")
float_annual_salary = float(annual_salary)
# print(float_annual_salary)

portion_saved = input("Enter the percent of your salary to save, as a decimal:")
float_portion_saved = float(portion_saved)
# print(float_portion_saved)

total_cost = input("Enter the cost of your dream home:")
float_total_cost = float(total_cost)

current_savings = 0  # amount saved so far
rate = 0.04  # annual rate of investment return

portion_down_payment = 0.25 * float_total_cost

print("down payment is:", portion_down_payment)


monthly_salary = float_annual_salary / 12


months = 0

while current_savings <= portion_down_payment:

    portion_saved = float_portion_saved * monthly_salary
    # print('portion saved is:', portion_saved)

    monthly_return = current_savings * rate / 12
    # print('monthly return is:', monthly_return)

    current_savings = current_savings + monthly_return + portion_saved

    # print('current saving is:', current_savings)

    months += 1

print("number of months =", months)
