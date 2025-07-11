monthly_income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - expenses
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)
print("your monthly savings are:", monthly_savings)
print("your projected savings after one year, with interest are:", projected_savings)