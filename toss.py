import random

toss = random.randint(0,1)
print(f"{toss}")

if toss == 1:
    print("Head")
else :
    print("Tail")