import sqlite3

try:
    # Conectando ao banco de dados
    banco_tarefa = sqlite3.connect('App/database/tarefas.db')
    cursor = banco_tarefa.cursor()
    
    # Cria a tabela    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status INTEGER NOT NULL DEFAULT 0
        )
    """)
    # Commit do banco
    banco_tarefa.commit()
    # Fecha cursor
    cursor.close()
except sqlite3.Error as error:
    print(f'Ocorreu algum erro: {error}')
finally:
    if cursor:
        cursor.close()
    if banco_tarefa:
        banco_tarefa.close()