#defining the list
L=[2,3,1,5,4,7]

#printing the list with a for loop
for i in L:
    print(i, end=" ")

#scenario 1: print the values in the list by multiplying to two
for i in L:
    print(i*2, end=" ")


#scenario 2: find the even and odd numbers
for i in L:
    if i%2==0:
        print("Even")
    else:
        print("Odd")

even = 0
odd = 0

##scenario 3: Get the count of Even and Odd Numbers
for i in L:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("No of Evens: ",even)
print("No of Odds: ",odd)