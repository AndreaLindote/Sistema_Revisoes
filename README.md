# Sistema_Revisoes (Em Desenvolvimento)

Projeto de sistema de gerenciamento de revisões de estudo desenvolvido em **Linguagem Python**.

## 📋 Descrição

O programa realiza o cadastro, leitura, edição e exclusão de usuários, matérias e revisões, informando as próximas revisões a serem realizadas.

## ⚙️ Funcionalidades:

- Cadastro, consulta, atualização e remoção de livros (CREATE - READ - UPDATE - DELETE).

- Gerenciamento de usuário, matérias e controle de revisões.

- Persistência de dados em bando de dados MySQL

## 🛠️ Tecnologias

- Linguagem **Python**
- MySQL
- Gerenciamento de banco de dados

## Pré Requisitos:
- Python 3.13 ou superior
- MySQL 8.0 ou superior
- Git

## 🚀 Como compilar e executar:

1. Clone o repositório: 
```bash
git clone https://github.com/AndreaLindote/Sistema_Revisoes
```
2. Crie o banco de dados:

- Abra o MySQL:
```bash
mysql -u -root -p
```
- Execute:
```bash
CREATE DATABASE sistema_revisoes_db;
USE sistema_revisoes_db;
SOURCE caminho/para/dados.sql
```
ou rode direto no terminal:
```bash
mysql -u root -p < dados.sql
```

3. Configure as credenciais:

Crie um arquivo `credenciais.env` na raiz do projeto com:
```bash
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=sistema_revisoes_db
```
⚠️ **Importante:** o arquivo `credenciais.env` não deve ser commitado. Ele já está no `.gitignore`.

4. Instale as dependências do Python
```bash
python -m pip install pymysql python-dotenv
```

5. Execute:
```bash
python3 main.py
```


## 📊 Resultados:
Ao executar o programa, um menu interativo é exibido:
```bash
SISTEMA DE REVISÕES
1. Adicionar Usuário
2. Listar Usuário
3. Excluir Usuário
4. Editar Usuário
5. Adicionar Matéria
5. Adicionar Estudante
6. Editar Matéria
7. Excluir Matéria
8. Exibir Matéria
9. Adicionar Revisão
10. Editar Revisão
11. Excluir Revisão
12. Exibir Revisão
0. Sair

Selecione uma opção:
```
Basta digitar o número da opção desejada e seguir as instruções na tela.
