"""
CS1026a 2023
Assignment 01 - Project 01 - Part B
Athul Charanthara
251395417
acharant
Sep 19, 2023
"""
print("Project One - Part B: Prime Choice")
count = 0

# gather the user input

start = int(input("Prime numbers starting with: "))
end = int(input("and ending with: "))

# verify validity of user input
if start < 2 or end < 2:
    print("Please enter a number greater than 1")
    quit()
elif start > end:
    print("\nIncorrect Input: %d is greater than %d" % (end, start))
    # switch the end and start numbers with the help of a temporary variable
    temp = end
    end = start
    start = temp
    print("The numbers have been automatically switched.")

# loop through the range of numbers
print("\nPrime numbers in the range from: %d and %d are: " % (start, end))
for i in range(start, end):
    # for each number, check if it is prime
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count <= 2:
        print("%d is prime" % i)
    count = 0

print("\nEND: Project One (01) - Part B")
print("Athul Charanthara acharant 251395417")