#biblioteca
import os
#lista
nomes = []
# loop
while True:
    #menu
    print("1 - Cadastrar novo nome.")
    print("2 - Exibir lista.")
    print("3 - Ordenar lista")
    print("4 - Alterar o nome na lista")
    print("5 - Excluir o nome da lista")
    print("6 - Sair do Programa")
    opcao = input("opção desejada: ")
    #limpa console
    os.system("cls")
    #opcao dada pelo usuario    
    
    match opcao:
        case "1":
            novo_nome = input("Informe nome a ser cadastrado. ")
            nomes.append(novo_nome)
            print(f"{novo_nome} cadastrado com sucesso.")
            continue
        case "2":
            print("LISTA:\n")
            for i in range(len(nomes)):
                print(f"Indice {i}: {nomes}[i].")
                print("\n")
                continue
        case "3":
            nomes.sort()
            print("lista ordenada com sucesso.")
            continue
        case "4":
            try:
                indice = int(input("informe o indice do nome a ser alterado. "))
                confirmar = input(f"Deseja alterar o nome{nomes[indice]}? Digite 'sim' para confirmar: ")
                
                if confirmar== "sim":
                    nomes[indice] = input("Informe novo nome:")
                    print ("nome alterado com sucesso!")
                else:
                    print("nome não foi alterado.")
            except Exception as e:
                print(f"não foi possível alterar. {e}.")
            finally:
                continue
        case "5":
            try:
                indice = int(input("informe o indice do nome que deseja deletar. "))
                confirmar = input(f"Deseja deletar o nome{nomes[indice]} da lista? Digite 'sim' para confirmar: ")
                
                if confirmar== "sim":
                    del (nomes[indice])
                    print ("nome deletado com sucesso!")
                else:
                    print("nome não foi deletado.")
                
            except Exception as e:
                print(f"não foi possível deletar. {e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("opção invalida")
            continue
                
                
            
         
        
    

    

