from tkinter import *
from tkinter import ttk
import math as mt

# Variáveis globais para as contas
valor1 = 0
valor2 = 0
anterior = ""
operacao = ""

# block vai bloquear a execução quando houver alguma operação impossível
block = False

# bloqueia o uso da vírgula de float
comma_block = False

# Criar a Janela e configurar ela
janela = Tk()
janela.iconbitmap("Icone.ico")
janela.geometry("352x490")
janela.minsize(352,490)
janela.maxsize(352, 490)
janela.title("Calculadora")
janela.configure(background= "#181818")



### 
# Receber o tamanho da janela
largura_janela = janela.winfo_width()
altura_janela = janela.winfo_height()

# Definir um tamanho para o botão
largura_botao = largura_janela // 4
altura_botao = altura_janela // 7


# Entrada de valores
entrada = Entry(janela, borderwidth=4, width= 15 , relief = FLAT, font=("Courier", 20, "bold"), bg="#78839F", fg="#000000", justify="left")
entrada.grid(
  row = 0,
  column = 0,
  columnspan = 3,
  pady = 2
)



# Função para entradas inválidas
def invalid_input():
  global block
  entrada.delete(0, END)
  entrada.insert(0, "Invalid Input")
  block = True


# Função de click
def click(numero):
  global comma_block
  if(block):
    return
  if (numero == "."):
    if(not comma_block):
      comma_block = True
    else:
      return
  entrada.insert(END, numero)


# Função clear
def click_clear():
  global operacao
  global valor1
  global valor2
  global anterior
  global block
  global comma_block
  # retira o bloqueio caso haja
  block = False
  comma_block = False
  # Reseta os valores
  operacao = ""
  valor1 = 0
  valor2 = 0
  anterior = ""
  entrada.delete(0, END)


def click_porcentagem():
  global valor1
  global operacao
  if(block):
    return
  if(valor1 == 0 or operacao == ""):
    auxiliar = 0
  else:
    try:
      auxiliar = float(entrada.get())
    except:
      auxiliar = valor1
    if (operacao == "+" or operacao == "-"):
      auxiliar = (auxiliar * valor1)/100
    elif (operacao == "*" or operacao == "÷"):
      auxiliar = auxiliar/100
  entrada.delete(0, END)
  entrada.insert(0, auxiliar)


def click_fatorial():
  global block
  if (block):
    return
  try:
    auxiliar = int(entrada.get())
  except:
    auxiliar = 0
  if (auxiliar < 0):
    invalid_input()
    return
  auxiliar = mt.factorial(auxiliar)
  entrada.delete(0,END)
  entrada.insert(0, auxiliar)


def click_mod():
  global valor1
  global operacao
  global anterior
  global block
  global comma_block

  if(block):
    return

  # operação de mod não usa float
  comma_block = True
  if(operacao == ""):
    try:
      valor1 = int(entrada.get())
    except:
      valor1 = 0
  anterior = "a%"
  operacao = "%"
  entrada.delete(0,END)



# Função delete
def click_delete():
  global block
  global comma_block
  if(block):
    return
  auxiliar = entrada.get()
  tamanho = len(auxiliar)
  try:
    entrada.delete(entrada.index(END)-1)
    # Se o comma foi removido então pode tirar o bloqueio
    if(auxiliar[tamanho-1] == "."):
      comma_block = False
  except:
    return

# Função dividir
def click_dividir():
  global valor1
  global operacao
  global anterior
  global block
  global comma_block
  if(block):
    return
  comma_block = False
  if (operacao == ""):
    try:
      valor1 = float(entrada.get())
    except:
      valor1 = 0
  anterior = "a÷"
  operacao = "÷"
  entrada.delete(0, END)


# Função multiplicar
def click_multiplicar():
  global valor1
  global operacao
  global anterior
  global block
  global comma_block
  if(block):
    return
  comma_block = False
  if (operacao == ""):
    try:
      valor1 = float(entrada.get())
    except:
      valor1 = 0
  operacao = "*"
  anterior = "a*"
  entrada.delete(0, END)


# Função subtrair
def click_subtrair():
  global valor1
  global operacao
  global anterior
  global block
  global comma_block
  if(block):
    return
  comma_block = False
  if (operacao == ""):
    try:
      valor1 = float(entrada.get())
    except:
      valor1 = 0
  operacao = "-"
  anterior = "a-"
  entrada.delete(0,END)




# Função adicionar
def click_adicionar():
  global valor1
  global operacao
  global anterior
  global block
  global comma_block
  if(block):
    return
  comma_block = False
  if (operacao == ""):
    try:
      valor1 = float(entrada.get())
    except:
      valor1 = 0  
  anterior = "a+"
  operacao = "+"

  entrada.delete(0, END)



# Função inverter sinal
def click_inverter():
  global comma_block
  if(block):
    return
  try:
    save = float(entrada.get())
    comma_block = True
  except:
    save = 0

  if (save != 0):
    save = save * - 1
  else:
    save = save
  
  entrada.delete(0, END)

  if (save == int(save)):
    entrada.insert(0, int(save))
    comma_block = False
  else:
    entrada.insert(0, float(save))
  
  
