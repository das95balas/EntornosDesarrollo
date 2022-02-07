# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:01:32 2021

@author: DavidAlcázarSánchez
"""


def pedirNumeros():
    Num1 = float(input("Elige el primer número: "))
    Num2 = float(input("Elige el segundo número: "))
    return Num1, Num2

def sumaAB(Num1, Num2):
    print("\nHas elegido la opción suma de dos números.")
    print(f"El resultado de la suma de {Num1} y {Num2} es {Num1 + Num2}")

def restaAB(Num1, Num2):
    print("\nHas elegido la opción resta de dos números.")
    print(f"El resultado de la resta de {Num1} y {Num2} es {Num1 - Num2}")
    
def multiplicacionAB(Num1, Num2):
    print("\nHas elegido la opción multiplicación de dos números.")
    print(f"El resultado de la multiplicación de {Num1} por {Num2} es {Num1 * Num2}")
    
def divisionAB(Num1, Num2):
    print("\nHas elegido la opción división de dos números.")
    while Num2 == 0:
        print ("\n¡El divisor no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de la división de {Num1} entre {Num2} es {Num1 / Num2}")
    
def moduloAB(Num1, Num2):
    print("\nHas elegido la opción módulo entre dos números.")
    while Num2 == 0:
        print ("\n¡El segundo número no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de calcular el módulo de {Num1} entre {Num2} es {Num1 % Num2}")
    
def cocienteAB(Num1, Num2):
    print("Has elegido la opción cociente entre dos números.")
    while Num2 == 0:
        print ("\n¡El segundo número no puede ser 0!")
        Num2 = float(input("Elige ahora el segundo número (puede tener también dos decimales): "))
    print(f"El resultado de calcular el cociente de {Num1} entre {Num2} es {Num1 // Num2}")
    
def exponenteAB(Num1, Num2):
    print("\nHas elegido la opción exponente de un número elevado a otro.")
    print(f"El resultado del expontente de {Num1} elevado a {Num2} es {Num1**Num2}")
    
def paresCuadrados():
    print("\nHas elegido la opción calculadora de áreas de cuadrados para 'n' números pares.")
    y = 1
    x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
    for i in range (1, (x*2+1)):
        if y <= x and i % 2 == 0:
            print(f"El área del cuadrado numero {y} para lado con valor", i, "es de", i**2, "metros cuadrados.")
            y= y+1

def paresCirculos():
    print("\nHas elegido la opción calculadora de áreas de círculos para 'n' números pares.")
    y = 1
    x = int(input("Introduce la cantidad de números pares que que quieres que aparezcan en la operación: "))
    for i in range (1, (x*2+1)):
        if y <= x and i % 2 == 0:
            print(f"El área del círculo numero {y} para radio valor", i, "es de", 3.14 * (i**2), "metros cuadrados.")
            y= y+1
    
