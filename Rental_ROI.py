# Write a program that will return the Cash on Cash ROI for a given rental property.
# All calculation will be based on the original cost of the property.

# Attributes: income (dictionary), expenses (dictionary), cash_flow (dictionary),
# ROI (dictionary)

# Methods: totalMonthlyIncome, totalMonthlyExpenses, monthlyCashFlow, rentalROI

class ROI_Calc():
    def __init__(self, purchase_price):
        self.purchase_price = purchase_price
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.ROI = ROI

    def totalMonthlyIncome(self):
        self.income['purchase price'] = self.purchase_price
        rental_income = self.purchase_price * 0.01
        # print(f"Your Rental Income will be ${rental_income}.")
        self.income['rental income'] = rental_income
        laundry_income = rental_income * 0.01
        # print(f"Your Laundry Income will be ${laundry_income}.")
        self.income['laundry income'] = laundry_income
        storage_income = rental_income * 0.0075
        # print(f"Your Storage Income will be ${storage_income}.")
        self.income['storage income'] = storage_income
        misc_income = rental_income * 0.02
        # print(f"Your Miscellaneous Income will be ${misc_income}.")
        self.income['miscellaneous income'] = misc_income
        monthly_income = sum(self.income.values())
        self.income['monthly income'] = monthly_income
    
    def totalMonthlyExpenses(self):
        taxes = self.income['rental income'] * 0.075
        self.expenses['taxes'] = taxes
        insurance = self.income['rental income'] * 0.05
        self.expenses['insurance'] = insurance
        electric = self.income['rental income'] * 0.075
        self.expenses['electric'] = electric
        water = self.income['rental income'] * 0.0325
        self.expenses['water'] = water
        sewer = self.income['rental income'] * 0.0075
        self.expenses['sewer'] = sewer
        trash = self.income['rental income'] * 0.01
        self.expenses['trash'] = trash
        gas = self.income['rental income'] * 0.025
        self.expenses['gas'] = gas
        HOA = self.income['rental income'] * 0.005
        self.expenses['HOA'] = HOA
        landscape = self.income['rental income'] * 0.01
        self.expenses['landscape'] = landscape
        vacancy = self.income['rental income'] * 0.05
        self.expenses['vacancy'] = vacancy
        repairs = self.income['rental income'] * 0.05
        self.expenses['repairs'] = repairs
        capex = self.income['rental income'] * 0.05
        self.expenses['CapEx'] = capex
        property_management = self.income['rental income'] * 0.10
        self.expenses['property management'] = property_management
        # n = number of periodic payments, i = periodic interest rate
        # formula is {[(1 + i)^n] - 1}/[i(1 + i)^n]
        def discountFactor(i, n):
            return (((1.0 + i) ** n) - 1.0) / (i * (1.0 + i) ** n)
        self.expenses['mortgage'] = (self.income['purchase price'] * 0.8) / discountFactor(0.05, 360.0)
        self.expenses['monthly expenses'] = sum(self.expenses.values())

    def monthlyCashFlow(self):
        cash_flow_calc = self.income['monthly income'] - self.expenses['monthly expenses']
        self.cash_flow['cash flow'] = cash_flow_calc

    def rentalROI(self):
        self.ROI['down payment'] = self.income['purchase price'] * 0.2
        self.ROI['closing cost'] = self.income['purchase price'] * 0.015
        self.ROI['rehab budget'] = self.income['purchase price'] * 0.035
        self.ROI['misc other'] = self.income['purchase price'] * 0
        self.ROI['total investment'] = sum(self.ROI.values())
        self.ROI['annual cash flow'] = self.cash_flow['cash flow'] * 12
        cash_ROI = self.ROI['annual cash flow'] / self.ROI['total investment']
        print(f"Your cash on cash ROI will be {cash_ROI}%.") 
    
income = {}
expenses = {}
cash_flow = {}
ROI = {}
house_1 = ROI_Calc(200000.0)
def run():
    house_1.totalMonthlyIncome()
    house_1.totalMonthlyExpenses()
    house_1.monthlyCashFlow()
    house_1.rentalROI()

run()