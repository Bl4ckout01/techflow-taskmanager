# TechFlow Task Manager

## 1. Sobre o projeto

A **TechFlow Solutions** é uma empresa fictícia especializada em soluções de software.  
Este projeto simula o desenvolvimento de um **sistema de gerenciamento de tarefas** para uma startup de logística, utilizando conceitos de **Engenharia de Software**, **metodologias ágeis**, **GitHub Projects**, **GitHub Actions** e **testes automatizados**.

O sistema permite cadastrar, listar, atualizar, priorizar, concluir e remover tarefas.  
A ideia é ajudar equipes de logística a acompanhar o fluxo de trabalho, priorizar atividades críticas e monitorar o andamento das entregas.

---

## 2. Objetivo

Criar um sistema simples de gerenciamento de tarefas com foco em:

- Organização de tarefas por status.
- Priorização de tarefas críticas.
- Registro de responsáveis.
- Controle básico de qualidade com testes automatizados.
- Simulação de mudanças de escopo durante o desenvolvimento.
- Uso do GitHub como ferramenta de gestão ágil.

---

## 3. Escopo inicial

O escopo inicial do projeto contempla:

- Criar tarefas.
- Listar tarefas cadastradas.
- Atualizar o status das tarefas.
- Marcar tarefas como concluídas.
- Remover tarefas.
- Validar dados obrigatórios.
- Executar testes automatizados com PyTest.
- Configurar pipeline de integração contínua com GitHub Actions.

---

## 4. Mudança de escopo simulada

Durante o desenvolvimento, o cliente solicitou uma nova necessidade:  
as tarefas deveriam possuir **níveis de prioridade**, pois algumas atividades logísticas são mais urgentes que outras.

### Justificativa da mudança

Em uma startup de logística, atrasos em tarefas críticas podem impactar diretamente entregas, clientes e custos operacionais.  
Por isso, foi adicionada a funcionalidade de **prioridade da tarefa**, permitindo classificar cada tarefa como:

- Baixa
- Média
- Alta
- Crítica

### Impacto no projeto

A mudança exigiu:

- Atualização da classe `Tarefa`.
- Inclusão do campo `prioridade`.
- Validação da prioridade.
- Atualização dos testes automatizados.
- Atualização do quadro Kanban no GitHub Projects.

---

## 5. Metodologia adotada

A metodologia utilizada foi baseada em práticas ágeis, principalmente o uso de um quadro **Kanban**.

O Kanban foi escolhido porque permite visualizar o fluxo de trabalho de forma simples, separando as tarefas em colunas:

- **A Fazer**
- **Em Progresso**
- **Concluído**

Essa organização facilita o acompanhamento do projeto, a priorização de atividades e a identificação de possíveis atrasos.

---

## 6. Como executar o projeto

### Pré-requisitos

Antes de começar, é necessário ter instalado:

- Python 3.10 ou superior
- Git
- VS Code ou outro editor de código

### Passo 1: clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/techflow-taskmanager.git
```

### Passo 2: entrar na pasta do projeto

```bash
cd techflow-taskmanager
```

### Passo 3: criar ambiente virtual

```bash
python -m venv venv
```

### Passo 4: ativar ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

### Passo 5: instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 6: executar o sistema

```bash
python main.py
```

### Passo 7: executar os testes

```bash
pytest
```

---

## 7. Estrutura do projeto

```text
techflow-taskmanager/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── src/
│   ├── __init__.py
│   ├── tarefa.py
│   └── gerenciador.py
│
├── tests/
│   ├── __init__.py
│   └── test_gerenciador.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 8. Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastrar nova tarefa.
- Listar tarefas.
- Buscar tarefa por ID.
- Atualizar status.
- Alterar prioridade.
- Marcar tarefa como concluída.
- Remover tarefa.
- Validar campos obrigatórios.

---

## 9. GitHub Actions

O projeto possui um pipeline de integração contínua configurado no arquivo:

```text
.github/workflows/tests.yml
```

