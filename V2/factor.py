num = int(input('enter a numer to find factor: '))
list=[]
for i in range(1,num+1):
    if  num % i == 0:
        list.append(i)
for x in list:
    print(x)
if len(list) == 2:
    print(num,'is a prime number')
