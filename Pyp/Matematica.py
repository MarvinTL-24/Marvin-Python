# Matemática Fundamental 1
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


# Matemática Fundamental 2
class OperacoesAvancadas:
    def potencial(base, expoente):
        resultado = 1
        for _ in range(abs(expoente)):
            resultado *= base
        return resultado if expoente >= 0 else 1 / resultado

    def raiz(n, indice=2):
        if n < 0 and indice % 2 == 0:
            raise ValueError("Não é possível calcular raiz par de número negativo.")
        aproximacao = n / 2.0
        for _ in range(20):  # Método de Newton para melhorar a precisão
            aproximacao = (1 / indice) * ((indice - 1) * aproximacao + n / OperacoesAvancadas.potencial(aproximacao, indice - 1))
        return aproximacao

    def fatorial(n):
        if n < 0:
            raise ValueError("Fatorial não é definido para números negativos.")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


class Equacoes:
    def resolver_equacao_1_grau(a, b):
        if a == 0:
            raise ValueError("Coeficiente 'a' não pode ser zero em uma equação de 1º grau.")
        return -b / a

    def resolver_equacao_2_grau(a, b, c):
        if a == 0:
            raise ValueError("Coeficiente 'a' não pode ser zero em uma equação de 2º grau.")
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Não existem raízes reais."
        elif delta == 0:
            raiz_unica = -b / (2 * a)
            return raiz_unica
        else:
            raiz1 = (-b + OperacoesAvancadas.raiz(delta)) / (2 * a)
            raiz2 = (-b - OperacoesAvancadas.raiz(delta)) / (2 * a)
            return raiz1, raiz2


class Trigonometria:
    def seno(angulo_graus):
        angulo_rad = Trigonometria.graus_para_radianos(angulo_graus)
        return Trigonometria.series_seno(angulo_rad)

    def cosseno(angulo_graus):
        angulo_rad = Trigonometria.graus_para_radianos(angulo_graus)
        return Trigonometria.series_cosseno(angulo_rad)

    def tangente(angulo_graus):
        seno = Trigonometria.seno(angulo_graus)
        cosseno = Trigonometria.cosseno(angulo_graus)
        if cosseno == 0:
            raise ValueError("Tangente indefinida para este ângulo.")
        return seno / cosseno

    def pitagoras(cateto1, cateto2):
        return OperacoesAvancadas.raiz(cateto1 ** 2 + cateto2 ** 2)

    def graus_para_radianos(angulo_graus):
        return angulo_graus * 3.14159 / 180

    def series_seno(x, termos=10):
        resultado = 0
        for n in range(termos):
            coeficiente = (-1) ** n
            numerador = OperacoesAvancadas.potencial(x, 2 * n + 1)
            denominador = OperacoesAvancadas.fatorial(2 * n + 1)
            resultado += coeficiente * (numerador / denominador)
        return resultado

    def series_cosseno(x, termos=10):
        resultado = 0
        for n in range(termos):
            coeficiente = (-1) ** n
            numerador = OperacoesAvancadas.potencial(x, 2 * n)
            denominador = OperacoesAvancadas.fatorial(2 * n)
            resultado += coeficiente * (numerador / denominador)
        return resultado


class Estatistica:
    def media(lista):
        if len(lista) == 0:
            raise ValueError("A lista não pode estar vazia.")
        return sum(lista) / len(lista)

    def mediana(lista):
        if len(lista) == 0:
            raise ValueError("A lista não pode estar vazia.")
        lista_ordenada = sorted(lista)
        meio = len(lista_ordenada) // 2
        if len(lista_ordenada) % 2 == 0:
            return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
        else:
            return lista_ordenada[meio]

    def moda(lista):
        if len(lista) == 0:
            raise ValueError("A lista não pode estar vazia.")
        frequencias = {}
        for valor in lista:
            frequencias[valor] = frequencias.get(valor, 0) + 1
        moda = max(frequencias, key=frequencias.get)
        return moda


# Ensino Médio
class Algebra:
    def resolver_equacao_1_grau(a, b):
        if a == 0:
            raise ValueError("Coeficiente 'a' não pode ser zero em uma equação de 1º grau.")
        return -b / a

    def resolver_equacao_2_grau(a, b, c):
        if a == 0:
            raise ValueError("Coeficiente 'a' não pode ser zero em uma equação de 2º grau.")
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Não existem raízes reais."
        elif delta == 0:
            raiz_unica = -b / (2 * a)
            return raiz_unica
        else:
            raiz1 = (-b + Algebra.aproximar_raiz(delta)) / (2 * a)
            raiz2 = (-b - Algebra.aproximar_raiz(delta)) / (2 * a)
            return raiz1, raiz2

    def aproximar_raiz(n, iteracoes=20):
        if n < 0:
            raise ValueError("Não é possível calcular raiz quadrada de um número negativo.")
        x = n / 2.0
        for _ in range(iteracoes):
            x = (x + n / x) / 2.0
        return x


class Funcoes:
    def avaliar(funcao, valor):
        return funcao(valor)


class Logaritmos:
    def logaritmo(base, valor):
        if base <= 0 or base == 1:
            raise ValueError("Base do logaritmo deve ser maior que 0 e diferente de 1.")
        return OperacoesAvancadas.raiz(valor, base)


class GeometriaAvancada:
    def volume_esfera(raio):
        return (4/3) * 3.14159 * raio ** 3

    def volume_cone(raio, altura):
        return (1/3) * 3.14159 * raio ** 2 * altura

    def volume_cilindro(raio, altura):
        return 3.14159 * raio ** 2 * altura
