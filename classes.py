from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        
        
class Usuario_Repositorio:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
        
    def registrar_usuario(self, usuario: Usuario):
        sql = "INSERT INTO usuarios(nome, email, senha) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha))
        self.conexao.commit()
        
    def listar_usuario(self, usuario_id):
        sql = "SELECT id, nome, email, senha FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, (usuario_id,))
        linha = self.cursor.fetchone()
        
        if linha:
            return Usuario(id=linha[0], nome=linha[1], email=linha[2], senha=linha[3])
        return None
    
    def deletar_usuario(self, usuario_id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(sql, (usuario_id,))
        self.conexao.commit()
        
        print(f"Usuário {usuario_id} foi excluído do sistema")
           
    def editar_usuario(self, usuario: Usuario):
        sql = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s"
        self.cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.id))
        self.conexao.commit()
    
    
class Materias:
    def __init__(self, usuario_id, nome, conteudos_registrados=None, id=None):
        self.id = id
        self.usuario_id = usuario_id
        self.nome = nome
        self.conteudos_registrados = conteudos_registrados
class Materias_Repositorio:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
        
    def registrar_materia(self, materia: Materias):
        sql = "INSERT INTO  materias(usuario_id, nome, conteudos_registrados) VALUES(%s, %s, %s)"
        self.cursor.execute(sql, (materia.usuario_id, materia.nome, materia.conteudos_registrados))
        self.conexao.commit()
        
    def listar_materia(self, materia_id):
        sql = "SELECT id, usuario_id, nome, conteudos_registrados FROM materias WHERE id = %s"
        self.cursor.execute(sql, (materia_id,))
        linha = self.cursor.fetchone()
 
        if linha:
            return Materias(id=linha[0], usuario_id =linha[1], nome=linha[2], conteudos_registrados=linha[3])
        return None

    def deletar_materia(self, materia_id):
        sql = "DELETE FROM materias WHERE id = %s"
        self.cursor.execute(sql, (materia_id,))
        self.conexao.commit()
        
        print(f"Matéria {materia_id} foi excluída do sistema")
                    
    def editar_materia(self, materia: Materias):
        sql = "UPDATE materias SET usuario_id = %s, nome = %s, conteudos_registrados = %s WHERE id = %s"
        self.cursor.execute(sql, (materia.usuario_id, materia.nome, materia.conteudos_registrados, materia.id))
        self.conexao.commit()
    
    
class Revisoes:
   def __init__(self, materia_id, descricao_revisao, status = 'pendente', id=None, data_criacao=None, data_revisao=None):
       self.id = id
       self.materia_id = materia_id
       self.descricao_revisao = descricao_revisao
       self.status = status
       self.data_criacao = data_criacao
       self.data_revisao = data_revisao
   
class Revisoes_Repositorio:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
        
    def registrar_revisao(self, revisao: Revisoes):
        sql = "INSERT INTO revisoes(materia_id, descricao_revisao, status, data_criacao, data_revisao) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (revisao.materia_id, revisao.descricao_revisao, revisao.status, revisao.data_criacao, revisao.data_revisao))
        self.conexao.commit()
        
    def listar_revisao(self, revisao_id):
        sql = "SELECT id, materia_id, descricao_revisao, status, data_criacao, data_revisao FROM revisoes WHERE id = %s"
        self.cursor.execute(sql, (revisao_id,))
        linha = self.cursor.fetchone()
        
        if linha:
            return Revisoes(id=linha[0], materia_id=linha[1], descricao_revisao=linha[2], status=linha[3], data_criacao=linha[4])
        return None
       
    def deletar_revisoes(self, revisao_id):
        sql = "DELETE FROM revisoes WHERE id = %s"
        self.cursor.execute(sql, (revisao_id,))
        self.conexao.commit()
        
        print(f"Revisao foi removida do sistema.")
        
    def editar_revisoes(self, revisao: Revisoes):
        sql = "UPDATE revisoes SET materia_id = %s, descricao_revisao = %s, status = %s, data_criacao = %s WHERE id = %s"
        self.cursor.execute(sql, (revisao.materia_id, revisao.descricao_revisao, revisao.status, revisao.data_criacao, revisao.id))
        self.conexao.commit()
        
    def data_revisoes (self, revisao: Revisoes, dias_proxima_revisao =7):
        
        nova_data = datetime.now() + timedelta(days=dias_proxima_revisao)
        
        sql = """UPDATE revisoes
                 SET status = 'pendente', data_revisao = %s
                 WHERE id = %s
               """
        
        self.cursor.execute(sql, (nova_data, revisao.id,))
        self.conexao.commit()
        print(f"Revisão {revisao.id} atualizada! Próxima revisão agendada para: {nova_data}")
    