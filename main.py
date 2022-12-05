from BinaryTree import BinaryTree

tree = BinaryTree()
print("Arvore Binaria")
opcao = 0
while opcao != 5:
     print("-----------------------------------")
     print("opcões:")
     print("  1: Adicionar")
     print("  2: Remover")
     print("  3: Printar")
     print("  4: Fechar")
     print("-----------------------------------")
     opcao = int(input(":"))
     if opcao == 1:
          x = int(input(" Informe o valor : "))
          tree.adicionar(x)
     elif opcao == 2:
          x = int(input(" Informe o valor : "))
          if tree.remover(x) == False:
               print(" Valor nao encontrado!")
     elif opcao == 4:
          tree.caminhar()
     elif opcao == 5:
          break