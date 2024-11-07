import tkinter as tk
from tkinter import ttk

# Função de conversão
def converter():
    valor = float(entrada.get())
    unidade_entrada = combo_entrada.get()
    unidade_saida = combo_saida.get()
    
    # Converter o valor dependendo das unidades selecionadas
    if unidade_entrada == "Celsius":
        if unidade_saida == "Celsius":
            resultado = valor
        elif unidade_saida == "Fahrenheit":
            resultado = (valor * 9/5) + 32
        elif unidade_saida == "Kelvin":
            resultado = valor + 273.15
    elif unidade_entrada == "Fahrenheit":
        if unidade_saida == "Celsius":
            resultado = (valor - 32) * 5/9
        elif unidade_saida == "Fahrenheit":
            resultado = valor
        elif unidade_saida == "Kelvin":
            resultado = (valor - 32) * 5/9 + 273.15
    elif unidade_entrada == "Kelvin":
        if unidade_saida == "Celsius":
            resultado = valor - 273.15
        elif unidade_saida == "Fahrenheit":
            resultado = (valor - 273.15) * 9/5 + 32
        elif unidade_saida == "Kelvin":
            resultado = valor

    # Exibir o resultado
    etiqueta_resultado.config(text=f"Resultado: {resultado:.2f} {unidade_saida}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de Temperatura")

# Rótulos e campos de entrada
etiqueta_entrada = tk.Label(janela, text="Temperatura desejada:")
etiqueta_entrada.grid(row=0, column=0, padx=10, pady=10)

entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=10, pady=10)

# ComboBox para selecionar a unidade de entrada
etiqueta_unidade_entrada = tk.Label(janela, text="Escala termométrica atual:")
etiqueta_unidade_entrada.grid(row=1, column=0, padx=10, pady=10)

combo_entrada = ttk.Combobox(janela, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_entrada.grid(row=1, column=1, padx=10, pady=10)
combo_entrada.set("Celsius")  # Valor padrão

# ComboBox para selecionar a unidade de saída
etiqueta_unidade_saida = tk.Label(janela, text="Escala termométrica desejada:")
etiqueta_unidade_saida.grid(row=2, column=0, padx=10, pady=10)

combo_saida = ttk.Combobox(janela, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_saida.grid(row=2, column=1, padx=10, pady=10)
combo_saida.set("Celsius")  # Valor padrão

# Botão para realizar a conversão
botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.grid(row=3, column=0, columnspan=2, pady=10)

# Rótulo para exibir o resultado
etiqueta_resultado = tk.Label(janela, text="Resultado:")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal
janela.mainloop()
