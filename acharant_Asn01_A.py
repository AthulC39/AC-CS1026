"""
CS1026a 2023
Assignment 01 - Project 01 - Part A
Athul Charanthara
251395417
acharant
Sep 19, 2023
"""
print("Project One (01) - Part A : Fibonacci Sequence")

# first get input from the user

end = int(input("Sequence ends at: "))

# hardcode the first 3 sequences(will always be the same), and set the initial values of term 1 and 2
term2 = 1
term1 = 2
print("0: 0 0")
print("1: 1 1")
print("2: 1 1")

# loop for the given sequence (from 3 to the designated end)
for i in range(3, end):
    # current is the current value in the fibonacci sequence
    current = term1 + term2
    print(str(i) + ":", current,'{:,}'.format(current))
    # reset the new term values
    term2 = term1
    term1 = current

print("\nEND: Project One (01) - Part A")
print("Athul Charanthara acharant 251395417")