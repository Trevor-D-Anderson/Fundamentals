for x in range(151):
    print(x)

for x in range(5, 1005, 5):
    print(x)


for x in range(1, 100):
    if x%10 == 0:
        print(x)
        print("Coding Dojo")
    elif x%5 == 0:
        print(x)
        print("Coding")


sum = 0
for x in range(0, 500000):
    if x%2 == 1:
        sum = sum + x
print(sum)


for x in range(2018, 0, -4):
    print(x)

lowNum = 2
highNum = 27
mult = 4

for x in range(lowNum, highNum + 1):
    if x%mult == 0:
        print(x)