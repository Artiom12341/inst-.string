   
n=str(input("dati cnp ="))
c="""0123456789"""
if ((len(n)>13) or (len(n)<13)):
    print("Ai introdus cnp gresit")
elif len(n)==13:
    for c in n:
        print("cnp corect")
        break
