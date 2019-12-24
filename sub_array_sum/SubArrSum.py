from time import sleep

testfile = open('testcases.txt' , 'r')

# this takes input of no of test cases...

n = int(testfile.readline())

# write your code after this...

for i in range(n):

    # this takes input form file and seperates array size and sum 

    val = testfile.readline().strip().split(' ')
    arrsize = int(val[0])
    sum = int(val[1])

    # this takes input of the actual array

    intarr = testfile.readline().strip().split(' ')
    arr = list(map(int , intarr))

    # variables used for calculation

    testsum = 0
    Spos = 0
    Epos = 0

    #sleep(1)
    
    # solution loop starts here...

    for start in range(arrsize):
        
        # this condition checks if a sloution is found , if yes then it'll skip to next array else it will keep searching for solution
        if start+1 == arrsize and end+1 == arrsize:
            print ("-1")

        if testsum == sum:
            testsum = 0
            break

        # this loop will add starting elements of the array till a solution is found , if testsum > required sum , then it will skip 
        # the first element and start from 2nd index , then 3rd index and so on...

        for end in range(start , arrsize):
            testsum = testsum + arr[end]


            if testsum == sum :
                Spos = start
                Epos = end
                print("Spos = " + str(Spos) + " and Epos = " + str(Epos))
                break

            elif testsum < sum:
                continue

            else:
                testsum = 0
                break


testfile.close()