#num = [1,2,3,4,5,6,7,8,9,10]
num = range(1,11)     #Range function
accum = 0
count =0
for w in num:
    accum = accum + w
    count = count + 1
    #print(accum)
    #print(count)
print(accum) 
print(count)
print(type(num)) # The Range function does not produce a list
num1 = list(num) # If we want a lis the we need to cast the range function
print(type(num1)) 