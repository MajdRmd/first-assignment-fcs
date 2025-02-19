salary = int(input('Enter your salary \n'))
month = input('Enter the month of the salary\n')
savings = int(input('Enter amount of savings (in percentage)\n'))
rent = int(input('Enter amount of rent (in percentage) \n'))
electricity = int(input('Enter amount of electricity (in percentage) \n'))

amountofsavings = salary*savings/100
amountofrent = rent*savings/100
amountofelectricity = electricity*savings/100

total = amountofsavings+amountofrent+amountofelectricity
remainder = salary - total
yearlycost = (amountofsavings+amountofelectricity)*12
power2 = salary**2