import pytest
from src.gerenciador import GerenciadorDeTarefas


def test_criar_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.criar_tarefa("Separar pedidos", "Ana", "Alta")

    assert tarefa.id == 1
    assert tarefa.titulo == "Separar pedidos"
    assert tarefa.responsavel == "Ana"
    assert tarefa.prioridade == "Alta"
    assert tarefa.status == "A Fazer"


def test_listar_tarefas():
    gerenciador = GerenciadorDeTarefas()
    gerenciador.criar_tarefa("Organizar rota", "Carlos", "Média")

    tarefas = gerenciador.listar_tarefas()

    assert len(tarefas) == 1


def test_atualizar_status():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.criar_tarefa("Conferir estoque", "Marina", "Baixa")

    gerenciador.atualizar_status(tarefa.id, "Em Progresso")

    assert tarefa.status == "Em Progresso"


def test_concluir_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.criar_tarefa("Enviar mercadoria", "João", "Crítica")

    gerenciador.concluir_tarefa(tarefa.id)

    assert tarefa.status == "Concluído"


def test_remover_tarefa():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.criar_tarefa("Atualizar relatório", "Bianca", "Média")

    gerenciador.remover_tarefa(tarefa.id)

    assert len(gerenciador.listar_tarefas()) == 0


def test_titulo_obrigatorio():
    gerenciador = GerenciadorDeTarefas()

    with pytest.raises(ValueError):
        gerenciador.criar_tarefa("", "Ana", "Alta")


def test_responsavel_obrigatorio():
    gerenciador = GerenciadorDeTarefas()

    with pytest.raises(ValueError):
        gerenciador.criar_tarefa("Separar pedidos", "", "Alta")


def test_prioridade_invalida():
    gerenciador = GerenciadorDeTarefas()

    with pytest.raises(ValueError):
        gerenciador.criar_tarefa("Separar pedidos", "Ana", "Urgente")


def test_alterar_prioridade():
    gerenciador = GerenciadorDeTarefas()
    tarefa = gerenciador.criar_tarefa("Separar pedidos", "Ana", "Baixa")

    gerenciador.alterar_prioridade(tarefa.id, "Crítica")

    assert tarefa.prioridade == "Crítica"