# Função resultado
def click_resultado():
  global operacao
  global valor1
  global anterior
  global valor2
  global block
  global comma_block

  if(block):
    return
  comma_block = False
  # Se anterior estiver vazio indica que a operação anterior se repete
  if(anterior == ""):
    anterior = "="
  
  # Caso contrário segue para receber o valor2
  else:
    try:
      valor2 = float(entrada.get())
      anterior = anterior + "b"
      anterior = anterior + "="
    except:
      anterior = anterior + "="
  
  # Caso a entrada do valor2 esteja vazia valor2 = valor1 
  if (anterior == "a+=" or anterior == "a-=" or anterior == "a*=" or anterior == "a÷=" or anterior == "a%="):
    valor2 = valor1
    print(valor2)

  entrada.delete(0, END)

  # Switch case operações

  #Executar a divisão 
  if (operacao == "÷"):
    # Verificar os casos onde a divisão não é possível
    if(valor2 == 0):
      invalid_input()
      return
    elif (valor1 == 0):
      # Se dividir o zero retorna zero
      valor1 = 0
    # Guardar o resultado em valor1
    else:
      valor1 = float(valor1)/float(valor2)


  elif (operacao == "*"): 
    valor1 = float(valor1)*float(valor2)
    


  elif (operacao == "-"):
    valor1 = float(valor1)-float(valor2)


  elif (operacao == "+"):
    valor1 = float(valor1)+float(valor2)

  elif (operacao == "%"):
    # Verificar os casos onde a divisão não é possível
    if(valor2 == 0):
      invalid_input()
      return
    valor1 = int(valor1) % int(valor2)

  anterior = ""
  if (int(valor1) == float(valor1)):
    entrada.insert(0, int(valor1))
  else:
    entrada.insert(0, float(valor1))

# Criar e posicionar os botões iterativos

# Definir os botões numéricos
comma = Button(janela, text = ".",background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click("."), pady = 10, padx = 20)

numero0 = Button(janela, text = "0", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(0), pady = 10, padx = 20)

numero1 = Button(janela, text = "1", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(1), pady = 10, padx = 20)

numero2 = Button(janela, text = "2", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(2), pady = 10, padx = 20)

numero3 = Button(janela, text = "3", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, comman = lambda: click(3), pady = 10, padx = 20)

numero4 = Button(janela, text = "4", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(4), pady = 10, padx = 20)

numero5 = Button(janela, text = "5", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(5), pady = 10, padx = 20)

numero6 = Button(janela, text = "6", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(6), pady = 10, padx = 20)

numero7 = Button(janela, text = "7", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(7), pady = 10, padx = 20)

numero8 = Button(janela, text = "8", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height = 2, width = 5, command = lambda: click(8), pady = 10, padx = 20)

numero9 = Button(janela, text = "9", background= "#FF8000", font = "Calibri", activebackground= "#C76400", height=2, width = 5, command = lambda: click(9), pady = 10, padx = 20)

# Definir os botões dos operadores e das funções

# Limpar
clear = Button(janela, text = "C", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_clear, pady = 10, padx = 20)


# Porcentagem
porcentagem = Button(janela, text = "%", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_porcentagem, pady = 10, padx = 20)


# Fatorial
fatorial = Button(janela, text = "n!", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_fatorial, pady = 10, padx = 20)


# Delete
b_delete = Button(janela, text = "←", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_delete, pady = 10, padx = 64)


# Dividir
dividir = Button(janela, text = "÷", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_dividir, pady = 10, padx = 20)


# Multiplicar
multiplicar = Button(janela, text = "X", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_multiplicar, pady = 10, padx = 20)


# Subtrair
subtrair = Button(janela, text = "-", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_subtrair, pady = 10, padx = 20)


# Adicionar
adicionar = Button(janela, text = "+", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_adicionar, pady = 45, padx = 20)


# Resultado
resultado = Button(janela, text = "=", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_resultado, pady = 10, padx = 20)


# Inverter sinal
inverter = Button(janela, text = "+/-", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_inverter, pady = 10, padx = 20)


# Mod
mod = Button(janela, text = "a mod b", background= "#262A2F", font = "Calibri", activebackground= "#373A3F", height=2, width=5, command = click_mod, pady = 10, padx = 64)


# fileira inicial
clear.grid(row = 0, column = 3)

# primeira fileira
porcentagem.grid(row = 1, column = 0)
fatorial.grid(row = 1, column = 1)
b_delete.grid(row = 1, column = 2, columnspan=2)

# segunda fileira
numero7.grid(row = 2, column=0)
numero8.grid(row = 2, column = 1)
numero9.grid(row = 2, column = 2)
dividir.grid(row = 2, column = 3)

# terceira fileira
numero4.grid(row = 3, column = 0)
numero5.grid(row = 3, column = 1)
numero6.grid(row = 3, column = 2)
multiplicar.grid(row = 3, column = 3)

# quarta fileira
numero1.grid(row = 4, column = 0)
numero2.grid(row = 4, column = 1)
numero3.grid(row = 4, column = 2)
subtrair.grid(row = 4, column = 3)

# quinta fileira
inverter.grid(row = 5, column = 0)
numero0.grid(row = 5, column = 1)
comma.grid(row = 5 ,column = 2)
adicionar.grid(row = 5, column = 3, rowspan = 2)

# sexta fileira
mod.grid(row = 6, column = 0, columnspan = 2)
resultado.grid(row = 6, column = 2)

janela.mainloop()
