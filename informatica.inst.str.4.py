s=str(input("dati sirul="))
c="""QWERTYUIOPĂÎÂASDFGHJKLȘȚZXCVBNM"""
d="""0123456789"""
e="""(){}[]+-*/="""
nr=0
for i in s:
    if i in c:
        nr=nr+1
print("Majuscule in sir =",nr)
b=0
for a in s:
    if a in d:
        b=b+1
print("cifre in sir =",b)
g=0
for f in s:
    if f in e:
        g=g+1
print("Caractere speciale in sir =",g)
    
