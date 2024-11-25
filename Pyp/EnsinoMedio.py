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
            raise ValueError("Não é possível calcular a raiz quadrada de números negativos.")
        aproximacao = n / 2.0
        for _ in range(iteracoes):
            aproximacao = (aproximacao + n / aproximacao) / 2
        return aproximacao


class Progressao:
    def termo_pa(a1, n, r):
        return a1 + (n - 1) * r

    def soma_pa(a1, n, r):
        return n * (a1 + Progressao.termo_pa(a1, n, r)) / 2

    def termo_pg(a1, n, q):
        return a1 * (q ** (n - 1))

    def soma_pg(a1, n, q):
        if q == 1:
            return a1 * n
        return a1 * (1 - q ** n) / (1 - q)


class Matrizes:
    def determinante_2x2(matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("A matriz deve ser 2x2.")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(matriz):
        if len(matriz) != 3 or any(len(linha) != 3 for linha in matriz):
            raise ValueError("A matriz deve ser 3x3.")
        a = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
        b = matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
        c = matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])
        return a - b + c


class GeometriaAnalitica:
    def distancia_entre_pontos(x1, y1, x2, y2):
        return Algebra.aproximar_raiz((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def equacao_reta(x1, y1, x2, y2):
        if x1 == x2:
            return f"x = {x1}"  # Reta vertical
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return f"y = {m}x + {b}"


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

    def graus_para_radianos(angulo_graus):
        return angulo_graus * 3.14159 / 180

    def series_seno(x, termos=10):
        resultado = 0
        for n in range(termos):
            coeficiente = (-1) ** n
            numerador = x ** (2 * n + 1)
            denominador = Trigonometria.fatorial(2 * n + 1)
            resultado += coeficiente * (numerador / denominador)
        return resultado

    def series_cosseno(x, termos=10):
        resultado = 0
        for n in range(termos):
            coeficiente = (-1) ** n
            numerador = x ** (2 * n)
            denominador = Trigonometria.fatorial(2 * n)
            resultado += coeficiente * (numerador / denominador)
        return resultado

    def fatorial(n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


# Exemplo de Uso (Valores ilustrativos para uso de variaveis pessoais.)
if __name__ == "__main__":
    # Álgebra
    print("Equação do 2º grau (x² - 4x + 3 = 0):", Algebra.resolver_equacao_2_grau(1, -4, 3))

    # Progressões
    print("5º termo de uma PA com a1=2, r=3:", Progressao.termo_pa(2, 5, 3))
    print("Soma dos 5 primeiros termos da PA:", Progressao.soma_pa(2, 5, 3))

    # Matrizes
    matriz_2x2 = [[1, 2], [3, 4]]
    print("Determinante de matriz 2x2:", Matrizes.determinante_2x2(matriz_2x2))

    # Geometria Analítica
    print("Distância entre pontos (1,1) e (4,5):", GeometriaAnalitica.distancia_entre_pontos(1, 1, 4, 5))
    print("Equação da reta entre (1,2) e (3,4):", GeometriaAnalitica.equacao_reta(1, 2, 3, 4))

    # Trigonometria
    print("Seno de 30°:", Trigonometria.seno(30))
    print("Cosseno de 60°:", Trigonometria.cosseno(60))
    print("Tangente de 45°:", Trigonometria.tangente(45))
