import pymysql
import classes


connection = pymysql.connect(
        host='DB_HOST',
        user="DB_USER",
        password="DB_PASSWORD",
        database = 'DB_NAME'
    )
try:        
    usuario_repo = classes.Usuario_Repositorio(connection)
    materia_repo = classes.Materias_Repositorio(connection)
    revisoes_repo = classes.Revisoes_Repositorio(connection)

    while True:    
        print("SISTEMA DE REVISÕES")
        print("1. Adicionar Usuário")
        print("2.Listar Usuário")
        print("3.Excluir Usuário")
        print("4.Editar Usuário")
        print("5.Adicionar Matéria")
        print("6.Editar Matéria")
        print("7.Excluir Matéria")
        print("8.Exibir Matéria")
        print("9.Adicionar Revisão")
        print("10.Editar Revisão")
        print("11.Excluir Revisão")
        print("12.Exibir Revisão")
        print("0. Sair")

        try:
            opcao = int(input("Selecione uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue
        #Usuários
        if opcao == 1: #adicionar usuário
            nome = input("Informe o nome: ")
            email = input("Informe o email: ")
            senha = input("Informe a senha: ")    
            usuario = classes.Usuario(nome, email, senha)
            confirma = usuario_repo.registrar_usuario(usuario)

            if confirma:
                print("Usuário criado com sucesso.")
            else:
                print("Não foi possível criar o usuário")

        if opcao == 2: #listar usuário
            id = input("Informe o ID: ")
                
            confirma = usuario_repo.listar_usuario(id)

            if confirma:
                print(f"ID: {usuario_repo.id} | Nome: {usuario_repo.nome} | Email: {usuario_repo.email}")
            else: 
                ("Usuário não encontrado.")
            
        if opcao == 3: #excluir usuário
            id = input("Informe o ID: ")

            confirma = usuario_repo.deletar_usuario(id)

            if confirma:
                print("Usuário deletado com sucesso")
            else:
                print("Não foi possível deletar o usuário")

        if opcao == 4: #editar usuário
            id = input("Informe o ID: ")
            nome_novo = input("Informe novo nome")
            novo_email = input("Informe novo email:")
            nova_senha = input("Informe nova senha:")

            editado_usuario = classes.Usuario(id, nome_novo, novo_email, nova_senha)
            confirma = usuario_repo.editar_usuario(editado_usuario)

            if confirma:
                print("Usuário editado com sucesso")
            else:
                print("Não foi possível editar o usuário.")
            
        # Matérias
        if opcao == 5: #adicionar matéria
            nome = input("Informe o nome da matéria: ")
            conteudo = input("Informe os conteudos: ")#### adicionar lista
            usuario_associado = input("Informe o ID do usuario associado: ")

            materia = classes.Materias(usuario_associado, nome, conteudo)
            confirma = materia_repo.registrar_materia(materia)

            if confirma:
                print("Matéria adicionada com sucesso.")
            else:
                print("Não foi possível adicionar a matéria.")

        if opcao == 6: #editar máteria
            id = input("Informe o ID da matéria: ")
            novo_nome = input("Informe novo nome")
            novo_conteudo = input("Informe os novos conteudos:")
            novo_usuario = input("Informe o novo usuario associado:")

            materia_editada = classes.Materias(id, novo_nome, novo_conteudo, novo_usuario)
            confirma = materia_repo.editar_materia(materia_editada)

            if confirma:
                print("Matéria editada com sucesso.")
            else:
                print("Não foi possível editar a matéria")

        if opcao == 7: #excluir matéria
            id = input("Informe o ID da matéria: ")
                
            confirma = materia_repo.deletar_materia(id)
            if confirma:
                print("Matéria excluída com sucesso.")
            else:
                print("Não foi possível excluir a matéria")
                
        if opcao == 8: #exibir matéria
            id = input("Informe o ID da matéria: ")
                
            confirma = materia_repo.listar_materia(id)

            if confirma:
                print(f"ID: {materia_repo.id} | Nome: {materia_repo.nome} | Email: {materia_repo.email}")
            else:
                print("Não foi possível exibir a matéria.")
                
        # Revisões
        if opcao == 9: #adicionar revisão
            descricao = input("Informe a descrição da revisão: ")
            status = input("Informe o status da revisão 'pendente' ou 'concluido'")
            data_criacao = input("Informe a data de criacao:")
            data_revisao = input("Informe a data para a nova revisao")
            materia_associada = input("Informe a matéria associada:")
                
            revisao = classes.Revisoes(materia_associada, descricao, status, data_criacao, data_revisao)
            confirma = revisoes_repo.registrar_revisao(revisao)

            if confirma:
                print("Revisão registrada com sucesso.")
            else:
                print("Não foi possível registrar a revisão.")

        if opcao == 10: #editar revisão
            id_nova_revisao = input("Informe o ID da revisão: ")
            nova_materia = input("Informe a nova matéria da revisão: ")
            nova_descricao = input("Informe a nova descrição da revisão: ")
            nova_revisao = input("Informe o novo status da revisão: ")
            nova_data_criacao = input("Informe a nova data de criação: ")    

            revisao_editada = classes.Revisoes(id_nova_revisao, nova_materia, nova_descricao, nova_revisao, nova_data_criacao)
            confirma = revisoes_repo.editar_revisoes(revisao_editada)

            if confirma:
                print("Revisão editada com sucesso.")
            else:
                print("Não foi possível editar a revisão")

        if opcao == 11: #excluir revisão
            revisao_id = input("Informe o ID da revisão a ser excluída: ")
                
            confirma = revisoes_repo.deletar_revisoes(revisao_id)

            if confirma:
                print("Revisão excluída com sucesso.")
            else:
                print("Não foi possível excluir a revisão.") 
                
        if opcao == 12: #exibir revisão
            revisao_id = input("Informe o ID da revisão a ser exibida: ")
                
            confirma = revisoes_repo.listar_revisao(revisao_id)
            if confirma:
                print(f"ID: {revisoes_repo.id} | Nome: {revisoes_repo.nome} | Email: {revisoes_repo.email}")

        if opcao == 0:
            break
            
except pymysql.Error as e:
    print("Erro MySQL: ", e)

finally:
    connection.close()
    print("Conexão Encerrada.")


