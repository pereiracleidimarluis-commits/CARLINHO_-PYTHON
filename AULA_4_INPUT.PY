
# 1 — Lendo um texto
 nome = input("Digite seu nome: ")
 print(nome)
 # 2 — Exibindo a informação digitalizada
 nome = input("Digite seu nome: ")
 print(f"Olá, {nome}!")
 # 3 — Lendo mais de uma informação
 nome = input("Digite seu nome: ")
 cidade = input("Digite sua cidade: ")
 print(f"Nome: {nome}")
 print(f"Cidade: {cidade}")
 # 4 — Atenção: o input() sempre retorna texto
 idade = input("Digite sua idade: ")
 print(idade)
 # 5 — O problema ao somar números
 numero1 = input("Digite o primeiro número: ")
 numero2 = input("Digite o segundo número: ")
 print(numero1 + numero2)
 # 6 — Convertendo para inteiro
 numero1 = int(input("Digite o primeiro número: "))
 numero2 = int(input("Digite o segundo número: "))
 print(numero1 + numero2)
 # 7 — Convertendo para número decimal
 altura = float(input("Digite sua altura: "))
 print(altura)
 # 8 — Exemplo completo
 nome = input("Digite seu nome: ")
 idade = int(input("Digite sua idade: "))
 altura = float(input("Digite sua altura: "))
 print()
 print("===== CADASTRO =====")
 print(f"Nome: {nome}")
 print(f"Idade: {idade} anos")
 print(f"Altura: {altura:.2f} metros")
 # 9 — Exemplo com cálculos (média)
 nota1 = float(input("Digite a primeira nota: "))
 nota2 = float(input("Digite a segunda nota: "))
 media = (nota1 + nota2) / 2
 print(f"Média = {media:.2f}")
