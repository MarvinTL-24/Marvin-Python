class Operacoes:
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador

    def somar(self, outra):
        novo_numerador = (self.numerador * outra.denominador) + (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao.simplificar(Fracao(novo_numerador, novo_denominador))

    def subtrair(self, outra):
        novo_numerador = (self.numerador * outra.denominador) - (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao.simplificar(Fracao(novo_numerador, novo_denominador))

    def multiplicar(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao.simplificar(Fracao(novo_numerador, novo_denominador))

    def dividir(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao.simplificar(Fracao(novo_numerador, novo_denominador))

    def simplificar(fracao):
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        divisor = mdc(fracao.numerador, fracao.denominador)
        return Fracao(fracao.numerador // divisor, fracao.denominador // divisor)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


class Geometria:
    def perimetro_quadrado(lado):
        return 4 * lado

    def area_quadrado(lado):
        return lado ** 2

    def perimetro_circulo(raio):
        return 2 * 3.14159 * raio

    def area_circulo(raio):
        return 3.14159 * raio ** 2

    def area_retangulo(base, altura):
        return base * altura

    def perimetro_retangulo(base, altura):
        return 2 * (base + altura)


class Medidas:
    def cm_para_metros(cm):
        return cm / 100

    def metros_para_cm(m):
        return m * 100

    def km_para_metros(km):
        return km * 1000

    def metros_para_km(m):
        return m / 1000


# Exemplo de Uso (Valores ilustrativos para uso de variaveis pessoais.)
if __name__ == "__main__":
    # Operações Básicas
    print("Soma:", Operacoes.soma(10, 5))
    print("Divisão:", Operacoes.divisao(15, 3))

    # Frações
    f1 = Fracao(1, 2)
    f2 = Fracao(1, 4)
    print("Soma de frações:", f1.somar(f2))

    # Geometria
    print("Área do quadrado:", Geometria.area_quadrado(5))
    print("Área do círculo:", Geometria.area_circulo(7))

    # Conversões
    print("10 cm em metros:", Medidas.cm_para_metros(10))
    print("5 km em metros:", Medidas.km_para_metros(5))
