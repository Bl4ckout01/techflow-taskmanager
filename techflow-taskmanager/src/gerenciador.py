from src.tarefa import Tarefa


class GerenciadorDeTarefas:
    """
    Classe responsável por controlar o CRUD de tarefas.
    CRUD significa: Create, Read, Update e Delete.
    """

    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def criar_tarefa(self, titulo, responsavel, prioridade="Média"):
        tarefa = Tarefa(self.proximo_id, titulo, responsavel, prioridade)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def buscar_tarefa_por_id(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa.id == tarefa_id:
                return tarefa

        raise ValueError("Tarefa não encontrada.")

    def atualizar_status(self, tarefa_id, novo_status):
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        tarefa.atualizar_status(novo_status)
        return tarefa

    def alterar_prioridade(self, tarefa_id, nova_prioridade):
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        tarefa.alterar_prioridade(nova_prioridade)
        return tarefa

    def concluir_tarefa(self, tarefa_id):
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        tarefa.concluir()
        return tarefa

    def remover_tarefa(self, tarefa_id):
        tarefa = self.buscar_tarefa_por_id(tarefa_id)
        self.tarefas.remove(tarefa)
        return tarefa
