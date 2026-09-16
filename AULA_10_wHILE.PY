Parte 1: Listas
 
Questão 1
 
python
  
frutas = ["maçã", "banana", "laranja", "uva", "melancia"]
print(frutas[0])   # primeira
print(frutas[-1])  # última
 
 
Questão 2
 
python
  
numeros = [10, 20, 30, 40]
numeros.append(50)
numeros.remove(20)
print(len(numeros))
 
 
Questão 3
 
python
  
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
print("Lista de notas:", notas)
 
 
Questão 4
 
python
  
linguagens = ["Python", "C++", "Java", "JavaScript"]
busca = input("Digite uma linguagem: ")
if busca in linguagens:
    print(f"{busca} está na lista!")
else:
    print(f"{busca} NÃO está na lista.")
 
 
Questão 5
 
python
  
valores = [15, 30, 45, 60]
print("Soma total:", sum(valores))
 
 
 
 
🔄 Parte 2: Laço  for 
 
Questão 6
 
python
  
for num in range(1, 16):
    print(num)
 
 
Questão 7
 
python
  
numeros = [2, 5, 8, 11, 14]
for n in numeros:
    print(n * 2)
 
 
Questão 8
 
python
  
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
 
 
Questão 9
 
python
  
idades = [12, 18, 25, 10, 30, 15, 22]
contador = 0
for idade in idades:
    if idade >= 18:
        contador += 1
print(f"Pessoas maiores de idade: {contador}")
 
 
Questão 10
 
python
  
for n in range(1, 21):
    if n % 2 == 0:
        print(n)
 
 
 
 
🔁 Parte 3: Laço  while 
 
Questão 11
 
python
  
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("Fim da contagem!")
 
 
Questão 12
 
python
  
SENHA_CORRETA = "python123"
senha = ""
while senha != SENHA_CORRETA:
    senha = input("Digite a senha: ")
print("Acesso liberado!")
 
 
Questão 13
 
python
  
soma = 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    soma += num
print(f"Soma total: {soma}")
 
 
Questão 14
 
python
  
numeros = []
while True:
    valor = int(input("Digite um número (negativo para parar): "))
    if valor < 0:
        break
    numeros.append(valor)
print("Lista digitada:", numeros)
 
 
Questão 15
 
python
  
valor = -1
while valor <= 0:
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Erro! Digite um valor válido maior que zero.")
print(f"Saque de R$ {valor:.2f} realizado!")
 
 
 
 
🔀 Parte 4:  match-case 
 
Questão 16
 
python
  
dia = int(input("Digite um número de 1 a 7: "))
match dia:
    case 1: print("Domingo")
    case 2: print("Segunda-feira")
    case 3: print("Terça-feira")
    case 4: print("Quarta-feira")
    case 5: print("Quinta-feira")
    case 6: print("Sexta-feira")
    case 7: print("Sábado")
    case _: print("Dia inválido!")
 
 
Questão 17
 
python
  
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

match op:
    case "+": print(f"Resultado: {n1 + n2}")
    case "-": print(f"Resultado: {n1 - n2}")
    case "*": print(f"Resultado: {n1 * n2}")
    case "/": 
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: divisão por zero!")
    case _: print("Operação inválida!")
 
 
Questão 18
 
python
  
codigo = input("Digite o código do produto: ")
match codigo:
    case "A1" | "A2": print("Categoria: Eletrônicos")
    case "B1" | "B2": print("Categoria: Vestuário")
    case "C1": print("Categoria: Alimentos")
    case _: print("Código desconhecido")
 
 
 
 
🧠 Parte 5: Desafios
 
Questão 19
 
python
  
comandos = ["iniciar", "pausar", "invalido", "parar"]
for cmd in comandos:
    match cmd:
        case "iniciar": print("Sistema iniciando...")
        case "pausar": print("Sistema pausado.")
        case "parar": print("Sistema desligado.")
        case _: print("Comando não reconhecido.")
 
 
Questão 20
 
python
  
compras = []
while True:
    produto = input("Digite um produto (ou 'sair' para encerrar): ")
    if produto.lower() == "sair":
        break
    compras.append(produto)

print("\n=== LISTA DE COMPRAS ===")
for i, item in enumerate(compras, 1):
    print(f"Item {i}: {item}")
 
 
 
 
✅ Como usar:
 
1. Abra o Bloco de Notas ou o Python IDLE
2. Copie a questão que quiser
3. Cole e salve com a extensão  .py  (ex:  questao1.py )
4. Execute!
 
