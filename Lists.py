# build container of containers - combine menus in a list of lists of menus.
menus =  [['Egg Sandwich', 'Bagel', 'Coffee'],
          ['BLT', 'PB&J', 'Turkey Sandwhich'],
          ['Soup', 'Salad', 'Spaghetti', 'Taco'] ]

menus2 ={ 'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch':     ['BLT', 'PB&J', 'Turkey Sandwhich'],
          'Dinner':    ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

# print items in a index list print bagel
print(menus[0][1])

print('Breakfast Menu:\t', menus2['Breakfast'])
print('Lunch Menu:\t', menus2['Lunch'])
print('Dinner Menu:\t', menus2['Dinner'])

# Using Dictionary Key and Value in a for loop to print
for name, menu in menus2.items():
    print(name, ':', menu)
