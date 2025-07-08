class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✅" if self.concluida else "❌"
        return f"{self.nome} [{status}]"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, nome):
        self.tarefas.append(Tarefa(nome))

    def concluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
        else:
            print("Índice inválido.")

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i}. {tarefa}")


class Aplicativo:
    def __init__(self):
        self.gerenciador = GerenciadorDeTarefas()

    def menu(self):
        while True:
            print("\n=== MENU ===")
            print("1. Adicionar tarefa")
            print("2. Listar tarefas")
            print("3. Concluir tarefa")
            print("4. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Digite o nome da tarefa: ")
                self.gerenciador.adicionar(nome)
            elif escolha == "2":
                self.gerenciador.listar()
            elif escolha == "3":
                try:
                    indice = int(input("Digite o número da tarefa a concluir: "))
                    self.gerenciador.concluir(indice)
                except ValueError:
                    print("Digite um número válido.")
            elif escolha == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = Aplicativo()
    app.menu()
