# Cria lista vazia
 alunos = []
 # Cadastra 3 nomes
 for i in range(3):
     nome = input("Digite o nome do aluno: ")
     alunos.append(nome)
 # Mostra a lista
 print("\n✅ Lista cadastrada:")
 print(alunos)
 # Quantidade de alunos
 print(f"\n📊 Total de alunos: {len(alunos)}")
 # Adiciona um aluno na posição 1
 alunos.insert(1, "Beatriz")
 print("\nApós insert(1, 'Beatriz'):")
 print(alunos)
 # Ordena em ordem alfabética
 alunos.sort()
 print("\nOrdenada (sort):")
 print(alunos)
 # Inverte a ordem
 alunos.reverse()
 print("\nInvertida (reverse):")
 print(alunos)
 # Remove um aluno
 alunos.remove("Beatriz")
 print("\nApós remover Beatriz:")
 print(alunos)S