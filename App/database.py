import sqlite3


# cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

# cursor.execute("INSERT INTO pessoas VALUES('Maria', 16, 'mariadb@gmail.com')")
nome = "Renato"
idade = 16
email = "dwm@gmail.com"

banco = sqlite3.connect('banco_tarefas.db')
cursor = banco.cursor()
    
cursor.execute("INSERT INTO pessoas VALUES({},{},{})".format(nome,str(idade),email))
banco.commit()
print("Os dados foram adicionados com sucesso!!")
