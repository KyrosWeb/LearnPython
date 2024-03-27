# Python Loops

# Without loops, we would have to write the same code over and over again
# For example, if we want to print numbers from 1 to 5, we would have to do something like this:

print(1)
print(2)
print(3)
print(4)
print(5)

# With loops, we can write the code once and repeat it
# Here's a for loop that prints numbers from 1 to 5:

for i in range(1, 6):
    print(i)


# For loop
# The for loop is used for iterating over a sequence (list, tuple, dictionary, string, or range)
print("For loop with range:")
for i in range(5):
    print(i)

# While loop
# The while loop is used for repeated execution as long as an expression is true
print("While loop:")
i = 0
while i < 5:
    print(i)
    i += 1

# Nested loops
# A nested loop is a loop inside a loop
print("Nested for loops:")
for i in range(2):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop control statements
# break: Terminates the loop statement and transfers execution to the statement immediately following the loop
# continue: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating
print("For loop with break:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("For loop with continue:")
for i in range(5):
    if i == 3:
        continue
    print(i)