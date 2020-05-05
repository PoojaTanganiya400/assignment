# WAP where numbers are divisible by 7 but not a multiple of 5 between 2000 and 3200(both included)
num = []
for i in range(2000,3200):
   if (i%7==0 and i%5!=0):
      num.append(i)
print(num)








