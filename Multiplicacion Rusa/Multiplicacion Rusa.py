#Program que realice la multiplicacion Rusa.

def multiplicacion_rusa(num1, num2):
    list1 = []
    cont = 0
    rus = 0
    if num1 < num2:
        mayor = num2
        menor = num1
    else:
        mayor = num1
        menor = num2
    
    
    limit = menor
    while cont <= limit:
        if menor % 2 != 0:
            list1.append(mayor)
        if menor <= 1:
            break
        
        menor = int(menor / 2)
        mayor = mayor * 2
        cont += 1
    
    for i in list1:
        rus = rus + i
    return rus 

print (multiplicacion_rusa(37, 12))
#>>>444
print (multiplicacion_rusa(250, 80))
#>>>20000
print (multiplicacion_rusa(41, 59))
#>>>2419
print (multiplicacion_rusa(27, 82))
#>>>2214
print (multiplicacion_rusa(13,888))
#>>>11544