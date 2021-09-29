# 1. Countdown
def countDown(num):
    numList = []
    for x in range(num, -1, -1):
        temp = x
        numList.append(temp)
    return numList
# print(countDown(6))

# 2. Print and Return
def printReturn(num1,):
    print(num1[0])
    return num1[1]
# val = printReturn([5,7])
# print(val)

# 3. First Plus Length
def firstPlusLength(num):
    return num[0] + len(num)
# val = firstPlusLength([5,2,3,4,5])
# print(val)

# 4. Values Greater Than Second
def valuesGreater(num):
    newNum = []
    sum = 0
    if len(num) < 2:
        return False
    for x in range(len(num)):
        if num[x] > num[1]:
            sum = sum + 1
            newNum.append(num[x])
    else:
        print(sum)
        return newNum
# print(valuesGreater([3,2,1,1,5,6]))
# print(valuesGreater([3]))
