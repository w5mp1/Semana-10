print("Semana No. 10: Ejercicio 1" )
mes=int(input("Ingrese un número entre 1 y 12: "))
if mes<1 or mes>12:
    print("Error: El número debe de estar entre 1 y 12")
else:
    #validando con if
    if mes==1:
        print("Mes: enero")
    elif mes==2:
        print("Me: febrero")
    elif mes==3:
        print("Mes: marzo")
    elif mes==4:
        print("Mes: abril")
    elif mes==5:
        print("Me: mayo")
    elif mes==6:
        print("Mes: junio")
    elif mes==7:
        print("Me: julio")
    elif mes==8:
        print("Mes: agosto")
    elif mes==9:
        print("Mes: septiembre")
    elif mes==10:
        print("Me: octubre")
    elif mes==11:
        print("Mes: noviembre")
    elif mes==12:
        print("Mes: diciembre")

    #variable con case
        match(mes):
            case 1:
                print("Mes: enero")
            case 2:
                print("Mes: febrero")
            case 3: 
                print("Mes: marzo")
            case 4:
                print("Mes: abril")
            case 5:
                print("Mes: mayo")
            case 6:
                print("Mes: junio")
            case 7:
                print("Mes: julio")
            case 8:
                print("Mes: agosto")
            case 9: 
                print("Mes: septiembre")
            case 10:
                print("Mes: octubre")
            case 11:
                print("Mes: noviembre")
            case 12:
                print("Mes: diciembre")
print()
print("Semana No. 10: Ejercicio 2")

A=int(input("Ingrese el primer numero:"))
B=int(input("Ingrese el segundo numero:"))
C=int(input("Ingrese el tercer numero:"))

if A>B:
    if A>B:
        print("El mayor es:",A)
    else:
            if A==C:
                print("los mayores son:",A,"y",C)
            else:
                print("el mayor es:",C)
elif A == B:
    if A > C:
        print("Los mayores son:", A, "y", B)
    elif A == C:
        print("Los tres valores son iguales")
    else:
        print("El mayor es:", C)
else:
    if B > C:
        print("El mayor es:", B)
    elif B == C:
        print("Los mayores son:", B, "y", C)
    else:
        print("El mayor es:", C)