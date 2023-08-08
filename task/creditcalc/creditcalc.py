# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

# principal = int(input("Enter the loan principal:\n> "))
# calculation_choice = input("""What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:\n> """)
# if calculation_choice == "m":
#     monthly_payment = int(input("Enter the monthly payment:\n> "))
#     number_of_months = math.ceil(principal / monthly_payment)
#     if number_of_months == 1:
#         print("\nIt will take 1 month to repay the loan")
#     else:
#         print(f"\nIt will take {number_of_months} months to repay the loan")
# elif calculation_choice == "p":
#     number_of_months = int(input("Enter the number of months:\n> "))
#     monthly_payment = math.ceil(principal / number_of_months)
#     if principal % number_of_months == 0:
#         print(f"\nYour monthly payment = {monthly_payment}")
#     else:
#         last_payment = principal - (number_of_months - 1) * monthly_payment
#         print(f"\nYour monthly payment = {monthly_payment}"
#               f" and the last payment = {last_payment}.")

import math
import argparse
import sys


def validate_arguments(arguments):
    """
    Validate that the arguments meet the requirements for calculation.
    :param arguments: The parsed command-line arguments.
    :return: True if arguments are valid, False otherwise.
    """
    # Ensure interest is not None
    if arguments.interest is None:
        return False

    if arguments.type == "diff":
        if not all([arguments.principal, arguments.periods]):
            return False
        if arguments.payment is not None:
            return False
        elif arguments.type == "annuity":
            if not any([arguments.payment, arguments.principal, arguments.periods]):
                return False

    return True


def calculate_differentiated_payments(principal, number_of_payments, interest):
    total_payment = 0
    for m in range(1, number_of_payments + 1):
        Dm = (
                principal / number_of_payments
                + interest * (principal - (principal * (m - 1)) / number_of_payments)
        )
        total_payment += math.ceil(Dm)
        print(f"Month {m}: payment is {math.ceil(Dm)}")
    print(f"\nOverpayment = {total_payment - principal}")


def calculate_annuity_payments(payment, principal, number_of_payments, nominal_interest):
    if payment is None:
        payment = math.ceil(
                principal * (nominal_interest * (1 + nominal_interest) ** number_of_payments)
                / ((1 + nominal_interest) ** number_of_payments - 1)
        )
        overpayment = math.ceil(number_of_payments * payment - principal)
        print(f"Your monthly payment = {payment}!")  # annuity
        print(f"Overpayment = {overpayment}")
    elif principal is None:
        principal = math.floor(
                payment / ((nominal_interest * (1 + nominal_interest) ** number_of_payments)
                           / ((1 + nominal_interest) ** number_of_payments - 1))
        )
        overpayment = math.ceil(number_of_payments * payment - principal)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpayment}")
    else:
        number_of_payments = (
            math.ceil(math.log(payment / (payment - nominal_interest * principal),
                               1 + nominal_interest))
        )
        years = number_of_payments // 12
        months = number_of_payments % 12
        if years == 0 and months == 1:
            print(f"It will take 1 month to repay this loan!")
        elif years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif years == 1 and months == 0:
            print(f"It will take 1 year to repay this loan!")
        elif years == 1 and months == 1:
            print(f"It will take 1 year and 1 month to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        overpayment = math.ceil(number_of_payments * payment - principal)
        print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser(
    description="Calculate differentiated or annuity loan payments "
                "based on provided loan parameters."
)

parser.add_argument(
    "-t",
    "--type",
    choices=["annuity", "diff"],
    help="Payment type: 'annuity' for fixed payments, 'diff' for decreasing payments."
)

parser.add_argument(
    "-p",
    "--payment",
    type=float,
    help="Monthly payment amount. Not valid with type 'diff'."
)

parser.add_argument(
    "-r",
    "--principal",
    type=int,
    help="Loan principal amount."
)

parser.add_argument(
    "-n",
    "--periods",
    type=int,
    help="Number of payments or periods."
)

parser.add_argument(
    "-i",
    "--interest",
    type=float,
    help="Annual interest rate without the % sign. Required for all calculations."
)

args = parser.parse_args()

if not validate_arguments(args):
    print("Incorrect parameters")
    sys.exit()

nominal_interest = args.interest / (12 * 100)

if args.type == "diff":
    calculate_differentiated_payments(args.principal, args.periods, nominal_interest)
elif args.type == "annuity":
    calculate_annuity_payments(args.payment, args.principal, args.periods, nominal_interest)

# calculation_choice = input("""What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:\n> """)
#
# if calculation_choice == "n":
#     principal = int(input("Enter the loan principal:\n> "))
#     annuity = int(input("Enter the monthly payment:\n> "))  # monthly annuity payment
#     annual_interest = float(input("Enter the loan interest:\n> "))
#     nominal_interest = annual_interest / (12 * 100)  # nominal (monthly) interest rate
#     number_of_months = math.ceil(
#         math.log(annuity / (annuity - nominal_interest * principal), 1 + nominal_interest)
#     )
#     years = number_of_months // 12
#     months = number_of_months % 12
#     if years == 0 and months == 1:
#         print(f"It will take 1 month to repay this loan!")
#     elif years == 0:
#         print(f"It will take {months} months to repay this loan!")
#     elif years == 1 and months == 0:
#         print(f"It will take 1 year to repay this loan!")
#     elif years == 1 and months == 1:
#         print(f"It will take 1 year and 1 month to repay this loan!")
#     else:
#         print(f"It will take {years} years and {months} months to repay this loan!")
#
# if calculation_choice == "a":
#     principal = int(input("Enter the loan principal:\n> "))
#     number_of_months = int(input("Enter the number of periods:\n> "))  # number of periods
#     annual_interest = float(input("Enter the loan interest:\n> "))
#     nominal_interest = annual_interest / (12 * 100)  # nominal (monthly) interest rate
#     annuity = math.ceil(
#             principal
#             * nominal_interest
#             * math.pow((1 + nominal_interest), number_of_months)
#             / (math.pow((1 + nominal_interest), number_of_months) - 1)
#     )
#     print(f"Your monthly payment = {annuity}!")
#
# if calculation_choice == "p":
#     annuity = float(input("Enter the annuity payment:\n> "))  # monthly annuity payment
#     number_of_months = int(input("Enter the number of periods:\n> "))  # number of periods
#     annual_interest = float(input("Enter the loan interest:\n> "))
#     nominal_interest = annual_interest / (12 * 100)  # nominal (monthly) interest rate
#     principal = round(
#             annuity
#             / ((nominal_interest * math.pow((1 + nominal_interest), number_of_months))
#             / (math.pow((1 + nominal_interest), number_of_months) - 1))
#     )
#     print(f"Your loan principal = {principal}!")
