n=str(input("dati cnp ="))
c="0123456789"
if len(n)>13:
    print("Ai introdus cnp gresit")
else:
    for i in n:
        if (i==c):
            nr=nr+1
            print("cnp corect")
        elif (i!=c):
            print("trebuie sa introduci cifre")    
