class Tarefa:
    """
    Classe que representa uma tarefa dentro do sistema.
    Cada tarefa possui ID, título, responsável, prioridade e status.
    """

    PRIORIDADES_VALIDAS = ["Baixa", "Média", "Alta", "Crítica"]

    def __init__(self, tarefa_id, titulo, responsavel, prioridade="Média"):
        if not titulo:
            raise ValueError("O título da tarefa é obrigatório.")

        if not responsavel:
            raise ValueError("O responsável pela tarefa é obrigatório.")

        if prioridade not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridade inválida.")

        self.id = tarefa_id
        self.titulo = titulo
        self.responsavel = responsavel
        self.prioridade = prioridade
        self.status = "A Fazer"

    def atualizar_status(self, novo_status):
        if not novo_status:
            raise ValueError("O status não pode ser vazio.")

        self.status = novo_status

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridade inválida.")

        self.prioridade = nova_prioridade

    def concluir(self):
        self.status = "Concluído"

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Título: {self.titulo} | "
            f"Responsável: {self.responsavel} | "
            f"Prioridade: {self.prioridade} | "
            f"Status: {self.status}"
        )