Esse pipeline executa automaticamente os testes sempre que houver um `push` ou `pull request` na branch `main`.

---

## 10. Questões norteadoras

### Quais são as principais causas de falhas em projetos ágeis e como o GitHub pode ajudar a mitigá-las?

As principais causas são falhas de comunicação, falta de organização das tarefas, ausência de documentação e mudanças de escopo mal controladas.

O GitHub ajuda a reduzir esses problemas por meio de:

- Issues para registrar tarefas e problemas.
- Projects para organizar o Kanban.
- Commits para manter histórico das alterações.
- Pull Requests para revisar mudanças.
- GitHub Actions para automatizar testes.

---

### Quem são os principais beneficiados por um sistema de gerenciamento ágil?

Os principais beneficiados são:

- Gestores de projeto, que acompanham o progresso.
- Desenvolvedores, que visualizam suas tarefas.
- Clientes, que recebem entregas mais organizadas.
- Equipes de logística, que conseguem priorizar tarefas críticas.

---

### Como o GitHub Actions pode garantir a entrega de um software confiável?

O GitHub Actions permite executar testes automaticamente sempre que o código é alterado.  
Isso ajuda a identificar erros rapidamente, evitando que funcionalidades com problemas sejam entregues.

---

### Quais são os principais desafios ao implementar mudanças em um projeto ágil?

Os principais desafios são:

- Reorganizar prioridades.
- Evitar atrasos.
- Atualizar documentação.
- Adaptar testes.
- Comunicar a mudança para a equipe.

Para lidar com isso, é importante registrar a mudança, justificar sua necessidade e atualizar o Kanban.

---

### Como as metodologias ágeis podem ser aplicadas neste projeto?

As metodologias ágeis foram aplicadas por meio de:

- Divisão do projeto em pequenas tarefas.
- Uso de Kanban.
- Entregas incrementais.
- Priorização de funcionalidades.
- Adaptação a mudanças de escopo.
- Testes contínuos com GitHub Actions.

---

## 11. Sugestão de quadro Kanban

### A Fazer

- Criar repositório público no GitHub.
- Criar README inicial.
- Criar estrutura de pastas.
- Criar classe Tarefa.
- Criar gerenciador de tarefas.
- Criar testes automatizados.
- Configurar GitHub Actions.
- Simular mudança de escopo.

### Em Progresso

- Implementar CRUD de tarefas.
- Atualizar README com mudança de escopo.
- Adicionar prioridade nas tarefas.

### Concluído

- Estrutura inicial criada.
- CRUD implementado.
- Testes criados.
- Pipeline configurado.
- Documentação atualizada.

---

## 12. Sugestão de commits

Use pelo menos 10 commits, por exemplo:

```bash
git add .
git commit -m "Cria estrutura inicial do projeto"

git add README.md
git commit -m "Adiciona documentação inicial no README"

git add src/tarefa.py
git commit -m "Cria classe Tarefa"

git add src/gerenciador.py
git commit -m "Implementa cadastro e listagem de tarefas"

git add src/gerenciador.py
git commit -m "Adiciona atualização de status das tarefas"

git add src/gerenciador.py
git commit -m "Implementa remoção de tarefas"

git add tests/test_gerenciador.py
git commit -m "Adiciona testes automatizados do gerenciador"

git add .github/workflows/tests.yml
git commit -m "Configura pipeline de testes com GitHub Actions"

git add src/tarefa.py tests/test_gerenciador.py
git commit -m "Adiciona prioridade nas tarefas"

git add README.md
git commit -m "Documenta mudança de escopo do projeto"
```

---

## 13. Tecnologias utilizadas

- Python
- PyTest
- Git
- GitHub
- GitHub Projects
- GitHub Actions

---

## 14. Autor

Projeto acadêmico desenvolvido para simular a aplicação de metodologias ágeis em um ambiente de desenvolvimento de software.

## Atualização 1

Revisão da documentação do projeto para melhoria das instruções de uso.
