import random

n = int(random.randint(90,100))

# test case generator for sub array sum program

testfile = open('testcases.txt' , 'w')

testfile.writelines(str(n))

for i in range(n):
    arrsize = random.randint(1,100)
    sum = random.randint(50,150)
    testfile.writelines('\n' + str(arrsize) + ' ' + str(sum) + '\n')
    
    for j in range(arrsize):
        testfile.writelines(str(random.randint(0,9)) + ' ') 

testfile.flush
testfile.close