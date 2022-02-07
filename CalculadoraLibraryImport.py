# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:01:32 2021

@author: DavidAlcázarSánchez
"""
#DESCRIPCION DEL PROGRAMA
#Calculadora 
#Suma de 2 números
#Resta de dos números
#Multiplicación de dos números
#División de dos números
#Módulo entre dos números
#Cociente entre dos números
#Exponente de un número elevado a otro
#Calculadora de áreas de cuadrados para 'n' números pares simultáneos
#Calculadora de áreas de círculos para 'n' números pares simultáneos
#Salir
#Introduce una opción

import CalculadoraV4_Funciones as cal

Calculadora = 0
while Calculadora != 10:
    Calculadora = int(input("¡Hola! Soy tu calculadora. Introduzca el número asignado a la operación que quieras realizar.\n \n \
    Las opciones son:\n \
    1. Suma de dos números.\n \
    2. Resta de dos números.\n \
    3. Multiplicación de dos números.\n \
    4. División de dos números.\n \
    5. Módulo entre dos números. \n \
    6. Cociente entre dos números. \n \
    7. Exponente de un número elevado a otro número. \n \
    8. Calculadora de áreas de cuadrados para 'n' números pares. \n \
    9. Calculadora de áreas de círculos para 'n' números pares. \n \
    10. Salir. \n \
    \nIntroduce el número para la operación que quieras realizar: "))

       
    if Calculadora == 1:
        Num1, Num2 = cal.pedirNumeros()
        cal.sumaAB(Num1, Num2)
       
    elif Calculadora == 2:
        Num1, Num2 = cal.pedirNumeros()
        cal.restaAB(Num1, Num2)
        
    elif Calculadora == 3:
        Num1, Num2 = cal.pedirNumeros()
        cal.multiplicacionAB(Num1, Num2)
        
    elif Calculadora == 4:
        Num1, Num2 = cal.pedirNumeros()
        cal.divisionAB(Num1, Num2)
        
    elif Calculadora == 5:
        Num1, Num2 = cal.pedirNumeros()
        cal.moduloAB(Num1, Num2)
        
    elif Calculadora == 6:
        Num1, Num2 = cal.pedirNumeros()
        cal.cocienteAB(Num1, Num2)
        
    elif Calculadora == 7:
        Num1, Num2 = cal.pedirNumeros()
        cal.exponenteAB(Num1, Num2)
        
    elif Calculadora == 8:
        cal.paresCuadrados()
        
    elif Calculadora == 9:
        cal.paresCirculos()
    
    elif Calculadora < 0 or Calculadora >10: 
       print("\n \nIntroduce un comando entre el 1 y el 10, por favor.")
        
else:
    print ("\nHas seleccionado la opción salir. ¡Hasta luego!")