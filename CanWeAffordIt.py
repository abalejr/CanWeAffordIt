#CAN... WE... AFFORD IT!?! Text Version

expenses = 4681.38
aj_wage = 400 #Weekly
chelcie_wage = 1866.51 #Biweekly
aj_funds = float(input("A.J.'s Current Funds: "))
chelcie_funds = float(input("Chelcie's Current Funds: "))
cost = float(input("Planned Expense: "))
funds = aj_funds + chelcie_funds - cost

print("Current Funds After Purchase: $%.2f" % funds)

aj_upcoming_checks = int(input("AJ checks by upcoming 1st: "))
chelcie_upcoming_checks = int(input("Chelcie checks by upcoming 1st: "))
upcoming_cost = float(input("Planned Expense for Upcoming Month: "))
aj_new_funds_upcoming = aj_wage * aj_upcoming_checks
chelcie_new_funds_upcoming = chelcie_wage * chelcie_upcoming_checks
upcoming_funds = funds + aj_new_funds_upcoming + chelcie_new_funds_upcoming - expenses - upcoming_cost

print("Funds After Expenses for Upcoming Month: $%.2f" % upcoming_funds)

aj_next_checks = int(input("AJ checks by next 1st: "))
chelcie_next_checks = int(input("Chelcie checks by next 1st: "))
next_cost = float(input("Planned Expense for Next Month: "))
aj_new_funds_next = aj_wage * aj_next_checks
chelcie_new_funds_next = chelcie_wage * chelcie_next_checks
next_funds = upcoming_funds + aj_new_funds_next + chelcie_new_funds_next - expenses - next_cost

print("Funds After Expenses for Next Month: $%.2f" % next_funds)

aj_following_checks = int(input("AJ checks by following 1st: "))
chelcie_following_checks = int(input("Chelcie checks by following 1st: "))
following_cost = float(input("Planned Expense for Following Month: "))
aj_new_funds_following = aj_wage * aj_following_checks
chelcie_new_funds_following = chelcie_wage * chelcie_following_checks
following_funds = next_funds + aj_new_funds_following + chelcie_new_funds_following - expenses - following_cost

print("Funds After Expenses for Following Month: $%.2f" % following_funds)


