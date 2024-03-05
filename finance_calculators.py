import math

user_choice = input("Enter 'investment' or 'bond': ").lower()

if user_choice == "investment":
    print("Investment - Calculate the amount of interest you'll earn on your investment ")

    deposit_amount = float(input("Enter the amount of money you would like to deposit: $"))
    interest_rate = float(input("Enter the interest rate (up to 8%): "))
    number_years = int(input("Enter the number of years you plan on investing: "))

    if not (0 <= interest_rate <= 8):
        print("Invalid interest rate. Please enter a rate between 0% and 8%.")
    else:
        interest_choice = input("Choose 'simple' or 'compound' interest: ").lower()

        if interest_choice == 'simple':
            simple_interest = deposit_amount * (1 + interest_rate * number_years / 100)
            print("Simple interest is: $", simple_interest)
        elif interest_choice == 'compound':
            compound_interest = deposit_amount * math.pow((1 + interest_rate / 100), number_years) - deposit_amount
            print("Compound interest is: $", compound_interest)
        else:
            print("Invalid choice. Please choose 'simple' or 'compound'.")

elif user_choice == "bond":
    print("Bond - Calculate the amount of bond you'll have to pay on a home loan")

    property_value = float(input("Enter the value of the property: $"))
    interest_rate = float(input("Enter the monthly interest rate (up to 7%): "))
    payback_months = int(input("Enter the number of months for repayment: "))

    monthly_repayment = (interest_rate * property_value) / (1 - math.pow(1 + interest_rate, -payback_months))
    print("Monthly repayment for the bond is: $", monthly_repayment)

else:
    print("Invalid choice. Please choose 'investment' or 'bond'.")



















   

