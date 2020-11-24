s=str(input("dati sirul="))
c='QWERTYUIOPĂÎÂASDFGHJKLȘȚZXCVBNM'
d='0123456789'
e='(){}[]+-*/='

for i in s:
    nr=0
    if(i==c):
        nr=nr+1
print("Majuscule in sir =",nr)

for a in s:
    b=0
    if(a==d):
        b=b+1
print("cifre in sir =",b)

for f in s:
    g=0
    if (f==e):
        g=g+1
print("Caractere speciale in sir =",g)
    