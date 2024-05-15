print("Signo Zodiacal, Ingrese su fecha de naciemiento:")
día=int(input("Ingrese el día de su nacimiento entre 1 y 31 :")) 
mes=int(input("Ingrese el mes de su nacimiento entre 1 y 12:"))

#Determinar el signo zodiacal
if (mes== 3 and día >= 21) or (mes== 4 and día<=19):
    signo="Aries"
elif (mes==4 and día>=20) or (mes==5 and día<=20):
    signo="Tauro"
elif (mes==5 and día>=21) or (mes==6 and día<=20):
    signo="Géminis"
elif (mes==6 and día>=21) or (mes==7 and día<=22):
    signo="Cancer"
elif (mes==7 and día>=23) or (mes==8 and día<=22):
    signo="Leo"
elif (mes==8 and día>=23) or (mes==9 and día<=22):
    signo="Virgo"
elif (mes==9 and día>=23) or (mes==10 and día<=22):
    signo="Libra"
elif (mes==10 and día>=23) or (mes==11 and día<=21):
    signo="Escorpio"
elif (mes==11 and día>=22) or (mes==12 and día<=21):
    signo="Sagitario"
elif (mes==12 and día>=22) or (mes==1 and día<=19):
    signo="Capricornio"
elif (mes==1 and día>=20) or (mes==2 and día<=18):
    signo="Acuario"
elif (mes==2 and día>=19) or (mes==3 and día<=20):
    signo="Piscis"

#Mostrar el signo zodiacal
print()
print("Tú signo zodiacal es:",signo)


