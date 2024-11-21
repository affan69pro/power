base=int(input("this is a power calculater,enter your base : "))
pow=int(input("enter your power : "))
i=base
for l in range(1,pow,1):
    i=i*base
print("the answer is ",i)