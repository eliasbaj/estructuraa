class Calculadora:
    def __init__(self,numero1,numero2):
        self.num1=numero1
        self.num2=numero2

    def suma(self):
        return self.num1+self.num2

    def resta(self):
        return self.num1-self.num2

    def multiplicacion(self):
        return self.num1*self.num2

    def division(self):
        return self.num1/self.num2

class CalEstandar(Calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)

    def multiplicacion(self):
        return self.num1*self.num2

    def Exponente(self):
        return self.num1**self.num2

    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        return numero

class CalCientifica(Calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)
        self.pi = 3.1416

    def circunferencia(self,radio):
        return 2*self.pi*radio

    def AreaCirculo(self,radio):
        return self.pi*radio**2

    def AreaCuadrado(self,lado):
        return lado**2

#cal = CalCientifica(1,2)
#print(cal.circunferencia(20))
# print(cal.multiplicacion())
# print(cal.valorAbsoluto(-5))
# cienti = CalCientifica(3,2)
# cienti.circunferencia()
# print(cienti.suma())