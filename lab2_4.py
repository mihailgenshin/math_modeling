a=int(input('Введите сколько палок закину в попу вадима: ') )
b=int(input('Введите значение b: ') )
N=int(input('Введите значение N: ') )
for i in range(N):
    c = a + b
    a=b
    b=c
    print(c)





