#Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
cont=0
sum=0
menor= None
while True:
    num=input("Ingrese el numero: ")
    if num=="done":#Trermina el ciclo while cuando se escribe por consola done
        break
    try:
        val=int(num)
    except:
        print("Entrada invalida")
        continue#Realiza el salto al inicio del ciclo while
    cont=cont+1
    sum=sum+val
print("La suma de los numeros es: ",sum)
print("El total de numeros es: ",cont)
print("El promedio es: ",sum/cont)