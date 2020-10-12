import csv
import itertools
#import pandas as pd
#import tkinter as tk
#from tkinter import filedialog


with open('expenses.csv', newline='') as f:
  reader = csv.reader(f)
  data = list(reader)
remove_title = data.pop(0)

raw_string = []

for item in data:
  for info in item:
    raw_string.append(info.split(';'))


#print(raw_string)
record_date = []
wallet_name = []
expense_type = []
set_category = []
amount = []
currency = []
notes = []
first_name = []
last_name = []


for block in raw_string:
  for idx in range(len(block)):
    if idx == 0:
      record_date.append(block[idx])
    elif idx == 1:
      wallet_name.append(block[idx])
    elif idx == 2:
      expense_type.append(block[idx])
    elif idx == 3:
      set_category.append(block[idx])
    elif idx == 4:
      amount.append(block[idx])
    elif idx == 5:
      currency.append(block[idx])
    elif idx == 6:
      notes.append(block[idx])
    elif idx == 7:
      first_name.append(block[idx])
    elif idx == 8:
      last_name.append(block[idx])


#raw data list
record_date_v2 = []
set_category_v2 = []
amount_v2 = []
amount_v3 = []
notes_v2 = []
notes_v3 = []
payment_mode = []


#tidy up the data and input into raw data list

def strip_anymark(old_list,new_list,mark):
  for list_item in old_list:
    new_list.append(list_item.strip(mark))

strip_anymark(record_date, record_date_v2,'"')
strip_anymark(set_category, set_category_v2,'"')
strip_anymark(amount, amount_v2,'"')
strip_anymark(notes, notes_v2 ,'"')
strip_anymark(amount_v2, amount_v3 ,'-')


for i in notes_v2:
  draft_note = i.strip(' ').split(' ')
  element_1 = draft_note[0].strip('#').lower()
  element_2 = draft_note[-1].strip('#').lower()
  if element_2 == 'rm_bank' or element_2=='rm_cash':
    notes_v3.append(element_1)
    payment_mode.append(element_2)
  else:
    notes_v3.append(element_2)
    payment_mode.append(element_1)



#categorizing the expense here
fixed_expense_list = []
fixed_expense_amount = 0
variable_expense_list = []
variable_expense_amount = 0
discretionary_expense_list =[]
discretionary_expense_amount = 0

#check
#add

#subvintentory
parent_contribution = ['parent_contribution']
rental = []
mobile =  ['mobile']
insurance = ['insurance']

fixed_expense_list.append(parent_contribution)
fixed_expense_list.append(rental)
fixed_expense_list.append(mobile)
fixed_expense_list.append(insurance)


food = ['dinningout', 'foodbank', 'takeaway']
petrol = ['petrol']
vehicle_service = []
tot = []
vehicle_accesories = []
parking = []

variable_expense_list.append(food)
variable_expense_list.append(petrol)
variable_expense_list.append(vehicle_service)
variable_expense_list.append(tot)
variable_expense_list.append(vehicle_accesories)
variable_expense_list.append(parking)


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


discretionary_expense_list.append(education)
discretionary_expense_list.append(subscription)
discretionary_expense_list.append(shopping)
discretionary_expense_list.append(medical)
discretionary_expense_list.append(personal_care)
discretionary_expense_list.append(sport)
discretionary_expense_list.append(loan_repayment)
discretionary_expense_list.append(penalty)
discretionary_expense_list.append(car_insurance)
discretionary_expense_list.append(other_transports)
discretionary_expense_list.append(tax)
discretionary_expense_list.append(working_miscellaneous)
discretionary_expense_list.append(charity)


#open source code for flatenning list
def oneDArray(x):
    return list(itertools.chain(*x))



#Just use it to check notes_v3 vs categorizing, if there is miss out, manual key into the categories
def record_once_check_exist(note_list, cat_1 = fixed_expense_list , cat_2 = variable_expense_list, cat_3= discretionary_expense_list):
  ind_list = note_list.copy()
  ind_list_v1 = []
  for item_1 in ind_list:
    #use linear search to eliminate the duplicate item
    if item_1 not in ind_list_v1:
      ind_list_v1.append(item_1)

  uncategorized_item = []

  for item_2 in ind_list_v1:

    cat_a = oneDArray(cat_1)
    cat_b = oneDArray(cat_2)
    cat_c = oneDArray(cat_3)
    if (not item_2 in cat_a) and (not item_2 in cat_b) and (not item_2 in cat_c):
      uncategorized_item.append(item_2)
  if uncategorized_item:
    print("LOL XD There are uncategorized items, which are:")
    for non_found in uncategorized_item:
      print("- " + non_found)


#record_once_check_exist(notes_v3)


#calculate
fixed_expense_list_v1 = oneDArray(fixed_expense_list)
variable_expense_list_v1 = oneDArray(variable_expense_list)
discretionary_expense_list_v1 = oneDArray(discretionary_expense_list)


for i in range(len(notes_v3)):
  temp_number = amount_v3[i]
  if notes_v3[i] in fixed_expense_list_v1:
    fixed_expense_amount += float(temp_number)
  elif notes_v3[i] in variable_expense_list_v1:
    variable_expense_amount += float(temp_number)
  elif notes_v3[i] in discretionary_expense_list_v1:
    discretionary_expense_amount += float(temp_number)
  else:
    record_once_check_exist(notes_v3)


total_month_expense = float(fixed_expense_amount) + float(variable_expense_amount) + float(discretionary_expense_amount)


#print statement


income = input("Huhuhu...How much you earn this month @@ \n")
net_loss_or_surplus = float(income) - float(total_month_expense)
def statement_presentation():
  if float(income) > 0:
    print ("Fixed Expense: " + '%.2f' % fixed_expense_amount)
    print ("Variable Expense: " + '%.2f' % variable_expense_amount)
    print ("Discretionary Expense: " + '%.2f' % discretionary_expense_amount)
    print ("Total Expense: " + '%.2f' % total_month_expense )
    print ("Net surplus/loss: " + '%.2f' % net_loss_or_surplus )

statement_presentation()


statement = {'Category': ['Income','Fixed Expense','Variable Expense','Discretionary Expense', 'Total Expense', 'Net surplus/loss'],
        'Amount': ['%.2f' % float(income) ,'%.2f' % float(fixed_expense_amount),'%.2f' % float(variable_expense_amount),'%.2f' % float(discretionary_expense_amount), '%.2f' % float(total_month_expense), '%.2f' % float(net_loss_or_surplus)]
        }


'''
#refer to https://datatofish.com/export-dataframe-to-excel/


df = pd.DataFrame(statement, columns = ['Category', 'Amount'])



root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportExcel ():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel (export_file_path, index = False, header=True)

saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButtonExcel)

root.mainloop()
'''



#code income and calculate the surplus too, as well as other items in expense, and financial ratio
