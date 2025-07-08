tarefas = []

def adicionar_tarefa(nome):
    tarefa = {"nome": nome, "concluida": False}
    tarefas.append(tarefa)

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
    else:
        print("Índice inválido.")

def listar_tarefas():
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. {tarefa['nome']} [{status}]")
    print()

# Menu
while True:
    print("=== MENU ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        indice = int(input("Digite o número da tarefa a concluir: "))
        concluir_tarefa(indice)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
