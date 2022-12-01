# code copied from stackoverflow, feeling pathetic and thinking of giving up, gave 4 hours but didn't make it :(, I just can't think about the logic. What should I do to improve it? Am I dumb or something?

annual_salary = float(input("What is your starting annual salary?"))
monthly_salary = annual_salary / 12
print("monthly salary is:", monthly_salary)
portion_saved = float(
    input("What percentage of your salary will you save each month(in decimals)?")
)
Total_cost = float(input("How much is your dream home?"))
semi_annual_raise = float(input("What is your raise every 6 months(in decimals)?"))
portion_down_payment = 0.25 * Total_cost
r = 0.04
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    current_savings += portion_saved * monthly_salary + current_savings * r / 12
    months += 1
    if months % 6 == 0:
        monthly_salary += semi_annual_raise * monthly_salary
        print(monthly_salary)
print("Number of months:", months)
