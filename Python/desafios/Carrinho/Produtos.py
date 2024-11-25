import tkinter as tk
from tkinter import messagebox




def adicionar_itens_gui():
    item = entry_item.get()
    try:
        quantidade = int(entry_quantidade.get())
        valor = float(entry_valor.get())
        
        if item and quantidade > 0 and valor > 0:
            itens.append(item)
            quantidade_items.append(quantidade)
            valores_items.append(valor)

            listbox_itens.insert(tk.END, f"{item} - Quantidade: {quantidade} - Valor Unitário: R${valor:.2f}")
            limpar_entradas()

        else:
            messagebox.showerror("Erro", "Quantidade e valor devem ser positivos e maior que zero!")
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro e Valor um número válido!")

def calcular_totais_gui():
    soma_total = 0
    total_itens = sum(quantidade_items)

    for i in range(len(itens)):
        total_item = quantidade_items[i] * valores_items[i]
        soma_total += total_item

    desconto = 0
    if total_itens >= 50:
        desconto = 0.15
    elif total_itens >= 20:
        desconto = 0.10
    elif total_itens >= 10:
        desconto = 0.05

    valor_total_com_desconto = soma_total * (1 - desconto)
    result_text.set(f"Valor Total: R${soma_total:.2f}\nDesconto: {desconto * 100:.0f}%\nTotal com Desconto: R${valor_total_com_desconto:.2f}")
    
def salvar_lista_gui():
    if not itens:
        messagebox.showwarning("Aviso", "Não há itens para salvar!")
        return

    try:
        with open("lista_compras.txt", "w") as file:
            file.write("Lista de Compras:\n")
            for i in range(len(itens)):
                total_item = quantidade_items[i] * valores_items[i]
                file.write(f"Item: {itens[i]}, Quantidade: {quantidade_items[i]}, Valor: R${valores_items[i]:.2f}, Total: R${total_item:.2f}\n")
            
            file.write("\n")
            file.write(result_text.get())
        
        messagebox.showinfo("Sucesso", "Lista salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

def limpar_entradas():
    entry_item.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

# Criando a interface gráfica
root = tk.Tk()
root.title("Carrinho de Compras")
root.geometry("600x500")

itens = []
quantidade_items = []
valores_items = []

# Frame de entrada de dados
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=20)

label_item = tk.Label(frame_entrada, text="Nome do item:")
label_item.grid(row=0, column=0, padx=5)

entry_item = tk.Entry(frame_entrada, width=30)
entry_item.grid(row=0, column=1, padx=5)

label_quantidade = tk.Label(frame_entrada, text="Quantidade:")
label_quantidade.grid(row=1, column=0, padx=5)

entry_quantidade = tk.Entry(frame_entrada, width=30)
entry_quantidade.grid(row=1, column=1, padx=5)

label_valor = tk.Label(frame_entrada, text="Valor: R$ ")
label_valor.grid(row=2, column=0, padx=5)

entry_valor = tk.Entry(frame_entrada, width=30)
entry_valor.grid(row=2, column=1, padx=5)

# Botão para adicionar item
button_adicionar = tk.Button(root, text="Adicionar Item", command=adicionar_itens_gui, width=20)
button_adicionar.pack(pady=10)

# Lista de itens
listbox_itens = tk.Listbox(root, width=80, height=10)
listbox_itens.pack(pady=10)

# Frame de resultados
frame_resultados = tk.Frame(root)
frame_resultados.pack(pady=20)

result_text = tk.StringVar()
label_resultados = tk.Label(frame_resultados, textvariable=result_text, justify=tk.LEFT)
label_resultados.pack()

# Botões de ação
button_calcular = tk.Button(root, text="Calcular Total", command=calcular_totais_gui, width=20)
button_calcular.pack(pady=5)

button_salvar = tk.Button(root, text="Salvar Lista", command=salvar_lista_gui, width=20)
button_salvar.pack(pady=5)

# Iniciando o loop da interface
root.mainloop()
