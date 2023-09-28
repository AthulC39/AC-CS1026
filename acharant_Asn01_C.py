"""
CS1026a 2023
Assignment 01 - Project 01 - Part C
Athul Charanthara
251395417
acharant
Sep 19, 2023
"""
# Lists all the unit names and the respective values to be assigned later
units = ['yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo']
unit_value = ['1000000000000000000000000','1000000000000000000000','1000000000000000000','1000000000000000','1000000000000','1000000000','1000000','1000']

print("Project One (01) - Part C: The Moore the Merrier")
# set the initial value of the flops variable which will list the flops for each year
flops = 1

# gather the user inputs
transistors = int(input("Starting Number of Transistors: "))
year = int(input("Starting Year: "))
total = int(input("Total Number of Years: "))


# print the header and the first case
print("\nYEAR : TRANSISTORS : FLOPS:")
print(year,transistors,"%.2f" % (transistors*50),"FLOPS",transistors*50)

# loop through all the years
for i in range(year,total + year,2):
    # calculate the year and the corresponding number of transistors and flops for that year
    year += 2
    transistors *= 2
    flops = transistors*50
    for j in range(0,len(units)):
        # For each unit type, find the largest unit type possible and set the prefix to the flop_unit variable
        if (flops/float(unit_value[j])) > 0:
            unit_flop = flops/float(unit_value[j])
            flop_unit = units[j]
            if unit_flop > 1:
                # once the correct unit type for the flops is found, break out of the loop
                break
    # print all the data required (years, transistors, flop units and flops) and format them
    print(year,'{:,}'.format(transistors),"%.2f" % unit_flop,flop_unit + "FLOPS",'{:,}'.format(flops))

print("\nEND: Project One (01) - Part C")
print("Athul Charanthara acharant 251395417")








