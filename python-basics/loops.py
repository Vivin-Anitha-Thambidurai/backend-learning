# loops.py
# --------
# This file demonstrates for loops and while loops

# for loop example
print("For loop example:")
for i in range(1, 6):
    print("Number:", i)

# while loop example
print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# break and continue example
print("\nBreak and Continue example:")
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break
    if i == 2:
        continue
    print("Value:", i)
