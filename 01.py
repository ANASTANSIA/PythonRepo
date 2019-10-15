mealBill=eval(input('Enter the price of your meal:'))
tip=eval(input('Enter your tip percent:'))
tipAmount=tip/100*mealBill
total=tipAmount+mealBill
print('Tip Amount:',tipAmount)
print('Total:',total)
