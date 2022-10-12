corn = True
Rice = True
Eba = True

if Eba:
    print('buy Eba')
elif Rice:
    print('buy Rice')
elif corn:
    print('buy corn')
else:
    print('dont buy anything')


Friends =['segun', 'tobi', 'bolu','akomolafe']
i = 0
while i < len(Friends):
    a=Friends[i]
    j = 0
    while j < len(a):
        b = a[j]
        print(b)
        j = j + 1
    i = i + 1
    #while i < len(a):
     #   print(a[i])


