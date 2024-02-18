#Sebastian Garcia Bustamante
#16/02/2024
#uvg.edu.gt

def enteroBinario():
    #Funcion de ingresar un numero decimal y convertirlo a binario
    try:
        arreglo = []*8
        numero = int(input("Por favor ingrese su numero a trasnformar: "))
        if numero > 255:
            print("Se ha pasado del limite de numeros que se puede representar")
            print(" ")
        else:
            arregloBinario = [128,64,32,16,8,4,2,1]  #arreglo para analizar los bits
            for i in range(8):
                #print(i)
                #print(arregloBinario[i]) 
                if(numero >= arregloBinario[i] ):   
                    numero = numero - arregloBinario[i] 
                    arreglo.append(1)
                    #print("Se agrego 1")
                else:
                    arreglo.append(0) 
                    #print("Se agrego 0 ")
            print("El numero en binario es: ")
            print(arreglo)
            print(" ")
    except:
        print("Ingreso algo que no es un numero decimal ")
        print(" ")

def complemento():
    #Funcion que hara la conversion de a A2
    try:
        binario = (input("Ingrese el numero binario a desarrollar: "))
        lista= binario.split(" ")
        print(lista)
        arreglo1 = []*8
        arreglo2 = []*8   #Arreglos a utilizar
        arreglo3 = []*8 
        for i in range(8):
            if (lista[i] == "1"):
                arreglo1.append(0)     #Crear una lista con Int para mejor manejo 
            else:
                arreglo1.append(1)
        print("Arreglo en a1")
        print(arreglo1)
        print(" ")
        lleva = 1
        for i in range(7,-1,-1):    #Ciclo que ira comparando para ir haciendo las conversiones correspondientes
            if(arreglo1[i] == 1):
                if(lleva == 1):
                    arreglo2.append(0)
                else:
                    arreglo2.append(1)
            else:
                if(lleva == 1):
                    arreglo2.append(1)
                    lleva = 0
                else:
                    arreglo2.append(0)
        #print("Invertido")
        #print(arreglo2)   
        z = 7
        for i in range(8):   # Ciclo que creara una lista de forma ordenada
            #print(arreglo2[z])
            arreglo3.append(arreglo2[z])
            z = z-1
        print("Arreglo en a2")
        print(arreglo3)
        print(" ")
    except:
        print("Ingreso un numero mayor a 8 bits o no ingreso los bits con espacios ")

def suma():
    try:
        sum1 = input("Ingrese el numero que quiere sumar: ")
        sum2 = input("Ingrese el otro numero que quiere sumar: ")
        lista1 = sum1.split(" ")
        lista2 = sum2.split(" ")
        arreg1 = []*8
        arreg2 = []*8  #arreglos a utilizar
        arreg3 = []*8
        arreg4 =[]*8

        for i in range(8):
            if(lista1[i] == "1"):
                arreg1.append(1)
            else:                       #Creacion de la lista con INT
                arreg1.append(0)
            if(lista2[i] == "1"):
                arreg2.append(1)
            else:
                arreg2.append(0)
        
        print("Numero 1 :")
        print(arreg1)
        print("Numero 2 : ")
        print(arreg2)
        print(" ")

        lleva = 0

        for i in range(7,-1,-1):            #for que analizara para realizar la suma correspondiente
            if(arreg1[i] == 1 and arreg2[i] == 1):
                if (lleva == 1):
                    arreg3.append(1)
                    lleva = 1
                else:
                    arreg3.append(0)
                    lleva = 1
            elif(arreg1[i] == 1 and arreg2[i] == 0):
                if(lleva == 1):
                    arreg3.append(0)
                    lleva = 1
                else:
                    arreg3.append(1)
                    lleva = 0
            elif(arreg1[i] == 0 and arreg2[i] == 1):
                if(lleva == 1):
                    arreg3.append(0)
                    lleva = 1
                else:
                    arreg3.append(1)
                    lleva = 0
            else:
                if(lleva == 1):
                    arreg3.append(1)
                    lleva = 0
                else:
                    arreg3.append(0)
                    lleva = 0
                
        #print(arreg3)
        z = 7
        for i in range(8):
            #print(arreglo2[z])
            arreg4.append(arreg3[z]) #crea un vector con los valores ordenados.
            z = z-1
        print("la suma es: ")
        print(arreg4)
        print(" ")
    except:
        print("Ingreso un numero mayor a 8 bits o no ingreso los bits con espacios ")
   #-----------------------------------------NOTA---------------------- ------------------
    #no hay progra defensiava, si el usuario ingresa numeros que su suma haga arriba de 8 bits, no dira overflow ni nada solamente mostrara 8 bits


bandera = True;
while True:
    print("Opcion 1: Numeros enteros a decimal")
    print("Opcion 2: Binarios a complemento a2") #menu
    print("Opcion 3: Suma de numeros de 8 bits")
    print("Opcion 4: Salir")
    opcion  = int(input("Por favor ingresar una opcion (Solo numero): "))
    if(opcion == 1):
        enteroBinario();
    elif(opcion == 2):
        complemento()
    elif(opcion == 3):
        suma()
    else:
        print("Gracias por ver")
        break
        

