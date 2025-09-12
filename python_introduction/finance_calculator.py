month_income=float(input("Enter your monthly income:"))
month_expenses=float(input("Enter your total monthly expenses:"))

save=month_expenses-month_income

Projected_Savings = save * 12 + (save * 12 * 0.05)

print(f"Your monthly savings are ${save}.")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.2f}.")
