import sqlite3
class Tarefas:
    def __init__(self,id,titulo,status):
        self.id = id
        self.titulo = titulo
        self.status = status
    
    def __str__(self):
        return f'Objeto criado a partir da definição CRUD'
    
    def criar_tarefa(self,titulo):
        try:
            banco_tarefa = sqlite3.connect('App/database/tarefas.db')
            cursor = banco_tarefa.cursor()
            cursor.execute(f'INSERT INTO tarefas VALUE({self.id},{self.titulo},{self.status})')
            banco_tarefa.commit()
            cursor.close()
            banco_tarefa.close()
            
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()
    
    def ler_tarefa(self):
        try:    
            banco_tarefa = sqlite3.connect('App/database/tarefas.db')
            cursor = banco_tarefa.cursor()
            read = cursor.execute("SELECT * FROM tarefas")         
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
            banco_tarefa = sqlite3.connect('App/database/tarefas.db')
            cursor = banco_tarefa.cursor()
            
            
            cursor.execute("UPDATE tarefas SET")
        except sqlite3.Error as error:
            print(f"Ocorreu um erro: {error}")
        finally:
            if cursor:
                cursor.close()
            if banco_tarefa:
                banco_tarefa.close()
                
    def excluir_tarefas(self,id):
        pass
    