#print("Target 2 mins statement. Goal short 10% of v1 code length")
import csv
import itertools
import os
import pandas as pd


#setting my path so that i can export.xlsx file to my desired folders
os.chdir("C:\\Users\\NkyGogo\\Desktop\\Development\\Re_Engineer\\2. Personal Project\\1.One code a day\\Sorcery Research\\Two Minutes Statements")

#direct to the folder that contain my csv file
with open('C:\\Users\\NkyGogo\\Desktop\\Development\\Re_Engineer\\2. Personal Project\\1.One code a day\\Sorcery Research\\Two Minutes Statements\\expenses.csv', newline='') as f:
  reader = csv.reader(f)
  data = list(reader)
  
remove_title = data.pop(0)

raw_string = []


def export_copy(statement):
    confirmation = input("Boss, do you want to export the statement to excel? Enter y/n: ")
    if confirmation == "y":
        statement.to_excel("First_export.xlsx")
 
def money_come_come():
  for item in data:
    for info in item:
      raw_string.append(info.split(';'))
  record_date =  []
  record_user = []
  record_type =  []
  record_categories = []
  expense_amount = []
  record_currency = []
  expense_type = []
  record_first_name =[ ]
  record_sub_name = []

  for daily_record in raw_string:
    for i in range(len(daily_record)):
      if i == 0:
        record_date.append(daily_record[i])
      elif i == 1:
        record_user.append(daily_record[i])
      elif i == 2:
        record_type.append(daily_record[i])
      elif i == 3:
        record_categories.append(daily_record[i])
      elif i == 4:
        expense_amount.append(daily_record[i].strip('"').strip('-'))
      elif i == 5:
        record_currency.append(daily_record[i])
      elif i == 6:
        expense_type.append(daily_record[i].lower().strip('"').split(' '))
      elif i == 7:
        record_first_name.append(daily_record[i])
      elif i == 8:
        record_sub_name.append(daily_record[i])


  expense_reference = []
  expense_type_v1 = list(itertools.chain(*expense_type))


  for item in expense_type_v1:
    if item[:3] !=  "#rm" and item:
      expense_reference.append(item.strip('#'))

  
  fixed_expense_amount = 0
  variable_expense_amount = 0
  discretionary_expense_amount= 0


  #fixed expense list
  parent_contribution = ['parent_contribution']
  rental = []
  mobile = ['mobile']
  insurance = ['insurance']

  parent_contribution_amount = 0
  rental_amount = 0
  mobile_amount = 0
  insurance_amount = 0


  #variable expense list
  food = ['takeaway', 'dinningout', 'foodbank']
  petrol =  ['petrol']
  vehicle_service = []
  tot = []
  vehicle_accesories = []
  parking = []

  food_amount = 0
  petrol_amount = 0
  vehicle_service_amount = 0
  tot_amount = 0
  vehicle_accesories_amount = 0
  parking_amount = 0


  #discretionary_expense list
  education = ['learning']
  subscription = ['subscription']
  shopping = []
  medical = []
  personal_care = ['personalcare']
  sport = ['fitness']
  loan_repayment = []
  penalty = []
  car_insurance = []
  other_transports = []
  tax = []
  working_miscellaneous = ['work']
  charity = []

  education_amount = 0
  subscription_amount = 0
  shopping_amount = 0
  medical_amount = 0
  personal_care_amount = 0
  sport_amount = 0
  loan_repayment_amount = 0
  penalty_amount = 0
  car_insurance_amount = 0
  other_transports_amount = 0
  tax_amount = 0
  working_miscellaneous_amount = 0
  charity_amount = 0

    #fixed expense start count here
  for i in range(len(expense_reference)):
    if expense_reference[i] in parent_contribution:
      parent_contribution_amount += float(expense_amount[i])
      fixed_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in rental:
      rental_amount += float(expense_amount[i])
      fixed_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in mobile:
      mobile_amount += float(expense_amount[i])
      fixed_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in insurance:
      insurance_amount += float(expense_amount[i])
      fixed_expense_amount += float(expense_amount[i])


    #variable expense start count here
    elif expense_reference[i] in food:
      food_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in petrol:
      petrol_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in vehicle_service:
      vehicle_service_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in tot:
      tot_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in vehicle_accesories:
      vehicle_accesories_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in parking:
      parking_amount += float(expense_amount[i])
      variable_expense_amount += float(expense_amount[i])


    #discretionary expense list
    elif expense_reference[i] in education:
      education_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in subscription:
      subscription_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in shopping:
      shopping_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in medical:
      medical_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in personal_care:
      personal_care_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in sport:
      sport_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in loan_repayment:
      loan_repayment_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in penalty:
      penalty_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in car_insurance:
      car_insurance_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in other_transports:
      other_transports_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in tax:
      tax_amount +=float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in working_miscellaneous:
      working_miscellaneous_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    elif expense_reference[i] in charity:
      charity_amount += float(expense_amount[i])
      discretionary_expense_amount += float(expense_amount[i])
    else:
      print("Emmm...can\'t find {a} in recorded categories, just adding it now LOL".format(a= expense_amount[i]) + "\n")





  print('Parent Contribution: ' + '%.2f' % parent_contribution_amount)
  print('Rental: ' + '%.2f' % rental_amount)
  print('Mobile: ' + '%.2f' % mobile_amount)
  print('Insurance: ' + '%.2f' % insurance_amount)
  print('Total Fixed Expense: ' + '%.2f' % fixed_expense_amount + '\n' )

  print('Food: ' + '%.2f' %food_amount)
  print('Petrol: ' + '%.2f' %petrol_amount)
  print('Vehicle Service: ' + '%.2f' %vehicle_service_amount)
  print('Tot: ' + '%.2f' %tot_amount)
  print('Vehicle Accessories: ' + '%.2f' %vehicle_accesories_amount)
  print('Parking: ' + '%.2f' %parking_amount)
  print('Total Variable Expense: ' + '%.2f' %variable_expense_amount + '\n')

  print('Education: ' + '%.2f' %education_amount)
  print('Subscription: ' + '%.2f' %subscription_amount)
  print('Shopping: ' + '%.2f' %shopping_amount)
  print('Medical: ' + '%.2f' %medical_amount)
  print('Personal Care: ' + '%.2f' %personal_care_amount)
  print('Sport: ' + '%.2f' %sport_amount)
  print('Loan Repayment: ' + '%.2f' %loan_repayment_amount)
  print('Penalty: ' + '%.2f' %penalty_amount)
  print('Car Insurance: ' + '%.2f' %car_insurance_amount)
  print('Other Transports: ' + '%.2f' %other_transports_amount)
  print('Tax: ' + '%.2f' %tax_amount)
  print('Work Miscellaneous: ' +'%.2f' % working_miscellaneous_amount)
  print('Charity: ' + '%.2f' %charity_amount)
  print('Total Discretionary Expense: ' + '%.2f' %discretionary_expense_amount + '\n')


  total_expense = float(fixed_expense_amount) + float(variable_expense_amount) + float(discretionary_expense_amount)

  print('Total Monthly Expense: ' + str(total_expense) + "\n")
  
  
  export_frame = pd.DataFrame({"Items":['Parent Contribution','Rental',
                                        'Mobile','Insurance',
                                        'Total Fixed Expense',
                                        'Food','Petrol','Vehicle Service',
                                        'Tot','Vehicle Accessories','Parking',
                                        'Total Variable Expense','Education',
                                        'Subscription','Shopping','Medical',
                                        'Personal Care','Sport',
                                        'Loan Repayment','Penalty',
                                        'Car Insurance','Other Transports',
                                        'Tax','Work Miscellaneous','Charity',
                                        'Total Discretionary Expense', 
                                        'Total Monthly Expense'], 
                               "Amount":[parent_contribution_amount, 
                                         rental_amount, mobile_amount, 
                                         insurance_amount, fixed_expense_amount,
                                         food_amount, petrol_amount,
                                         vehicle_service_amount,tot_amount,
                                         vehicle_accesories_amount, 
                                         parking_amount, 
                                         variable_expense_amount, 
                                         education_amount, subscription_amount,
                                         shopping_amount, medical_amount, 
                                         personal_care_amount, sport_amount,
                                         loan_repayment_amount, penalty_amount,
                                         car_insurance_amount, 
                                         other_transports_amount, tax_amount, 
                                         working_miscellaneous_amount, 
                                         charity_amount, 
                                         discretionary_expense_amount, 
                                         total_expense]})
  export_copy(export_frame)
  


money_come_come()


    
    




