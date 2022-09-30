acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
word = 'WTG'
acronyms.append('YAA')
acronyms.append('WTG')

if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')

for acronym in acronyms:
    print(acronym)