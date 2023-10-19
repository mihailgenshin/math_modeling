a=int(input('Введите значение а: ') )
b=int(input('Введите значение b: ') )
N=int(input('Введите значение N: ') )
for i in range(N):
    c = a + b
    a=b
    b=c
    print(c)