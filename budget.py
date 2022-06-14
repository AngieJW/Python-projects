import datetime
import math

def main() :
    try :
        next_month = get_nextmonth()

        print("Welcome to the budget planner")
        print(f"Let's start planning for {next_month.strftime('%B')}")
        print("How do you want to budget?")
        print("1-Budget your income")
        print("2-Track your expenses")
        choice = input("Select 1 or 2 :")

        if choice == "1":
            revenues = compute_revenues()
            print()
            print(f"Your total revenue is {revenues} dollars per month")
            expenses, ten_percent = compute_expenses(revenues)

            print(f"Your aim would be to spend {math.ceil(expenses)} dollars maximum")
            print(f'to pay for all your expenses, save {math.ceil(ten_percent)} dollars,')
            print(f'invest {math.ceil(ten_percent)} dollars and tithe {math.ceil(ten_percent)} dollars')
    
        elif choice == "2":
            expenses = track_expenses()
            revenues = compute_revenues()
            money_left = revenues - expenses
            if money_left == 0:
                print(f"At the end of {next_month.strftime('%B')}, you will not have any money left.")
                print("Be careful not to spend any more money.")
            elif money_left > 0:
                print(f"At the end of {next_month.strftime('%B')}, you will have {money_left} dollars left.")

            else :
                print("Oh no ! Looks like you are going into your overdraft. ")
                print(f"At the end of {next_month.strftime('%B')}, you will be in the negative with {money_left}dollars.")
                print("Review the list of your expenses and find ways to reduce them!")

        else : 
            print("Sorry, you must enter either 1 or 2. Run the program one more time.")

    except ValueError as val_err:
        print("The value wasn't a number. Please")
        print("run the program again and enter a number.")

def get_nextmonth():
    """ 
    computes today's date in order to determine what the next month will be
    returns the next month
    """
    current_date = datetime.datetime.now()
    next_month = current_date  + datetime.timedelta(days=+31)
    return next_month

def compute_revenues():
    """ 
    computes the monthly salary and any additional revenue like a bonus
    returns the total revenues
    """
    salary = int(input("What is your monthly salary in dollars after taxes?"))
    additional_revenue = input("Any additional revenue?")
    if additional_revenue.capitalize() == "Yes":
        bonus = int(input("How much? "))
    else:
        bonus = 0 
    total_revenue = salary + bonus
    return total_revenue

def compute_expenses(total_revenue):
    print("The ideal would be to use 70% of your revenues as expenses,")
    print("10% savings, 10% investing and 10% tithing")
    print()
    ten_percent = float(total_revenue* 0.1)
    expenses = float(total_revenue*0.7) 
    return expenses, ten_percent

def track_expenses():
    expenses = []
    amounts = []
    expense = ""
    total_expenses = 0
    expense = input("What monthly expense do you have? Type 'none' when all your expenses are listed : ")
    while expense != "none":
        expenses.append(expense)
        amount = float(input(f"What is the amount spent in dollars of '{expense}'?"))
        amounts.append(amount)
        total_expenses += amount
        expense = input("What monthly expense do you have? Type 'none' when all your expenses are listed : ")
    
    print()
    print("Your montly expenses are:")
    for i in range(len(expenses)):
        expense = expenses[i]
        print(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
    print(f'The total of your expenses is {total_expenses} dollars')
    return total_expenses

if __name__ == "__main__":
    main()
