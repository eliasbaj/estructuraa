# -*- coding: utf-8 -*-
"""MENÚ OPERACIÓN NÚMEROS"""
class Básico:
    def __init__(self):
        pass
    
    def numerosN(self, n):
        print(f"Números del 1 al {n}")
        for i in range(1, n+1):
            print(i)
            
    def sumaN(self, n):
        acum = 0
        for i in range(1, n+1):
            acum += i
        print(f"El acumulado del rango de 1 a {n} es de: {acum}")
        
    def multiplo(self, n):
        aux = []
        for i in range(1, 13):
            res = n * i
            aux.append(res)
        print(f"Los multiplos de {n} son : {aux}")
        
    def DivisoresNumero(self, n):
        div = []
        for i in range(1, n):
            c = n % 2
            if c == 0: div.append(i)
        print("Los divisores del numero {n} son: ")
        return div
    
    def primo(self, n):
        acum = 0
        for i in range(1, n+1):
            if (n % 2) == 0:
                acum += 1
        if acum == 2: return (f"El numero {n} es primo")
        else: 
            return (f"El numero {n} no es primo")
        
    def perfecto(self, n):
        acum = 0
        for i in range(1, n):
            c = n % 2
            if c == 0: acum += i
        if acum == n: 
            return (f"El numero {n} es perfecto")
        else : 
            return (f"El numero {n} no es perfecto")
        
class Intermedio(Básico):
    
    def numerosN(self, n):
        acum , i = 0, 0
        while i <= n: acum += i
        return(f"La suma de los numero de 1 hasta {n} es de: {acum}")
    
    def factorial(self, n):
        fact , i = 1, 1
        while i <= n: fact += fact * i
        (f"El factorial de {n} es de: ")
        return fact
    
    def fibonacci(self, n):
        fb = [0, 1]
        if n >= 2:
            for i in range(0, n): fb[i+2] = fb[i] + fb[i+1]
        elif n == 1: 
            return (f"El valor fibonacci hasta la posicion {n} es: {fb}")
        elif n == 0: 
            return (f"El valor fibonacci hasta la posicion {n} es: {fb[0]}")
        return (f"El valor fibonacci hasta la posicion {n} es: {fb}")
    
    def primosGemelos(self, n1, n2):
        if super().primo(n1) == (f"{n1} es primo"):
            pass
        else: 
            return (f"{n1} no es primo")

        if super().primo(n2) == (f"{n2} es primo"):
            pass
        else: 
            return (f"{n2} no es primo")

        if n1 > n2: aux = n1 - n2
        else: 
            aux = n2 - n1

        if aux == 2: return (f"{n1} ; {n2} son primos gemelos")
        else: 
            return (f"{n1} ; {n2} no son primos gemelos")
        
    def amigos(self, n1, n2):
        div_n1 = super().divisoresNumero(n1)
        div_n2 = super().divisoresNumero(n2)
        acu1, acu2 = 0, 0
        for i in div_n1: acu1 += i
        for j in div_n2: acu2 += j
        if n1 == acu2 and n2 == acu1: 
            return (f"{n1} ; {n2} son números amigos")
        else: 
            return (f"{n1} ; {n2} no son números amigos")
        
    

    