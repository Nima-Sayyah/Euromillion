import random

list1=[]
for i in range(1,51):
        list1.append(i)

print(list1,"\n")
        
list2=[]
for i in range(1,13):
        list2.append(i)

print(list2,"\n")

cnt1=len(list1)
cnt2=len(list2)

list3=[]
for i in range(5):
        this = random.randrange(cnt1)
        if this !=0:
                list3.append(this)
        else:
                print("Something Went Wrong, Try Again")

print("Numbers (1-50) - Five Numbers :",sorted(list3))

list4=[]

for i in range(2):
        that = random.randrange(cnt2)
        if that !=0:
                list4.append(that)
        else:
                print("Something Went Wrong, Try Again")

print("Lucky Stars (1-12) - Two Numbers :",sorted(list4))

        


