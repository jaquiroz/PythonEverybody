# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'. Once 'done' is entered, print out the 
# largest and smallest of the numbers. If the user enters anything other 
# than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
# match the output below. 

mayor= None
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
    if mayor is None or val>mayor:
        mayor=val
    
    if menor is None or val<menor:
        menor=val

print("El numero mayor es: ",mayor)
print("El numero menor es: ",menor)