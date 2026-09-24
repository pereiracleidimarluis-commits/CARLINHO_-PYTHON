# Lista global para armazenar os nomes
 nomes = []
 def exibir_menu():
     print("""
     #####################
     # 1. Incluir 👍     #
     # 2. Excluir 🤦‍♀️     #
     # 3. Listar ✔️       #
     # 4. Atualizar 😎   #
     # 5. Sair 😜        #
     #####################
     """)
 def incluir_nome():
     nome = input("Digite seu nome: ")
     nomes.append(nome)
     print(f"'{nome}' adicionado com sucesso!")
 def excluir_nome():
     nome = input("Digite o nome para excluir: ")
     if nome in nomes:
         nomes.remove(nome)
         print(f"'{nome}' removido!")
     else:
         print("Nome não encontrado.")
 def listar_nomes():
     print("Nomes na lista:", nomes)
 def atualizar_nome():
     antigo = input("Digite o nome que deseja atualizar: ")
     if antigo in nomes:
         novo = input("Digite o novo nome: ")
         indice = nomes.index(antigo)
         nomes[indice] = novo
         print("Nome atualizado!")
     else:
         print("Nome não encontrado.")
 # Função principal que controla o fluxo do programa
 def principal():
     opcao = None
     while opcao != 5:
         exibir_menu()
         try:
             opcao = int(input("Digite a opção: "))
         except ValueError:
             print("Por favor, digite um número válido.")
             continue
         if opcao == 1:
             incluir_nome()
         elif opcao == 2:
             excluir_nome()
         elif opcao == 3:
             listar_nomes()
         elif opcao == 4:
             atualizar_nome()
         elif opcao == 5:
             print("Saindo do programa... Até mais!")
         else:
             print("Opção inválida! Tente novamente.")
     print("\nLista final de nomes:", nomes)
 principal()
