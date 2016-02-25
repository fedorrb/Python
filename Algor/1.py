def karatsuba(x,y):
    # Функция умножения х на у методом Кацубы """
    if len(x)%2!=0 and len(x)!=1:
        x='0'+x
    if len(y)%2!=0 and len(y)!=1:
        y='0'+y

    while len(x)>len(y):
        y='0'+y
    while len(x)<len(y):
        x='0'+x

    n=len(x) # количество символов в переменной (они одинаковы по этому параметру)
    if n==1:
        return int(x)*int(y)
    else:
        a=x[:int(len(x)/2)]
        b=x[int(len(x)/2):]
        c=y[:int(len(y)/2)]
        d=y[int(len(y)/2):]

        ac=int(karatsuba(a,c))
        bd=int(karatsuba(b,d))

        a_b=str(int(a)+int(b))
        c_d=str(int(c)+int(d))

        ad_plus_bc=-int(ac)-int(bd)+int(karatsuba(a_b,c_d))


        if ad_plus_bc==105:
            z[0]=int(z[0])+1
        if ad_plus_bc==72:
            z[1]=int(z[1])+1
        if ad_plus_bc==12:
            z[2]=int(z[2])+1

        unswer=(10**n)*ac+(10**int((n/2)))*ad_plus_bc+bd

        return int(unswer)

X=1685287499328328297814655639278583667919355849391453456921116729
Y=7114192848577754587969744626558571536728983167954552999895348492

z=[0,0,0]

X=str(X)
Y=str(Y)
X_Y=karatsuba(X,Y)
print X_Y