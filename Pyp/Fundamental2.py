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


# Exemplo de Uso (Valores ilustrativos para uso de variaveis pessoais.)
if __name__ == "__main__":
    # Operações Avançadas
    print("Potência:", OperacoesAvancadas.potencial(2, 3))
    print("Raiz quadrada de 16:", OperacoesAvancadas.raiz(16))
    print("Fatorial de 5:", OperacoesAvancadas.fatorial(5))

    # Equações
    print("Equação do 1º grau (2x + 6 = 0):", Equacoes.resolver_equacao_1_grau(2, 6))
    print("Equação do 2º grau (x² - 4x + 3 = 0):", Equacoes.resolver_equacao_2_grau(1, -4, 3))

    # Trigonometria
    print("Seno de 30°:", Trigonometria.seno(30))
    print("Cosseno de 45°:", Trigonometria.cosseno(45))
    print("Hipotenusa (catetos 3 e 4):", Trigonometria.pitagoras(3, 4))

    # Estatística
    dados = [1, 2, 2, 3, 4]
    print("Média:", Estatistica.media(dados))
    print("Mediana:", Estatistica.mediana(dados))
    print("Moda:", Estatistica.moda(dados))
