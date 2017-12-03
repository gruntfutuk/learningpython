#!/usr/bin/env python3
# simple programme to calculate largest demoninations of change to give

# demoninations lists, values and names one-to-one mapping!
# sterling
currency_values = [200, 100, 50, 20, 10, 5, 2, 1]
currency_names = ['two pound', 'pound', 'fifty pence', 
                    'twenty pence', 'ten pence', 
                    'five pence', 'two pence', 'one pence']

def breakdown(amountstr):
  if not amountstr:
    return ""
  change = ""
  amount = int(amountstr)
  for name, currency in zip(currency_names, currency_values):
      if amount <= 0: # end if no change left
          break
      if amount >= currency: # we have some of this demonination to pay
          quantity = amount // currency
          change +=  f'\n{quantity}x \t{name} '
          amount = amount % currency
  return change

request = '\nHow much, in whole pence, needs to be returned in change (return to exit)? ' 
while True:
  change = breakdown(input(request))
  if change:
    print(f'Change breakdown is: {change}')
  else:
    break