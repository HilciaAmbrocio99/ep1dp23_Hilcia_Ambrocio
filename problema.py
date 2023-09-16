v1=int(input("Ingrese numero1"))
v2=int(input("Ingrese numero2"))
v3=int(input("Ingrese numero3"))
v4=int(input("Ingrese numero4"))
v5= int(input("Ingrese numero5"))

promedio=(v1+v2+v3+v4+v5)/5
print("el promedio de los valores ingresados es ", promedio)

menor=v5
if v5>v1:
    menor=v1
    if v5>v2:
        menor=v2
        if v5>v3:
            menor=v3
            if v5>v4:
                menor=v4
else:
    menor=v5
    if v4>v3:
        menor=v3
        if v4>v2:
            menor=v2
            if v4>v1:
                menor=v1
            
    else: 
        menor=v4
        if v3>v2:
            menor=v2
            if v3>v1:
                menor=v1
        else:
            menor=v3
            if v2>v1:
                menor=v1
            else: 
                menor=v2
print("el numero menor es ",menor)
        

suma=(v1+v2+v3+v4+v5)
multi= (v1*v3)
if  suma>multi:
    print("el valor de la suma es mayor")
else: 
    if suma<multi:
        print("el valor de la suma es menor")
    else:
         print("el valor de la suma es igual")