# Write a program that will return the Cash on Cash ROI for a given rental property.
# All calculation will be based on the original cost of the property.

# Attributes: income (dictionary), expenses (dictionary), cash_flow (dictionary),
# ROI (dictionary)

# Methods: totalMonthlyIncome, totalMonthlyExpenses, monthlyCashFlow, rentalROI

class ROI_Calc():
    def __init__(self, income, expenses, cash_flow, ROI):
        # self.purchase_price = purchase_price
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.ROI = ROI

    def totalMonthlyIncome(self, purchase_price):
        income['purchase price'] = purchase_price

        rental_income = int(input("How much would you like to charge for rent? "))
        income['rental income'] = rental_income

        laundry_income = int(input("How much would you like to charge for laundry? If you do not wish to, type a 0. "))
        income['laundry income'] = laundry_income

        storage_income = int(input("How much would you like to charge for storage? If you do not wish to, type a 0. "))
        income['storage income'] = storage_income

        misc_income = int(input("How much would you like to charge for miscellaneous fees? If you do not wish to, type a 0. "))
        income['miscellaneous income'] = misc_income

        monthly_income = sum(income.values()) - income['purchase price']
        income['monthly income'] = monthly_income

        print(f"Your total monthly income will be ${monthly_income}.")
        house_1.totalMonthlyExpenses()
    
    def totalMonthlyExpenses(self):
        taxes = int(input("How much will the taxes be for your rental property? "))
        expenses['taxes'] = taxes

        insurance = int(input("How much will the insurance cost for your rental property? "))
        expenses['insurance'] = insurance

        utilities = input("Do you intend for your renters to pay for utilities or do it yourself? Please select: renters/owner ")
        if utilities.lower() == 'owner':
            electric = int(input("How much do you expect your electric bill will be? "))
            expenses['electric'] = electric
            water = int(input("How much do you expect your water bill will be? "))
            expenses['water'] = water
            sewer = int(input("How much do you expect your sewer bill will be? "))
            expenses['sewer'] = sewer
            trash = int(input("How much do you expect your trash bill to be? "))
            expenses['trash'] = trash
            gas = int(input("How much do you expect your gas bill to be? "))
            expenses['gas'] = gas
        else:
            expenses['utilities']= 0

        hoa_inquiry = input("Is this property part of an HOA? Please select: yes/no ")
        if hoa_inquiry.lower() == 'yes':
            hoa = int(input("How much are the HOA fees per month? "))
            expenses['HOA'] = hoa
        else:
            pass

        landscape_inquiry = input("Do you intend to charge for landscape upkeep? Please select: yes/no ")
        if landscape_inquiry == 'yes':
            landscape = int(input("How much do you intend to charge for landscape services? "))
            expenses['landscape'] = landscape
        else:
            pass

        vacancy = int(input("How much do you intend to set aside to cover vacancies? "))
        expenses['vacancy'] = vacancy

        repairs = int(input("How much do you intend to set aside for repairs each month? "))
        expenses['repairs'] = repairs

        capex = int(input("How much do you intend to set aside for capital expenses each month? "))
        expenses['capex'] = capex

        downpayment = int(input("How much do you intend to spend on your house downpayment? "))
        ROI['downpayment'] = downpayment

        apr = int(input("What is the interest rate you have been approved for? "))
        expenses['APR'] = apr / 100

        loan_length = int(input("How many years will your loan be? "))
        expenses['loan length'] = loan_length

        closing_cost = int(input("How much do you expect your closing costs to be? "))
        ROI['closing cost'] = closing_cost

        rehab = int(input("How much do you expect your rehab budget to be? "))
        ROI['rehab budget'] = rehab

        misc = int(input("How much do you anticipate any miscellaneous costs being during closing? "))
        ROI['miscellaneous'] = misc

        property_management = int(input("How much do you anticipate property management costing? "))
        expenses['property management'] = property_management

        # P = principal, r = interest rate, t = time in years, n = payments per year
        # Payment = P * (r / n) * (1 + r / n) ** (n * t) / ((1 + r / n) ** (n * t)) - 1
        def mortgageCalc(p, r, t, n):
            return (p * (r / n) * (1 + r / n) ** (n * t)) / (((1 + r / n) ** (n * t)) - 1)
        expenses['mortgage'] = round(mortgageCalc((income['purchase price'] - downpayment + ROI['closing cost'] + ROI['rehab budget'] + ROI['miscellaneous']), expenses['APR'], loan_length, 12), 2)
        print(f"Your mortage will be ${expenses['mortgage']}.")
        
        expenses['monthly expenses'] = round(sum(expenses.values()) - expenses['APR'], 2)
        print(f"Your total monthly expenses will be ${expenses['monthly expenses']}.")
        house_1.monthlyCashFlow()


    def monthlyCashFlow(self):
        cash_flow_calc = income['monthly income'] - expenses['monthly expenses']
        cash_flow['cash flow'] = round(cash_flow_calc, 2)
        print(f"Your monthly cash flow will be ${cash_flow['cash flow']}.")
        house_1.rentalROI()

    def rentalROI(self):        
        total_investment = round(sum(ROI.values()), 2)
        ROI['total investment'] = total_investment
        cash_ROI = round((((cash_flow['cash flow'] * 12)) / total_investment) * 100, 2)
        print(f"Your cash on cash ROI will be {cash_ROI}%.") 
    
income = {}
expenses = {}
cash_flow = {}
ROI = {}
house_1 = ROI_Calc({}, {}, {}, {})
def run():
    while True:
        user_decision = input("Would you like to learn what you cash on cash rental ROI could be? Enter yes/no/quit ")
        if user_decision == 'yes':
            purchase_price = int(input("How much will you be looking to spend on your rental property? "))
            return house_1.totalMonthlyIncome(purchase_price)
        elif user_decision == 'no':
            continue
        elif user_decision == 'quit':
            break
        else:
            print("Please select one of the given prompts.")
            continue

run()