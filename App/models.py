import sqlite3

# Criação do CRUD
class Tarefas:
    def __init__(self,id,titulo,status):
        self.id = id
        self.titulo = titulo
        self.status = status
    
    def __str__(self):
        return f'{self.titulo} = [{self.status}]'
    
    def conectar(self):
            banco_tarefa = sqlite3.connect('App/database/tarefas.db')
            cursor = banco_tarefa.cursor()
            return banco_tarefa, cursor
        
    def criar_tarefa(self,titulo):
        try:
            banco_tarefa, cursor = self.conectar()
            status = 0
            cursor.execute('INSERT INTO tarefas (titulo, status) VALUES(?, ?)',(titulo, status))
            banco_tarefa.commit()
            
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()
    
    def ler_tarefa(self):
        try:    
            banco_tarefa, cursor = self.conectar()
            read = cursor.execute("SELECT * FROM tarefas").fetchall()
            if read == []:
                return []
            else: 
                return read
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()
        
    def atualizar_tarefa(self,id,status):
        try:
            banco_tarefa, cursor = self.conectar()
            cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?",(status,id)) # USAR O ? NO LUGAR DO F-STRING 
            banco_tarefa.commit()
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()
                
    def excluir_tarefas(self,id):
        try:
            banco_tarefa, cursor = self.conectar()
            cursor.execute("DELETE FROM tarefas WHERE id = ?",(id,))
            banco_tarefa.commit()
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()