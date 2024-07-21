# 1. Importando Pandas

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import filedialog


# 2. Lendo Excel:
file = filedialog.askopenfilename()
df = pd.read_excel(file)


print("\n",df,"\n")

produto = df["Produto"].to_list()
produto = list(set(produto))
produto.sort()

valor = df["Valor"]

quantidade = df["Quantidade"]

mes = df["Mês"].to_list()
mes = list(set(mes))
mes.sort()


print(produto,mes) 


#Mês mais lucrativo
df["Lucro"] = df["Valor"] * df["Quantidade"]

mml = df.groupby("Mês")["Lucro"].sum()
mmll = mml.to_list()

print(mml)
#Mês com mais vendas

mmv = df.groupby("Mês")["Quantidade"].sum()
mmvl = mmv.to_list()
print(mmv)
#Produto mais vendido

pmv = df.groupby("Produto")["Quantidade"].sum()
pmvl = pmv.to_list()
print(pmv)
#Produto mais lucrativo

pml = df.groupby("Produto")["Lucro"].sum()
pmll = pml.to_list()
print(pml)
#Quantidade média vendida por mês:

qmv = float(mmv.mean())
print(f'{qmv:.2f}')

#Lucro médio mensal:
lmm = float(mml.mean())
# # 7. Testando gráficos(Ok):

# # 7.1 Mês mais lucrativo
# plt.bar(mes,mmll)
# plt.xlabel("Mês")
# plt.ylabel("Lucro")
# plt.title("Mês mais lucrativo")

# plt.show()

# # 7.2 Mês com mais vendas
# plt.bar(mes,mmvl)
# plt.xlabel("Mês")
# plt.ylabel("Quantidade")
# plt.title("Mês com mais vendas")

# plt.show()

# # 7.3 Produto mais lucrativo
# plt.bar(produto,pmvl)
# plt.xlabel("Produto")
# plt.ylabel("Lucro")
# plt.title("Produto mais lucrativo")

# plt.show()


# # 7.4 Produto com mais vendas
# plt.bar(produto,pmll)
# plt.xlabel("Produto")
# plt.ylabel("Quantidade")
# plt.title("Produto com mais vendas")

# plt.show()


# Interface:

janela = tk.Tk()

janela.title("Desafio Final Data Science")

text = tk.Label(janela,text= "Desafio Final - Analise de Vendas")
text2 = tk.Label(janela,text= "                             ")
text.grid(row=0,column=0,columnspan=999,pady=5)
text2.grid(row=8,column=0,columnspan=999,pady=5)

info = tk.Label(janela,text= "Princiapl:")
def main():
    info.config(text= f"""
                Introdução
                                                                                
                O objetivo é utilizar os conhecimentos adiquiridos em aula e criar uma aplicação de analise de dados.
                O tipo de analise escolhida foi o de vendas.
                              
                                
                Situação Problema:
                
                Num supermercado, foi decidido realizar um levantamento de quais chocolates até 80g eram os mais vendidos, 
                num periodo de um ano com meses aleatórios, foram escolhidos:
                1 - Kinder Bueno 
                2 - Snickers
                3 - Sufflair
                4 - Trento
                
                Através de dados como quantidade, valor e tempo,a analise foi feita e um relátorio foi emitido.
                Selecione entre os botões 1,2,3,4 para ver os gráficos e o botão 5 para ver o relatorio.
                O botão 6 retorna a esta tela.
        
            """ ,justify="left",anchor="ne") 
    info.grid(row=2,rowspan=7,column=4,columnspan=16)
    
main()

#Graficos:
    
def v1():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(mes,mmll)
    grafico.set_xlabel("Mês")
    grafico.set_ylabel("Lucro")
    grafico.set_title("1.Mês mais lucrativo")
    grafico.grid
    
    for i, v in enumerate(mmll):
         grafico.text(i , v+100, str(v),ha = "center")
                                        
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,rowspan=6,column=30,columnspan=39,padx=20)
    
def v2():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(mes,mmvl)
    grafico.set_xlabel("Mês")
    grafico.set_ylabel("Quantidade")
    grafico.set_title("2.Mês com mais vendas")
    
    for i, v in enumerate(mmvl):
         grafico.text(i , v+100, str(v),ha = "center")
         
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,rowspan=6,column=30,columnspan=39,padx=20)
    
def v3():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(produto,pmvl)
    grafico.set_xlabel("Produto")
    grafico.set_ylabel("Lucro")
    
    for i, v in enumerate(pmvl):
         grafico.text(i , v+100, str(v),ha = "center")
    
    grafico.set_title("3.Produto mais lucrativo")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,rowspan=6,column=30,columnspan=39,padx=20)
    
def v4():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(produto,pmll)
    grafico.set_xlabel("Produto")
    grafico.set_ylabel("Quantidade")
    grafico.set_title("4.Produto com mais vendas")
    
    for i, v in enumerate(pmll):
         grafico.text(i , v+100, str(v),ha = "center")
    
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,rowspan=6,column=30,columnspan=39,padx=20)

def rel():
    info.config(text= f"""
                Relátorio
                
                Através da análise de dados,concluimos que:
                1 - Agosto é o periodo de maior venda, e consequentemente,maior lucro(ver gráfico 1 e 2);
                2 - O produto mais lucrativo é o mais vendido, no caso,kinder bueno (ver gráfico 3 e 4).
                
                Quantidade média vendida por mês: {qmv:.0f} Unidades
                Lucro médio mensal: {lmm:.2f} R$
                
                Logo,a medidas a serem tomadas para melhorar ainda mais a vendas são as seguintes:
                1 - Impulsionar as vendas nos demais meses, afim de ter uma média de lucro maior;
                2 - Aumentar o marketing dos produtos que tiveram uma menor quantidade de venda (Snickers e Trento).
                
        
            """ ,justify="left",anchor="ne") 
   
    
v3()   
    
#Botões:
btn1 = tk.Button(janela,text="   1.Mês mais lucrativo  ", command=v1) # Executa o comando
btn2 = tk.Button(janela,text="  2.Mês com mais vendas  ", command=v2) # Executa o comando
btn3 = tk.Button(janela,text="3.Produto mais lucrativo ", command=v3) # Executa o comando
btn4 = tk.Button(janela,text="4.Produto com mais vendas", command=v4) # Executa o comando
btn5 = tk.Button(janela,text="       5.Relátorio       ", command=rel) # Executa o comando
btn6 = tk.Button(janela,text="       6.Principal       ", command=main) # Executa o comando

btn1.grid(column=0,row=2,padx=20)
btn2.grid(column=0,row=3,padx=20)
btn3.grid(column=0,row=4,padx=20)
btn4.grid(column=0,row=5,padx=20)
btn5.grid(column=0,row=6,padx=20)
btn6.grid(column=0,row=7,padx=20)



        

janela.mainloop()