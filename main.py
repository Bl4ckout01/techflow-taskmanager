from src.gerenciador import GerenciadorDeTarefas


def exibir_menu():
    print("\n=== TechFlow Task Manager ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar status")
    print("4 - Alterar prioridade")
    print("5 - Concluir tarefa")
    print("6 - Remover tarefa")
    print("0 - Sair")


def main():
    gerenciador = GerenciadorDeTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            responsavel = input("Responsável: ")
            prioridade = input("Prioridade (Baixa, Média, Alta ou Crítica): ")

            try:
                tarefa = gerenciador.criar_tarefa(titulo, responsavel, prioridade)
                print(f"Tarefa criada com sucesso: {tarefa}")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            tarefas = gerenciador.listar_tarefas()

            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for tarefa in tarefas:
                    print(tarefa)

        elif opcao == "3":
            try:
                tarefa_id = int(input("ID da tarefa: "))
                novo_status = input("Novo status: ")
                tarefa = gerenciador.atualizar_status(tarefa_id, novo_status)
                print(f"Status atualizado: {tarefa}")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                tarefa_id = int(input("ID da tarefa: "))
                nova_prioridade = input("Nova prioridade: ")
                tarefa = gerenciador.alterar_prioridade(tarefa_id, nova_prioridade)
                print(f"Prioridade atualizada: {tarefa}")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            try:
                tarefa_id = int(input("ID da tarefa: "))
                tarefa = gerenciador.concluir_tarefa(tarefa_id)
                print(f"Tarefa concluída: {tarefa}")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "6":
            try:
                tarefa_id = int(input("ID da tarefa: "))
                gerenciador.remover_tarefa(tarefa_id)
                print("Tarefa removida com sucesso.")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
