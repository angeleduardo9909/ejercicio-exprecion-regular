import re
import os
def pedirNumeroEntero():
     
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print()
    print("------------seleccione una opcion---------------")
    print ("1. Todas las palabras que tengan una longitud de 7 o más letras")
    print ("2. Expresiones que NO finalicen con una vocal")
    print ("3. Las palabras que inicien con M y donde la segunda letra no sea vocal")
    print ("4. todas las expreciones en comillas")
    print ("5. encontrar los ip's")
    print ("6. todas las horas")
    print ("7. todos los telefonos")
    print ("8. todos los correos electronicos")
    print ("9. todas las url") 
    print ("10. todos los codigos postales") 
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        
        print ("1.Todas las palabras que tengan una longitud de 7 o más letras")
        
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="[A-Za-z]{7,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
        
    elif opcion == 2:
        print ("las palabras que no finalizan con vocales son:")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="[a-zA-Z]+[^aeiou]\s"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
    elif opcion == 3:
        print("las palabras que inicien con M donde la segunda letra no sea vocal son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="M[^aeiou][a-zA-Z]{1,}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
        
    elif opcion == 4:
        print("las palabras en comillas son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="\"([\w\s]+)\""
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
    elif opcion == 5:
        print ("las ip's son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
    elif opcion == 6:
        print("las horas son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="\d{1,2}:\d{1,2}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    
    elif opcion == 7:        
        print("los telefonos son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="(\d{3}[\s-]\d{3}[\s-]\d{4})|(\d[0-9]{7,10})"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    
    elif opcion == 8:
        print("los correos electronicos son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
        
    elif opcion == 9:
        print("Opcion 9")    
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="https?:\/\/[\w\-]+\.[\w\-]+[#?]?.*"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    
    elif opcion == 10:
        print("los codigos postales son: ")
        textfile = open("C:/Users/angel/Desktop/kkk/ejemplo.txt","r")
        regex="\d{5}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()  
        
    elif opcion == 11:
            salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
 
print ("Fin")